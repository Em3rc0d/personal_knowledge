# S-117 — langflow-ai/langflow

Status: **SOURCE RECEIPT / QUARRY_ONLY / NON-CANONICAL**  
Observed: **2026-10-12**  
Scope: static code/documentation analysis only; no install, execution, security exploitation, benchmark or product adoption.

## Source identity and custody

| Field | Value |
|---|---|
| ID | `S-117` |
| Input pointer | https://github.com/langflow-ai/langflow |
| Resolved primary repository | https://github.com/langflow-ai/langflow |
| Owner | langflow-ai |
| Observed `main` SHA | `504c02fc47e76087b82b0e7cbe4186e9cdd916d4` |
| Package version in `pyproject.toml` | `1.12.5` at inspected revision; this is **not** proof of latest PyPI/release |
| License signal | MIT, as stated in root `README.md` and `pyproject.toml` |
| Languages/frameworks observed | Python/FastAPI, TypeScript/React/Vite, graph editor via `@xyflow/react` |
| Source authority | upstream is primary evidence of its code/manifests and documentation; not proof of operational reliability |
| Capture | selected pinned source files and README; not exhaustive repository clone |
| Confidence | HIGH for selected inspected manifests/docs; MEDIUM for inferred architectural benefits; UNKNOWN for target deployments |
| Promotion | QUARRY_ONLY; no MK1 schema, records, gates, or product runtime modified |

**Pinned root:** https://github.com/langflow-ai/langflow/tree/504c02fc47e76087b82b0e7cbe4186e9cdd916d4

## Inspected evidence (all links pinned)

- [README](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/README.md) — upstream feature claims: visual workflows, APIs, MCP, JSON export, deployment, desktop, installation.
- [Root pyproject](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/pyproject.toml) — `langflow` distribution metadata, optional bundles, workspace composition, versions/license.
- [Backend base pyproject](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/src/backend/base/pyproject.toml) — `langflow-base`, FastAPI, models, telemetry and persistence dependencies.
- [LFX pyproject](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/src/lfx/pyproject.toml) — isolated executor package and optional integrations.
- [LFX README](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/src/lfx/README.md) — `lfx run`, `lfx serve`, `lfx-mcp`, Flow DevOps tooling and statelessness limitations.
- [Frontend package.json](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/src/frontend/package.json) — React 19, TypeScript, Zustand and graph UI dependencies.
- [Architecture boundaries](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/docs/agents/ARCHITECTURE.md) — upstream package boundary rules and known violations.
- [User-facing contracts](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/docs/agents/CONTRACTS.md) — components, persisted-flow shape, backwards compatibility and migrations.
- [Testing guide](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/docs/agents/TESTING.md) — graph test style, fixtures and environment/test caveats.
- [Anti-patterns](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/docs/agents/ANTI-PATTERNS.md) — upstream regression claims linked to commits (not independently reproduced).
- [Repository AGENTS.md](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/AGENTS.md) — development conventions, security notes and system guidance.
- [Workflow v2 route](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/src/backend/base/langflow/api/v2/workflow.py) — background/stream/sync, job status, stop, HITL resume and event stream.
- [MCP v1 route](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/src/backend/base/langflow/api/v1/mcp.py) — MCP tools/resources endpoints and transport handling.
- [Docker compose example](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/docker_example/docker-compose.yml) — app + PostgreSQL + persistent volume illustration.
- [Security policy](https://github.com/langflow-ai/langflow/blob/504c02fc47e76087b82b0e7cbe4186e9cdd916d4/SECURITY.md) — vulnerability reporting process; **not** evidence of secure-by-default operation.

## Source observations vs claims

1. **OBSERVED:** `langflow` is a curated distribution depending on `langflow-base` and `lfx-*` packages; `langflow-base` depends on `lfx`. `lfx` has a separately installable package and CLI.
2. **OBSERVED:** frontend declares React, TypeScript, Zustand and `@xyflow/react`; application API/backend are Python/FastAPI.
3. **SOURCE CLAIM + CODE SURFACE:** flows are created visually and can be exposed over REST/MCP. V1 MCP router and v2 workflow endpoints exist; this is not a live compatibility/security test.
4. **OBSERVED:** LFX README explicitly says standalone LFX uses `NoopSession` and does **not** persist saved flows, users or messages as the full application does.
5. **OBSERVED:** upstream lists component name/path/input/output/defaults and JSON shape among persisted public contracts; extension changes can break saved graphs.
6. **OBSERVED:** package docs define LFX environment and server environment separately, and recommend bundle boundary discipline.
7. **OBSERVED:** workflow route documents synchronous, streaming and durable background modes, stop/pending/resume/event status surfaces. Code inspection alone does not establish exactly-once effects or safe cancellation.
8. **OBSERVED:** optional sandbox backend exists in `lfx` metadata; installed package/execution isolation is not automatic or verified.
9. **OBSERVED:** `AGENTS.md` describes an OSS authorization pass-through implementation. Feature existence does not establish strict RBAC without a suitable enforcement plugin.
10. **OBSERVED:** `docs/agents/ARCHITECTURE.md` and `AGENTS.md` present somewhat different packaging narratives (e.g. `langflow-core`); root manifests are stronger evidence of actual declared dependencies at this revision.

## Material limitations / negative evidence

- No full-code coverage claim: selected files only.
- No executed tests, load benchmark, Docker launch, security test, numerical performance result or independent deployment audit.
- No verified claim about third-party advisories in this receipt; vulnerability assessment requires issue/advisory IDs, affected-version mapping and independent validation.
- No conclusion that visual editing automatically improves reliability; runtime and evaluator must still pass project-specific gates.
- Headless is not a synonym for offline, stateless, free, secure or deterministic execution.
- MIT permissiveness is a license signal at root; third-party bundle/assets/dependencies require separate license evaluation before distribution.

## Outputs and reuse

- [Five technical tracks quarry](../quarries/langflow-workflow-engineering.md).
- [Adoption and transfer decision record](../quarries/langflow-adoption-transfer.md).

**No promotion:** source receipt + quarries only. MK1 remains active/unchanged; no new canonical `systems/langflow` package, REC-012 completion, MK2 advancement, dependency addition or build authorization.
