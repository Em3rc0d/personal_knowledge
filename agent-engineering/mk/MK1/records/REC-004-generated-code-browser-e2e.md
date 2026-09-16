# REC-004 — Generated-Code Browser E2E Agent

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-004
name: GenAI_Agents E2E testing agent
schema_revision: mk1-draft-2026-09-16.1
classification_scope: model-derived Playwright Python promoted into in-process execution
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
  name: E2E testing agent
  source: NirDiamant/GenAI_Agents/all_agents_tutorials/e2e_testing_agent.ipynb
  snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
  evidence_state: SUPPORTED

control:
  primary_authority: mixed
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads:
    - natural-language test request
    - browser DOM/environment observations
  writes:
    - generated Playwright/Python script in graph state
  generated_code_execution: true
  browser: general
  database: none
  communication: none
  publication: none
  file_egress: unknown
  capability_compositions:
    - model-derived executable Python + in-process exec + browser/network authority + host-process inherited permissions

side_effects:
  class: unknown
  reversible: unknown
  external_mutation: unknown
  data_egress: unknown
  verification: workflow observes browser/test behavior; no general containment or external side-effect verifier established

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: graph-state persistence not materialized as durable evidence in this record
  replay_semantics: unknown
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: unknown
  locking: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none | unknown
  retrieval_policy: none established
  write_policy: none established
  isolation_key: none established
  retention_policy: none established
  provenance: runtime/browser observations only

human_control:
  level: H0 | unknown
  mode: none | unknown
  dispatcher_enforcement: no | unknown
  enforcement_owner: unknown
  enforcement_boundary: no deterministic approval boundary before generated Python execution established by current evidence
  approval_binding: not established

errors_and_retries:
  error_model: mixed
  retry_owner: runtime/model workflow
  retry_budget: not established from inspected call path
  idempotency: not established
  unknown_outcome_handling: browser/external action dependent

termination:
  success_predicate: test workflow/path completion; external application state verification is test-specific
  terminal_failure_predicate: execution/test/runtime failure
  turn_budget: not established
  turn_budget_enforcement: unknown
  tool_budget: not established
  tool_budget_enforcement: unknown
  time_budget: not established as a complete agent contract
  time_budget_enforcement: unknown
  cost_or_token_budget: not established
  cost_or_token_budget_enforcement: unknown
  overshoot_semantics: unknown
  oscillation_detection: not established
  cancellation: not established
  cancellation_effective_boundary: unknown

evaluation:
  static_contracts: []
  unit_integration:
    - target application/browser test behavior is part of the tutorial workflow
  trajectory:
    - structured actions converted into accumulated executable script
  outcome:
    - browser/E2E assertions or observations are test-specific
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols: []

security:
  trust_boundaries:
    - user test request
    - model-generated actions/code
    - Python execution boundary
    - host process
    - browser session
    - target web application/network
  least_privilege: unknown
  sandbox: unknown
  data_classification: not established
  receipts:
    - generated `state["script"]` is directly executed with Python `exec(...)`
    - Playwright controls the browser

reproducibility:
  model_receipt: upstream artifact-specific
  dependency_receipt: repository snapshot pinned; per-slice executable environment not globally certified
  external_api_receipt: demonstration target is a local Flask app in the inspected tutorial
  execution_evidence: call-path/source verification; not independent E2E execution by this knowledge base

unknowns:
  - concrete sandbox/isolation boundary around generated Python
  - filesystem/environment/process/network reachability inherited by exec
  - credential/session scope for browser in non-demo deployments
  - allowed browser origins/actions/downloads
  - mutating browser side effects in authenticated targets
  - cancellation/time budgets
  - safe promotion policy for generated test code
```

## Verified call path

```text
natural-language test request
  ↓
LLM converts request into structured actions
  ↓
workflow builds/extends Playwright Python script
  ↓
script stored in graph state
  ↓
Python exec(state["script"], ...)
  ↓
Playwright controls browser / observes DOM
  ↓
workflow continues until test path completes
```

The critical boundary is **not merely the browser**. Model-derived text is promoted to general Python inside the notebook process.

## Capability composition

```text
MODEL-DERIVED CODE
      +
IN-PROCESS PYTHON EXECUTION
      +
BROWSER / NETWORK SESSION
      +
HOST PROCESS PERMISSIONS
      =
R4-LIKE HIGH BLAST RADIUS
```

The MK1 side-effect class remains `unknown` because the exact reachable mutation/credential/network environment is not established by the pinned static evidence.

This is intentional: capability risk and observed external mutation are related but not interchangeable fields.

## Engineering conclusion

Supported rule:

> Generation and execution are separate authority domains.

Safe reusable shape:

```text
generate
→ isolate
→ execute/test under bounded capabilities
→ collect evidence
→ promote result intentionally
```

Not:

```text
generate
→ exec inside trusted runtime
→ assume safe because task is “testing”
```

## Production-certification boundary

This record does **not** certify the tutorial as sandboxed, least-privilege, production-ready, credential-safe or confined to the nominal browser target.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: false
normalization_issue: capability composition is essential; generated-code execution and browser authority must remain distinct fields while security containment stays independently classified
```

## Evidence

- [`../../../quarries/genai-agents-risk-scan.md`](../../../quarries/genai-agents-risk-scan.md)
- [`../../../quarries/genai-agents-p0-p1-callpaths.md`](../../../quarries/genai-agents-p0-p1-callpaths.md)
- [`../../../mining-site/SOURCES.md`](../../../mining-site/SOURCES.md)
