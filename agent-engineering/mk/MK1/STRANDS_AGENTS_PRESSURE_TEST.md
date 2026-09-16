# MK1 Pressure Test — Strands Agents

Status: **HISTORICAL PRESSURE-TEST RECEIPT / SUBSEQUENT GATES RESOLVED**  
Observed: **2026-09-16**  
Primary source snapshot: `strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20`

Detailed quarry: [`../../quarries/strands-agents.md`](../../quarries/strands-agents.md)  
Current canonical synthesis: [`../../systems/strands/README.md`](../../systems/strands/README.md)

## Resolution notice

This file intentionally preserves the **first MK1 pressure-test state**. It is valuable because it shows which distinctions Strands surfaced *before* they had independent support.

Do not use the candidate/UNKNOWN labels below as the current status.

Subsequent evidence resolved the major debts from this first pass:

```text
concurrency semantics
  → independently confirmed with LangGraph + OpenAI Agents SDK
  → PROMOTED under state

budget enforcement boundary
  → independently confirmed with LangGraph + OpenAI Agents SDK
  → PROMOTED under termination

intervention enforcement owner/boundary
  → independently confirmed with LangGraph + OpenAI Agents SDK
  → PROMOTED under human_control

Strands ↔ MCP 2026-07-28 core compatibility
  → modern-only lifecycle fixture + upstream CI + trace receipt
  → SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED
```

Current schema: [`./CLASSIFICATION_SCHEMA.md`](./CLASSIFICATION_SCHEMA.md) — `mk1-draft-2026-09-16.1`  
Cross-runtime receipt: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md)  
MCP receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md)  
Current Strands classification: [`../../systems/strands/CLASSIFICATION.md`](../../systems/strands/CLASSIFICATION.md)

The unresolved multi-agent benchmark question remains open.

## Purpose

Pressure-test the MK1 classification schema against a modern framework that intentionally supports several control authorities inside one SDK: model-directed loops, deterministic workflows, structured graphs, peer swarms, agents-as-tools, persistent sessions, long-term memory, hooks/interventions, open protocols, observability and evaluation.

The record below classifies the **SDK family and its built-in architecture surfaces**, not a specific deployed application. Application-dependent fields stay `variable` or `UNKNOWN` rather than being inferred from framework capability.

## Historical normalized classification at first pass

The YAML below is preserved as the classification **before** `mk1-draft-2026-09-16.1` added the cross-runtime qualifiers. For the current normalized record, use [`../../systems/strands/CLASSIFICATION.md`](../../systems/strands/CLASSIFICATION.md).

```yaml
identity:
  name: Strands Agents SDK
  source: https://github.com/strands-agents/harness-sdk
  snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
  evidence_state: SUPPORTED

control:
  primary_authority: mixed
  horizon: bounded_multistep
  topology: mixed
  model_count: variable
  notes:
    - core Agent loop is model_directed
    - Workflow is deterministic dependency execution
    - Graph is developer-structured with potentially model-routed/dynamic nodes
    - Swarm is peer/model-directed handoff
    - Agents-as-tools is manager/specialist hierarchy

capabilities:
  reads: framework-dependent
  writes: framework-dependent
  generated_code_execution: variable
  shell: variable
  browser: variable
  database: variable
  communication: variable
  publication: variable
  file_egress: variable
  capability_compositions:
    - tool capabilities inherit host-process permissions unless separately contained

side_effects:
  class: unknown
  reversible: unknown
  external_mutation: variable
  data_egress: unknown
  verification: application-defined

state:
  runtime_state: structured
  checkpointing: durable-capable
  persistence_backend: local/S3/custom/repository-style depending manager
  replay_semantics: partial
  notes:
    - conversation history, agent state and invocation state are distinct
    - session persistence and cross-session memory are distinct
    - documented session model assumes one live writer per conversation
    - session managers do not provide distributed locking

memory:
  semantic_role:
    - cross_session_knowledge
    - recall
    - injection
    - extraction
  scope: user | project | shared | custom
  persistence: local_durable | remote_durable | custom
  retrieval_policy: configurable search and/or injection
  write_policy: extraction and explicit add can be configured
  isolation_key: store/scope dependent
  retention_policy: backend/application dependent
  provenance: store/application dependent

human_control:
  level: mixed
  mode: approval_before | mixed | application_defined
  dispatcher_enforcement: possible_but_not_automatic
  approval_binding: depends on implementation
  notes:
    - interrupts and steering can pause before tools
    - deterministic hooks can enforce policy
    - LLM steering is probabilistic guidance unless wrapped by hard policy

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: application/provider/runtime dependent
  idempotency: application/tool dependent
  unknown_outcome_handling: application/tool dependent

termination:
  success_predicate: loop stop reason end_turn by default; external outcome predicate application-defined
  terminal_failure_predicate: stop reason / exception / application policy
  turn_budget: supported per invocation
  tool_budget: not a universal core budget surface in inspected docs
  time_budget: external cancellation/timeout composition; tool cooperation may be required
  cost_or_token_budget: output_tokens + total_tokens supported
  oscillation_detection: steering/custom evaluation dependent
  cancellation: cooperative, boundary-dependent
  notes:
    - token/turn caps are soft at loop boundaries
    - in-flight work can exceed nominal budget before next boundary

concurrency_candidate:
  agent_instance: overlapping invocation rejected by default
  session_writer_model: single live writer per conversation
  distributed_locking: none in documented session managers
  schema_state: CANDIDATE_DIMENSION_ONLY

evaluation:
  static_contracts:
    - structured output validation
    - deterministic evaluators
  unit_integration:
    - SDK repository tests exist
  trajectory:
    - trace/trajectory evaluators
    - tool-called evaluators
  outcome:
    - output/session evaluators
    - custom evaluators
  repeated_trials: supported_by_harness_not_automatic
  regression_gate: possible
  production_observability: supported

protocols:
  - name: MCP
    revision: must_be_pinned_per_deployment
    role: tool/context interoperability
    transport: multiple via MCP SDK
    capabilities: external tool access
    auth_model: deployment/protocol dependent
    extensions: protocol dependent
  - name: A2A
    revision: must_be_pinned_per_deployment
    role: remote agent interoperability
    transport: network service
    capabilities: remote agent discovery/invocation/delegation
    auth_model: deployment/protocol dependent
    extensions: implementation dependent

security:
  trust_boundaries:
    - host process
    - model provider
    - tool implementations
    - MCP/A2A remote endpoints
    - session/memory storage
  least_privilege: application_required
  sandbox: none_by_core_default
  data_classification: application-defined
  receipts:
    - OpenTelemetry traces available
    - tool/model metrics available

reproducibility:
  model_receipt: provider/model/config must be pinned by application
  dependency_receipt:
    repository: strands-agents/harness-sdk
    snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
    python_release_observed: python/v1.56.0
    typescript_release_observed: typescript/v1.18.0
  external_api_receipt: application-dependent
  execution_evidence: documentation/source inspection only for this pass

unknowns:
  - exact MCP 2026-07-28 execution compatibility not yet independently executed
  - A2A revision/auth matrix not yet pinned
  - project-level idempotency and exactly-once semantics
  - project-level multi-agent benefit vs simpler baseline
  - hard containment for arbitrary host-process tools
  - cross-language feature parity over time
```

