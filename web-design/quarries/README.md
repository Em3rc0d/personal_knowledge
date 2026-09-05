# Web Design — Quarries

Quarries contain processed evidence and analysis extracted from specific sources. They are **not automatically accepted domain rules**.

A quarry may contain:

- `OFFICIAL` source claims;
- `OBSERVED` implementation behavior;
- `INFERRED` conclusions;
- unresolved contradictions;
- caveats;
- candidate rules;
- rejected ideas.

Promotion flow:

```text
source
  → quarry evidence
  → source/inference separation
  → cross-source review
  → normalization
  → design / architecture / build rule
```

Source-specific folders keep lineage explicit. `ricoui/`, for example, means “knowledge extracted while studying RICOUI”, not “rules owned by RICOUI”.
