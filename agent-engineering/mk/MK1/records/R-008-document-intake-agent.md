# R-008 — Document Intake Agent

Status: **CLASSIFIED WITH MATERIAL UNKNOWNS**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `document_intake_agent_langgraph.ipynb`

## Normalized record

```yaml
identity:
  name: Document Intake Agent
  evidence_state: OBSERVED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [LOCAL_FILE, CONVERSION_RESULT]
  writes: [REMOTE_CONVERSION_JOB]
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: true
  delegation: false
  capability_compositions:
    - local_file_read + remote_job_create + presigned_upload + polling + remote_download

side_effects:
  observed_class: S3
  reachable_class: S3
  reversible: partial
  external_mutation: true
  data_egress: file_bytes
  verification: remote job status + downloaded converted bytes

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: graph/runtime state
  replay_semantics: partial

memory:
  semantic_role: [grounded_document_context]
  scope: session
  persistence: process
  retrieval_policy: converted markdown supplied to downstream QA
  write_policy: none beyond runtime state
  isolation_key: unknown
  retention_policy: remote/local retention unknown
  provenance: conversion output originates from uploaded local file

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: mixed
  retry_owner: tool
  retry_budget: polling/retry behavior exists; complete global budget unknown
  idempotency: optional idempotency key supported
  unknown_outcome_handling: partial

termination:
  success_predicate: conversion job completes and converted bytes are retrieved
  terminal_failure_predicate: remote conversion error / transfer failure
  turn_budget: downstream agent dependent
  tool_budget: unknown
  time_budget: HTTP operation timeouts observed; global deadline unknown
  cost_or_token_budget: unknown
  oscillation_detection: n/a for conversion polling
  cancellation: unknown

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: [job-create/upload/poll/download]
  outcome: [converted bytes/markdown available]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [local_file_to_external_converter, presigned_storage, conversion_output_to_model_context]
  least_privilege: partial
  sandbox: none
  data_classification: unknown
  authorization_boundary: external service credentials/presigned URL
  receipts: remote job/status and returned bytes

unknowns:
  - whether file classification permits egress
  - remote retention/deletion guarantees
  - global deadline/cancellation
  - malware/content validation
  - tenant/isolation properties of remote conversion
```

## Evidence basis

Observed call path:

`local path → convert_file → create remote job → PUT original bytes to presigned URL → poll status → GET converted bytes → downstream grounded QA`.

Optional idempotency-key support and explicit transfer timeouts are present.

Primary quarry paths: `quarries/genai-agents-p0-p1-callpaths.md` P0-07 and `quarries/genai-agents-risk-scan.md` RS-07/RS-11.

## Classification result

This record is the clearest counterexample to **“read/transform = harmless.”** The logical task is document conversion, but the actual authority includes file-byte egress across a trust boundary.

## MK2 handoff seed

Require data classification, destination allowlist, retention contract, file/type/size validation, idempotency, overall deadline/cancellation and returned-byte provenance.
