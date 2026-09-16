# REC-003 — Trace-Evaluation Harness

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-003
name: GenAI_Agents trace-based agent evaluation harness
schema_revision: mk1-draft-2026-09-16.1
classification_scope: deterministic trace/trajectory evaluator and suite-level quality gates
source_receipts:
  - S-001
  - S-104
primary_quarries:
  - quarries/genai-agents.md
evidence_state: SUPPORTED / QUALIFIED
production_certification: false
```

Pinned upstream snapshot: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`.

## Classification

```yaml
identity:
  name: trace-based agent evaluation harness
  source: NirDiamant/GenAI_Agents/all_agents_tutorials/trace_based_agent_evaluation.ipynb
  snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
  evidence_state: SUPPORTED

control:
  primary_authority: deterministic
  horizon: bounded_multistep
  topology: single_model | mixed
  model_count: evaluated-system dependent

capabilities:
  reads:
    - execution traces
    - tool sequence/arguments
    - claims/evidence fields
    - latency/errors
  writes:
    - evaluation scores/results
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: false
  capability_compositions:
    - deterministic trace inspection + suite aggregation + threshold gate

side_effects:
  class: S1
  reversible: yes
  external_mutation: false
  data_egress: none
  verification: evaluator verifies selected trace/claim/latency contracts; it does not independently establish every external task outcome

state:
  runtime_state: structured
  checkpointing: none | unknown
  persistence_backend: not material to inspected evaluator
  replay_semantics: known for deterministic fixture inputs; evaluated-agent replay remains external to harness
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: not material to core evaluator semantics
  locking: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: not applicable
  write_policy: not applicable
  isolation_key: evaluation-case/suite identity where implemented
  retention_policy: not established
  provenance: trace/evaluation fixture dependent

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  enforcement_owner: runtime_code
  enforcement_boundary: deterministic evaluator/gate after or around captured execution evidence
  approval_binding: not applicable

errors_and_retries:
  error_model: structured | mixed
  retry_owner: none | harness/application dependent
  retry_budget: not central to evaluator
  idempotency: evaluation over same deterministic trace should be repeatable at harness level
  unknown_outcome_handling: execution exceptions are represented as failed traces rather than aborting the entire suite

termination:
  success_predicate: evaluator/suite thresholds pass for declared metrics; this is evaluation success, not automatically business-outcome success
  terminal_failure_predicate: failed evaluator checks or suite quality gates
  turn_budget: evaluated-system dependent
  turn_budget_enforcement: outside evaluator scope
  tool_budget: evaluated-system dependent
  tool_budget_enforcement: outside evaluator scope
  time_budget: latency budget/threshold is evaluated
  time_budget_enforcement: post-execution/trace evaluation rather than execution cancellation
  cost_or_token_budget: not established in inspected deterministic harness
  cost_or_token_budget_enforcement: none established
  overshoot_semantics: latency threshold can fail a trace/suite after observed execution; it is not a runtime preemption boundary
  oscillation_detection: extra/repeated tool sequence can be penalized when encoded in expected trajectory
  cancellation: not central to evaluator
  cancellation_effective_boundary: not applicable/unknown

evaluation:
  static_contracts:
    - expected tool sequence checks
    - tool-argument checks
    - evidence/claim checks
    - latency-budget checks
    - execution-error checks
  unit_integration:
    - dedicated upstream test suite for evaluator behavior
  trajectory:
    - exact/expected tool sequence
    - extra tool-call detection
    - argument checks
    - execution errors
  outcome:
    - claim/evidence consistency checks
    - suite-level pass/fail metrics
    - not a universal external-world outcome verifier
  repeated_trials: false
  regression_gate: true
  production_observability: false

protocols: []

security:
  trust_boundaries:
    - evaluated agent/runtime
    - trace capture
    - deterministic evaluator
    - suite aggregation/gate
  least_privilege: yes | not material
  sandbox: none | not applicable
  data_classification: trace contents may require application-specific handling
  receipts:
    - exceptions become failed traces without aborting the suite
    - contradictory claims lose evidence credit
    - extra tool calls can violate trajectory expectations
    - latency boundary behavior is tested

reproducibility:
  model_receipt: evaluated-agent dependent
  dependency_receipt: repository snapshot pinned
  external_api_receipt: not required for deterministic evaluator fixtures
  execution_evidence: dedicated upstream tests exercise evaluator semantics

unknowns:
  - repeated stochastic-trial policy for capability reliability claims
  - whether exact trajectory matching is appropriate for each future task family
  - external-world outcome graders for tasks where multiple valid trajectories exist
  - production trace retention/privacy policy
  - token/cost evaluation contract in the inspected slice
```

## What the harness actually evaluates

Observed deterministic checks include:

```text
expected tool sequence
tool arguments
evidence / claims
latency
execution errors
```

Dedicated tests also cover:

- exceptions converted into failed traces without aborting the suite;
- contradictory claims losing evidence credit;
- extra tool calls violating the expected trajectory;
- latency-budget boundary behavior;
- suite-level quality gates such as pass rate, tool accuracy and p95 latency.

## Key normalization

A trace evaluator is not automatically an outcome evaluator.

```text
TRAJECTORY
what the agent did

OUTCOME
what became true in the task/environment
```

They can disagree.

Therefore:

> Never allow a trajectory-only grader to become the sole evidence of semantic success when the external outcome can contradict it.

## Exact-sequence qualification

Exact expected tool sequences are strong for:

- policy tests;
- deterministic contracts;
- regression fixtures where the required path matters.

They can be too brittle for open capability evaluation when several trajectories are valid.

The schema can express this distinction by keeping `trajectory` and `outcome` evaluation surfaces separate rather than assigning one scalar maturity level.

## Reliability qualification

The inspected harness has deterministic regression/gating semantics, but this record does not establish repeated stochastic trials as part of the upstream slice.

Therefore:

```text
regression_gate: true
repeated_trials: false
```

is intentional rather than contradictory.

## Production-certification boundary

A green deterministic evaluation suite does not certify the evaluated agent as production-ready. Production evidence still requires representative outcome evals, stochastic/repeated trials where relevant, operational telemetry, security and deployment-specific controls.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: false
normalization_issue: evaluation must remain multi-surface; final freeze audit should verify boolean/list fields remain sufficient without introducing a misleading ordinal maturity score
```

## Evidence

- [`../../quarries/genai-agents.md`](../../quarries/genai-agents.md)
- [`../../mining-site/SOURCES.md`](../../mining-site/SOURCES.md)
- official evaluation contrast registered as `S-104`
