# REC-002 — HITL Approval Agent

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-002
name: GenAI_Agents human-in-the-loop approval agent
schema_revision: mk1-draft-2026-09-16.1
classification_scope: consequential action proposal→approval/edit/reject→dispatcher
source_receipts:
  - S-001
  - S-105
  - S-106
  - S-107
primary_quarries:
  - quarries/genai-agents.md
evidence_state: SUPPORTED / QUALIFIED
production_certification: false
```

Pinned upstream snapshot: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`.

## Classification

```yaml
identity:
  name: HITL approval agent
  source: NirDiamant/GenAI_Agents/all_agents_tutorials/human_in_the_loop_approval_agent.ipynb
  snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
  evidence_state: SUPPORTED

control:
  primary_authority: mixed
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads:
    - low-risk lookup/tool results
  writes:
    - refund/mutating action through protected dispatcher
  generated_code_execution: false
  shell: false
  browser: none
  database: unknown
  communication: none
  publication: none
  file_egress: false
  capability_compositions:
    - model-proposed consequential mutation + human approval + dispatcher enforcement

side_effects:
  class: S3
  reversible: partial | unknown
  external_mutation: true
  data_egress: none | unknown
  verification: audit/action path is tested; downstream business-system outcome verification remains implementation-specific

state:
  runtime_state: structured
  checkpointing: memory
  persistence_backend: LangGraph persisted thread/checkpointer semantics in inspected integration slice; production durability not established by this tutorial record
  replay_semantics: partial
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: unknown
  locking: unknown

memory:
  semantic_role: []
  scope: none
  persistence: process
  retrieval_policy: not semantic memory
  write_policy: not semantic memory
  isolation_key: thread/execution scope for resume path
  retention_policy: not established
  provenance: checkpointer/runtime state, not long-term memory

human_control:
  level: H4
  mode: approval_edit_before
  dispatcher_enforcement: yes
  enforcement_owner: mixed
  enforcement_boundary: deterministic runtime/tool dispatcher prevents consequential execution without valid approval; human owns approve/edit/reject decision
  approval_binding: modified action is revalidated; unexpected/invalid arguments are rejected before execution

errors_and_retries:
  error_model: structured | mixed
  retry_owner: runtime/application
  retry_budget: not established as a general retry policy
  idempotency: not established for every downstream mutation
  unknown_outcome_handling: not established for post-dispatch timeout/failure

termination:
  success_predicate: approved/validated action executes or rejection terminates without side effect; external business outcome still requires downstream verification where material
  terminal_failure_predicate: validation/policy denial/rejection/runtime error
  turn_budget: framework/application-dependent; not central to this evidence slice
  turn_budget_enforcement: unknown
  tool_budget: not established
  tool_budget_enforcement: unknown
  time_budget: not established
  time_budget_enforcement: unknown
  cost_or_token_budget: not established
  cost_or_token_budget_enforcement: unknown
  overshoot_semantics: unknown
  oscillation_detection: not established
  cancellation: interrupt/reject path supported at workflow level
  cancellation_effective_boundary: approval is before protected dispatcher; replay behavior before interrupt remains relevant

evaluation:
  static_contracts:
    - argument validation
    - policy/dispatcher bypass protection
  unit_integration:
    - dedicated HITL behavior tests
    - conditional LangGraph pause/resume integration test
  trajectory:
    - approve/edit/reject paths
    - direct dispatcher bypass rejection
  outcome:
    - rejection prevents side effect
    - mutation path executes only after authorization path
  repeated_trials: false
  regression_gate: partial
  production_observability: false

protocols: []

security:
  trust_boundaries:
    - model proposal
    - validation/risk classification
    - human reviewer
    - protected dispatcher
    - downstream mutation target
  least_privilege: partial
  sandbox: none | unknown
  data_classification: application-specific
  receipts:
    - direct dispatcher bypass is rejected in dedicated tests
    - modified actions are revalidated before execution
    - audit events capture decisions/actions

reproducibility:
  model_receipt: not material to core HITL invariants
  dependency_receipt: tutorial/test slice pins a LangGraph version distinct from repository root environment
  external_api_receipt: downstream refund target details remain application-specific
  execution_evidence: dedicated tests for low-risk bypass, protected mutation, approve/reject/modify, validation and audit behavior

unknowns:
  - durable production checkpointer/backend semantics
  - replay/idempotency behavior for any side effects placed before interrupt
  - downstream timeout/unknown-outcome semantics after mutation dispatch
  - concurrency behavior for simultaneous approvals on shared external state
  - complete downstream business outcome verification
```

## Material observations

| Observation | State | Evidence |
|---|---|---|
| Low-risk lookup can execute without approval | OBSERVED | dedicated upstream tests summarized in quarry |
| Refund/mutating request pauses before side effect | OBSERVED | dedicated upstream tests summarized in quarry |
| Direct dispatcher bypass is rejected | OBSERVED | dedicated upstream tests summarized in quarry |
| Approve/reject/modify have distinct tested behavior | OBSERVED | dedicated upstream tests summarized in quarry |
| Modified arguments are revalidated | OBSERVED | dedicated upstream tests summarized in quarry |
| Unexpected/invalid numeric arguments are rejected | OBSERVED | dedicated upstream tests summarized in quarry |
| Audit events capture decisions/actions | OBSERVED | dedicated upstream tests summarized in quarry |
| Pause/resume uses persisted thread state in inspected LangGraph integration path | OBSERVED | upstream integration slice + official LangGraph contrast |

## Consequential side-effect path

```text
model proposes action
      ↓
schema validation
      ↓
risk classification
      ├─ low risk → execute permitted lookup
      └─ mutation → persist pending request
                       ↓
                    interrupt
                       ↓
              approve / edit / reject
                 │        │        │
                 │        │        └─ terminate without effect
                 │        └─ revalidate modified action
                 └──────────── authorization state
                                ↓
                       protected dispatcher
                                ↓
                         external mutation
                                ↓
                              audit
```

The strongest property is not merely `human reviewed`. It is that the consequential dispatcher is protected against direct bypass in the tested slice.

## Replay qualification

LangGraph interrupt/resume semantics can replay code before an interrupt boundary. Therefore:

```text
approval-before-dispatch = strong
side effect before interrupt = must be replay-safe/idempotent
```

This record does not infer production-safe replay for arbitrary surrounding code.

## Production-certification boundary

This record supports a strong HITL enforcement pattern. It does **not** certify every downstream mutation as idempotent, every deployment as durably persisted, every timeout as safely recoverable, or the tutorial as production-ready.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: false
normalization_issue: current human_control fields correctly distinguish human decision, deterministic dispatcher enforcement, approval binding and replay qualification
```

## Evidence

- [`../../quarries/genai-agents.md`](../../quarries/genai-agents.md)
- [`../../mining-site/SOURCES.md`](../../mining-site/SOURCES.md)
- official LangGraph HITL/interrupt/persistence sources registered as `S-105`–`S-107`
