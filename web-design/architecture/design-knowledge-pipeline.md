# Design Knowledge Pipeline

Status: `MK0 architecture draft`

## Pipeline

```text
[Sources]
   │
   ├── official docs
   ├── public websites
   ├── design-system repos
   ├── research / standards
   └── product evidence
   ↓
[Mining registry]
   ↓
[Evidence records]
   ├── OFFICIAL
   ├── OBSERVED
   └── timestamps / source ids
   ↓
[Reasoning]
   ├── INFERRED
   ├── contradictions
   ├── confidence
   └── applicability
   ↓
[Normalized web-design knowledge]
   ↓
[Semantic design contract]
   ├── visual grammar
   ├── tokens
   ├── component rules
   ├── responsive
   ├── accessibility
   └── motion
   ↓
[Generated artifacts]
   ├── tokens.json
   ├── CSS variables
   ├── framework theme
   ├── component metadata
   └── agent context
   ↓
[Implementation]
   ↓
[Verification]
   ├── structural checks
   ├── a11y checks
   ├── component/state checks
   ├── viewport rendering
   └── visual regression
```

## Design lineage

A future implementation should be able to trace important generated values back toward the semantic rule and, where relevant, the external evidence that influenced it.

Ideal graph:

```text
source evidence
  → normalized rule
  → token/component contract
  → generated artifact
  → rendered evidence
```

## Fail-closed principle

If provenance or applicability is unknown, the system should prefer `UNKNOWN / NEEDS REVIEW` over inventing authority.

If a visual reference cannot be verified as official, classify it as observed/inferred rather than upgrading it.
