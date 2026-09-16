# REC-011 — Memory Lifecycle Contrast Fixture

Status: **MATERIALIZED / QUALIFIED CONTRAST FIXTURE**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Why this record is a contrast fixture

This record intentionally does **not** pretend that one framework object represents “memory”.

Its purpose is to pressure-test whether MK1 can distinguish:

```text
runtime state
checkpoint/persistence
session history
cross-session semantic/episodic memory
external knowledge / RAG
```

using evidence from the broad `GenAI_Agents` corpus and the specialized `Agent_Memory_Techniques` corpus.

## Record identity

```yaml
record_id: REC-011
name: memory lifecycle contrast fixture
schema_revision: mk1-draft-2026-09-16.1
classification_scope: cross-source distinction between persistence/state and intentional memory lifecycle
source_receipts:
  - S-001
  - S-002
primary_quarries:
  - quarries/genai-agents-p0-p1-callpaths.md
  - quarries/cross-source-memory-production-mcp.md
evidence_state: SUPPORTED / QUALIFIED
production_certification: false
```

Pinned sources:

```text
S-001  NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46
S-002  NirDiamant/Agent_Memory_Techniques@b7f7240eb4d4510f3b45300a89126858a474b31d
```

## Contrast A — Checkpoint/session persistence

Representative evidence includes LangGraph examples using `MemorySaver`/checkpointers/stores for execution/session continuity.

Normalized classification:

```yaml
state:
  runtime_state: structured
  checkpointing: memory | durable depending concrete example
  persistence_backend: example-dependent
  replay_semantics: example-dependent

memory:
  semantic_role: []
  scope: session | unknown
  persistence: process | local_durable | unknown
  retrieval_policy: not established as semantic retrieval merely because a checkpointer/store exists
  write_policy: runtime/checkpoint-driven
  isolation_key: thread/session dependent
  retention_policy: unknown
  provenance: execution-state provenance
```

Key rule:

> A persisted checkpoint can survive process/turn boundaries without becoming semantic long-term memory.

## Contrast B — Intentional long-term memory

The specialized memory corpus separates short-term context and long-term memory techniques across families and explicitly distinguishes persistence, retrieval mechanism, token-cost behavior and intended lifecycle.

Normalized shape:

```yaml
memory:
  semantic_role:
    - conversation
    - episodic
    - semantic
    - procedural
    - working
    - shared
    - external_knowledge
  scope: session | cross_session | user | project | shared
  persistence: none | process | local_durable | remote_durable
  retrieval_policy: recency | semantic | lexical | graph | time | hybrid | tool_selected | custom
  write_policy: explicit | automatic | model_selected | background_consolidation | custom
  isolation_key: session | user | tenant | project | shared | custom
  retention_policy: technique/application dependent
  provenance: technique/application dependent
```

This is a **schema pressure shape**, not a claim that every memory implementation provides every role/policy.

## Contrast C — RAG / external knowledge

```text
retrieve external source material
      !=
remember information about a user/session
```

A vector/database/document retriever may provide durable knowledge without representing agent/user memory.

Therefore external knowledge belongs to context/knowledge retrieval semantics unless the system intentionally treats it as a retained memory lifecycle.

## Cross-source classification

