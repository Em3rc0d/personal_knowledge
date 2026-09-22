# Railly Skills — Normalized Skill Catalog

Provenance: OBSERVED
Source of current catalog state: foundry/maturity.json
Pinned release metadata: 0.0.10

The registry contains 20 skills. Channel and maturity are independent.

| Skill | Type | Channel | Maturity | Owns | Important boundary / evidence debt |
|---|---|---|---|---|---|
| issue-intake | intake | stable | dogfooded | backlog survey, bounded shortlist, user selection, contract seed | stops before reproduction/implementation; xref is evidence not authority |
| record-a-case | foundry | stable | dogfooded | durable evidence ledger + compiled-knowledge disposition | case does not auto-promote procedure |
| review-gate | gate | stable | evaluated | exact-state pre-promotion review, deterministic checks, triggered lenses | consumes specialist receipts; mixed blind-replication result, not validated |
| solution-gate | gate | stable | dogfooded | evidence-only frame, independent shaping, adversarial probes, shape verdict | mechanical work skips; formal baseline comparison pending |
| trail-decisions | foundry | candidate | experimental | append-only in-the-moment decision trail | real dogfood still owed |
| signature-repro | triage | candidate | dogfooded | structural/visual signature when target platform/hardware unavailable | signature without confirmation remains hypothesis |
| before-after | communication | experimental | dogfooded | reproducible visual comparison artifact | visual proof does not prove timing/backend correctness; baseline comparison pending |
| handoff | foundry | experimental | dogfooded | end-of-cycle current-state recovery artifact | human override maturity; dedicated retrievable case gap |
| herdr-workstreams | coordination | experimental | experimental | visible runtime topology and specialist launch | runtime adapter only; end-to-end dogfood pending |
| quality-baseline | audit | experimental | dogfooded | read-only critical-path/control audit | not a generic score; baseline comparison pending |
| performance-proof | optimization | experimental | experimental | measurement-first optimization | only for evidenced performance claim; no recorded application proof at snapshot |
| test-strength | verification | experimental | dogfooded | falsification/mutation/property/boundary test strength | baseline comparison pending |
| resilience-audit | audit | experimental | experimental | forced failure/recovery/resource behavior | conditional, not default; maturity registry still conservative |
| security-review | audit | experimental | evaluated | attacker/trust/exploitability classification + receipt | positive small benchmark; transfer/repetition pending |
| simplify | optimization | experimental | dogfooded | bounded behavior-preserving reduction | one real reduction; transfer comparison pending |
| work-intake | intake | experimental | experimental | classify one selected source and recommend minimum Formula | read-only; admission is human decision; real cross-intent dogfood pending |
| workstream-reconcile | coordination | experimental | dogfooded | reconcile stale handoff/portfolio claims with live sources | read-only; baseline comparison pending |
| xref | intake | experimental | dogfooded | GitHub issue/PR graph snapshot, orphan/overlap/hazard discovery | tool-specific/internal dependency; no no-skill baseline yet |
| software-factory | protocol | experimental | experimental | staged implementation→reduction→hardening→strengthening→proof | overlap value explicitly unproven; first real run must justify existence |
| factory-loop | orchestration | experimental | experimental | master phase router, admission, freshness, re-entry, promotion boundary | full router has no baseline/validated production claim |

## Functional families

### Intake and routing

- issue-intake
- work-intake
- xref
- factory-loop

Question they answer:

    what work is this, what deserves attention, and what is the minimum authorized path?

### Design / solution choice

- solution-gate

Question:

    what shape deserves implementation?

### Execution

- software-factory
- simplify
- performance-proof

Question:

    how do we implement/reduce/optimize without letting the implementer’s claim become proof?

### Verification and risk

- test-strength
- resilience-audit
- security-review
- review-gate
- quality-baseline
- signature-repro

Question:

    which claims survive falsification at the correct boundary?

### Communication and continuity

- before-after
- handoff
- workstream-reconcile
- herdr-workstreams

Question:

    how do humans/agents see, resume and coordinate work without mistaking presentation for evidence?

### Learning / Foundry evolution

- record-a-case
- trail-decisions

Question:

    what should future work remember and why?

## Trigger-boundary pattern

The skill packages repeatedly test both:

- positive trigger requests;
- near misses that should route elsewhere.

Examples:

- “review completed diff” triggers review-gate, not implementation;
- “broad health audit” routes to quality-baseline, not simplify;
- “measure p95 cache” routes to performance-proof, not test-strength;
- “startup cleanup/retry” routes resilience, not security;
- “selected issue already reproduced” does not re-run issue-intake;
- “implement accepted shape” does not invoke factory-loop.

INFERRED lesson:

A skill catalog scales only when **negative ownership** is as explicit as positive ownership.

## Evidence caution

This catalog is not a ranking.

Stable means recommended distribution, not validated causal improvement.

Dogfooded means real use evidence under the source’s lifecycle, not proof of portability.

Evaluated means some baseline comparison exists, not repeated validated transfer.
