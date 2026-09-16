# Strands Agents — MK1 Classification

Status: **CURRENT NORMALIZED PROFILE**  
Schema: `mk1-draft-2026-09-16.1`  
Evidence baseline: `strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20`

## Scope

This record classifies the **Strands SDK family and built-in architecture surfaces**, not a particular application deployed with Strands.

Fields whose concrete value depends on registered tools, model/provider, storage backend or application policy are intentionally omitted or marked `unknown`. Framework capability must not be converted into a claim about every application.

```yaml
schema_revision: mk1-draft-2026-09-16.1

identity:
  name: Strands Agents SDK
  source: https://github.com/strands-agents/harness-sdk
  snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
  evidence_state: QUALIFIED

control:
  primary_authority: mixed
  horizon: bounded_multistep
  topology: mixed
  model_count: application/topology-dependent

capabilities:
  capability_compositions:
    - registered tool authority composes with host-process permissions
    - MCP/A2A endpoints can extend reachable remote capabilities
    - agent-as-tool and Graph/Swarm composition can transitively expand reachable capabilities

side_effects:
  class: unknown
  reversible: unknown
  external_mutation: application-defined
  data_egress: unknown
  verification: application-defined; framework execution success is not external outcome proof

state:
  runtime_state: structured
  checkpointing: durable
  persistence_backend: local files / S3 / custom / repository-style managers depending surface
  replay_semantics: partial
  invocation_concurrency: framework_defined
  writer_model: single_writer
  concurrency_conflict_semantics: overlapping agent invocation is constrained; documented session model assumes one live writer per conversation; external shared state remains application-defined
  locking: none

memory:
  semantic_role:
    - cross_session_knowledge
    - recall
    - context_injection
    - durable_memory_extraction
  scope: cross_session
  persistence: remote_durable
  retrieval_policy: configurable search and/or pre-model injection
  write_policy: explicit add and/or configurable extraction
  isolation_key: store/scope dependent
  retention_policy: backend/application dependent
  provenance: store/application dependent

human_control:
  level: mixed
  mode: mixed
  dispatcher_enforcement: partial
  enforcement_owner: mixed
  enforcement_boundary: hooks/human confirmation can gate before tools; LLM steering is guidance unless backed by a deterministic policy boundary
  approval_binding: application-defined; edited arguments must be treated as a new action when policy requires exact binding

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: provider/runtime/tool/application dependent
  idempotency: tool/application dependent
  unknown_outcome_handling: tool/application dependent

termination:
  success_predicate: default loop termination/end-turn is runtime completion, not proof of external task success
  terminal_failure_predicate: runtime stop reason / exception / application policy
  turn_budget: supported per invocation
  turn_budget_enforcement: loop-boundary / soft with respect to in-flight work
  tool_budget: no universal framework-wide tool-count budget established by current evidence
  tool_budget_enforcement: unknown
  time_budget: cancellation/timeout composition available; exact effect depends on execution path
  time_budget_enforcement: cooperative/boundary-dependent for arbitrary in-process tools
  cost_or_token_budget: output-token and total-token limits supported
  cost_or_token_budget_enforcement: loop-boundary checks
  overshoot_semantics: an in-flight model turn can exceed a nominal token cap and already-dispatched tool work may finish before the next limit check
  oscillation_detection: application/steering/evaluation dependent
  cancellation: cooperative / remote best-effort depending path
  cancellation_effective_boundary: runtime safe points; tool cooperation or remote protocol behavior may be required after dispatch

evaluation:
  static_contracts:
    - structured output validation
    - deterministic evaluators
  unit_integration:
    - upstream SDK tests
    - protocol integration fixtures
  trajectory:
    - trace evaluation
    - tool-use/trajectory evaluators
  outcome:
    - output evaluators
    - session evaluators
    - custom project evaluators
  repeated_trials: false
  regression_gate: false
  production_observability: true

protocols:
  - name: MCP
    revision: "2026-07-28"
    role: client / external capability consumer
    transport: Streamable HTTP tested upstream; additional MCP transports available through SDK integration
    capabilities:
      - modern server/discover lifecycle
      - tools/list
      - tools/call
      - structured tool results
      - multi-round-trip input-required flow
      - prompts
      - resources
      - tools-list change subscription
      - task extension support
      - trace propagation
    auth_model: client-credentials adapter supported; deployed authorization remains endpoint/application-specific
    extensions:
      - SEP-2322 multi-round-trip input
      - SEP-2663 tasks when configured/supported

  - name: A2A
    revision: unknown
    role: remote-agent interoperability
    transport: network service / implementation dependent
    capabilities:
      - remote agent invocation/delegation surfaces
    auth_model: unknown
    extensions: unknown

security:
  trust_boundaries:
    - host process
    - model provider
    - registered tool implementations
    - MCP/A2A remote endpoints
    - session storage
    - memory storage
    - deployment infrastructure
  least_privilege: partial
  sandbox: none
  data_classification: application-defined
  receipts:
    - tool/model OpenTelemetry surfaces available
    - MCP modern trace continuity tested upstream
    - framework documentation explicitly places tool permission responsibility on host/application boundary

reproducibility:
  model_receipt: application must pin provider/model/config
  dependency_receipt:
    repository: strands-agents/harness-sdk
    snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
    python_release_observed: python/v1.56.0
    typescript_release_observed: typescript/v1.18.0
  external_api_receipt: deployment-specific
  execution_evidence:
    framework_source_inspection: PASS
    runtime_crosscheck: PASS
    mcp_2026_07_28_upstream_ci: PASS
    mcp_trace_continuity_upstream_ci: PASS
    independent_local_mcp_rerun: NOT_RUN_ENVIRONMENT_BLOCKED

unknowns:
  - A2A exact revision/auth/transport execution receipt
  - distributed concurrency semantics of each concrete persistence backend
  - application-specific idempotency and unknown-outcome recovery
  - hard containment for arbitrary host-process tools
  - exact Python/TypeScript feature parity as releases evolve
  - benchmarked benefit of Graph/Swarm/agents-as-tools against simpler baselines
  - repeated/adversarial reliability of LLM-mediated steering
  - external protected-server OAuth E2E behavior for a concrete MCP deployment
  - remote side-effect state when cancellation occurs after execution has begun
```

