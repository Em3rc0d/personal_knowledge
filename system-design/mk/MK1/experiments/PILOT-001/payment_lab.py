"""PILOT-001: synthetic payment-event idempotency lab. NOT a PSP integration."""
from __future__ import annotations

import hashlib
import hmac
import json
import sqlite3
from dataclasses import dataclass, replace
from pathlib import Path

MOCK_PROVIDER = "MOCK_PSP"
TEST_SECRET = b"pilot-001-local-synthetic-key-not-for-production"


@dataclass(frozen=True)
class Event:
    event_id: str
    order_id: str
    outcome: str
    amount_minor: int
    currency: str = "PEN"
    provider: str = MOCK_PROVIDER
    signature: str = ""

    def payload(self) -> bytes:
        fields = {"provider": self.provider, "event_id": self.event_id,
                  "order_id": self.order_id, "outcome": self.outcome,
                  "amount_minor": self.amount_minor, "currency": self.currency}
        return json.dumps(fields, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sign(event: Event) -> Event:
    """Synthetic HMAC fixture; cannot verify any real provider webhook."""
    return replace(event, signature=hmac.new(TEST_SECRET, event.payload(), hashlib.sha256).hexdigest())


class InjectedFailure(RuntimeError):
    pass


class PaymentLab:
    """One SQLite file. Each operation owns a connection and one write transaction."""

    def __init__(self, path: str | Path):
        self.path = str(path)
        db = self._connection()
        try:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS payment_orders (
                  order_id TEXT PRIMARY KEY,
                  amount_minor INTEGER NOT NULL CHECK(amount_minor > 0),
                  currency TEXT NOT NULL,
                  verified_state TEXT NOT NULL DEFAULT 'NEW'
                    CHECK(verified_state IN ('NEW','PENDING','FAILED','PAID'))
                );
                CREATE TABLE IF NOT EXISTS payment_events (
                  provider TEXT NOT NULL,
                  event_id TEXT NOT NULL,
                  payload_sha256 TEXT NOT NULL,
                  order_id TEXT NOT NULL REFERENCES payment_orders(order_id),
                  outcome TEXT NOT NULL,
                  PRIMARY KEY(provider, event_id)
                );
                CREATE TABLE IF NOT EXISTS entitlements (
                  order_id TEXT NOT NULL REFERENCES payment_orders(order_id),
                  entitlement_type TEXT NOT NULL,
                  PRIMARY KEY(order_id, entitlement_type)
                );
            """)
        finally:
            db.close()

    def _connection(self) -> sqlite3.Connection:
        db = sqlite3.connect(self.path, timeout=10, isolation_level=None)
        db.execute("PRAGMA foreign_keys=ON")
        db.execute("PRAGMA busy_timeout=10000")
        return db

    def add_order(self, order_id: str, amount_minor: int = 1000, currency: str = "PEN") -> None:
        db = self._connection()
        try:
            db.execute("INSERT INTO payment_orders(order_id, amount_minor, currency) VALUES(?,?,?)",
                       (order_id, amount_minor, currency))
        finally:
            db.close()

    def process_event(self, event: Event, *, inject_failure_at: str | None = None) -> str:
        if inject_failure_at not in (None, "after_event", "after_state", "after_grant"):
            raise ValueError("unsupported injection point")
        # Reject untrusted events before any write, with an explicit synthetic trust boundary.
        if event.provider != MOCK_PROVIDER or event.outcome not in ("SUCCEEDED", "FAILED", "PENDING"):
            return "REJECTED"
        signature = hmac.new(TEST_SECRET, event.payload(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, event.signature):
            return "REJECTED"
        fingerprint = hashlib.sha256(event.payload()).hexdigest()
        db = self._connection()
        try:
            db.execute("BEGIN IMMEDIATE")  # serializes concurrent local writers
            order = db.execute("SELECT amount_minor, currency, verified_state FROM payment_orders WHERE order_id=?",
                               (event.order_id,)).fetchone()
            if order is None or (order[0], order[1]) != (event.amount_minor, event.currency):
                db.rollback()
                return "REJECTED"
            prior = db.execute("SELECT payload_sha256 FROM payment_events WHERE provider=? AND event_id=?",
                               (event.provider, event.event_id)).fetchone()
            if prior:
                db.rollback()
                return "DUPLICATE" if prior[0] == fingerprint else "REPLAY_CONFLICT"
            db.execute("INSERT INTO payment_events VALUES(?,?,?,?,?)",
                       (event.provider, event.event_id, fingerprint, event.order_id, event.outcome))
            if inject_failure_at == "after_event":
                raise InjectedFailure("synthetic crash after event insert")
            previous_state = order[2]
            if event.outcome == "SUCCEEDED":
                db.execute("UPDATE payment_orders SET verified_state='PAID' WHERE order_id=?", (event.order_id,))
                if inject_failure_at == "after_state":
                    raise InjectedFailure("synthetic crash after order update")
                db.execute("INSERT OR IGNORE INTO entitlements VALUES(?,?)", (event.order_id, "REPORT_ACCESS"))
                if inject_failure_at == "after_grant":
                    raise InjectedFailure("synthetic crash after entitlement insert")
            elif previous_state != "PAID":
                if event.outcome == "FAILED":
                    db.execute("UPDATE payment_orders SET verified_state='FAILED' WHERE order_id=?", (event.order_id,))
                elif previous_state == "NEW":
                    db.execute("UPDATE payment_orders SET verified_state='PENDING' WHERE order_id=?", (event.order_id,))
            db.commit()
            return "APPLIED"
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    def reconcile(self, order_id: str, authoritative_mock_state: str) -> str:
        """Synthetic *independent* lookup result; not proof of a real provider API."""
        if authoritative_mock_state not in ("UNKNOWN", "PAID", "FAILED"):
            return "REJECTED"
        db = self._connection()
        try:
            db.execute("BEGIN IMMEDIATE")
            state = db.execute("SELECT verified_state FROM payment_orders WHERE order_id=?", (order_id,)).fetchone()
            if state is None:
                db.rollback()
                return "REJECTED"
            if authoritative_mock_state == "UNKNOWN":
                db.rollback()
                return "UNRESOLVED"
            if authoritative_mock_state == "PAID":
                db.execute("UPDATE payment_orders SET verified_state='PAID' WHERE order_id=?", (order_id,))
                db.execute("INSERT OR IGNORE INTO entitlements VALUES(?,?)", (order_id, "REPORT_ACCESS"))
            elif state[0] != "PAID":
                db.execute("UPDATE payment_orders SET verified_state='FAILED' WHERE order_id=?", (order_id,))
            db.commit()
            return "RECONCILED"
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    def snapshot(self, order_id: str) -> tuple[str, int, int]:
        db = self._connection()
        try:
            state = db.execute("SELECT verified_state FROM payment_orders WHERE order_id=?", (order_id,)).fetchone()[0]
            events = db.execute("SELECT count(*) FROM payment_events WHERE order_id=?", (order_id,)).fetchone()[0]
            grants = db.execute("SELECT count(*) FROM entitlements WHERE order_id=?", (order_id,)).fetchone()[0]
            assert db.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
            return state, events, grants
        finally:
            db.close()
