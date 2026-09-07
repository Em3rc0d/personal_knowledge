# MK2 — Proposed Operational Schemas

Status: **DESIGN SEED / NOT YET CANON**

These shapes are intentionally provisional. MK1 must freeze the classification vocabulary before MK2 can version them as operational contracts.

## Tool contract seed

```yaml
tool:
  id:
  version:
  purpose:
  input_schema:
  output_schema:
  capabilities: []
  authorization:
    policy:
    principal_scope:
  side_effect:
    class: S0 | S1 | S2 | S3 | S4
    reversible:
    preview_supported:
  idempotency:
    mode: none | key | dedupe | verification | compensation
    key_source:
  errors:
    classes: []
    retryable: []
  budgets:
    timeout_ms:
    max_attempts:
  provenance:
  receipt:
    required:
    external_id_field:
```

## Side-effect policy seed

```yaml
side_effect_policy:
  action:
  effect_class:
  risk_reason:
  allowed_mode: preview | live | both
  approval:
    required:
    timing: before_effect
    editable:
    revalidate_after_edit:
    dispatcher_enforced:
  retry:
    idempotent:
    unknown_outcome_strategy:
  verification:
    expected_external_evidence:
  audit:
    receipt_required:
```

## Human approval seed

```yaml
approval:
  request_id:
  execution_id:
  proposed_tool:
  proposed_args_hash:
  reviewer:
  decision: approve | reject | edit
  edited_args:
  validation_version:
  authorization_version:
  expires_at:
  execution_binding:
  audit_receipt:
```

## Retry policy seed

```yaml
retry_policy:
  owner: model | tool | runtime | provider_sdk
  error_class:
  retryable:
  max_attempts:
  backoff:
  jitter:
  deadline_ms:
  idempotency_strategy:
  timeout_outcome: known_failure | unknown
  verify_before_retry:
  terminal_action:
```

## Termination policy seed

```yaml
termination:
  success_predicate:
  terminal_failures: []
  max_model_turns:
  max_tool_calls:
  retry_budgets:
  wall_clock_ms:
  token_budget:
  cost_budget:
  oscillation_detection:
  cancellation:
  incomplete_receipt:
```

## Memory policy seed

```yaml
memory_policy:
  semantic_role:
  scope:
  isolation_key:
  persistence:
  write_policy:
  validation:
  provenance_required:
  retrieval_policy:
  retention:
  deletion:
  correction:
  poisoning_controls:
  evaluation:
```

## Protocol receipt seed

```yaml
protocol_receipt:
  name:
  revision:
  role:
  transport:
  capabilities: []
  auth_model:
  extensions: []
  timeout_semantics:
  cancellation_semantics:
  compatibility_evidence:
```

## Evidence receipt seed

```yaml
evidence_receipt:
  claim:
  source_sha:
  execution_id:
  evidence_type: static | test | trace | outcome | external_receipt
  inputs_hash:
  validated_args_hash:
  observed_result:
  external_result_id:
  evaluator_version:
  timestamp:
  limitations: []
```

## Schema versioning rule

When MK2 becomes active, every machine-readable schema must have:

- a semantic version or explicit revision id;
- migration rules for breaking changes;
- examples/fixtures;
- validation tests;
- a documented relationship to the MK1 schema revision that produced it.
