"""P01..P08 and negative controls. Run: python -m unittest -v test_payment_lab.py"""
import concurrent.futures
import sqlite3
import tempfile
import threading
import unittest
from dataclasses import replace
from pathlib import Path

from payment_lab import Event, InjectedFailure, PaymentLab, sign


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="pilot001-")
        self.addCleanup(self.temp.cleanup)
        self.db_file = Path(self.temp.name) / "payment.sqlite"
        self.lab = PaymentLab(self.db_file)
        self.lab.add_order("ORDER-001", amount_minor=1000)

    def event(self, event_id="evt-001", outcome="SUCCEEDED", order_id="ORDER-001", amount_minor=1000):
        return sign(Event(event_id, order_id, outcome, amount_minor))

    def test_p01_duplicate_transport(self):
        event = self.event()
        self.assertEqual(self.lab.process_event(event), "APPLIED")
        self.assertEqual(self.lab.process_event(event), "DUPLICATE")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 1, 1))

    def test_p02_distinct_transport_ids_same_business_order(self):
        self.assertEqual(self.lab.process_event(self.event("evt-a")), "APPLIED")
        self.assertEqual(self.lab.process_event(self.event("evt-b")), "APPLIED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 2, 1))

    def test_p03_concurrent_race(self):
        barrier = threading.Barrier(12)
        event = self.event("evt-race")
        def deliver(_):
            barrier.wait(timeout=8)
            return self.lab.process_event(event)
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
            results = list(pool.map(deliver, range(12)))
        self.assertEqual(results.count("APPLIED"), 1)
        self.assertEqual(results.count("DUPLICATE"), 11)
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 1, 1))

    def test_p04_stale_failure_after_success(self):
        self.assertEqual(self.lab.process_event(self.event("evt-success")), "APPLIED")
        self.assertEqual(self.lab.process_event(self.event("evt-stale", "FAILED")), "APPLIED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 2, 1))

    def test_p05_restart_persistence(self):
        event = self.event("evt-restart")
        self.assertEqual(self.lab.process_event(event), "APPLIED")
        reopened = PaymentLab(self.db_file)
        self.assertEqual(reopened.process_event(event), "DUPLICATE")
        self.assertEqual(reopened.snapshot("ORDER-001"), ("PAID", 1, 1))

    def test_p06_forgery_no_effect(self):
        forged = replace(self.event("evt-forged"), signature="incorrect")
        self.assertEqual(self.lab.process_event(forged), "REJECTED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("NEW", 0, 0))

    def test_p07_transaction_rollback_and_retry(self):
        event = self.event("evt-crash")
        for point in ("after_event", "after_state", "after_grant"):
            with self.subTest(failure_at=point):
                with self.assertRaises(InjectedFailure):
                    self.lab.process_event(event, inject_failure_at=point)
                self.assertEqual(self.lab.snapshot("ORDER-001"), ("NEW", 0, 0))
        self.assertEqual(self.lab.process_event(event), "APPLIED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 1, 1))

    def test_p08_unresolved_awaits_reconciliation(self):
        self.assertEqual(self.lab.process_event(self.event("evt-pending", "PENDING")), "APPLIED")
        self.assertEqual(self.lab.reconcile("ORDER-001", "UNKNOWN"), "UNRESOLVED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PENDING", 1, 0))
        self.assertEqual(self.lab.reconcile("ORDER-001", "PAID"), "RECONCILED")
        self.assertEqual(self.lab.reconcile("ORDER-001", "PAID"), "RECONCILED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 1, 1))

    def test_n01_transport_id_reused_with_changed_payload(self):
        self.assertEqual(self.lab.process_event(self.event("evt-collision", "PENDING")), "APPLIED")
        self.assertEqual(self.lab.process_event(self.event("evt-collision", "SUCCEEDED")), "REPLAY_CONFLICT")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PENDING", 1, 0))

    def test_n02_signed_wrong_amount(self):
        self.assertEqual(self.lab.process_event(self.event("evt-amount", amount_minor=999)), "REJECTED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("NEW", 0, 0))

    def test_n03_signed_unknown_order(self):
        self.assertEqual(self.lab.process_event(self.event("evt-unknown", order_id="NONEXISTENT")), "REJECTED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("NEW", 0, 0))

    def test_n04_invalid_provider_and_outcome(self):
        foreign = sign(replace(self.event("evt-provider"), provider="OTHER"))
        invalid = sign(replace(self.event("evt-outcome"), outcome="REFUNDED"))
        self.assertEqual(self.lab.process_event(foreign), "REJECTED")
        self.assertEqual(self.lab.process_event(invalid), "REJECTED")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("NEW", 0, 0))

    def test_n06_concurrent_distinct_events_same_order(self):
        barrier = threading.Barrier(8)
        def deliver(i):
            barrier.wait(timeout=8)
            return self.lab.process_event(self.event(f"evt-distinct-{i}"))
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(deliver, range(8)))
        self.assertEqual(results, ["APPLIED"] * 8)
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 8, 1))

    def test_n05_database_uniqueness_survives_direct_writes(self):
        self.assertEqual(self.lab.process_event(self.event("evt-success")), "APPLIED")
        with sqlite3.connect(self.db_file) as db:
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO entitlements VALUES('ORDER-001', 'REPORT_ACCESS')")
        self.assertEqual(self.lab.snapshot("ORDER-001"), ("PAID", 1, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
