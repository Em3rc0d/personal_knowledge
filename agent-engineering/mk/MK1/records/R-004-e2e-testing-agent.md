# R-004 — E2E Testing Agent

Status: **CLASSIFIED WITH SECURITY UNKNOWNS**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/e2e_testing_agent.ipynb`

## Normalized record

```yaml
identity:
  name: E2E Testing Agent
  evidence_state: OBSERVED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [USER_INSTRUCTION, DOM, BROWSER_STATE]
  writes: [GENERATED_PYTHON, BROWSER_ACTIONS]
  generated_code_execution: true
  shell: false
  browser: general
  database: none
  communication: none
  publication: none
  file_egress: unknown
  delegation: false
  capability_compositions:
    - model_generated_actions + generated_python + exec + browser_runtime

side_effects:
  observed_class: S1
  reachable_class: S4
  reversible: unknown
  external_mutation: unknown
  data_egress: unknown
  verification: DOM/browser observations and workflow state; no sandbox attestation

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: graph/runtime state
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none
  write_policy: none
  isolation_key: none
  retention_policy: none
  provenance: browser observations enter runtime state

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: mixed
  retry_owner: runtime
  retry_budget: workflow-dependent; complete contract unknown
  idempotency: not established
  unknown_outcome_handling: unknown

termination:
  success_predicate: workflow completes requested test path
  terminal_failure_predicate: execution/workflow failure
  turn_budget: unknown
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: unknown
  cancellation: unknown

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: [generated action sequence implicit in state]
  outcome: [test/browser result]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_generated_code, generated_code_to_python_runtime, python_runtime_to_browser]
  least_privilege: no
  sandbox: none
  data_classification: unknown
  authorization_boundary: Python process authority
  receipts: workflow/browser observations only

unknowns:
  - filesystem/network restrictions of exec environment
  - secret/credential exposure
  - allowed browser origins/actions
  - authenticated mutation reachability
  - cancellation/global timeout
```

## Evidence basis

Observed call path:

`natural-language request → structured actions → accumulated Playwright Python → exec(state["script"]) → browser/DOM observations`.

Primary quarry paths:

- `quarries/genai-agents-p0-p1-callpaths.md` P0-01;
- `quarries/genai-agents-risk-scan.md` RS-02.

## Classification result

The defining authority boundary is not merely browser automation. **Model-derived Python is executed inside the notebook process.** Therefore the reachable authority can exceed the nominal E2E target.

This is a strong case for classifying execution substrate separately from task label.

## MK2 handoff seed

Require disposable sandbox, network allowlist, isolated credentials, resource limits, browser-origin policy and promotion receipts for generated tests.
