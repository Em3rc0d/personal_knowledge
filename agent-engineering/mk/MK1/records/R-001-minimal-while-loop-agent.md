# R-001 — Minimal While-Loop Agent

Status: **CLASSIFIED**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/agent_while_loop_from_scratch.ipynb`

## Normalized record

```yaml
identity:
  name: Minimal While-Loop Agent
  evidence_state: OBSERVED

control:
  primary_authority: model_directed
  control_class: C2
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [FILESYSTEM_READ]
  writes: [SHELL_DERIVED_UNKNOWN_SCOPE]
  generated_code_execution: false
  shell: true
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: unknown
  delegation: false
  capability_compositions:
    - model_selected_tool + shell=True + inherited_process_authority

side_effects:
  observed_class: S0
  reachable_class: S4
  reversible: unknown
  external_mutation: unknown
  data_egress: unknown
  verification: tool result appended to transcript; no external outcome verifier

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: process memory
  replay_semantics: unknown

memory:
  semantic_role: [transcript_context]
  scope: session
  persistence: process
  retrieval_policy: append tool/model messages into next-turn context
  write_policy: runtime appends conversation/tool results
  isolation_key: none observed
  retention_policy: bounded indirectly by turn loop, not a memory lifecycle policy
  provenance: tool results become context

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: MAX_TURNS plus failed-call guard
  idempotency: not defined for shell
  unknown_outcome_handling: not formalized

termination:
  success_predicate: model returns final answer / stops requesting tools
  terminal_failure_predicate: turn budget exhaustion or tool failure path
  turn_budget: MAX_TURNS = 10
  tool_budget: bounded indirectly by turns
  time_budget: command timeout = 60s per shell call; no global wall-clock budget observed
  cost_or_token_budget: unknown
  oscillation_detection: exact repeated failed-call guard
  cancellation: unknown

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_tool_dispatcher, shell_to_host_process]
  least_privilege: no
  sandbox: none
  data_classification: unknown
  authorization_boundary: tool name/schema only; shell command authority broad
  receipts: transcript/tool result only

unknowns:
  - filesystem scope under runtime
  - network availability
  - credential/environment exposure
  - shell mutation reachability in intended demo
  - global time/cost budget
```

## Evidence basis

Observed quarry evidence establishes:

- model → tool → result iteration;
- tools `list_files`, `read_file`, `run_command`;
- `run_command` reaches `subprocess.run(..., shell=True, timeout=60)`;
- hard `MAX_TURNS`;
- exact failed-call registry and repeat guard.

Primary quarry paths:

- `quarries/genai-agents.md` §4 / §6;
- `quarries/genai-agents-p0-p1-callpaths.md` P0-03;
- `quarries/genai-agents-risk-scan.md` RS-01.

## Classification result

This is a genuine **model-directed bounded tool loop** even without an agent framework. It is therefore a useful counterexample to framework-defined taxonomy.

Its observed demo behavior can be benign while the granted shell authority is not. This record directly motivated `observed_class` vs `reachable_class` in MK1.

## MK2 handoff seed

Operationalization must require:

- narrowed command/tool surface or sandbox;
- explicit filesystem/network/secret boundaries;
- structured tool errors;
- global wall-clock/tool/cost budgets;
- side-effect receipts where mutation is possible.
