# MK1 — Classification Schema

Status: **OPEN / IN PROGRESS**

This is the normalized record shape used to classify representative agent systems without relying on framework or marketing labels.

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
  browser: none | read_only | transactional | general
  database: none | read_only | write_capable
  communication: none | draft | external_send
  publication: none | draft | live
  file_egress: false
  capability_compositions: []

side_effects:
  class: S0 | S1 | S2 | S3 | S4 | unknown
  reversible: yes | no | partial | unknown
  external_mutation: false
  data_egress: none | metadata | content | file_bytes | mixed | unknown
  verification:

state:
  runtime_state: none | transient | structured
  checkpointing: none | memory | durable
  persistence_backend:
  replay_semantics: known | partial | unknown

memory:
  semantic_role: []
  scope: none | session | cross_session | user | project | shared
  persistence: none | process | local_durable | remote_durable
  retrieval_policy:
  write_policy:
  isolation_key:
  retention_policy:
  provenance:

human_control:
  level: H0 | H1 | H2 | H3 | H4 | mixed | unknown
  mode: none | review_after | approval_before | approval_edit_before | mixed
  dispatcher_enforcement: yes | no | unknown
  approval_binding:

errors_and_retries:
  error_model: prose | structured | mixed | unknown
  retry_owner: model | tool | runtime | provider_sdk | mixed | none
  retry_budget:
  idempotency:
  unknown_outcome_handling:

termination:
  success_predicate:
  terminal_failure_predicate:
  turn_budget:
  tool_budget:
  time_budget:
  cost_or_token_budget:
  oscillation_detection:
  cancellation:

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols:
  - name:
    revision:
    role:
    transport:
    capabilities:
    auth_model:
    extensions:

security:
  trust_boundaries: []
  least_privilege: yes | no | partial | unknown
  sandbox: none | process | container | vm | managed | unknown
  data_classification:
  receipts:

reproducibility:
  model_receipt:
  dependency_receipt:
  external_api_receipt:
  execution_evidence:

unknowns: []
```

## Schema rules

1. No implementation must populate every field.
2. Missing material facts remain `unknown`; they are not inferred from neighboring fields.
3. Framework/provider names belong in identity/reproducibility metadata, not in top-level architecture classes.
4. A system may have mixed control authority across stages; record this rather than forcing one misleading label.
5. Capability composition matters: multiple individually moderate permissions may combine into a high-blast-radius path.
6. Side-effect class is explicit and independent of control authority.
7. Data egress is represented even when the logical business operation sounds read-only or transformational.
8. Protocol records are revision-aware. `MCP=true` without revision/role/capability set is incomplete.
9. Human review in one node does not prove dispatcher enforcement for every consequential tool.
10. Evidence-state vocabulary matches the domain reasoning-state labels and must remain explicit.
11. A classification record describes the system supported by evidence; it is not a production-readiness certificate.

## Minimal record

When evidence is sparse, the minimum useful record is:

```yaml
identity:
control:
capabilities:
side_effects:
human_control:
termination:
evaluation:
security:
unknowns:
```

The objective is not completeness by form-filling; it is explicit architecture with visible uncertainty.