## Pressure-test result at first pass

The existing schema represented most Strands surfaces without framework-specific fields. No framework label needed promotion to a top-level dimension.

However, Strands exposed material distinctions that were not represented cleanly enough.

### Candidate 1 — concurrency semantics

At this point in the investigation, the schema recorded persistence and replay but not whether concurrent invocations/writers were valid.

Evidence pressure:

- one agent instance rejects overlapping invocation by default;
- session persistence assumes one live writer per conversation;
- distributed locking is not supplied by the documented managers.

Candidate future shape:

```yaml
state:
  concurrency:
    invocation_mode:
    writer_model:
    local_locking:
    distributed_locking:
    conflict_semantics:
```

**Historical decision:** do **not** add yet. Seek a second independent system or a stronger counterexample before changing the schema.

**Final outcome:** independently confirmed and promoted under `state`.

### Candidate 2 — budget enforcement semantics

The old schema could say `turn_budget` or `token_budget`, but not whether that budget was a hard wall or a soft boundary.

Strands demonstrated:

- caps are checked between loop cycles;
- a single model response may overshoot token limits;
- tools from the previous turn finish before the next budget check;
- cooperative cancellation may not interrupt an already-running non-cooperative tool.

Candidate future shape:

```yaml
termination:
  budgets:
    turns:
      value:
      enforcement_boundary:
      overshoot_semantics:
    tokens:
      value:
      enforcement_boundary:
      overshoot_semantics:
    time:
      value:
      cancellation_boundary:
```

**Historical decision:** keep as MK1 pressure-test debt until independently confirmed.

**Final outcome:** independently confirmed and promoted under `termination`.

### Candidate 3 — intervention enforcement owner

Strands can enforce or influence behavior through deterministic hooks, human confirmation, provider guardrails or LLM steering. These mechanisms have different guarantees.

Candidate future qualifier:

```yaml
human_control:
  enforcement_owner: runtime_code | human | model_judge | provider_guardrail | infrastructure | mixed
```

**Historical decision:** likely useful, but test against independent HITL/guardrail systems before schema mutation.

**Final outcome:** independently confirmed and promoted under `human_control` with `enforcement_boundary` while retaining `dispatcher_enforcement`.

## Invariant decisions

### Strengthened

- policy belongs in enforceable code;
- every loop is bounded, with enforcement semantics recorded;
- tools are typed contracts but permissions are separate;
- context is curated state;
- persistence is not memory;
- least privilege is an agent invariant;
- version compatibility is evidence.

### Still qualified

- model-driven orchestration is not preferred by default;
- multi-agent complexity must prove value;
- steering/reflection requires external verification for reliability claims;
- observability support does not equal adequate production monitoring;
- deployment guidance does not equal application certification.

## Original MK1 action list and current resolution

The first pass required:

1. **pressure-test concurrency semantics against another independent runtime** — ✅ completed via LangGraph + OpenAI Agents SDK;
2. **pressure-test budget enforcement against another framework/runtime** — ✅ completed via LangGraph + OpenAI Agents SDK;
3. **compare deterministic HITL enforcement vs LLM steering** — ✅ completed through the cross-runtime enforcement-owner/boundary pass;
4. **execute a protocol-focused Strands/MCP compatibility fixture against the domain-pinned protocol revision** — ✅ completed at `SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED` source-evidence level;
5. **benchmark at least one Strands multi-agent topology against a single-agent baseline before deriving any performance rule** — 🟡 still open.

This historical receipt therefore explains **why** the current schema and Strands package look the way they do, while current-state retrieval should use [`../../systems/strands/`](../../systems/strands/).
