# R-005 — Self-Healing Code Agent

Status: **CLASSIFIED WITH SECURITY UNKNOWNS**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/self_healing_code.ipynb`

## Normalized record

```yaml
identity:
  name: Self-Healing Code Agent
  evidence_state: OBSERVED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [TARGET_CODE, TEST_OR_FAILURE_CONTEXT]
  writes: [GENERATED_REPLACEMENT_CODE]
  generated_code_execution: true
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: unknown
  delegation: false
  capability_compositions:
    - model_generated_code + exec(new_code, namespace) + subsequent_function_use

side_effects:
  observed_class: S1
  reachable_class: S4
  reversible: partial
  external_mutation: unknown
  data_egress: unknown
  verification: functional evaluation/reuse of generated callable; containment not verified

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: process state
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none
  write_policy: none
  isolation_key: none
  retention_policy: none
  provenance: generated source retained as runtime artifact

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: mixed
  retry_owner: model
  retry_budget: workflow dependent; exact bound not established in MK0 evidence
  idempotency: not applicable to pure function replacement, but host side effects remain unconstrained
  unknown_outcome_handling: unknown

termination:
  success_predicate: revised code passes/evaluates sufficiently for workflow continuation
  terminal_failure_predicate: repair/evaluation failure
  turn_budget: unknown
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: unknown
  cancellation: unknown

evaluation:
  static_contracts: []
  unit_integration: [repair/test concept]
  trajectory: []
  outcome: [functional behavior of revised callable]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_generated_source, source_to_python_exec, generated_callable_to_host_runtime]
  least_privilege: no
  sandbox: none
  data_classification: unknown
  authorization_boundary: Python process authority
  receipts: generated source + functional result only

unknowns:
  - sandbox/resource isolation
  - network/filesystem access available to generated code
  - secret exposure
  - promotion/review gate before codebase integration
  - comprehensive regression coverage
```

## Evidence basis

Observed implementation explicitly calls `exec(new_code, namespace)` to load model-generated replacement code.

Primary quarry paths:

- `quarries/genai-agents-p0-p1-callpaths.md` P0-02;
- `quarries/genai-agents-risk-scan.md` RS-03.

## Classification result

The useful engineering pattern is **generate → evaluate → revise**. The unsafe generalization is **generate → execute in trusted runtime → infer safety from functional success**.

Functional correctness and execution containment are orthogonal evidence dimensions.

## MK2 handoff seed

Operational contract should require isolated execution, test evidence, diff/promotion review, secret/network/filesystem policy and rollback provenance.