## Important reading notes

### `checkpointing: durable` does not mean every Strands agent persists

It means the framework exposes durable-capable session/state mechanisms. A concrete application must still identify the manager/backend it actually uses.

### `writer_model: single_writer` is not a universal database theorem

It records the documented live-session assumption relevant to Strands session handling. External databases or custom managers may implement stronger concurrency semantics and must be classified separately.

### `sandbox: none` means no core security sandbox is implied

A deployment may add containers, VMs, managed runtimes or capability-specific isolation. Those are application/deployment facts, not inferred framework properties.

### Evaluation booleans do not certify project quality

The SDK provides evaluation and observability surfaces. `repeated_trials: false` and `regression_gate: false` intentionally mean those controls are not automatic properties of merely using Strands.

## Historical promotion path

The first Strands pressure test could not cleanly encode:

- concurrency semantics;
- budget enforcement boundary;
- intervention enforcement owner.

Those fields were held as candidate dimensions rather than immediately changing the schema. Independent evidence from LangGraph and OpenAI Agents SDK later confirmed all three, producing `mk1-draft-2026-09-16.1`.

That sequence matters: **the classification schema changed because a reusable engineering distinction survived cross-runtime pressure, not because Strands had a feature name for it.**

## Related documents

- schema definition: [`../../mk/MK1/CLASSIFICATION_SCHEMA.md`](../../mk/MK1/CLASSIFICATION_SCHEMA.md)
- dimension definitions: [`../../mk/MK1/DIMENSIONS.md`](../../mk/MK1/DIMENSIONS.md)
- normalization rules: [`../../mk/MK1/NORMALIZATION_RULES.md`](../../mk/MK1/NORMALIZATION_RULES.md)
- cross-runtime promotion evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md)
- Strands raw processed evidence: [`../../quarries/strands-agents.md`](../../quarries/strands-agents.md)
