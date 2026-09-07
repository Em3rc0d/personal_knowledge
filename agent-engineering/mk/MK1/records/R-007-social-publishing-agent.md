# R-007 — Social Publishing Agent

Status: **CLASSIFIED WITH MATERIAL UNKNOWNS**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `social_media_publishing_agent_publora_langgraph.ipynb`

## Normalized record

```yaml
identity:
  name: Social Publishing Agent
  evidence_state: OBSERVED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [CONTENT_REQUEST, PLATFORM_RULES]
  writes: [DRAFT_OR_SCHEDULED_POST]
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: live
  file_egress: false
  delegation: false
  capability_compositions:
    - generation + review/revision + deterministic_publish_stage + external_API

side_effects:
  observed_class: S2
  reachable_class: S3
  reversible: partial
  external_mutation: true
  data_egress: content
  verification: API response per platform; full external-state reconciliation unknown

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: graph/runtime state
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none
  write_policy: none
  isolation_key: none
  retention_policy: none
  provenance: generated content and reviewer feedback retained in workflow state

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: no human approval established in inspected path

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: bounded content revision via MAX_ITERS; per-platform publish retry contract unknown
  idempotency: optional Idempotency-Key supported
  unknown_outcome_handling: partial / external reconciliation unknown

termination:
  success_predicate: platform publish/draft results collected
  terminal_failure_predicate: per-platform failure recorded or workflow completion
  turn_budget: bounded revision loop
  tool_budget: unknown
  time_budget: unknown
  cost_or_token_budget: unknown
  oscillation_detection: bounded by MAX_ITERS
  cancellation: unknown

evaluation:
  static_contracts: [deterministic length checks]
  unit_integration: []
  trajectory: [review/revise/publish stages]
  outcome: [API publish/draft result]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_content, runtime_mode_to_publish_capability, publisher_to_external_platform]
  least_privilege: partial
  sandbox: none
  data_classification: public-content workflow; account/credential handling unknown
  authorization_boundary: trusted DRY_RUN configuration materially changes executable capability
  receipts: per-platform API results

unknowns:
  - human approval semantics before live publication
  - credential/account scope
  - external-state verification after ambiguous timeout
  - idempotency behavior across every supported platform
```

## Evidence basis

Observed:

- `DRY_RUN = True` by default;
- dry-run path creates drafts/avoids scheduled live publication;
- bounded self-revision count;
- optional idempotency key support;
- per-platform failures isolated.

Primary quarry paths: `quarries/genai-agents-p0-p1-callpaths.md` P0-05 and `quarries/genai-agents-risk-scan.md` RS-04/RS-11.

## Classification result

This is a useful positive case for **deterministic capability mode**. Dry-run is stronger than a prompt instruction because trusted configuration changes what the publish stage is allowed to do.

Observed demo behavior may be S2 while live mode makes S3 reachable.

## MK2 handoff seed

Operational contract should bind live-mode configuration outside model control, require idempotency/reconciliation, account-scope receipts, optional approval policy and publish-result verification.
