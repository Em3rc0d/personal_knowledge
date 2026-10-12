# Langflow — Workflow Engineering Quarry (five tracks)

Status: **NON-CANONICAL / QUARRY_ONLY**  
Source: [S-117 pinned receipt](../mining-site/S-117-langflow.md)  
Observed: 2026-10-12  
Purpose: extract framework-agnostic patterns from Langflow; do not import its runtime or certify them by association.

## Research question

What reusable execution and governance patterns can be learned from a visual AI workflow platform **without** making the visual editor, Python packages or provider SDKs mandatory dependencies?

```text
authoring surface / canvas
          ↓
serialized persisted graph (versioned)
          ↓
validation + compatibility
          ↓
execution owner (full app OR LFX-style lightweight worker)
          ↓
trace / receipt / outcome verification
```

This is an **INSPIRED synthesis**, not an exact description of every upstream execution path.

## Track 1 — Executable graphs

**Evidence:** `AGENTS.md` and `ARCHITECTURE.md` differentiate React graph authoring from FastAPI services and LFX primitives. Upstream graph testing builds components, connects via `.set()`, drives `async_start` and asserts outputs.

**Candidate principle G-01 (INSPIRED):** graph *definition*, validation, execution scheduling, and display state are separate responsibilities. Do not infer execution truth from node UI state.

**Candidate principle G-02 (INFERRED):** compilation/planning should check node IDs, reference resolution, port-type compatibility, dependency cycles, credential references and policy-bound side effects before a run. This check set is a **proposal**, not a claim that Langflow currently implements all of it.

**Failure modes:** invalid node references; UI says success while an external side effect failed; hidden parallel races; implicit retry duplicates.

**Future acceptance tests (NOT RUN):**
- known graph → expected output and canonical event sequence;
- unknown node/input/output → typed fail-closed validation error;
- dependency cycle without explicit loop semantics → reject;
- aborted run → output `STOP_REQUESTED` vs confirmed terminal state distinguished;
- `run completed` does not assert `external objective achieved`.

## Track 2 — JSON contracts and portability

**Evidence:** `docs/agents/CONTRACTS.md` lists component class identifiers, `name`, inputs, output order/types, defaults, `data.nodes[*].data.node` and `data.edges` as persistence-sensitive contracts. `LFX README` supports loading flow JSON.

**Candidate principle J-01 (INFERRED):** a workflow JSON artifact is an API across time, not disposable editor state. Version its semantics, not only its syntax.

**Candidate principle J-02 (INSPIRED):** keep a **vendor-neutral canonical definition** and explicit adapters to Langflow or other engines *if a real use case proves portability value*. Do not adopt upstream JSON as Prompt Machine's canonical format by default.

**Generated candidate semantic fields (NOT Langflow schema):**
```yaml
spec_version: 0.1.0
workflow_id: example
graph:
  nodes: []
  edges: []
execution:
  side_effect_policy: deny_by_default
  retry_policy: explicit
evidence:
  source_revision: required
  evaluator_version: required
```

**Future acceptance tests (NOT RUN):**
- JSON Schema parse + domain rules + discriminated revision;
- lossless round-trip for supported fields; unknown critical field triggers rejection;
- deterministic normalization/diff that does not remove semantic IDs;
- prohibit embedding plaintext secrets in exported artifacts;
- rejected/unsupported nodes yield explainable diagnostics.

## Track 3 — Versioning, backwards compatibility, upgrades

**Evidence:** upstream `CONTRACTS.md` describes stable component identifiers, additive defaults, legacy replacement patterns, database migrations and saved-flow compatibility. `ANTI-PATTERNS.md` documents historical regressions associated with component/field changes.

**Candidate principle V-01 (INFERRED):** treat `input.name`, output type/order, node class/path, default values and side-effect semantics as behavioral contracts. A valid JSON file can still be an incompatible workflow.

**Candidate principle V-02 (INSPIRED):** maintain a compatibility matrix: `spec_version × adapter_version × runtime_version × component_version × provider_model_revision`.

**Future acceptance tests (NOT RUN):**
- fixtures from N previous schema revisions load or fail with named migration;
- old/defaulted values reproduce unchanged behavior within defined tolerance;
- adapter release cannot silently remap a node/port ID;
- migration is versioned, explicit and reversible where applicable;
- re-export produces a meaningful change diff and records migrated provenance.

**Anti-pattern:** upgrade dependency names or tool/model IDs based on guesses. Pin/retrieve observed versions before applying a migration.

## Track 4 — Headless execution and dependency boundaries

**Evidence:** `src/lfx/README.md` describes `lfx run`, `lfx serve`, `lfx-mcp`, `lfx validate/export/push/pull`; standalone LFX uses `NoopSession` and cannot persist users, flows, messages like the full application. Packages `lfx`, `langflow-base` and provider bundles define dependency boundaries.

