# MK1 — Five candidate patterns (Normalize & Classify)

**State: IN REVIEW, NOT CERTIFIED.** MK1 is not automatically completed merely because cards exist. The source was a secondary set of interview notes; primary contrasts and real project gates still apply.

| ID | Candidate | Decision trigger |
|---|---|---|
| SD-001 | [Architecture Decision](./patterns/SD-001-architecture-decision.md) | Consequential component/boundary decision |
| SD-002 | [Capacity Estimation](./patterns/SD-002-capacity-estimation.md) | Throughput, traffic, quota or resource constraint |
| SD-003 | [Resilience](./patterns/SD-003-resilience.md) | A dependency can fail, slow down or overload |
| SD-004 | [Idempotency & Consistency](./patterns/SD-004-idempotency-consistency.md) | Retriable event could repeat a business side effect |
| SD-005 | [Observability](./patterns/SD-005-observability.md) | Need evidence that outcomes/reliability meet targets |

**Order:** retrieve just the relevant card → gather system measurements/contracts → compare alternatives → controlled test → decision recorded in **project** repository → review and possible promotion.

See [pilot design](./PILOT-001-payment-idempotency.md), [PILOT-001 executed receipt](./experiments/PILOT-001/RESULTS-2026-10-12.md) and [MK1 review gate](./REVIEW-GATE.md). No blanket software implementation or technology recommendation is implied.

## Optional evidence case study

The [PILOT-001 / Plate read-only crosswalk](./experiments/PILOT-001/PLATE-READONLY-CROSSWALK-2026-10-12.md) records similarities, material differences, and unproven gates from the observed Plate code. It does **not** close MK1, license live provider testing, or recommend edits to Plate.
