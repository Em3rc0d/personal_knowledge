# SD-004 — Idempotent Business Effects & Reconciliation

Status: `CANDIDATE / IN REVIEW` · Class: `INSPIRED` + `GENERATED`.
Upstream: [19 message queue](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/19.%20Distributed%20Message%20Queue/README.md), [21 event aggregation](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/21.%20Ad%20Click%20Event%20Aggregation/README.md), [26 payment](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/26.%20Payment%20System/README.md).
Primary contrast: [Stripe API idempotent requests](https://docs.stripe.com/api/idempotent_requests). **Stripe rules only apply if Stripe is the relevant provider; no assertion about PlacaClara's provider.**

## Use when
A duplicated request/event could charge, issue access, send an irreversible action, or double-count an outcome.

## Contract
- Separate **transport dedup key** (`provider + event_id`) from **business effect uniqueness key** (`order_id + entitlement_type`, chosen after confirming domain invariants).
- Authenticate event and bind it to a known account/order; untrusted events produce **no mutation**.
- Atomically record the event/state transition and business effect where possible, enforcing uniqueness **in durable storage**, not merely an in-memory lookup.
- Define explicit legal transitions; stale failure must not reverse independently verified success.
- An acknowledgement is not sufficient proof of a completed business effect; uncertain provider state → reconcile via authoritative provider API/report.
- Treat webhook order/duplication behavior and signature rules as **UNKNOWN until actual provider contract is inspected**.
- If publishing other side effects, evaluate transactional outbox / recovery; don't assume local DB transaction spans external services.

## Tests (minimum)
Repeat same event ID; distinct event IDs same business order; concurrent duplicate deliveries; out-of-order success/failure; duplicate retry after process restart; forged/missing auth; unresolved provider state; recovery after partial local failure.

## Claim boundary
Guarantee sought: **at most one local business effect for one confirmed order under the tested persistence/transaction boundary**. No claim of global exactly-once delivery, no guarantee about actual charges without provider-side evidence.
