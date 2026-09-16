# S-109 — Strands Agents

Status: **REGISTERED / OFFICIAL + OBSERVED**  
Observed: **2026-09-16**

## Source identity

| Field | Value |
|---|---|
| ID | `S-109` |
| System | Strands Agents |
| Type | open-source agent SDK / official documentation / official source repository |
| Documentation | https://strandsagents.com |
| Repository | https://github.com/strands-agents/harness-sdk |
| Snapshot | `a9361c54ca190117d5801dd09a1ab8d6d3d9bf20` |
| Snapshot date observed | 2026-09-16 |
| Python release observed | `python/v1.56.0` published 2026-09-15 |
| TypeScript release observed | `typescript/v1.18.0` published 2026-09-15 |
| License | Apache-2.0 |
| Use here | MK1 framework pressure test; runtime/state/tool/multi-agent/eval/protocol comparison |
| Authority | official for Strands-specific behavior; not normative for general agent engineering |
| Confidence | HIGH for documented/source-specific facts; VARIABLE for general claims of superiority or production readiness |

## Canonical project state at observation

The active repository is `strands-agents/harness-sdk`. It contains the Python SDK, TypeScript SDK, documentation site and supporting packages. Earlier standalone repositories were consolidated/archived during 2026.

This matters for reproducibility: old links and package-era assumptions must not be treated as current source topology.

## Primary slices inspected

- root monorepo README;
- Agent Loop and invocation limits;
- Tools Overview / custom tools;
- Hooks / plugins / steering / interventions;
- State Management;
- Session Management;
- Conversation Management;
- Memory;
- Structured Output;
- Graph / Swarm / Workflow / Agents-as-Tools;
- MCP integration;
- A2A integration;
- Observability / OpenTelemetry / metrics;
- Strands Evals SDK;
- Responsible AI / Guardrails;
- production operations/deployment guidance;
- model-provider matrix;
- release metadata and repository-consolidation history;
- MCP `2026-07-28` compatibility docs/source/integration fixtures and upstream CI receipts.

## Official external context inspected

AWS Open Source / AWS AI posts:

- Introducing Strands Agents — 2025-05-16;
- Strands Agents 1.0 — 2025-07-15;
- technical deep dive into architectures and observability — 2025-07-31;
- model-driven approach — 2025-09-12;
- Agent SOPs — 2025-11-20;
- Strands Labs — 2026-02-23;
- Open Protocols with Strands Agents SDK — 2026-07-16.

## MCP `2026-07-28` execution evidence

At the pinned snapshot, the Python SDK declares `mcp>=1.23.0,<2.2`; its migration documentation states that normal installs resolve to the newest accepted 2.x line while CI separately retains 1.x compatibility coverage.

The source contains a dedicated 2.x compatibility layer and an integration suite that:

- runs MCP 2.x's real `MCPServer` over Streamable HTTP;
- rejects any legacy `initialize` request with HTTP `405`;
- verifies modern connection negotiation;
- exercises tools, structured results, errors, multi-round-trip input, prompts, resources and tools-list change subscription behavior.

Upstream PR `#4129` introduced the dedicated MCP 2.x integration fixture and merged with a successful CI run. The `Python / MCP 2.x Compat` job explicitly installed MCP 2.x and ran the integration tests. PR `#4131` separately added an end-to-end MCP 2.x OpenTelemetry continuity test and merged successfully.

Evidence state:

```text
MCP 2026-07-28 core interoperability  SUPPORTED / UPSTREAM-EXECUTED
modern lifecycle vs initialize        DIRECTLY REGRESSION-TESTED
trace continuity                      UPSTREAM E2E TESTED
auth adapter compatibility            SOURCE/UNIT SUPPORTED
external protected-server OAuth E2E   DEPLOYMENT-SPECIFIC / OPEN
remote-effect rollback on cancel      NOT IMPLIED
independent local reproduction        NOT RUN — ENVIRONMENT NETWORK BLOCKED
```

Detailed receipt: [`../quarries/strands-mcp-2026-07-28-compatibility.md`](../quarries/strands-mcp-2026-07-28-compatibility.md).

## Legal / reuse boundary

Apache-2.0 permits broad reuse subject to its license requirements. This knowledge base still prefers independent synthesis over copying implementation because the objective is framework-independent engineering knowledge rather than code mirroring.

## Promotion boundary

Use `S-109` to:

- pressure-test MK1 dimensions;
- extract runtime and state semantics;
- compare control topologies;
- identify missing schema qualifiers;
- cross-check existing invariants;
- provide a revision-aware MCP interoperability case with pinned execution receipts.

Do not use `S-109` alone to:

- certify model-driven orchestration as universally superior;
- certify a Strands application as production-ready;
- infer tool safety from schema typing;
- infer hard authorization from LLM steering;
- infer protocol security from MCP/A2A support;
- infer authenticated authorization correctness from an unauthenticated local MCP fixture;
- infer transactional rollback from cancellation signaling;
- infer multi-agent performance improvement without task-level evidence.

Processed evidence: [`../quarries/strands-agents.md`](../quarries/strands-agents.md)  
MK1 pressure test: [`../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)  
MCP compatibility receipt: [`../quarries/strands-mcp-2026-07-28-compatibility.md`](../quarries/strands-mcp-2026-07-28-compatibility.md)
