# REC-009 — DataScribe / Database Authority

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-009
name: GenAI_Agents DataScribe / database discovery fleet
schema_revision: mk1-draft-2026-09-16.1
classification_scope: database exploration agent with source-level warning about possible DML authority
source_receipts:
  - S-001
primary_quarries:
  - quarries/genai-agents-p0-p1-callpaths.md
  - quarries/genai-agents-risk-scan.md
evidence_state: QUALIFIED
production_certification: false
```

Pinned upstream snapshot: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`.

## Classification

```yaml
identity:
  name: database discovery fleet / DataScribe representative
  source: NirDiamant/GenAI_Agents/all_agents_tutorials/database_discovery_fleet.ipynb
  snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
  evidence_state: QUALIFIED

control:
  primary_authority: model_directed | mixed
  horizon: bounded_multistep | unknown
  topology: mixed | unknown
  model_count: implementation-dependent

capabilities:
  reads:
    - database schema/data depending configured principal
  writes:
    - potentially database mutation if credentials/dispatcher permit DML
  generated_code_execution: false
  shell: false
  browser: none
  database: write_capable | read_only depending actual database principal
  communication: none
  publication: none
  file_egress: unknown
  capability_compositions:
    - model-generated/query-directed database access + credential-level DB authority

side_effects:
  class: S0 | S3 | S4 depending effective DB principal and reachable statements
  reversible: unknown
  external_mutation: unknown
  data_egress: content | unknown
  verification: exact mutation dispatcher/filter path remains UNKNOWN in inspected evidence

state:
  runtime_state: structured | unknown
  checkpointing: unknown
  persistence_backend: database is business/environment data, not automatically agent checkpointing
  replay_semantics: unknown
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: database transaction/concurrency semantics depend on concrete backend/path
  locking: database/application-defined

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: database retrieval is not semantic agent memory by default
  write_policy: not applicable as memory
  isolation_key: database credential/schema scope
  retention_policy: database policy
  provenance: query/database result provenance required for downstream claims

human_control:
  level: unknown
  mode: unknown
  dispatcher_enforcement: unknown
  enforcement_owner: infrastructure | database principal is the strongest established boundary in current evidence
  enforcement_boundary: source itself recommends a READONLY database user; exact application-level query filtering is not proven
  approval_binding: unknown

errors_and_retries:
  error_model: unknown
  retry_owner: application/model/runtime dependent
  retry_budget: unknown
  idempotency: query/transaction dependent
  unknown_outcome_handling: critical if write-capable path exists; not established

termination:
  success_predicate: exploration/query task-specific; not established as universal external outcome
  terminal_failure_predicate: database/runtime/task dependent
  turn_budget: unknown
  turn_budget_enforcement: unknown
  tool_budget: unknown
  tool_budget_enforcement: unknown
  time_budget: unknown
  time_budget_enforcement: unknown
  cost_or_token_budget: unknown
  cost_or_token_budget_enforcement: unknown
  overshoot_semantics: unknown
  oscillation_detection: unknown
  cancellation: unknown
  cancellation_effective_boundary: database transaction/query dependent

evaluation:
  static_contracts:
    - source warning/recommended read-only credential boundary
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols: []

security:
  trust_boundaries:
    - model/query generation
    - application DB dispatcher
    - database credentials/principal
    - database engine
    - target schema/data
  least_privilege: application_required
  sandbox: none | not applicable
  data_classification: database/application-specific
  receipts:
    - upstream notebook explicitly warns it has no safety rails and may attempt INSERT/UPDATE/DELETE
    - upstream recommends a READONLY database user

reproducibility:
  model_receipt: implementation-dependent
  dependency_receipt: repository snapshot pinned
  external_api_receipt: concrete DB engine/principal not normalized as one universal runtime fact
  execution_evidence: source/call-path warning sufficient for capability classification; exact mutation dispatcher remains unverified

unknowns:
  - exact reachable DML dispatcher path
  - parser/statement allowlist/denylist behavior
  - database transaction isolation
  - whether credentials in a concrete run are read-only or write-capable
  - retry/idempotency semantics for mutating statements
  - timeout unknown-outcome semantics for writes
  - human approval/policy enforcement around consequential SQL
```

## Core engineering result

The intended use case is “database exploration”, but risk is determined by **effective authority**, not intent.

```text
READONLY DB PRINCIPAL
        → read-only database capability

WRITE-CAPABLE PRINCIPAL
        +
model/query dispatcher
        → potentially consequential mutation authority
```

The strongest observed recommendation is therefore outside the model:

> Use a database principal whose credentials cannot perform forbidden writes.

That boundary is stronger than prompting the model to “only generate SELECT”.

## Why this record remains qualified

The inspected evidence does **not** fully reconstruct the lower-level mutation dispatcher or prove a specific SQL filter.

Therefore this record must not claim:

```text
DML definitely reachable
or
DML definitely blocked
```

It records that the tutorial itself warns the path may attempt DML and that least-privilege credentials materially determine effective capability.

## Production-certification boundary

This record does not certify read-only enforcement, database isolation, safe retries, transaction rollback or production suitability. Those require the concrete database principal/dispatcher/runtime receipt.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: false
normalization_issue: confirms capability classification must use effective credentials/dispatcher authority rather than task intent; UNKNOWN preserves unresolved lower-level mutation path
```

## Evidence

- [`../../../quarries/genai-agents-p0-p1-callpaths.md`](../../../quarries/genai-agents-p0-p1-callpaths.md)
- [`../../../quarries/genai-agents-risk-scan.md`](../../../quarries/genai-agents-risk-scan.md)
- [`../../../mining-site/SOURCES.md`](../../../mining-site/SOURCES.md)
