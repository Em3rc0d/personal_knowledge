# R-012 — Multi-Agent Collaboration System

Status: **CLASSIFIED / TAXONOMY COUNTEREXAMPLE**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/multi_agent_collaboration_system.ipynb`

## Normalized record

```yaml
identity:
  name: History and Data Analysis Collaboration System
  evidence_state: OBSERVED

control:
  primary_authority: deterministic
  control_class: C0
  horizon: bounded_multistep
  topology: deterministic_multi_role
  model_count: 1 shared model client / 2 logical role agents

capabilities:
  reads: [USER_TASK, PRIOR_GENERATED_CONTEXT]
  writes: [IN_PROCESS_CONTEXT, FINAL_TEXT]
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: false
  delegation: false
  capability_compositions:
    - fixed_step_orchestrator + role_conditioned_model_calls + shared_context

side_effects:
  observed_class: S1
  reachable_class: S1
  reversible: yes
  external_mutation: false
  data_egress: none
  verification: final generated answer only

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: process list
  replay_semantics: known

memory:
  semantic_role: [shared_working_context]
  scope: session
  persistence: process
  retrieval_policy: each later role receives accumulated context
  write_policy: deterministic step functions append generated messages
  isolation_key: per solve() call local context list
  retention_policy: duration of solve call
  provenance: context labels role source but not external factual provenance

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: prose
  retry_owner: none
  retry_budget: none
  idempotency: n/a
  unknown_outcome_handling: exceptions terminate with error string

termination:
  success_predicate: fifth fixed step returns synthesized answer
  terminal_failure_predicate: exception or wall-clock timeout
  turn_budget: exactly five orchestrated role calls in normal path
  tool_budget: n/a
  time_budget: solve(timeout=300) checked before each step
  cost_or_token_budget: unknown
  oscillation_detection: n/a
  cancellation: timeout only

evaluation:
  static_contracts: [fixed step order]
  unit_integration: []
  trajectory: []
  outcome: [example answer only]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [generated_role_output_to_next_role_context]
  least_privilege: yes
  sandbox: none
  data_classification: user task + generated content only
  authorization_boundary: n/a
  receipts: printed role outputs

unknowns:
  - measurable benefit versus one-model single-prompt/workflow baseline
  - factual grounding of historical data produced by roles
  - coordination value versus increased tokens/latency
  - robustness under contradictory role outputs
```

## Direct source observation

`HistoryDataCollaborationSystem.solve()` defines a fixed ordered list:

1. research historical context;
2. identify data needs;
3. provide historical data;
4. analyze data;
5. synthesize final answer.

A normal `for` loop invokes those steps in code-defined order. The same `ChatOpenAI` client is shared by the logical History and Data roles.

## Classification result

This is the clearest MK1 counterexample to the assumption:

```text
multiple named agents ⇒ model-directed multi-agent system
```

It is **multi-role/multi-agent by presentation**, but **deterministically orchestrated C0** by control authority.

Topology and control therefore must remain orthogonal.

## MK2 handoff seed

Any multi-agent admission contract should require baseline comparison, explicit specialization/parallelism/isolation hypothesis, outcome metrics and coordination-cost accounting.
