# Quarries

Quarries preserve extracted findings that may influence Jett Engineering Method but are not automatically canonical.

Suitable contents:

- project failure patterns;
- review findings;
- candidate rules;
- contradictions;
- caveats;
- external source extracts;
- alternative models;
- evidence fragments;
- reusable cases pending normalization.

## Promotion rule

```text
interesting finding
      ≠
canonical rule
```

Promotion requires provenance, reasoning, compatibility with current architecture and evidence/review proportional to the claim.

## Current external workflow quarries

- [`agent-workflow-artifacts-evidence-cost.md`](./agent-workflow-artifacts-evidence-cost.md) — candidate rules for generated-artifact lineage, deterministic islands around stochastic generation, invalidation before regeneration, cheapest-sufficient evidence and remote CI billing discipline. Source basis: Agent Engineering S-114.

## Current codebase-intelligence quarries

- [`understand-anything-codebase-intelligence.md`](./understand-anything-codebase-intelligence.md) — revision-bound recovery artifacts, freshness, completeness boundaries, incremental reconciliation, proportional recomputation and promotion gates from `Egonex-AI/Understand-Anything@6df3065f...`.
