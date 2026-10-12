# PILOT-001 / PLATE — readonly architecture evidence crosswalk

**Observation date:** 2026-10-12 (America/Lima).  
**Subject:** `Em3rc0d/plate` at `main@df334632c6d606a3601ea61680e4cb7d0f2c8878`, viewed **read-only** via GitHub file/tree reads.  
**Evidence class:** `OBSERVED` static repository contents; mapping to PILOT = `INFERRED` / `INSPIRED`.  
**Status:** `READONLY_STUDY_COMPLETE_WITH_LIMITATIONS`. **Not** a security audit, payment-provider certification, live integration run, or permission to modify Plate.  
**Authority:** PLATE is reference evidence, **not** an implementation target. No production systems, databases, secrets, settings, webhooks, branches, tests, or code in PLATE were changed or executed.

## Why read Plate?

Pressure-test whether the PILOT-001 synthetic assumptions transfer cleanly to an actual product design. In PILOT, one SQLite file models `payment_events(provider,event_id)`, `payment_orders`, and `entitlements(order_id,entitlement_type)`; that fixture is **not** a prescription that products must adopt those tables or SQLite.

## Inspected paths (all pinned)

- [Mercado Pago service](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/src/payments/mercado-pago.ts) — payment attempts, verified provider snapshots, provider lookups, signature verification.
- [Payment submission API](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/app/api/orders/[id]/payments/route.ts) and [webhook API](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/app/api/payments/mercado-pago/webhook/route.ts) — entry points / fulfillment routing.
- [Payment schema + RPC](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/supabase/migrations/20260927210000_mercado_pago_checkout.sql), [TEST isolation/state guards](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/supabase/migrations/20260927222105_harden_payment_test_isolation.sql), [base orders/reports uniqueness](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/supabase/migrations/20260926025742_initial_vehicle_platform.sql), [report lifecycle changes](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/supabase/migrations/20260926040731_finishing_launch_controls.sql) — constraints and transaction boundaries.
- [Vehicle/report generation](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/src/vehicle/service.ts) and [report lookup](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/src/reports/repository.ts) — effects and externally accessible artifact logic.
- [Offline payment safety tests](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/tests/payment-safety.test.mjs), [isolated SQL driver](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/tests/payment-sql.test.mjs) and [SQL state assertions](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/tests/payment-state.sql) — existing tests, **not executed in this review**.
- [Financial reconciliation admin route](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/app/api/admin/payments/reconcile/route.ts) — bounded financial refresh, not general terminal-state reconciliation.
- [Historical TEST certification memo](https://github.com/Em3rc0d/plate/blob/df334632c6d606a3601ea61680e4cb7d0f2c8878/docs/MERCADO-PAGO-TEST-CERTIFICATION.md) — dated 2026-09-27; recorded **NOT CERTIFIED** and outstanding real-provider/deployed-DB gates then. Its historical observations are **not** a current deployment status check.

## Identity mapping — do not force an irrelevant schema

| Concern | PILOT-001 SQLite toy | Plate observed implementation | Transfer judgment |
|---|---|---|---|
| Payment initiation duplicate | Toy processes incoming `event_id` | Hash of (`order_id`, client idempotency key); `payment_attempts.request_key_hash` unique; provider uses `X-Idempotency-Key: attempt.id`; active-attempt unique index | **Comparable effect goal, different identity model** |
| Provider callback trust | Synthetic local HMAC over fixture event payload | HMAC of Mercado Pago notification fields, bounded timestamp, provider payment GET and verification of amount/currency/collector/method/mode/reference | **Different contract; don't transplant HMAC fixture** |
| Business effect uniqueness | `entitlements(order_id,entitlement_type)` unique | `reports.order_id` unique + order payment state + `begin_report`/generation token and `commit_report` | **Same invariant category, different domain effect** |
| Ordering and paid-state | Synthetic `PAID` resists stale `FAILED` | `provider_updated_at`, `ever_approved`, SQL state-regression protections, TEST never marks order paid | **Observed guards; deployed migration unknown** |
| Unknown external outcome | Synthetic mock `reconcile` argument | Existing attempt recovered via provider ID GET or `external_reference` search; ambiguous creation doesn't automatically POST again | **Observed recovery boundary, not certified end-to-end settlement** |

### P01–P08 crosswalk

Use labels: `CODE_GUARD` = guard visible in code/SQL, `OFFLINE_TEST_PRESENT` = test defined in Plate, not run here, `NOT_PROVEN` = deployment or end-to-end result unknown.

| Scenario | What inspection supports | Classification / residual uncertainty |
|---|---|---|
| P01 same transport event replay | Webhook verifies signature, fetches authoritative provider payment, invokes SQL state sync; report creation is gated by transition; no standalone `(provider,event_id)` receipt table found in inspected flow | `CODE_GUARD`; repeated real webhook/effect counts `NOT_PROVEN`. A ledger is **not automatically necessary** |
| P02 two event identities, one order | Unique active MP attempt per order; provider payment ID unique; `reports.order_id` unique; report lifecycle claims control concurrent effect | `CODE_GUARD`, isolated SQL test present; real replay `NOT_PROVEN` |
| P03 race | `claim_mercado_pago_attempt` locks order `FOR UPDATE`; partial unique active-order index; JS offline fixture simulates eight concurrent submissions with one POST | `OFFLINE_TEST_PRESENT`; deployed PostgreSQL/browser multi-connection race `NOT_PROVEN` |
| P04 stale/out-of-order updates | Provider timestamp comparison and regression exceptions; `tests/payment-state.sql` covers stale PENDING after APPROVED and terminal REFUNDED | `CODE_GUARD + OFFLINE_TEST_PRESENT`; remotely applied migration `UNKNOWN` |
| P05 persistence across restart | DB uniqueness constraints persist by design; no per-restart integration test observed in inspected tests | `CODE_GUARD`, process/deployment restart `NOT_PROVEN` |
| P06 spoofing | HMAC signature verification, 5-minute time tolerance, mismatch handling and authoritative provider GET; offline valid/tampered/stale test exists | `CODE_GUARD + OFFLINE_TEST_PRESENT`; real signed provider delivery `NOT_PROVEN` |
| P07 partial failures | Ambiguous transport/5xx/429 remains `CREATING` without automatic second POST; report creation has claim/recovery and existing-report checks | `CODE_GUARD`; crash after remote charge, before local commit, and duplicate paid provider calls `NOT_PROVEN` |
| P08 unresolved authoritative state | Recovery by provider ID/external reference; admin reconciliation route targets **approved LIVE attempts missing net-received financials**, not arbitrary unresolved/CREATING orders | `PARTIAL`; end-to-end CREATING settlement recovery `NOT_PROVEN` |

## What the evidence changes in PILOT-001

1. **Business effect ≠ a fixed entitlement table.** The invariant is at-most-once *logical access/report for an approved order* within the relevant state/persistence boundary. Implementations may enforce it with durable order states + unique report row + transactional claim, rather than copying the toy schema.
2. **Three distinct idempotency boundaries:** `payment submission → provider payment attempt`; `provider snapshot/webhook → paid-state transition`; `paid state → report generation/delivery`. A single success in one boundary does not prove the other two.
3. **Provider-sourced reconciliation is not a mock bool.** Real flows require validated provider identity, state, method, amount, currency, environment and correlation IDs; financial fee reconciliation is a separate concern from uncertain charge settlement.
4. **Effect ≠ provider cost.** One report row does not itself prove only one paid provider invocation; recovery/refresh paths and costs require separate evidence where needed.
5. **Order state ≠ public report authentication.** Plate's report retrieval uses a long unguessable capability code + report status/expiry checks. Scope and code ownership are product-specific; this study does not prove or disprove an authorization vulnerability.
6. **Do not over-generalize.** PostgreSQL RPC transaction semantics, Supabase role grants and Mercado Pago verification are domain/environment-specific; the SQLite HMAC fixture must remain a pedagogical model.

## Outcome / decision

- `PILOT-001` already **PASS WITH LIMITATIONS** as an isolated SQLite experiment. No change to the 14/14 local test result.
- `PLATE_READONLY_STUDY`: **PASS WITH LIMITATIONS** for source-to-pattern crosswalk; **not** certification of Plate or a discovered exploitable defect.
- **Pattern decision:** retain SD-004 as `CANDIDATE / IN REVIEW`; refine documentation conceptually with the three effect boundaries; **no implementation in Plate**.
- **Product decision:** `NO_CHANGE / NO_DEPLOY / NO_LIVE_TEST`. No new checkout table, library, queue, provider SDK or reconciliation job is justified by this reading.
- **UNKNOWN:** exact deployed migrations/flags/SHA, real PSP callback semantics, actual concurrent behavior, recovery after power loss or partial remote charge, real refunds, paid provider-call counts.

## Evidence and falsification conditions

A later project-specific evaluation would need an **explicitly authorized**, isolated test environment, exact deployed SHA and migration state, real provider TEST callback evidence, concurrency and crash/reconciliation receipts, and physical provider-call counts. That work is **out of scope and not requested** here. Any contradiction with live evidence should supersede this static crosswalk with a dated receipt.

**Provenance boundary:** historical memo dated 2026-09-27 is not a current statement that PLATE is (or is not) live, vulnerable, unconfigured or payment-certified. No access to real database/payment provider/runtime was used.
