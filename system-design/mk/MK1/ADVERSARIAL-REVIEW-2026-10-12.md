# MK1 adversarial review — 2026-10-12

Scope: source-bound review of all five normalized records and the `PILOT-001` experiment. **Reviewer:** the executing assistant's internal static/negative-test review; **NOT an independent external or qualified peer review**. No Plate code, branch, database or deployment was modified.

## Evidence boundary

- Source: upstream notes pinned at `liquidslr/system-design-notes@9d8388721e7231442763ad37398b8d82224aa68f`; incomplete/secondary work in progress, license UNKNOWN. [Intake](../../mining-site/S-001-system-design-notes.md).
- Pilot code already committed to `personal_knowledge` in [PILOT-001](./experiments/PILOT-001/README.md) with original SHA-256 hashes `payment_lab.py=a57b1b7a3b946ffffdc0c8676ffd9be3d0ae09f579e437c88bf3deefdbacc664`, `test_payment_lab.py=5963f376210834eb7cc938c6e90ff3faa13bf6bf160ff2c10bd98cafd6b416b0`.
- Current review reproduced it locally on **Linux x86_64, Python 3.13.5, SQLite 3.46.1** using `cd /mnt/data/pilot001 && python -m unittest -v test_payment_lab.py`; then five additional runs `python -m unittest -q test_payment_lab.py` (total: **six runs × 14 tests, zero failures**). /mnt/data is local scratch, **not** a link for permanent retrieval; canonical source is the GitHub repository.
- Temporary adversarial mutations under independent auto-removed temporary directories (original two source files untouched):
  - **M01** replace `PRIMARY KEY(order_id, entitlement_type)` with an irrelevant non-unique check: test suite exits nonzero, **four failed test checks** (`N05`, `N06`, `P02`, `P08`).
  - **M02** replace `db.execute("BEGIN IMMEDIATE")` with `db.execute("SELECT 1")` removing the transaction: test suite exits nonzero, **four failed subtest checks**, all in `P07`.
- Meaning: the selected tests **discriminate** loss of local uniqueness and atomic rollback. They do not verify a live provider, true process termination/power loss or distributed system behavior.
- Documentation links: 17 existing `system-design/*.md` files were scanned; **zero broken repository-relative links**; new/updated links require PR diff review.
- Primary guidance contrasted: [AWS retry limits and jitter](https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_mitigate_interaction_failure_limit_retries.html), [Google SRE four signals](https://sre.google/sre-book/monitoring-distributed-systems/), [Stripe provider-specific idempotency](https://docs.stripe.com/api/idempotent_requests). These support bounded *questions*, not universal provider guarantees.

## Adversarial findings and resolutions

| ID | Severity for knowledge accuracy | Challenge | Decision/resolution | Status |
|---|---|---|---|---|
| F01 | Medium | SD-001 redefines ADR choices already owned by JEM | `REFERENCE_ONLY`; JEM retains architecture and lifecycle authority | **RESOLVED** |
| F02 | Medium | SD-004 conflated event dedup, paid state and effect uniqueness; SQLite entitlement not general product architecture | Replace with three bounded **B1/B2/B3** contract questions, link Plate non-production observation | **RESOLVED** |
| F03 | Medium | P07 is an injected exception; word `crash` can imply physical process/power-loss resilience | Clearly scope to rollback simulation, not real power-loss recovery | **RESOLVED** |
| F04 | Medium | Earlier root README calls executed pilot `synthetic design only` | Update current navigation/state; preserve initial/historical receipts without rewriting them | **RESOLVED** |
| F05 | Medium | Generic capacity equations hide constant-rate and physical storage assumptions | Add bounds on DAU/event assumptions, retention, backup factor and provider price uncertainty | **RESOLVED** |
| F06 | Medium | Retry response/error does not make non-idempotent side effects safe | Make unknown-commit/timeout stop rule explicit; restrict by provider scope | **RESOLVED** |
| F07 | Medium | Metrics of attempts/duplicates can inflate business success if counted as outcomes | Explicit eligible denominator, test-data exclusions, owner and delayed-events window | **RESOLVED** |
| F08 | High if promoted | Static Plate review ≠ deployed contracts, independent review or live PSP verification | Separate **internal classification gate A** from **operational promotion gate B** | **LIMITATION HELD** |
| F09 | Low | Historical MK0 `pilot pending` could look stale | Treat MK0 and initial pilot receipts as point-in-time records; use root STATUS for current status | **RESOLVED BY AUTHORITY** |

## Final classification and evidence strength

| ID | Internal disposition | Source confidence | Product applicability |
|---|---|---|---|
| SD-001 | `REFERENCE_ONLY` | Strong for ownership boundary (JEM); secondary for sample prompts | Reuse JEM's ADR, no competing gate |
| SD-002 | `CANDIDATE` | Concept-level, arithmetic valid only under stated inputs | `NEEDS_CONTEXT_EVIDENCE` |
| SD-003 | `CANDIDATE` | Concept-level + primary retry guidance | `NEEDS_CONTEXT_EVIDENCE` |
| SD-004 | `LAB_SUPPORTED_CANDIDATE` | Six local successful suites + two discriminative mutations for SQLite-specific invariant | `NEEDS_PROVIDER_AND_SYSTEM_EVIDENCE` |
| SD-005 | `CANDIDATE` | Concept-level + Google SRE contrast | `NEEDS_CONTEXT_EVIDENCE` |

## Verdict

- **MK1 normalization/classification task: `CLOSED WITH LIMITATIONS`** — source and status scoped, five records classified, genuine adversarial tests run and useful contradictions corrected.
- **Operational pattern promotion or production certification: `HOLD / NEEDS_EVIDENCE`** — no independent peer signoff, no provider/live proof, no project deployment approval.
- **Plate: `NO_CHANGE`** — only read-only evidence previously inspected at pinned commit, not a target to edit or re-test.
- No new infrastructure, cloud model, SDK, queuing or generic platform is justified. Future consumption only under actual project decision pressure.

This review does **not** close JEM's own independent MK1, rewrite previous source receipts, or claim quantitative token savings.
