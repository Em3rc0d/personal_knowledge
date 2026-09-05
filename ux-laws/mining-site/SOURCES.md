# Mining Site — Source Registry

This registry tracks where UX-law knowledge comes from and what authority each source has.

## Seed source

### SRC-UXL-001 — Laws of UX

```yaml
id: SRC-UXL-001
name: Laws of UX
author: Jon Yablonski
canonical_url: https://lawsofux.com/
spanish_url: https://lawsofux.com/es/
source_type: curated_secondary_reference
status: active
languages:
  - en
  - es
captured_on: 2026-09-05
provenance: OFFICIAL
```

### Authority boundary

Laws of UX is treated as the **seed index and curated explanation layer**, not automatically as the strongest possible empirical authority for every claim.

For each law we should progressively locate, when applicable:

```text
original study / primary literature
        ↓
replications / modern evidence
        ↓
reputable UX/HCI synthesis
        ↓
Laws of UX explanation
        ↓
our operational interpretation
```

The hierarchy is not absolute: some entries are Gestalt principles, heuristics, named effects, engineering principles or broad conceptual models rather than a single experimentally established "law".

## Mining rules

1. Never copy large source passages into the repository.
2. Store concise paraphrases, metadata, citations and our analysis.
3. Preserve the distinction between source claim and operational interpretation.
4. Record caveats, contested formulations and historical context.
5. Prefer original research for empirical claims when discoverable.
6. Never turn a memorable number into a hard UI limit without checking its evidential scope.
7. A design heuristic is not automatically a universal requirement.

## Planned source classes

- `PRIMARY_RESEARCH`
- `SYSTEMATIC_REVIEW`
- `HCI_TEXTBOOK`
- `STANDARD_OR_GUIDELINE`
- `CURATED_SECONDARY_REFERENCE`
- `INDUSTRY_EVIDENCE`
- `PRODUCT_OBSERVATION`
- `INTERNAL_EXPERIMENT`

## Important research flags

### Miller / working-memory simplification

The popular `7 ± 2` formulation must not be converted blindly into "always show seven items". MK0 must capture the historical claim and modern working-memory nuance before MK2 generates rules.

### Doherty `<400 ms`

Treat the number as a historical interaction-response heuristic requiring context. Operational rules should distinguish immediate acknowledgement from total task completion.

### Pareto `80/20`

Treat as a distribution heuristic, not a guaranteed mathematical ratio.

### Postel

Before product/security operationalization, evaluate modern robustness and security criticism of overly permissive input acceptance.

### Psychology → product ethics

Any use of attention, motivation, Zeigarnik, goal-gradient, peak-end or salience mechanisms must include an ethics boundary preventing coercive or compulsive interaction design.
