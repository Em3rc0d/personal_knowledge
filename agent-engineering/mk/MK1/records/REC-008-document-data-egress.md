# REC-008 — Document Intake / Data-Egress Agent

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-008
name: GenAI_Agents document intake agent
schema_revision: mk1-draft-2026-09-16.1
classification_scope: local-document conversion through external service followed by grounded processing
source_receipts:
  - S-001
primary_quarries:
  - quarries/genai-agents-risk-scan.md
  - quarries/genai-agents-p0-p1-callpaths.md
evidence_state: SUPPORTED / QUALIFIED
production_certification: false
```

Pinned upstream snapshot: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`.

## Classification

```yaml
identity:
  name: document-intake agent
  source: NirDiamant/GenAI_Agents/all_agents_tutorials/document_intake_agent_langgraph.ipynb
  snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
  evidence_state: SUPPORTED

control:
  primary_authority: mixed
  horizon: bounded_multistep
  topology: single_model
  model_count: application/workflow-dependent

capabilities:
  reads:
    - local document bytes
    - remote conversion status
    - converted document bytes
  writes:
    - conversion job metadata to external service
    - original file bytes to presigned remote object-storage URL
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: true
  capability_compositions:
    - local private-file read + external upload + remote processing + returned artifact

side_effects:
  class: S2
  reversible: partial | unknown
  external_mutation: true
  data_egress: file_bytes
  verification: converted bytes are retrieved; retention/deletion and remote processing guarantees are not established

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: workflow/framework-dependent; not established as material durable storage in this record
  replay_semantics: partial | unknown
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: remote job/idempotency semantics are only partially established
  locking: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none | unknown
  retrieval_policy: converted document becomes grounded-answer input; this is document context/knowledge, not automatically long-term memory
  write_policy: none established
  isolation_key: none established
  retention_policy: remote conversion/storage retention UNKNOWN
  provenance: local source document → remote conversion result; returned-byte provenance depends on service receipt

human_control:
  level: H0 | unknown
  mode: none | unknown
  dispatcher_enforcement: unknown
  enforcement_owner: runtime/application
  enforcement_boundary: upload/conversion function executes deterministically when workflow reaches the conversion step; no human approval gate established by current evidence
  approval_binding: not established

errors_and_retries:
  error_model: mixed
  retry_owner: runtime/application/external service
  retry_budget: polling behavior exists; complete retry budget not established
  idempotency: optional idempotency-key support is observed
  unknown_outcome_handling: incomplete for timeout/disconnect after remote job/upload begins

termination:
  success_predicate: conversion reaches terminal success and converted bytes are retrieved; downstream grounded-answer success is separate
  terminal_failure_predicate: conversion/transfer/runtime error or service terminal failure
  turn_budget: not central to conversion path / unknown
  turn_budget_enforcement: unknown
  tool_budget: not established
  tool_budget_enforcement: unknown
  time_budget: explicit HTTP operation timeouts observed
  time_budget_enforcement: per-operation; complete end-to-end deadline not established
  cost_or_token_budget: not established
  cost_or_token_budget_enforcement: unknown
  overshoot_semantics: polling/global workflow deadline not established
  oscillation_detection: not established
  cancellation: not established as a complete remote-job contract
  cancellation_effective_boundary: remote conversion/upload may already have begun; rollback/deletion not proven

evaluation:
  static_contracts:
    - deterministic conversion helper/path
  unit_integration: []
  trajectory:
    - upload → poll → download call path is statically verified
  outcome:
    - converted bytes returned on successful service path
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols: []

security:
  trust_boundaries:
    - local filesystem/document
    - application runtime
    - external conversion API
    - presigned object-storage destination
    - returned converted artifact
  least_privilege: partial | unknown
  sandbox: none | unknown
  data_classification: required but not established by tutorial evidence
  receipts:
    - original file bytes cross the local trust boundary
    - optional idempotency key is supported
    - explicit HTTP transfer timeouts are present

reproducibility:
  model_receipt: not material to the conversion boundary
  dependency_receipt: repository snapshot pinned; per-slice runtime not independently executed here
  external_api_receipt: conversion-service implementation/retention policy requires deployment-specific receipt
  execution_evidence: static call-path verification; no independent live service execution claimed

unknowns:
  - document classification / allowed-data policy before upload
  - external service retention/deletion policy
  - malware/content scanning boundary where relevant
  - full-file size/type enforcement
  - complete end-to-end deadline and cancellation semantics
  - remote job state after client timeout/disconnect
  - provenance/integrity receipt for returned bytes beyond normal service response
  - replay/duplicate behavior when workflow resumes around upload/job creation
```

## Verified call path

```text
local document path
  ↓
convert_document(state)
  ↓
convert_file(path, to="md")
  ↓
POST conversion-job metadata
  ↓
PUT original file bytes to presigned upload URL
  ↓
poll remote conversion status
  ↓
GET converted bytes
  ↓
markdown becomes downstream grounded-answer input
```

## Why this is a side effect even though the task says “convert/read”

The important architectural fact is:

```text
local private bytes
      ↓
leave the trust boundary
      ↓
remote service stores/processes them
```

That is **data egress**, independent of whether the final business intent sounds read-only.

The current schema represents this with:

```yaml
side_effects:
  class: S2
  external_mutation: true
  data_egress: file_bytes
```

This is useful pressure: confidentiality exposure does not collapse cleanly into integrity-oriented mutation severity.

## Reliability qualification

Positive evidence:

- optional idempotency-key support;
- explicit HTTP operation timeouts;
- deterministic conversion step before downstream grounded QA.

Still missing:

```text
global deadline
remote cancellation contract
unknown-outcome recovery
retention/deletion guarantee
```

Therefore `timeout configured` must not be promoted to `safe retry/cancellation`.

## Production-certification boundary

This record does **not** certify that uploaded documents are allowed to leave the organization, that the conversion provider has acceptable retention/security, that retries are duplicate-safe in every failure window, or that the overall workflow is production-ready.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: candidate_only_at_freeze_audit
normalization_issue: current `data_egress` field successfully preserves confidentiality movement separately from side-effect class; final freeze audit should decide whether egress severity/data-classification needs stronger normalized structure
```

No schema change is proposed from this record alone.

## Evidence

- [`../../../quarries/genai-agents-risk-scan.md`](../../../quarries/genai-agents-risk-scan.md)
- [`../../../quarries/genai-agents-p0-p1-callpaths.md`](../../../quarries/genai-agents-p0-p1-callpaths.md)
- [`../../../mining-site/SOURCES.md`](../../../mining-site/SOURCES.md)
