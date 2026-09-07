# R-014 — ShopGenie Outbound Email

Status: **CLASSIFIED WITH MATERIAL UNKNOWNS**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/ShopGenie.ipynb`

## Normalized record

```yaml
identity:
  name: ShopGenie Outbound Email
  evidence_state: OBSERVED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [PRODUCT_RESEARCH_RESULTS]
  writes: [EMAIL_CONTENT, EXTERNAL_EMAIL]
  generated_code_execution: false
  shell: false
  browser: unknown
  database: none
  communication: external_send
  publication: none
  file_egress: false
  delegation: false
  capability_compositions:
    - recommendation_generation + email_template + SMTP_SEND

side_effects:
  observed_class: S3
  reachable_class: S3
  reversible: no
  external_mutation: true
  data_egress: content
  verification: SMTP send call; end-recipient delivery receipt not established

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: process
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: n/a
  write_policy: n/a
  isolation_key: n/a
  retention_policy: n/a
  provenance: generated recommendation becomes email body

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: no approval contract established

errors_and_retries:
  error_model: mixed
  retry_owner: unknown
  retry_budget: unknown
  idempotency: unknown
  unknown_outcome_handling: unknown

termination:
  success_predicate: send_email returns without failure
  terminal_failure_predicate: SMTP/runtime error
  turn_budget: unknown
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: n/a
  cancellation: unknown

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: [SMTP send invocation]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_content_to_email_template, SMTP_credentials_to_server, server_to_recipient]
  least_privilege: partial
  sandbox: none
  data_classification: recipient/product data; policy unknown
  authorization_boundary: SMTP credential + direct send function
  receipts: transport invocation only

unknowns:
  - recipient approval/authorization
  - idempotency/deduplication
  - delivery reconciliation after timeout
  - recipient data/privacy policy
```

## Evidence basis

Observed final path generates email subject/body, formats HTML and directly calls `send_email(...)`, which uses SMTP with STARTTLS and sends externally.

Primary quarry paths: `quarries/genai-agents-p0-p1-callpaths.md` P0-06 and `quarries/genai-agents-risk-scan.md` RS-06.

## Classification result

Transport encryption is not action authorization. `generate email` and `send email` are separate capabilities and should be classified/gated independently.

## MK2 handoff seed

Require explicit send privilege, recipient binding, preview/approval mode where appropriate, idempotency/reconciliation and delivery receipts.
