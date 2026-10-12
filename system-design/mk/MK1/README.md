# MK1 — System Design internal normalization & classification

**State: CLOSED WITH LIMITATIONS — INTERNAL NORMALIZATION ONLY (2026-10-12).**
This closes a **bounded taxonomy/review task**, not production certification, independence of the reviewer, or universal applicability. Source material remains secondary and incomplete; products must make their own evidence-backed decisions.

## Normalized records (distinct classifications)

| ID | Record | Internal disposition | What is actually supported |
|---|---|---|---|
| SD-001 | [Architecture Decision](./patterns/SD-001-architecture-decision.md) | `REFERENCE_ONLY` | Jett Engineering Method is authoritative for ADR/process; no competing canon |
| SD-002 | [Capacity Estimation](./patterns/SD-002-capacity-estimation.md) | `CANDIDATE` | Unit-bearing scenario math; workload, pricing and benchmark validation are project-specific |
| SD-003 | [Resilience](./patterns/SD-003-resilience.md) | `CANDIDATE` | Failures/retries vocabulary and test ideas; dependency contracts not proven |
| SD-004 | [Idempotency & Consistency](./patterns/SD-004-idempotency-consistency.md) | `LAB_SUPPORTED_CANDIDATE` | Synthetic SQLite local invariant under P01–P08/N01–N06 only |
| SD-005 | [Observability](./patterns/SD-005-observability.md) | `CANDIDATE` | Signal definitions/test prompts; actual SLOs and alerts unknown |

`REFERENCE_ONLY` means **no duplicate operating standard**. `CANDIDATE` means usable as a question/checklist with validation required. `LAB_SUPPORTED_CANDIDATE` means one bounded fixture passed, not a production guarantee.

## Supporting evidence

- [Adversarial review and negative-control receipts](./ADVERSARIAL-REVIEW-2026-10-12.md).
- [Initial PILOT-001 scope](./PILOT-001-payment-idempotency.md), [execution receipt](./experiments/PILOT-001/RESULTS-2026-10-12.md) and [standalone local lab](./experiments/PILOT-001/README.md).
- [Plate read-only crosswalk](./experiments/PILOT-001/PLATE-READONLY-CROSSWALK-2026-10-12.md) is **not** a product audit or delivery certification.
- [MK1 gate](./REVIEW-GATE.md) separates internal normalized knowledge from external/operational promotion.

## On-demand use

Exact question → open the minimum relevant card → read its boundaries and source → gather product evidence → compare baseline vs alternative → project-specific review. **Do not reopen MK1** just because a new project uses a pattern: record real-world learnings in that project's own documents and feed back contradictions when material.