**Candidate principle H-01 (INFERRED):** use the **cheapest sufficient runtime**. Authoring/registry UI may be optional at execution time; any necessary persistence must be supplied explicitly.

**Candidate principle H-02 (INSPIRED):** a portable execution interface should explicitly declare capabilities:
```text
requires: secrets | network | persistence | user_identity | gpu | side_effects
provides: invocation | output | events | receipt | cancellation_semantics
```
This vocabulary is a proposed abstraction, not a Langflow API.

**Future acceptance tests (NOT RUN):**
- headless flow without installed full Langflow UI;
- same supported graph produces equivalent **semantic output** (not presumed identical timing) in two target modes;
- request without required persistence is rejected before execution;
- bounded timeouts and resource budgets; no implicit remote network access;
- no proprietary/project runtime added merely for a visual prototype.

## Track 5 — Observability, evaluation and evidence

**Evidence:** backend pyproject includes OpenTelemetry SDK/exporters and integrations; workflow v2 route exposes job status, stop/resume and streaming event surfaces; README advertises observability integrations. None of these imply externally verified tasks.

**Candidate principle O-01 (INFERRED):** distinguish logs, traces, metrics, test fixtures, evaluator decisions and real-world outcomes. Traces are execution evidence, not automatic success certificates.

**Candidate principle O-02 (INSPIRED):** minimal future execution receipt:
```yaml
workflow_spec_sha256: required
runtime_identity: required
adapter_version: optional
attempt_id: required
started_at: required
ended_at: optional
terminal_state: required
side_effects: []
output_artifact_hashes: []
policy_decisions: []
evaluation:
  outcome: UNKNOWN
  trajectory: UNKNOWN
```
This is a **candidate design**, not a deployed schema.

**Future acceptance tests (NOT RUN):**
- correlation `request_id → run_id → node/attempt → tool action`;
- redact secrets and sensitive payloads before emission;
- capture retry/cancellation/approval boundary and side-effect receipts;
- distinguish `completed`, `failed`, `timed_out`, `cancelled`, `unknown`;
- evaluator independently checks outcome versus trace trajectory;
- benchmark claims require repeated runs, workloads, cost and environment identity.

## Cross-cutting trust boundaries

| Boundary | Risk | Candidate gate |
|---|---|---|
| User/editor → stored JSON | malicious or stale component config | parse, typecheck, revision pin |
| Graph → code-execution component | arbitrary host effects | sandbox/allowlist verified on target |
| Agent tool → MCP | capability mistaken for authorization | transport auth + per-action policy |
| Resume/retry → external API | duplicate publication/charges | idempotency and receipts |
| Background queue → cancellation | false rollback claim | explicit stop/effect semantics |
| Flow exports → secret store | credential exfiltration | secret references only |
| Observability → external collector | sensitive context egress | redaction and retention controls |
| Visual graph → product deployment | heavy dependency load | measured cost/value gate |

**Specific source qualification:** `AGENTS.md` describes an OSS pass-through authorization service; no assumption of enforced RBAC without checking effective deployment policies. `lfx` metadata includes an optional sandbox dependency; existence does not prove isolation is enabled.

## Contradictions / source-document drift

- One upstream architecture document presents `langflow → langflow-base → lfx` with `lfx-*` bundles; `AGENTS.md` also refers to `langflow-core` as an intermediate package. The inspected root `pyproject.toml` declares `langflow-base` and `lfx-*` directly; use the pinned manifests as the package-dependency evidence.
- Upstream README's `enterprise-ready` language is **SOURCE CLAIM**, not proof of production security or throughput.
- A platform supporting MCP does not establish compatibility with every MCP revision, client auth scheme or deployment topology.
- Lightweight headless is not the same as a stateful server with user/message storage.

## Reusable primitives (quarry only)

`graph_spec`, `node_contract`, `port_contract`, `runtime_adapter`, `capability_manifest`, `flow_migration`, `run_receipt`, `trace_span`, `outcome_evaluation`, `version_matrix`, `trust_boundary`.

No automatic promotion into MK1 taxonomy. Existing terms may already cover them; deduplicate before considering new records.

## UNKNOWN / no-promotion list

- independent runtime reliability, benchmarks, performance and operating costs;
- effective security of any chosen deployment and plugin configuration;
- flow portability coverage across LFX/other engines;
- exact compatibility of every deployed MCP transport/revision;
- incremental benefit over simpler Python/TypeScript DAG orchestrators;
- legal posture of third-party dependencies/assets.

**No-pass:** no new flagship, no runtime adoption, no SDK install, no MK2 promotion and no change to REC-012 on this evidence.
