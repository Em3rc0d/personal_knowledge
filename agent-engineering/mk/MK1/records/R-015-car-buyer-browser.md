# R-015 — Car Buyer Browser Agent

Status: **CLASSIFIED WITH AUTHORITY QUALIFICATION**  
Source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/car_buyer_agent_langgraph.ipynb`

## Normalized record

```yaml
identity:
  name: Car Buyer Browser Agent
  evidence_state: QUALIFIED

control:
  primary_authority: mixed
  control_class: C4
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads: [WEB_PAGES, VEHICLE_LISTINGS]
  writes: []
  generated_code_execution: false
  shell: false
  browser: read_only
  database: none
  communication: none
  publication: none
  file_egress: false
  delegation: false
  capability_compositions:
    - browser_navigation + dynamic_page_render + scraping + model_analysis

side_effects:
  observed_class: S0
  reachable_class: S1
  reversible: yes
  external_mutation: false
  data_egress: metadata
  verification: scraped page content; origin/action restrictions not formally proven

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: graph/process state
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: session
  persistence: process
  retrieval_policy: scraped content becomes analysis context
  write_policy: n/a
  isolation_key: n/a
  retention_policy: unknown
  provenance: web-page/listing provenance depends on scrape capture

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  approval_binding: none

errors_and_retries:
  error_model: mixed
  retry_owner: mixed
  retry_budget: unknown
  idempotency: n/a for observed read path
  unknown_outcome_handling: n/a for observed read path

termination:
  success_predicate: listing/research workflow completes
  terminal_failure_predicate: browser/scrape/workflow failure
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
  outcome: [retrieved listing information]
  repeated_trials: false
  regression_gate: false
  production_observability: false

security:
  trust_boundaries: [model_to_browser_workflow, browser_to_web_origin, scraped_content_to_model]
  least_privilege: partial
  sandbox: browser process
  data_classification: public web data in observed path
  authorization_boundary: browser action surface / origin policy not formalized
  receipts: scraped content only

unknowns:
  - authenticated browser session support
  - form submission/transaction reachability
  - download/file access
  - origin/domain allowlist
  - prompt injection handling in scraped content
```

## Evidence basis

Observed use of a Playwright-compatible browser runtime (`patchright.async_api.async_playwright`) for dynamic web scraping/retrieval.

No inspected evidence established authenticated mutations, purchases, form submissions or other transactional browser actions.

Primary quarry paths: `quarries/genai-agents-p0-p1-callpaths.md` P0-09 and `quarries/genai-agents-risk-scan.md` RS-08.

## Classification result

This record prevents another common error:

```text
browser library present ≠ browser is transaction-capable in the inspected system
```

Observed authority is retrieval-oriented. The substrate is capable of much more, but MK1 does not promote hypothetical capabilities to facts. If future code exposes authentication/forms/downloads, the same record must be reclassified.

## MK2 handoff seed

Operational browser contract should declare allowed origins, auth context, action classes, downloads, data egress, untrusted-page/prompt-injection handling and session cleanup.
