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

- [`genai-agents.md`](./genai-agents.md) — detailed mining pass over `NirDiamant/GenAI_Agents@4c95ae14...`, contrasted with official documentation and scientific literature.
- [`genai-agents-inventory.md`](./genai-agents-inventory.md) — normalized 55-tutorial inventory seed by engineering family/risk cue rather than upstream content category.
- [`genai-agents-risk-scan.md`](./genai-agents-risk-scan.md) — capability/blast-radius scan covering generated code, shell, browser, mutation, egress, persistence, retries and controls.
- [`genai-agents-p0-p1-callpaths.md`](./genai-agents-p0-p1-callpaths.md) — P0/P1 verification pass that reconstructs consequential call paths and preserves material UNKNOWNs.
- [`cross-source-memory-production-mcp.md`](./cross-source-memory-production-mcp.md) — specialized cross-check against Agent Memory Techniques, Agents Towards Production and MCP `2026-07-28`.

## Architecture evidence promoted from quarries

The framework-independent threat model lives at [`../architecture/THREAT_MODEL.md`](../architecture/THREAT_MODEL.md). It is an MK0 architecture seed derived from quarry evidence, not a claim that every upstream system implements the listed controls.

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

## Current promotion boundary

MK0 is closed because the evidence base is strong enough to begin normalization. Candidate rules remain un-certified until later MK gates.

```text
quarry evidence
  ↓
MK1 normalize/classify
  ↓
MK2 operational contracts/tests
  ↓
MK5+ certification
```
