# PILOT-001 — Payment-event replay without production exposure

**Status: LOCAL SYNTHETIC PILOT EXECUTED — PASS WITH LIMITATIONS (2026-10-12).** Synthetic evaluation of SD-004; **not** an integration with PlacaClara and not evidence that PlacaClara currently has or lacks these protections.

## Purpose and scope
Can a minimal SQLite local transaction + durable uniqueness boundary avoid multiple entitlement grants when a payment-related event is delivered repeatedly or concurrently? This only evaluates a proposed **local-effect** contract. It does **not** verify PSP billing, webhook authenticity, payment settlement or live business implementation.

## Preconditions / gate
Before coding: close order identity, entitlement uniqueness invariant, source of truth for paid state, allowed transition matrix, trust boundary and recovery rule. All remain **UNRESOLVED FOR ANY REAL PRODUCT**. Toy assumptions may be fixed as `SYNTHETIC` in a fixture for a local lab, never silently substituted into a product.

## Candidate test model (not schema migration)
- `payment_events(provider, event_id)` unique; `payment_orders(order_id, verified_state)`; `entitlements(order_id, entitlement_type)` unique.
- Reconciliation is separate from event receipt.
- A success event passes synthetic verifier; only a validated transition can grant one synthetic entitlement; an old failure event cannot revoke already confirmed success.
- Rollback on transaction failure; uniqueness constraint protects concurrent writers.

## Acceptance matrix
| Test | Fixture input | Expected local effect |
|---|---|---|
| P01 duplicate transport | Same event twice | one event record / one grant |
| P02 two transport identities | Two success event IDs, same order | at most one grant |
| P03 race | Concurrent success deliveries | at most one grant, both handlers terminate |
| P04 reorder | SUCCESS then stale FAILED | success remains authoritative per fixture policy |
| P05 restart | Deliver same event after storage reopen | grant still unique |
| P06 forgery | Unverified event | zero grants |
| P07 partial failure | Crash/rollback during insert | no partial grant; retry resumes safely |
| P08 unresolved settlement | Ambiguous external state | no new grant without independent validation |

## Executed evidence

See [local reproducibility package](./experiments/PILOT-001/README.md) and [execution receipt](./experiments/PILOT-001/RESULTS-2026-10-12.md). Six local suite executions passed 14 tests per run (84 total test executions); P01–P08 and N01–N06. **The signed events and the reconciliation authority are synthetic fixtures, not actual PSP guarantees.** This closes the bounded local pilot only; it does not certify SD-004 or any real application.

## Evidence required to mark PASS
Runnable lab fixture committed at exact SHA; isolated database with deterministic setup; P01-P08 outputs plus negative controls; local command, runtime version, artifacts and known limitations. Independent review of the **business** key vs transport key distinction.

## Decision
- **GO to project-specific discovery** only if lab tests pass and actual provider/order contract is recovered.
- **HOLD** if provider invariants or concurrency isolation unknown.
- **KILL** generic abstraction if it adds complexity without improving observable correctness.

No payment credentials, real orders, user data, live webhooks, API calls or cloud jobs are authorized by this pilot specification.
