# REC-012 — Candidate multi-actor baseline (IN_PROGRESS)

Status: **IN_PROGRESS / EVIDENCE_PARTIAL / NOT MATERIALIZED FOR G7**  
Schema: **`mk1-draft-2026-09-16.1`**  
Observed/classified: **2026-10-12**

> This is a bounded classification pressure test using offline **deterministic policy actors**, not an LLM-based multi-agent benchmark. It is explicitly **not** a completed representative REC-012 record.

## Record identity

```yaml
record_id: REC-012
name: Offline deterministic incident-triage actor topology
schema_revision: mk1-draft-2026-09-16.1
classification_scope: offline synthetic two-tool task
source_receipts:
  - ../../quarries/rec-012-offline-topology-baseline.md
primary_quarries:
  - ../../quarries/rec-012-offline-topology-baseline.md
evidence_state: QUALIFIED_FOR_TOPOLOGY_ONLY
production_certification: false
```

## Classification of compared implementations (not general agent families)

```yaml
identity:
  name: Synthetic incident triage policy-actor fixture
  source: ../../experiments/rec-012/
  snapshot: branch PR / receipt hash
  evidence_state: QUALIFIED
control:
  primary_authority: deterministic
  horizon: bounded_multistep
  topology: manager_workers    # evaluated multi variant; single baseline has single_model-shaped topology without any model
  model_count: 0
capabilities:
  reads: [local_log_fixture, local_impact_fixture]
  writes: []
  shell: false
  generated_code_execution: false
  file_egress: false
  capability_compositions: []
side_effects:
  class: S0
  reversible: yes
  external_mutation: false
  data_egress: none
  verification: exact expected label comparison per fixture
state:
  runtime_state: transient
  checkpointing: none
  persistence_backend: none
  replay_semantics: known for deterministic fixture
  invocation_concurrency: bounded_concurrent
  writer_model: single_writer
  concurrency_conflict_semantics: no mutable shared data between specialist workers
  locking: none
memory:
  semantic_role: []
  scope: none
  persistence: none
human_control:
  level: H0
  mode: none
  dispatcher_enforcement: unknown
  enforcement_owner: runtime_code
  enforcement_boundary: local validation and manager-owned termination
errors_and_retries:
  error_model: structured
  retry_owner: none
  retry_budget: 0
  idempotency: no mutating tools
  unknown_outcome_handling: explicit failure status; in-flight thread cancellation is not hard
termination:
  success_predicate: output matches held-out fixture labels (external test verifier)
  terminal_failure_predicate: structured invalid handoff, tool exception or time-budget-exceeded
  time_budget: 10ms
  time_budget_enforcement: cooperative / checked at runtime boundaries
  overshoot_semantics: observed overrun for 25ms stall injection
  cancellation: future.cancel + thread pool wait
  cancellation_effective_boundary: pending futures; in-flight Python threads cannot be hard-stopped
evaluation:
  static_contracts: [typed_handoff, exact_expected_labels]
  unit_integration: [six_locally_passed_unittest_methods]
  trajectory: [tool_count, handoff_count, typed_errors]
  outcome: [per_task_correctness]
  repeated_trials: true
  regression_gate: false
  production_observability: false
protocols: []
security:
  trust_boundaries: [manager_to_specialist_handoff]
  least_privilege: yes
  sandbox: none
  data_classification: synthetic_no_real_personal_data
reproducibility:
  model_receipt: NOT_APPLICABLE_NO_LLM
  dependency_receipt: Python_3.13.5_stdlib_only
  external_api_receipt: NONE
  execution_evidence: LOCAL_RUN_2026_10_12_RESULTS_JSON
unknowns:
  - REAL_LLM_MULTIAGENT_COMPARISON_NOT_RUN
  - model_quality_and_token_cost_NOT_MEASURED
  - remote_effect_and_hard_cancel_NOT_TESTED
  - real_agent_delegation_and_stochastic_drift_NOT_TESTED
```

## Material observations

- Both variants had 480/480 correct expected labels in a 16-case, 30-repeat local benchmark. This measures fixture outputs, not real-world task utility.
- Multi-worker version had 960 handoffs vs zero, with higher measured cold-start median wall time; the numerical ratio varies by local execution.
- Six fault categories failed closed under both variants. A 25ms injected stall overruns a nominal 10ms deadline because threads are not preemptively cancelled.
- No tokens were consumed; this is not evidence that actual multiagent inference has zero cost.
- The schema can express topology and measurable benefit separately **for this deterministic fixture**. That is insufficient pressure from actual model-directed agents.

## Admission and outcome decision

```yaml
admission_hypothesis: independent_tool_observations_might_parallelize
baseline: single_deterministic_policy_actor
candidate: manager_plus_two_deterministic_specialists
relative_outcome: equivalent_on_synthetic_fixture
coordination_cost: higher_in_observed_cold_start_run
model_benefit_conclusion: INCONCLUSIVE_NOT_TESTED
mk1_g7: OPEN
record_status: IN_PROGRESS
production_certification: false
schema_pressure:
  fits_current_schema: qualified
  new_dimension_required: false
  reason: no pressure from actual LLM delegation yet
```

## Remaining completion gate

Execute the same-task, real-model single-agent vs manager/specialists comparison with pinned provider/model/config, budgets, repeated evaluation and failure/termination receipts as defined by [baseline spec](../MULTI_AGENT_BASELINE_SPEC.md). **Until then do not promote this draft to MATERIALIZED/QUALIFIED completed or close U-MK1-001.**

## Related files

- [Experiment](../../../experiments/rec-012/README.md)
- [Execution receipt](../../../quarries/rec-012-offline-topology-baseline.md)
- [Record registry](./README.md)
