# Langflow — Adoption and transfer decision

Status: **RESEARCH DECISION / QUARRY_ONLY / NON-CANONICAL**  
Date: 2026-10-12  
Inputs: [S-117](../mining-site/S-117-langflow.md) and [five-track extraction](./langflow-workflow-engineering.md).

## Decision

**ADOPT KNOWLEDGE; HOLD SOFTWARE ADOPTION.**

No Langflow server, `lfx`, vendor bundle, Docker service, provider key, package-lock edit, workflow migration, new flagship, or production change is authorized by this study.

## Relevance matrix (not a roadmap)

| Workspace/product | Valuable candidate lesson | Decision | Evidence needed before build |
|---|---|---|---|
| `personal_knowledge` / `agent-engineering` | pinned receipts; graph/runtime contracts; version drift; policy/observability | record in source/quarry only | second source, schema pressure and MK promotion gate |
| Prompt Machine | vendor-neutral certified workflow specification, portability, evaluator and receipts | INSPIRED candidate; **no dependency** | concrete workflows, acceptance metrics and schema/adapter decision |
| `em3rc0d-foundry` | compilation from typed workflow spec to executable artifacts, versioned adapters | explore only if linked to an admitted Foundry use case | preservation of contract, reproducibility, cost, consumer demand |
| Content Seller / NINFA | conditional orchestration, approval and side-effect receipts for scheduled publication/media | hold; do not replace existing implementation | demonstrated unmet workflow + comparison to simpler orchestration |
| ECHO | no clear value for primary acoustic event detection/classification | do not integrate | a directly relevant requirement and controlled improvement |
| Logan Garage | contrary to edge/local-first lightweight Android MVP | reject integration for core app | explicit change in product gate and on-device cost justification |

These are **project fit evaluations** (`INFERRED/INSPIRED`), not measurements or new project decisions.

## Prompt Machine — bounded candidate contract

Candidate lifecycle (GENERATED; **not** official Langflow schema):

```text
goal / use-case
 → WorkflowSpec (owned by Prompt Machine)
 → semantic validation / permissions / schema version
 → optional adapter per runtime
 → execution with bounded resources
 → trace and evidence receipt
 → evaluator separate from generator
 → versioned certification decision
```

Invariants to test **before** any adoption:
- identity and typed node contracts independent of an editor;
- deterministic validator rejects unsupported semantics;
- no secrets in export, clear egress and side-effect policies;
- runtime adapter has capability/compatibility matrix;
- outcome judged against independent acceptance criteria;
- actual user-value/cost comparison with an existing simpler baseline.

Do not assume `langflow` JSON itself meets this contract. No schema or executor implementation created here.

## Foundry — candidate adapter rule

If a future approved use case needs interoperability, prototype **one boundary adapter** (not a fork or full orchestration platform). Adapter translates from a Foundry-owned specification to a pinned engine version and produces proof of conversion, feature loss and a runtime receipt.

Entry gate: admitted user-facing need + specific supported nodes + defined fixture + rollback strategy + engineering budget. No default platform dependency.

## Security and operational admission gate (future only)

- pinned source/runtime/build identity and license inventory;
- explicit authentication, authorization and secret storage;
- isolate any arbitrary-code component by executed negative tests;
- authorization for MCP tools and per-dispatch side effects;
- persistence/concurrency/idempotency semantics demonstrated under restart and retry;
- metrics: latency distribution, CPU/RAM, API/token cost, time to author/debug, failure and rework rate;
- comparison to existing code-based alternative on same workload;
- independent evaluator/canary criteria and migration rollback path.

If these cannot be measured, decision remains `HOLD` or `NO_GO`. Feature-count comparisons and framework publicity are insufficient.

## Non-goals

- No new `systems/langflow` canonical package in this pass.
- No modification of MK1 records, classification schema or REC-012.
- No new development plan/sprint triggered by research alone.
- No automatic transfer of external source license assumptions to bundled integrations.
- No GitHub Actions, paid cloud runner or background service.
- No changes to Prompt Machine, Foundry, Content Seller, NINFA, ECHO or Logan Garage repositories.

## Close condition for this research intake

`S-117` pinned + five tracks mined + adoption decision recorded + repository source/quarry indexes updated + links verified. **Research intake done** is not **runtime certified**.

Review/reassess on an explicit product problem or meaningful upstream breaking/security revision; otherwise avoid spending maintenance effort tracking this source continuously.
