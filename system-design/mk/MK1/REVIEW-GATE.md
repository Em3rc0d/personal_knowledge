# MK1 two-level review gate — 2026-10-12

## A. Bounded internal classification (MK1 normalization only)

| Gate | Evidence | Verdict |
|---|---|---|
| Source identity and scope | [MK0 receipt](../MK0/REVIEW-GATE.md); 28 title screening / 9 inspected | PASS WITH LIMITATIONS |
| Five records normalized without duplicate canon | [Classification](./README.md), [adversarial review](./ADVERSARIAL-REVIEW-2026-10-12.md) | PASS |
| Known contradictions/overclaiming addressed | SD-001 downgraded to reference; SD-004 split into three effect boundaries | PASS WITH LIMITATIONS |
| Original pilot replayed, source hashes checked | 6 independent local runs ×14 tests, hashes matched recorded source | PASS |
| Negative controls detect broken invariants | Two temporary mutations cause 4 failing checks each | PASS |
| Read-only Plate semantics not assumed to prove production | [Pinned crosswalk](./experiments/PILOT-001/PLATE-READONLY-CROSSWALK-2026-10-12.md) | PASS |
| Links/provenance/in-scope diff checked | 17 original domain Markdown links resolved at review; PR diff to be verified | PASS (local review) |

**Gate A verdict: `CLOSED WITH LIMITATIONS — INTERNAL NORMALIZATION ONLY`.** Its acceptance criteria are that source-bounded patterns are **classified** and major overclaims identified, not that every candidate becomes an externally validated standard.

## B. Pattern promotion and product-specific certification (NOT CLOSED)

- [ ] Independent/qualified reviewer **other than the generating assistant** accepts each candidate's intended guarantee and limitations.
- [ ] Primary source contract and license/freshness rechecked for the target environment.
- [ ] Relevant real workload, cost, failure and privacy boundaries demonstrated for that **specific** project.
- [ ] Provider/deployment integration, concurrency and failure evidence where operations are high-risk.
- [ ] Project owner authorizes an ADR or implementation separately.
- [ ] Change and monitoring gates pass in that project.

**Gate B verdict: `HOLD / NEEDS_EVIDENCE`.** No claim of independent peer review, benchmarked capacity, live PSP correctness, universal idempotency, SLO compliance or operational readiness. Gate A's closure is not a shortcut around Gate B.

## Preservation and triggers

Historical pilot receipts and MK0 documents preserve their *then-current* state; current state lives in [STATUS](../../STATUS.md). Reopen only for materially wrong rules, broken source identity, contradictory evidence, a failed reproduction, or a real reuse that requires revising the normalized taxonomy.
