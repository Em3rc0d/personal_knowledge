# R-002 — Human-in-the-Loop Approval Agent

Status: **CLASSIFIED / TEST-SUPPORTED**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifacts: `human_in_the_loop_approval_agent.ipynb`, `tests/test_hitl_approval_agent.py`

## Normalized record

```yaml
identity:
  name: Human-in-the-Loop Approval Agent
  evidence_state: SUPPORTED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [LOW_RISK_LOOKUP]
  writes: [CONSEQUENTIAL_REFUND]
  generated_code_execution: false
  shell: false
  browser: none
  database: unknown
  communication: none
  publication: none
  file_egress: false
  delegation: false
  capability_compositions:
    - model_proposal + policy_classification + persisted_interrupt + dispatcher_authorization

side_effects:
  observed_class: S3
  reachable_class: S3
  reversible: partial
  external_mutation: true
  data_egress: none
  verification: audit/action result plus dedicated tests

state:
  runtime_state: structured
  checkpointing: memory
  persistence_backend: in-memory checkpointer in tutorial; durable production backend recommended by official guidance
  replay_semantics: partial

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none
  write_policy: none
  isolation_key: none
  retention_policy: none
  provenance: not semantic memory

human_control:
  level: H4
  mode: approval_edit_before
  dispatcher_enforcement: yes
  approval_binding: approval/reject/modify decision bound to pending action; modified args revalidated

errors_and_retries:
  error_model: structured
  retry_owner: runtime
  retry_budget: unknown
  idempotency: replay safety required by framework semantics; specific business idempotency unknown
  unknown_outcome_handling: consequential action is blocked before dispatch until authorization exists

termination:
  success_predicate: authorized action executes or low-risk lookup completes
  terminal_failure_predicate: reject / validation failure / policy denial
  turn_budget: graph-bounded path; exact global model-turn budget unknown
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: unknown
  cancellation: human reject path

evaluation:
  static_contracts: [argument validation, unexpected-argument rejection]
  unit_integration: [low-risk execution, approval pause, dispatcher bypass rejection, approve/reject/modify, invalid edited args]
  trajectory: [interrupt-before-side-effect]
  outcome: [refund not executed before approval, reject leaves action unexecuted]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_proposal_to_policy, approval_to_dispatcher, dispatcher_to_consequential_tool]
  least_privilege: partial
  sandbox: none
  data_classification: unknown
  authorization_boundary: low-level dispatcher independently requires authorization
  receipts: audit events + persisted pending action/decision

unknowns:
  - durable production checkpointer configuration
  - business-level idempotency key/transaction semantics
  - global runtime budgets
  - external refund provider receipt shape
```

## Evidence basis

Dedicated tests establish that:

- low-risk lookup executes without approval;
- refund pauses **before** side effect;
- direct dispatcher bypass raises authorization failure;
- approve, reject and modify have distinct semantics;
- edited arguments are revalidated;
- invalid numerics/unexpected args are rejected;
- integration path can pause/resume with checkpointed state.

Primary quarry path: `quarries/genai-agents.md` §7.

## Classification result

This record is the strongest upstream example of **human control as an enforceable runtime boundary**, not merely a review UI.

The key taxonomy result is that `H4` is independent of whether the model initially proposed the action. The system can remain model-assisted while authorization belongs to deterministic policy/runtime code.

## MK2 handoff seed

Derive explicit contracts for:

- pending-action schema;
- authorization receipt;
- argument hash/binding;
- edit invalidation + revalidation;
- durable resume/replay safety;
- dispatcher-level policy denial tests.
