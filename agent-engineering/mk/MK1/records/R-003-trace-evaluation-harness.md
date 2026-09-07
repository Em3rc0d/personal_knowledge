# R-003 — Trace-Based Agent Evaluation Harness

Status: **CLASSIFIED / TEST-SUPPORTED**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifacts: `trace_based_agent_evaluation.ipynb`, `tests/test_trace_based_agent_evaluation.py`

## Normalized record

```yaml
identity:
  name: Trace-Based Agent Evaluation Harness
  evidence_state: SUPPORTED

control:
  primary_authority: deterministic
  control_class: C0
  horizon: bounded_multistep
  topology: single_model
  model_count: 0-or-evaluated-system-dependent

capabilities:
  reads: [TRACE, TOOL_CALLS, CLAIMS, LATENCY, ERRORS]
  writes: [EVALUATION_RESULT]
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
  verification: deterministic grader outputs + tests

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: process / fixture dependent
  replay_semantics: known

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none
  write_policy: none
  isolation_key: none
  retention_policy: none
  provenance: evaluated trace is evidence input, not agent memory

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: structured
  retry_owner: none
  retry_budget: none
  idempotency: deterministic evaluation over same trace
  unknown_outcome_handling: exceptions become failed traces rather than aborting suite

termination:
  success_predicate: trace scored and suite gates computed
  terminal_failure_predicate: grader/evaluation failure is recorded as failed result
  turn_budget: n/a
  tool_budget: n/a
  time_budget: latency is evaluated; harness wall-clock budget not established
  cost_or_token_budget: n/a for deterministic grader slice
  oscillation_detection: n/a
  cancellation: unknown

evaluation:
  static_contracts: [expected tool sequence, tool arguments]
  unit_integration: [grader behavior, exception handling]
  trajectory: [sequence, args, errors, latency]
  outcome: [evidence/claim consistency only; external task outcome not generally proven]
  repeated_trials: false
  regression_gate: true
  production_observability: false

security:
  trust_boundaries: [trace_to_grader, grader_to_quality_gate]
  least_privilege: yes
  sandbox: none
  data_classification: trace may contain sensitive tool args; policy not specified
  authorization_boundary: n/a
  receipts: per-trace score + suite metrics

unknowns:
  - sensitive trace redaction/retention policy
  - repeated stochastic trial policy
  - external outcome verifier for open-ended tasks
  - production telemetry integration
```

## Evidence basis

Tests cover:

- exact tool sequence;
- tool arguments;
- evidence/claims;
- latency boundaries;
- errors/exceptions;
- contradictory claims;
- extra tool calls;
- suite gates for pass rate, tool accuracy and p95 latency.

Primary quarry path: `quarries/genai-agents.md` §9.

## Classification result

This is **not itself an agent**. It is a deterministic evaluation harness around agent traces. That distinction matters: the same repository category can contain agent systems and supporting evaluation infrastructure.

Exact trajectories are strong for policy/contract tests but can be over-constraining for capability evaluation when multiple valid paths exist.

## MK2 handoff seed

Operationalization should split:

- policy trajectory assertions;
- capability/outcome graders;
- repeated trials;
- regression thresholds;
- trace privacy/redaction;
- production feedback ingestion.
