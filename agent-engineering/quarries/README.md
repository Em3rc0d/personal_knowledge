# Agent Engineering — Quarries

`quarries/` contains processed evidence extracted from upstream sources.

A quarry is **not canon**. It may contain:

- source claims;
- direct observations;
- contradictions;
- failure signals;
- candidate rules;
- unresolved questions;
- historical states that were later promoted, closed or qualified.

Promotion requires normalization in MK1 and operationalization/testing in later MKs.

## Important current-state rule

Do **not** treat the newest-looking paragraph inside a quarry as the current domain answer without checking the active synthesis/gates.

For current system-level interpretation:

```text
../STATUS.md
→ ../systems/<system>/
→ ../mk/MK1/ current schema/gates
```

For evidence/provenance, descend back into the quarry and source receipt.

The first complete current system package is Strands Agents:

- canonical synthesis: [`../systems/strands/README.md`](../systems/strands/README.md)
- machine context: [`../systems/strands/LLM_CONTEXT.md`](../systems/strands/LLM_CONTEXT.md)
- evidence map: [`../systems/strands/EVIDENCE.md`](../systems/strands/EVIDENCE.md)

This matters because the original Strands quarry intentionally preserves candidate states that were later resolved by cross-runtime and MCP gates.

## Current quarries

- [`genai-agents.md`](./genai-agents.md) — detailed mining pass over `NirDiamant/GenAI_Agents@4c95ae14...`, contrasted with official documentation and scientific literature.
- [`genai-agents-inventory.md`](./genai-agents-inventory.md) — normalized 55-tutorial inventory seed by engineering family/risk cue rather than upstream content category.
- [`genai-agents-risk-scan.md`](./genai-agents-risk-scan.md) — capability/blast-radius scan covering generated code, shell, browser, mutation, egress, persistence, retries and controls.
- [`genai-agents-p0-p1-callpaths.md`](./genai-agents-p0-p1-callpaths.md) — P0/P1 verification pass that reconstructs consequential call paths and preserves material UNKNOWNs.
- [`cross-source-memory-production-mcp.md`](./cross-source-memory-production-mcp.md) — specialized cross-check against Agent Memory Techniques, Agents Towards Production and MCP `2026-07-28`.
- [`strands-agents.md`](./strands-agents.md) — Strands Agents `harness-sdk@a9361c54...` framework pressure test covering model-driven control, Graph/Swarm/Workflow, state/session/memory, budgets, concurrency, interventions, observability, evals and protocol boundaries. **Historical candidate states inside this quarry are superseded for current status by `systems/strands/` and later MK1 gates.**
- [`runtime-semantics-strands-langgraph-openai.md`](./runtime-semantics-strands-langgraph-openai.md) — cross-runtime synthesis that validates concurrency semantics, budget-enforcement boundaries and intervention ownership across Strands Agents, LangGraph and OpenAI Agents SDK, promoting them into MK1 schema revision `mk1-draft-2026-09-16.1`.
- [`strands-mcp-2026-07-28-compatibility.md`](./strands-mcp-2026-07-28-compatibility.md) — revision-aware interoperability receipt for Strands Python against MCP `2026-07-28`, including a modern-only lifecycle fixture, upstream CI execution, MRTR/list-change behavior, trace continuity and explicit auth/cancellation qualifications.

- [`reproducible-multimodal-agent-workflows.md`](./reproducible-multimodal-agent-workflows.md) — S-114 synthesis covering skill/recipe/capability separation, build-time generative dependencies, deterministic artifact normalization, cost-aware retries, provenance manifests, generated-media budgets and graceful degradation.

- [`understand-anything-code-intelligence.md`](./understand-anything-code-intelligence.md) — `Egonex-AI/Understand-Anything@6df3065f...` pressure test for deterministic-vs-semantic responsibility, topology-aware context partitioning, durable graph freshness, incremental reconciliation, bounded retry and fail-closed publication.

- [`repository-harness-engineering-refinements.md`](./repository-harness-engineering-refinements.md) — S-115 synthesis refining repository-level harness mechanics: revision-bound verification, externalized acceptance authority, clean handoff gates, review-feedback promotion, actionable diagnostics, context operations, concurrency admission and harness-pruning pressure tests.

## REC-012 — evidencia separada por procedencia (G7 PASS / QUALIFIED_UPSTREAM)

- [`rec-012-offline-topology-baseline.md`](./rec-012-offline-topology-baseline.md) — experimento **ejecutado localmente** con actores deterministas, no LLM; conserva su decisión histórica OPEN de ese momento.
- [`multiagent-external-scaling-evidence.md`](./multiagent-external-scaling-evidence.md) — investigaciones S-118/S-119 con LLM reales, estudio 260-cell outcome CSV re-aggregated y comparación de latencia por estudio separado; [REC-012](../mk/MK1/records/REC-012-external-agent-scaling.md) `MATERIALIZED / QUALIFIED_UPSTREAM`, sin modelo local.
- [Código reproducible y resultados](../experiments/rec-012/README.md); [draft no materializado](../mk/MK1/records/REC-012-deterministic-topology-draft.md).

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
source receipt
  ↓
quarry evidence
  ↓
MK1 normalize/classify
  ↓
systems/<system>/ current synthesis
  ↓
MK2 operational contracts/tests
  ↓
MK5+ certification
```


## Langflow (S-117) — non-canonical knowledge intake

- [`langflow-workflow-engineering.md`](./langflow-workflow-engineering.md) — five evidence-bounded tracks: executable graphs, JSON contracts, versioning, lightweight headless execution, observability/evaluation; each has failure modes and proposed tests (NOT RUN).
- [`langflow-adoption-transfer.md`](./langflow-adoption-transfer.md) — explicit `ADOPT KNOWLEDGE / HOLD SOFTWARE ADOPTION` for personal_knowledge, Prompt Machine, Foundry, Content Seller/NINFA, ECHO and Logan Garage. No dependency, deployment or MK promotion.
- Pinned evidence: [`S-117-langflow.md`](../mining-site/S-117-langflow.md).
