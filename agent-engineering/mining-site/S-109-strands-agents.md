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
- release metadata and repository-consolidation history.

## Official external context inspected

AWS Open Source / AWS AI posts:

- Introducing Strands Agents — 2025-05-16;
- Strands Agents 1.0 — 2025-07-15;
- technical deep dive into architectures and observability — 2025-07-31;
- model-driven approach — 2025-09-12;
- Agent SOPs — 2025-11-20;
- Strands Labs — 2026-02-23;
- Open Protocols with Strands Agents SDK — 2026-07-16.

## Legal / reuse boundary

Apache-2.0 permits broad reuse subject to its license requirements. This knowledge base still prefers independent synthesis over copying implementation because the objective is framework-independent engineering knowledge rather than code mirroring.

## Promotion boundary

Use `S-109` to:

- pressure-test MK1 dimensions;
- extract runtime and state semantics;
- compare control topologies;
- identify missing schema qualifiers;
- cross-check existing invariants.

Do not use `S-109` alone to:

- certify model-driven orchestration as universally superior;
- certify a Strands application as production-ready;
- infer tool safety from schema typing;
- infer hard authorization from LLM steering;
- infer protocol security from MCP/A2A support;
- infer multi-agent performance improvement without task-level evidence.

Processed evidence: [`../quarries/strands-agents.md`](../quarries/strands-agents.md)  
MK1 pressure test: [`../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)
