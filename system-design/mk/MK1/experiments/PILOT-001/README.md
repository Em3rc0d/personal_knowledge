# PILOT-001 — Offline synthetic SQLite replay lab

**Only standard-library Python and SQLite. Not real payment infrastructure.** No network, credentials, GitHub Actions, docker, external API, cloud quota or environment-variable secret required.

## Reproduce locally

```bash
cd system-design/mk/MK1/experiments/PILOT-001
python -m unittest -v test_payment_lab.py
```

Requirements: Python 3.10+ (tested Python 3.13.5), sqlite3 stdlib (tested SQLite 3.46.1), writable temporary directory. Tests allocate independent temporary SQLite files and clean them up. To repeat six times: `for i in 1 2 3 4 5 6; do python -m unittest -q test_payment_lab.py || exit 1; done` (POSIX shell). No project checkout dependency.

### Test scope

- P01 duplicate event ID → one persisted transport event and one entitlement.
- P02 different event IDs, same order → two events, one entitlement.
- P03 twelve concurrent identical deliveries → one applied, eleven duplicates; one entitlement.
- P04 paid then stale failed notification → order remains paid.
- P05 reopening SQLite file → duplicate still deduplicated.
- P06 mismatched synthetic signature → no mutation.
- P07 synthetic exceptions after event insert, order update and entitlement insert → entire transaction rolled back, retry grants exactly once.
- P08 ambiguous state with mock authoritative lookup → no grant until synthetic `PAID`; repeated reconciliation remains idempotent.
- N01–N06: event ID same/different payload, wrong signed amount, unknown order, wrong provider/status, uniqueness constraint direct violation, eight concurrent *different* event IDs for the same order.

### Design contract and limits

The two uniqueness boundaries are distinct: `(provider,event_id)` identifies a transport event; `(order_id,entitlement_type)` identifies a local business effect. Write transactions use `BEGIN IMMEDIATE` in a **single SQLite file**; no claims about distributed writes, actual concurrency across multiple databases or external providers.

`TEST_SECRET`, `sign()` and `reconcile(...,authoritative_mock_state)` are entirely **lab fixtures**. The secret is deliberately present in source; this is NOT secure authentication. `reconcile()` trusts an argument provided by the test, not a genuine provider. Transaction injections simulate exceptions/rollback, **not physical power loss**. These cases do not prove external charges were unique, prevent paid-state fraud, or meet PSP callback semantics.

Before any project use: discover actual payment processor, signature, amounts/currency, partial/refunded payments, event versions, order ownership, entitlement taxonomy, persistence/transaction boundaries, provider reconciliation and data-retention rules. **DO NOT COPY THIS LAB INTO PRODUCTION.**

Execution evidence: [RESULTS-2026-10-12.md](./RESULTS-2026-10-12.md) and [results.json](./results.json).
