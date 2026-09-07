# R-011 — Memory-Enhanced Conversational Agent

Status: **CLASSIFIED / SOURCE CLAIM QUALIFIED**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/memory_enhanced_conversational_agent.ipynb`

## Normalized record

```yaml
identity:
  name: Memory-Enhanced Conversational Agent
  evidence_state: QUALIFIED

control:
  primary_authority: deterministic
  control_class: C0
  horizon: single_step
  topology: single_model
  model_count: 1

capabilities:
  reads: [CHAT_HISTORY, IN_PROCESS_MEMORY]
  writes: [CHAT_HISTORY, IN_PROCESS_MEMORY]
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
  data_egress: none
  verification: in-notebook memory inspection/example output

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: Python dictionaries + ChatMessageHistory in process
  replay_semantics: known

memory:
  semantic_role: [conversation_history, selected_user_utterances]
  scope: session
  persistence: process
  retrieval_policy: exact session_id lookup; long-term store joined into prompt
  write_policy: append user input when len(input) > 20
  isolation_key: session_id
  retention_policy: keep last 5 selected memory strings
  provenance: selected strings are derived directly from user input

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: prose
  retry_owner: none
  retry_budget: none observed
  idempotency: n/a
  unknown_outcome_handling: n/a

termination:
  success_predicate: one model response returned
  terminal_failure_predicate: model/runtime exception
  turn_budget: one inference per chat call
  tool_budget: n/a
  time_budget: unknown
  cost_or_token_budget: model max_tokens = 1000
  oscillation_detection: n/a
  cancellation: caller-controlled

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: [manual/example recall demonstration]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [user_input_to_memory_store, memory_store_to_prompt]
  least_privilege: yes
  sandbox: none
  data_classification: conversation/user preference data; policy unknown
  authorization_boundary: session_id lookup only
  receipts: in-memory store inspection

unknowns:
  - persistence across process restart
  - user authentication/ownership of session_id
  - retention/privacy policy
  - memory-quality or false-memory metrics
  - isolation under hostile/guessed session IDs
```

## Direct source observation

The notebook uses:

```text
chat_store = {}
long_term_memory = {}
```

Both stores are in-process. `get_chat_history(session_id)` and the long-term-memory dictionary are keyed by `session_id`. The “long-term” write rule stores user inputs longer than 20 characters and retains only the last five strings.

## Classification result

The upstream documentation describes cross-session/long-term memory, but the inspected implementation does **not** provide durable storage across process restarts and does not show a cross-session identity layer.

Therefore:

```text
source label: long-term memory
normalized evidence: session-scoped, process-persistent memory
```

This is precisely why `memory=true` is not a useful engineering classification.

## MK2 handoff seed

A real long-term-memory contract must state durable backend, identity/isolation, write/retrieval policy, retention/deletion, provenance, memory-quality eval and migration/versioning semantics.
