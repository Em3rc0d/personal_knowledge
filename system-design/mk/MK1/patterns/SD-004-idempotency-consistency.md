# SD-004 — Separate Idempotency & Consistency Boundaries

Status: `LAB_SUPPORTED_CANDIDATE / MK1 CLASSIFIED` · Sources: `INSPIRED` + `GENERATED` + `OBSERVED` synthetic lab and pinned read-only product code. **NOT** a product implementation or guarantee.

Upstream discussions: [19 queue](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/19.%20Distributed%20Message%20Queue/README.md), [21 aggregation](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/21.%20Ad%20Click%20Event%20Aggregation/README.md), [26 payments](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/26.%20Payment%20System/README.md). Provider-specific contrast: [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — Stripe rules **are not** Mercado Pago rules. Existing non-production evidence: [PILOT-001 receipt](../experiments/PILOT-001/RESULTS-2026-10-12.md) and [read-only Plate crosswalk](../experiments/PILOT-001/PLATE-READONLY-CROSSWALK-2026-10-12.md).

## Trigger

Use when duplicate, late, concurrent or retried requests/events can cause an irreversible or cost-bearing effect. If the use case is pure read-only, there may be no new idempotency design to add.

## Three independent boundaries — never conflate them

| Boundary | Unit of identity | Requested invariant | Proof required |
|---|---|---|---|
| B1 — Client request → provider attempt | Order + request idempotency key / provider-scoped operation ID | Safe repetition of **attempt creation** without unintended extra remote charges | Persisted claim + provider-specific idempotency contract + ambiguous-request handling |
| B2 — Provider callback/snapshot → durable paid state | Provider payment ID, order correlation, event identifier if supplied | Only an authenticated, correctly matched, authoritative provider state can move business state forward; stale or duplicate notifications cannot create a second transition | Signature/trust + provider GET/verification + allowed state transitions + recovery from ambiguous state |
| B3 — Paid business state → fulfillment | Domain-specific business key (e.g. order + report type/revision; not necessarily a generic `entitlement` table) | No unintended duplicate **logical fulfillment** and no double-paid downstream effects for the same authorized action | Durable uniqueness/claim + transaction boundaries + separate external side-effect cost/delivery checks |

**B1 ≠ B2 ≠ B3.** An HTTP idempotency header does not prove fulfillment uniqueness; one report row does not prove one paid data-provider call; rejecting a duplicate callback does not prove a customer never paid twice.

## Normalized rules

1. Distinguish **transport dedup** `(source,event_id)` when available from **business uniqueness** `(business_key,effect_type,version)`. Choose scope/TTL/collision rules from provider and product contracts. A separate event ledger is optional, not a universal requirement.
2. Authenticate and authorize events; correlate expected order, amount, currency, environment, collector, payment method and authoritative reference **when relevant to the actual provider**; untrusted messages have no business effect.
3. Serialize competing local transitions and place related **local** state/claim/entitlement writes in one durable transaction where possible; use uniqueness constraints for the *real* business effect.
4. Define allowed state transitions and monotonic guarantees; late, repeated or terminal/refund events must follow explicit domain policy. Never assume `PAID` should resist **every** later provider status (refund/chargeback requires its own policy).
5. If a remote outcome is unknown, do not blindly create another remote operation. Requery or reconcile using verified provider data; financial settlement reconciliation is distinct from charge-state resolution.
6. For effects outside the local DB (paid API, email, external provider), separate **logical record uniqueness** from **number of side-effect executions**; decide if an outbox/recovery mechanism is justified, not automatic.
7. Provider idempotency-key lifetime, event delivery ordering, webhook signature material and refund semantics remain `UNKNOWN` until the actual documented contract and deployment evidence are checked.

## Minimum tests / falsifiers

- B1: same request key, different key to same order, changed payload with same key, concurrent attempts, 408/409/429/5xx/timeout after remote acceptance.
- B2: duplicate provider event, spoofed signature, mismatched amount/currency/collector/environment/reference, out-of-order and terminal refunds, replay beyond allowed window.
- B3: repeated/cross-worker fulfillment, DB crash/rollback/restart, failure after external cost but before DB commit, duplicate delivery, explicit revision/reprocess.
- Track observed counts separately: provider **charges**, durable paid-state transitions, logical reports, paid data-provider calls, user-facing deliveries.

## Evidence and boundary

PILOT-001 supports **at-most-one local entitlement** in one synthetic SQLite database under 14 fixture tests (six repeated runs); two destructive mutations were detected by its tests. This does **not** prove global exactly-once semantics, distributed atomicity, live provider identity, production crash safety or any property of Plate. A pinned Plate [read-only crosswalk](../experiments/PILOT-001/PLATE-READONLY-CROSSWALK-2026-10-12.md) shows alternative PostgreSQL constraints and guards **without** demonstrating production outcomes or authorizing modifications. No new stack, table or PR in Plate is prescribed.
