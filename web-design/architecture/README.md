# Web Design — Architecture

Architecture defines how evidence becomes reusable and verifiable design knowledge.

## Layer boundaries

```text
EXTERNAL SOURCES
      ↓
MINING SITE
      ↓
QUARRIES / EVIDENCE
      ↓
NORMALIZED KNOWLEDGE
      ↓
SEMANTIC DESIGN CONTRACT
      ↓
DERIVED ARTIFACTS
      ↓
FRONTEND IMPLEMENTATION
      ↓
VALIDATION EVIDENCE
```

No lower layer may silently rewrite the meaning of an upper layer.

A generated CSS file, for example, should not become the undocumented source for semantic design decisions if the contract remains canonical.
