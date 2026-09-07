# R-009 — DataScribe Database Explorer

Status: **CLASSIFIED WITH MATERIAL UNKNOWN**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/database_discovery_fleet.ipynb`

## Normalized record

```yaml
identity:
  name: DataScribe Database Explorer
  evidence_state: QUALIFIED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: manager_workers
  model_count: multiple logical agents

capabilities:
  reads: [DATABASE_SCHEMA, DATABASE_ROWS]
  writes: [DATABASE_WRITE_IF_CREDENTIAL_PERMITS]
  generated_code_execution: false
  shell: false
  browser: none
  database: write_capable
  communication: none
  publication: none
  file_egress: false
  delegation: true
  capability_compositions:
    - supervisor + specialized_agents + model_authored_database_query + database_principal

side_effects:
  observed_class: unknown
  reachable_class: S4
  reversible: unknown
  external_mutation: unknown
  data_egress: none
  verification: database response; exact dispatcher/filter path not fully reconstructed

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: workflow state + database
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: database query rather than semantic memory
  write_policy: n/a
  isolation_key: database credential/principal
  retention_policy: database-owned
  provenance: query/result provenance incomplete in inspected evidence

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: unknown
  approval_binding: none established

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: unknown
  idempotency: unknown for write-capable statements
  unknown_outcome_handling: unknown

termination:
  success_predicate: supervisor/workers complete requested exploration/analysis
  terminal_failure_predicate: workflow/query failure
  turn_budget: unknown
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: unknown
  cancellation: unknown

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: [database query results]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_query_generation, query_to_database_driver, database_principal_to_database]
  least_privilege: depends_on_database_principal
  sandbox: none
  data_classification: database-dependent
  authorization_boundary: database principal is the strongest evidenced boundary
  receipts: query/result receipt shape unknown

unknowns:
  - exact lower-level query dispatcher
  - SQL parser/statement filtering
  - whether mutating statements are actually reachable in current implementation
  - transaction/rollback behavior
  - query allowlist/read-only enforcement beyond credentials
```

## Evidence basis

The notebook itself explicitly warns that it is untested, has no safety rails, may attempt `INSERT`, `UPDATE` or `DELETE`, should not be used on production data and recommends a **READONLY database user**.

Primary quarry path: `quarries/genai-agents-p0-p1-callpaths.md` P0-08.

## Classification result

The important MK1 result is conditional authority:

```text
same model/workflow
+ enforced read-only DB principal  → approximately R1/S0 read authority
+ write-capable DB principal       → S3/S4-capable authority
```

Therefore intended use or SQL prompt wording is weaker evidence than the database principal's actual privileges.

## MK2 handoff seed

Operational contract must specify DB principal privileges, statement policy, transaction mode, time/row budgets, audit/query receipts and mutation denial tests.
