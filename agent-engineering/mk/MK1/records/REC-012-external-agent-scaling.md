# REC-012 — Real LLM agent topology vs baseline (external evidence)

Status: **MATERIALIZED / QUALIFIED_UPSTREAM**  
Schema: **`mk1-draft-2026-09-16.1`**  
Observed: **2026-10-12**  
Certification: **NONE**; local inference/reproduction **NOT RUN**.

## Identity and evidence

```yaml
record_id: REC-012
name: source-reported cross-benchmark single-vs-multi LLM topology contrast
schema_revision: mk1-draft-2026-09-16.1
classification_scope: 260 model/benchmark/topology configurations; six domains; same-task single versus multi architecture
source_receipts: [S-118, S-119]
primary_quarries: [quarries/multiagent-external-scaling-evidence.md]
evidence_state: QUALIFIED
evidence_basis:
  authors_reported_execution: true
  public_code_and_summary_data: true
  summary_data_reaggregated_by_us: true
  independent_original_llm_rerun: false
  independent_latency_failure_trace_replay: false
production_certification: false
```

Paper [arXiv v3](https://arxiv.org/html/2512.08296v3); paper DOI `10.1038/s42256-026-01268-y`; code [`v2.2.2@072276fd`](https://github.com/ybkim95/agent-scaling/tree/072276fd3ae71cf095587f1232e8eefc17a21898).

## Normalized classification — contrasted family

```yaml
identity:
  name: Single-agent and four multi-agent variants across six agentic benchmarks
  source: ybkim95/agent-scaling + paper arXiv:2512.08296v3
  snapshot: paper_v3_2026-04-08; code_v2.2.2_072276fd
  evidence_state: QUALIFIED

control:
  primary_authority: model_directed
  horizon: bounded_multistep
  topology: mixed  # independent, manager_workers, peers, mixed; single_model is baseline
  model_count: varies_by_topology

capabilities:
  reads: [benchmark_task_context, tool_observations]
  writes: [benchmark_environment_actions_when_enabled]
  generated_code_execution: unknown
  shell: unknown
  browser: unknown
  database: unknown
  communication: none
  publication: none
  file_egress: unknown
  capability_compositions: [LLM_planning_plus_benchmark_tools_plus_inter_agent_coordination]

side_effects:
  class: unknown
  reversible: unknown
  external_mutation: unknown
  data_egress: unknown
  verification: domain_specific_task_grading_not_production_receipts

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: unknown
  replay_semantics: partial
  invocation_concurrency: framework_defined
  writer_model: unknown
  concurrency_conflict_semantics: benchmark_and_topology_dependent
  locking: unknown

memory:
  semantic_role: []
  scope: session
  persistence: unknown
  retrieval_policy: working_context_per_agent_or_orchestrator
  write_policy: not_established_as_long_term_memory
  isolation_key: not_established
  retention_policy: unknown
  provenance: source_execution_traces_and_benchmark_context

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: unknown
  enforcement_owner: runtime_code
  enforcement_boundary: budgets_and_benchmark_tool_dispatch
  approval_binding: not_studied

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: bounded_iterations_not_universal_tool_retries
  idempotency: unknown
  unknown_outcome_handling: unknown

termination:
  success_predicate: benchmark_grader_task_success
  terminal_failure_predicate: runtime_budget_exhaustion_or_benchmark_failure
  turn_budget: bounded_per_architecture
  turn_budget_enforcement: configuration_exists_but_not_independently_rerun
  tool_budget: unknown
  tool_budget_enforcement: unknown
  time_budget: centralized_config_max_execution_time_600_worker_timeout_300_seconds
  time_budget_enforcement: source_configuration_observed_not_independently_tested
  cost_or_token_budget: authors_claim_matched_total_reasoning_compute
  cost_or_token_budget_enforcement: source_reported_not_independently_verified
  overshoot_semantics: unknown
  oscillation_detection: unknown
  cancellation: unknown
  cancellation_effective_boundary: unknown

evaluation:
  static_contracts: [architecture_and_benchmark_configuration]
  unit_integration: [upstream_repo_tests_present_success_not_independently_checked]
  trajectory: [authors_trace_error_categories,coordination_overhead,turn_count]
  outcome: [published_per_configuration_success_260_rows, separate_S119_100_scenarios_5_repeats]
  repeated_trials: unknown  # many tasks/configs; cannot infer repeated identical stochastic draws
  regression_gate: false
  production_observability: false

protocols: []
security:
  trust_boundaries: [model_provider,tool_environment,agent_handoff,external_benchmark_sources,judge]
  least_privilege: unknown
  sandbox: unknown
  data_classification: benchmark_dependent
  receipts: [public_source_csv,source_reported_methods,pinned_configs]
reproducibility:
  model_receipt: three_public_model_families_source_reported
  dependency_receipt: code_v2.2.2_072276fd
  external_api_receipt: upstream_per_provider_keys_and_benchmark_credentials_required
  execution_evidence: SOURCE_REPORTED_EXECUTION_PLUS_PUBLIC_260_ROW_SUMMARY_REAGGREGATION
unknowns:
  - no_independent_provider_model_trace_replay
  - no_independent_latency_and_cost_reproduction
  - no_test_of_hard_cancellation_or_production_side_effects
  - architecture_specific_prompt_and_grader_confounding_possible
  - cross_domain_predictive_transfer_not_established
```

## Admission/outcome evidence (separate from taxonomy — PA-01)

```yaml
admission_hypotheses: [parallel_decomposition,independent_verification,context_partitioning]
single_baseline: 1 model with shared benchmark tools and task
variants: [3_independent,manager_plus_3_workers,3_peers,hybrid]
outcome_evidence:
  finance_single_mean: 0.34889
  finance_centralized_mean: 0.63111
  plancraft_single_mean: 0.56782
  plancraft_centralized_mean: 0.28173
  basis: arithmetic_grouping_of_author_deposited_CSV_not_original_run
cost_evidence: source_reported_inter_agent_overhead_and_token_efficiency
latency_evidence: S118_directional_unverified_per_run_wall_clock; S119_separate_toolless_comparison_2_32_vs_11_83_seconds_GPT4o_and_6_06_vs_35_59_seconds_GPT5_5_author_reported
coordination_failure_evidence: source_reported_failure_taxonomy_and_trace_measures
termination_evidence: explicit_round_and_timeout_config_present; enforcement_not_independently_verified
interpretation: MULTI_AGENT_BENEFIT_IS_TASK_DEPENDENT; no_general_winner
```

The current MK1 YAML schema encodes topology and evaluation but **does not yet contain the named comparison-evidence fields above**. This appendix is evidence metadata **outside** the frozen schema. PA-01 remains open until the final freeze audit chooses an explicit contract reference or a versioned field change.

## Scalar normalization receipt — 2026-10-12

These edits choose **one scoped enum value** or preserve uncertainty as `unknown`. The original classifications are reproduced below for traceability and remain evidence of variations, **not confirmed settings of a single deployed system**.

- `control.model_count`: `1 baseline | 3 workers or 3 workers + lead depending topology` → `varies_by_topology`
- `capabilities.generated_code_execution`: `unknown_by_benchmark` → `unknown`
- `capabilities.shell`: `unknown_by_benchmark` → `unknown`
- `capabilities.browser`: `unknown_by_benchmark` → `unknown`
- `capabilities.database`: `unknown_by_benchmark` → `unknown`
- `errors_and_retries.retry_owner`: `runtime_or_model_dependent` → `mixed`

**Per-topology model-count comparison (authors' experiment):**

| Variant | `control.topology` (specific instance) | Model-role count |
|---|---|---|
| Single baseline | `single_model` | one model-directed agent |
| Independent parallel | `peers` / independent role group | three agents in examined architecture |
| Centralized | `manager_workers` | lead plus three workers in reported configuration |
| Decentralized | `peers` | three agent peers |
| Hybrid | `mixed` | topology-specific worker and coordinator configuration |

`model_count` in the family-level record is a scoped descriptor (`varies_by_topology`), **not** an exact invariant or a computed cost claim. Browser/shell/generated-code capabilities were not established for every benchmark, so `unknown` must not be silently converted into `false`.

## Pass limits

G7 **PASS / QUALIFIED_UPSTREAM_EVIDENCE** for MK1 taxonomy pressure: S-118 source-reported tool-using comparison and validated arithmetic on its public summary CSV, plus separately S-119 source-reported short-context latency/token/failure comparison. This is **qualified** by source trust and independent reanalysis limits. Two studies are **not one experiment**. It does **not** prove performance, cost, safety or reliability for Prompt Machine, Foundry, Content Seller, ECHO or any application.

The prior [deterministic REC-012 fixture](./REC-012-deterministic-topology-draft.md) remains separate, historically accurate and explicitly not a model comparison.

## Related

- [Source S-118](../../../mining-site/S-118-agent-scaling-research.md)
- [Independent complement S-119](../../../mining-site/S-119-mars-rover-agent-benchmark.md)
- [Detailed comparison quarry](../../../quarries/multiagent-external-scaling-evidence.md)
- [Original gate spec](../MULTI_AGENT_BASELINE_SPEC.md)
- [Gate dashboard](../GATES.md)
