# R-016 — External Pressure Test: Conversation Buffer Memory

Status: **CLASSIFIED / CROSS-SOURCE PRESSURE TEST**  
Source: `NirDiamant/Agent_Memory_Techniques@b7f7240eb4d4510f3b45300a89126858a474b31d`  
Artifact: `all_techniques/01_conversation_buffer_memory/conversation_buffer_memory.ipynb`

## Purpose

This record intentionally comes from outside the primary `GenAI_Agents` mining site. It tests whether MK1 can classify an independently organized memory implementation without adding a source-specific top-level dimension.

## Normalized record

```yaml
identity:
  name: Conversation Buffer Memory
  evidence_state: OBSERVED

control:
  primary_authority: deterministic
  control_class: C0
  horizon: single_step
  topology: single_model
  model_count: 1

capabilities:
  reads: [IN_PROCESS_MESSAGE_BUFFER]
  writes: [IN_PROCESS_MESSAGE_BUFFER]
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: false
  delegation: false
  capability_compositions: []

side_effects:
  observed_class: S1
  reachable_class: S1
  reversible: yes
  external_mutation: false
  data_egress: content
  verification: buffer can be inspected directly; API receives full buffer each turn

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: Python list in process
  replay_semantics: known

memory:
  semantic_role: [conversation_buffer]
  scope: session
  persistence: process
  retrieval_policy: send entire ordered message buffer on every inference
  write_policy: append user message then assistant response
  isolation_key: memory-object instance
  retention_policy: unbounded until clear() or process lifecycle
  provenance: verbatim ordered messages

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: SDK/runtime dependent
  retry_owner: provider_sdk
  retry_budget: unknown
  idempotency: n/a for local buffer; API retry semantics provider-dependent
  unknown_outcome_handling: unknown

termination:
  success_predicate: one model response returned
  terminal_failure_predicate: SDK/runtime error
  turn_budget: one inference per chat() call
  tool_budget: n/a
  time_budget: unknown
  cost_or_token_budget: max_tokens=1024 for output; history input grows unbounded
  oscillation_detection: n/a
  cancellation: caller-controlled

evaluation:
  static_contracts: [ordered role/message structure]
  unit_integration: []
  trajectory: []
  outcome: [manual recall demo, token-usage bookkeeping]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [conversation_buffer_to_external_model_API]
  least_privilege: yes
  sandbox: none
  data_classification: conversation content; explicit policy unknown
  authorization_boundary: model API credential
  receipts: response usage token counts and inspectable message history

unknowns:
  - conversation-data retention/privacy policy
  - provider-side retention assumptions
  - retry behavior
  - context-window failure policy
```

## Direct source observations

- the core memory is `self.messages: list[dict] = []`;
- `chat()` appends a user message, sends the **entire** message list to the model API and appends the assistant response;
- `clear()` removes the in-process history;
- token usage is recorded per turn;
- the notebook explicitly demonstrates linear per-turn input growth and cumulative token-cost growth.

## Pressure-test result

**PASS:** the existing MK1 axes classify this external source without a new top-level category.

It also reinforces two existing rules:

1. memory scope/persistence must be stated explicitly (`session` + `process` here);
2. context projection has operational cost — a full buffer is a retrieval policy, not merely a boolean memory feature.

No schema extension was needed for this source.

## MK2 handoff seed

Operational buffer-memory contracts should include context/token budget, truncation/failure policy, privacy/retention, identity/isolation and provider data-egress assumptions.
