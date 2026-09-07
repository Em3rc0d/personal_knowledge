# R-006 — HR Messaging Agent

Status: **CLASSIFIED WITH MATERIAL UNKNOWN**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifacts: `HR_AI-Assistant.ipynb`, `Hr_AI_Agent.ipynb`

## Normalized record

```yaml
identity:
  name: HR Messaging Agent
  evidence_state: QUALIFIED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [CANDIDATE_SEARCH, CANDIDATE_PROFILE]
  writes: [OUTBOUND_MESSAGE]
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: external_send
  publication: none
  file_egress: false
  delegation: false
  capability_compositions:
    - model_tool_routing + send_linkedin_message + HTTP_POST

side_effects:
  observed_class: S3
  reachable_class: S3
  reversible: no
  external_mutation: true
  data_egress: content
  verification: HTTP response path; complete delivery receipt semantics unknown

state:
  runtime_state: structured
  checkpointing: memory
  persistence_backend: framework-dependent / tutorial state
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none
  write_policy: none
  isolation_key: none
  retention_policy: none
  provenance: candidate/profile context feeds generation

human_control:
  level: mixed
  mode: mixed
  dispatcher_enforcement: unknown
  approval_binding: NodeInterrupt exists for job-description/interview-review stages; outbound sender gate not established

errors_and_retries:
  error_model: mixed
  retry_owner: unknown
  retry_budget: unknown
  idempotency: unknown
  unknown_outcome_handling: unknown

termination:
  success_predicate: workflow completes recruitment/message path
  terminal_failure_predicate: workflow/tool error or interrupt decision depending stage
  turn_budget: unknown
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: unknown
  cancellation: partial through human interrupts in selected stages

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_toolnode, candidate_data_to_generation, sender_to_external_message_endpoint]
  least_privilege: partial
  sandbox: none
  data_classification: candidate/HR data; explicit policy unknown
  authorization_boundary: UNKNOWN for outbound sender
  receipts: external request/result details incomplete in inspected evidence

unknowns:
  - whether every send path is pre-approved
  - whether sender can be invoked independently of reviewed stages
  - idempotency/deduplication of outbound messaging
  - retry behavior after timeout/unknown delivery outcome
  - candidate-data retention/privacy policy
```

## Evidence basis

Observed:

- `send_linkedin_message` is an exposed tool;
- it shares a `ToolNode` with read-oriented search/profile tools;
- sender performs an external HTTP POST;
- `NodeInterrupt` exists elsewhere for human review of generated artifacts.

Primary quarry paths:

- `quarries/genai-agents-p0-p1-callpaths.md` P0-04;
- `quarries/genai-agents-risk-scan.md` RS-05.

## Classification result

This record is deliberately **not** classified as H2/H3/H4 for sending. Human review elsewhere in the workflow does not prove enforcement at the consequential dispatcher.

That UNKNOWN is the important result.

## MK2 handoff seed

Require separate read/send privileges, dispatcher-level send authorization, recipient/content binding, idempotency or delivery reconciliation, privacy/retention rules and auditable delivery receipts.
