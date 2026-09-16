# REC-XXX — <System / Representative Case>

Status: **IN_PROGRESS | MATERIALIZED | QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Observed/classified: **YYYY-MM-DD**

> This template is a classification contract, not a form that must be filled blindly. Leave material facts `unknown` or omit non-applicable optional detail when evidence does not support them.

## Record identity

```yaml
record_id: REC-XXX
name:
schema_revision: mk1-draft-2026-09-16.1
classification_scope:
source_receipts:
  -
primary_quarries:
  -
evidence_state:
production_certification: false
```

## Classification

```yaml
identity:
  name:
  source:
  snapshot:
  evidence_state: OBSERVED | SOURCE_CLAIM | INFERRED | SUPPORTED | QUALIFIED | CONTRADICTED | UNKNOWN

control:
  primary_authority: deterministic | model_routed | model_directed | mixed
  horizon: single_step | bounded_multistep | open_ended
  topology: single_model | router_workers | manager_workers | peers | mixed
  model_count:

capabilities:
  reads: []
  writes: []
  generated_code_execution: false
  shell: false
  browser: none | read_only | transactional | general | unknown
  database: none | read_only | write_capable | unknown
  communication: none | draft | external_send | unknown
  publication: none | draft | live | unknown
  file_egress: false | true | unknown
  capability_compositions: []

side_effects:
  class: S0 | S1 | S2 | S3 | S4 | unknown
  reversible: yes | no | partial | unknown
  external_mutation: false | true | unknown
  data_egress: none | metadata | content | file_bytes | mixed | unknown
  verification:

state:
  runtime_state: none | transient | structured | unknown
  checkpointing: none | memory | durable | unknown
  persistence_backend:
  replay_semantics: known | partial | unknown
  invocation_concurrency: serial_only | concurrent | bounded_concurrent | framework_defined | unknown
  writer_model: single_writer | multi_writer | reducer_merge | optimistic | locked | framework_defined | unknown
  concurrency_conflict_semantics:
  locking: none | local | distributed | optimistic | custom | framework_defined | unknown

memory:
  semantic_role: []
  scope: none | session | cross_session | user | project | shared | unknown
  persistence: none | process | local_durable | remote_durable | unknown
  retrieval_policy:
  write_policy:
  isolation_key:
  retention_policy:
  provenance:

human_control:
  level: H0 | H1 | H2 | H3 | H4 | mixed | unknown
  mode: none | review_after | approval_before | approval_edit_before | mixed | unknown
  dispatcher_enforcement: yes | no | partial | unknown
  enforcement_owner: runtime_code | human | model_judge | provider_guardrail | infrastructure | mixed | unknown
  enforcement_boundary:
  approval_binding:

errors_and_retries:
  error_model: prose | structured | mixed | unknown
  retry_owner: model | tool | runtime | provider_sdk | mixed | none | unknown
  retry_budget:
  idempotency:
  unknown_outcome_handling:

termination:
  success_predicate:
  terminal_failure_predicate:
  turn_budget:
  turn_budget_enforcement:
  tool_budget:
  tool_budget_enforcement:
  time_budget:
  time_budget_enforcement:
  cost_or_token_budget:
  cost_or_token_budget_enforcement:
  overshoot_semantics:
  oscillation_detection:
  cancellation:
  cancellation_effective_boundary:

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false | true | unknown
  regression_gate: false | true | unknown
  production_observability: false | true | unknown

protocols: []

security:
  trust_boundaries: []
  least_privilege: yes | no | partial | unknown
  sandbox: none | process | container | vm | managed | unknown
  data_classification:
  receipts: []

reproducibility:
  model_receipt:
  dependency_receipt:
  external_api_receipt:
  execution_evidence:

unknowns: []
```

## Material observations

Only include observations that materially explain the classification.

| Observation | State | Evidence |
|---|---|---|
|  | OBSERVED/SUPPORTED/etc. | quarry/source receipt |

## Capability composition

Describe dangerous or important **combinations**, not only individual capabilities.

Example:

```text
model-directed tool choice
+ generated code
+ shell execution
+ network access
= materially higher blast radius than any one field alone
```

If no material composition is evidenced, state `none established by current evidence` rather than inventing one.

## Side-effect path

For consequential systems, reconstruct:

```text
model/routing decision
→ proposed action
→ validation / approval boundary
→ actual dispatcher
→ external effect
→ verification / receipt
```

Mark every unsupported link `UNKNOWN`.

## Termination semantics

Distinguish:

```text
runtime stopped
vs
semantic objective satisfied
vs
external effect verified
```

A framework stop reason is not automatically a success predicate.

## Evidence gaps / UNKNOWNs

List only material unknowns that could change classification, risk, reliability or MK decisions.

Each UNKNOWN should include, where useful:

```text
unknown
why it matters
what evidence would close it
routing: MK1 | MK2 | MK5+
```

## Production-certification boundary

Explicitly state:

```text
This record classifies architecture and evidence at MK1.
It does not certify this system as production-ready, secure, reliable or superior.
```

If separate production evidence exists, link it and state its exact scope.

## Schema pressure result

```yaml
fits_current_schema: true | false | qualified
new_dimension_required: false | candidate
normalization_issue:
```

If proposing a schema change, apply the admission rule in `../CLASSIFICATION_QUEUE.md`; do not add framework-specific fields directly from this record.

## Related artifacts

- registry: [`README.md`](./README.md)
- schema: [`../CLASSIFICATION_SCHEMA.md`](../CLASSIFICATION_SCHEMA.md)
- dimensions: [`../DIMENSIONS.md`](../DIMENSIONS.md)
- normalization rules: [`../NORMALIZATION_RULES.md`](../NORMALIZATION_RULES.md)
- gates: [`../GATES.md`](../GATES.md)