```yaml
identity:
  name: memory lifecycle contrast fixture
  source: S-001 + S-002
  snapshot:
    S-001: 4c95ae14cc2462c442b5c064cccd74430d02bc46
    S-002: b7f7240eb4d4510f3b45300a89126858a474b31d
  evidence_state: SUPPORTED

control:
  primary_authority: mixed
  horizon: bounded_multistep | unknown
  topology: mixed
  model_count: implementation-dependent

capabilities:
  reads:
    - runtime state/checkpoints depending implementation
    - retained memory entries depending technique
    - external knowledge depending retriever
  writes:
    - checkpoints/session state depending runtime
    - memory entries depending write policy
  generated_code_execution: false
  shell: false
  browser: none | unknown
  database: read_only | write_capable | unknown
  communication: none
  publication: none
  file_egress: unknown
  capability_compositions:
    - memory write + cross-session retrieval can influence future model behavior

side_effects:
  class: S1 | S2 | unknown
  reversible: partial | unknown
  external_mutation: implementation-dependent
  data_egress: unknown
  verification: memory quality/correctness requires separate evaluation; persistence alone is not correctness

state:
  runtime_state: structured
  checkpointing: framework/technique-dependent
  persistence_backend: implementation-dependent
  replay_semantics: implementation-dependent
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: memory/update conflict policy is technique/application-dependent
  locking: unknown

memory:
  semantic_role:
    - lifecycle-dependent
  scope: session | cross_session | user | project | shared | unknown
  persistence: none | process | local_durable | remote_durable | unknown
  retrieval_policy: explicit lifecycle dimension
  write_policy: explicit lifecycle dimension
  isolation_key: explicit lifecycle dimension
  retention_policy: explicit lifecycle dimension
  provenance: explicit lifecycle dimension

human_control:
  level: unknown
  mode: unknown
  dispatcher_enforcement: unknown
  enforcement_owner: application/runtime
  enforcement_boundary: memory write/read policy is implementation-specific
  approval_binding: not generally established

errors_and_retries:
  error_model: implementation-dependent
  retry_owner: implementation-dependent
  retry_budget: implementation-dependent
  idempotency: memory-write dependent
  unknown_outcome_handling: memory-store dependent

termination:
  success_predicate: memory subsystem operation success is not evidence that recalled content is useful/correct
  terminal_failure_predicate: implementation-dependent
  turn_budget: application-dependent
  turn_budget_enforcement: application-dependent
  tool_budget: application-dependent
  tool_budget_enforcement: application-dependent
  time_budget: application-dependent
  time_budget_enforcement: application-dependent
  cost_or_token_budget: context/memory retrieval can affect token budget but exact contract is implementation-dependent
  cost_or_token_budget_enforcement: unknown
  overshoot_semantics: unknown
  oscillation_detection: not applicable/generalized
  cancellation: implementation-dependent
  cancellation_effective_boundary: unknown

evaluation:
  static_contracts:
    - isolation/lifecycle policy can be statically specified
  unit_integration:
    - implementation-dependent
  trajectory:
    - retrieval/write behavior may be evaluated
  outcome:
    - memory usefulness/correctness must be measured separately
  repeated_trials: unknown
  regression_gate: unknown
  production_observability: unknown

protocols: []

security:
  trust_boundaries:
    - model/context projection
    - memory/checkpoint store
    - user/tenant isolation boundary
    - retriever/external knowledge source
  least_privilege: application-required
  sandbox: unknown
  data_classification: memory contents may be sensitive and require application-specific classification
  receipts: []

reproducibility:
  model_receipt: implementation-dependent
  dependency_receipt:
    S-001: 4c95ae14cc2462c442b5c064cccd74430d02bc46
    S-002: b7f7240eb4d4510f3b45300a89126858a474b31d
  external_api_receipt: implementation-dependent
  execution_evidence: taxonomy/implementation-source contrast; not one universal executable memory fixture

unknowns:
  - quality metrics for each memory technique
  - poisoning/write validation
  - tenant/user isolation guarantees of concrete stores
  - retention/deletion enforcement
  - conflict semantics for concurrent memory writers
  - provenance integrity of recalled memory
  - when automatic extraction/consolidation should be trusted
```

## Why this record matters

It rejects several misleading equivalences:

```text
MemorySaver object     != semantic memory
checkpoint persistence != long-term memory
vector retrieval       != user memory
stored text             != trustworthy memory
memory recall           != correct/current fact
```

## Memory lifecycle contract

A meaningful memory claim should answer at least:

```text
WHAT is retained?
WHY is it memory rather than transient state/knowledge?
FOR WHOM is it scoped?
HOW is it written?
HOW is it retrieved?
WHERE is it persisted?
HOW is it isolated?
HOW LONG is it retained?
HOW can it be updated/forgotten?
WHAT provenance does it carry?
HOW is quality evaluated?
```

Without these, `memory=true` is not useful architecture evidence.

## Production-certification boundary

This contrast fixture does not certify any memory framework/store as private, isolated, accurate, poison-resistant or production-ready.

Those properties require concrete implementation/deployment evidence.

## Schema pressure result

```yaml
fits_current_schema: qualified
new_dimension_required: candidate_only_at_freeze_audit
normalization_issue: current schema correctly separates state/checkpoint/persistence from memory lifecycle, but final freeze audit should compare its memory fields against the richer specialized-source lifecycle dimensions such as update-conflict/forgetting/evaluation before freezing v1
```

No immediate schema mutation is justified from this fixture alone because richer fields may belong to MK2 operational memory contracts rather than MK1 classification.

## Evidence

- [`../../../quarries/genai-agents-p0-p1-callpaths.md`](../../../quarries/genai-agents-p0-p1-callpaths.md)
- [`../../../quarries/cross-source-memory-production-mcp.md`](../../../quarries/cross-source-memory-production-mcp.md)
- [`../../../mining-site/SOURCES.md`](../../../mining-site/SOURCES.md)
