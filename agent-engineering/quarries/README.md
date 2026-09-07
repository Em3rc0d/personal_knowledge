# Agent Engineering — Quarries

`quarries/` contains processed evidence extracted from upstream sources.

A quarry is **not canon**. It may contain:

- source claims;
- direct observations;
- contradictions;
- failure signals;
- candidate rules;
- unresolved questions.

Promotion requires normalization in MK1 and operationalization/testing in later MKs.

## Current quarries

- [`genai-agents.md`](./genai-agents.md) — detailed mining pass over `NirDiamant/GenAI_Agents@4c95ae14...`, contrasted with current official documentation and scientific literature.

## Required discipline

Every non-trivial statement should make clear whether it is:

```text
SOURCE CLAIM
OBSERVED
INFERRED
SUPPORTED
QUALIFIED
CONTRADICTED
UNKNOWN
```

These reasoning-state labels complement the repository provenance labels (`OFFICIAL`, `OBSERVED`, `INFERRED`, `INSPIRED`, `GENERATED`).
