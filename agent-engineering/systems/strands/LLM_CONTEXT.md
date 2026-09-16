# Strands Agents — LLM Context Contract

Status: **MACHINE-ORIENTED CURRENT CONTEXT**  
Use: retrieval/routing guide for LLMs and agents reading `personal_knowledge`  
Observed baseline: `2026-09-16`

This file is intentionally explicit and redundant at the decision boundaries. It tells an LLM **what to read, what is current, what is historical, and what must not be inferred**.

## Canonical routing

```yaml
system: Strands Agents
canonical_entrypoint: systems/strands/README.md
current_classification: systems/strands/CLASSIFICATION.md
reusable_rules: systems/strands/ENGINEERING_RULES.md
protocol_state: systems/strands/PROTOCOLS.md
evidence_map: systems/strands/EVIDENCE.md
source_receipt: mining-site/S-109-strands-agents.md
raw_processed_evidence: quarries/strands-agents.md
runtime_crosscheck: quarries/runtime-semantics-strands-langgraph-openai.md
mcp_execution_receipt: quarries/strands-mcp-2026-07-28-compatibility.md
historical_pressure_test: mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md
schema: mk/MK1/CLASSIFICATION_SCHEMA.md
domain_status: STATUS.md
```

## Read order

For a general Strands question:

```text
1. systems/strands/README.md
2. systems/strands/CLASSIFICATION.md
3. systems/strands/ENGINEERING_RULES.md
4. systems/strands/PROTOCOLS.md if protocol-related
5. systems/strands/EVIDENCE.md if evidence/provenance is required
6. descend into quarries/mining-site only for audit/detail
```

For current repository/MK state:

```text
STATUS.md
→ mk/MK1/GATES.md
→ mk/MK1/UNKNOWNS.md
```

## Current facts safe to carry forward

```yaml
identity:
  repository: strands-agents/harness-sdk
  snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
  observed_date: 2026-09-16
  python_release_observed: python/v1.56.0
  typescript_release_observed: typescript/v1.18.0
  type: in-process SDK / agent harness
  hosted_control_plane_required: false

core_model:
  core_agent_loop: model_directed
  runtime_envelope: true
  deterministic_workflow_surface: true
  graph_surface: true
  swarm_surface: true
  agents_as_tools_surface: true

state:
  conversation_history_distinct: true
  invocation_state_distinct: true
  agent_state_distinct: true
  session_persistence_distinct: true
  context_management_distinct: true
  long_term_memory_distinct: true
  documented_live_session_writer_assumption: single_writer
  distributed_locking_implied_by_framework: false

security:
  tool_schema_implies_safety: false
  core_sandbox_implied: false
  host_process_permissions_material: true
  application_least_privilege_required: true

runtime_semantics:
  budget_boundary_semantics_material: true
  in_flight_overshoot_possible: true
  cancellation_is_boundary_dependent: true
  cancellation_implies_rollback: false
  intervention_owner_semantics_material: true
  llm_steering_equals_hard_authorization: false

mk1_promotions:
  concurrency_semantics: promoted_under_state
  budget_enforcement_semantics: promoted_under_termination
  intervention_owner_boundary: promoted_under_human_control
  promotion_basis: Strands + LangGraph + OpenAI Agents SDK

mcp:
  pinned_revision: "2026-07-28"
  core_interoperability: SUPPORTED_UPSTREAM_EXECUTED_QUALIFIED
  modern_lifecycle_regression_fixture: true
  legacy_initialize_rejected_by_fixture: true
  streamable_http_fixture: true
  tools_list_call_tested: true
  multi_round_trip_input_tested: true
  prompts_resources_tested: true
  list_changed_subscription_tested: true
  trace_continuity_tested_upstream: true
  universal_oauth_authorization_certified: false
  remote_side_effect_rollback_certified: false
  independent_local_rerun: NOT_RUN_ENVIRONMENT_BLOCKED

a2a:
  framework_support_observed: true
  exact_revision_pinned: false
  auth_transport_execution_receipt_closed: false
```

## Current conceptual interpretation

Use this statement as the preferred compact model:

> Strands is an in-process agent SDK whose core Agent loop is model-directed but runtime-bounded, while the same SDK also provides deterministic and mixed orchestration forms. Its tools inherit effective authority from the application/host boundary, its state/session/memory concepts are distinct, and its intervention/budget/cancellation guarantees depend on where enforcement occurs. Strands is therefore a useful implementation and taxonomy pressure test, not a taxonomy, security boundary or production certificate by itself.

## Prohibited inferences

Do not infer any of the following:

```yaml
prohibited:
  - "Strands is the best agent framework"
  - "Strands framework identity determines architecture"
  - "using Strands makes an application production-ready"
  - "structured output proves semantic correctness"
  - "session persistence means safe multi-writer concurrency"
  - "MemoryManager means memory is trustworthy or correctly isolated"
  - "hooks/steering/HITL mean every side effect is approved"
  - "LLM steering is deterministic authorization"
  - "MCP support means every MCP server/revision is compatible"
  - "MCP cancellation rolls back remote side effects"
  - "MCP authentication adapter proves business authorization"
  - "A2A support has a closed revision/auth/transport receipt"
  - "Graph, Swarm or multi-agent improves performance without a baseline"
  - "Python and TypeScript have permanent feature parity"
```

## Historical-state warning

Some older documents intentionally preserve the state *before* later gates closed.

Examples:

- `quarries/strands-agents.md` originally labels concurrency, budget-boundary and intervention-owner semantics as candidate dimensions;
- `mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md` preserves the initial decision not to promote those fields from Strands alone;
- those candidates were later independently confirmed and promoted in `mk1-draft-2026-09-16.1`;
- the original Strands quarry also carried MCP `2026-07-28` execution compatibility as open debt;
- that debt was later qualified/closed at source-evidence level by `quarries/strands-mcp-2026-07-28-compatibility.md`.

When current state and historical state differ, **do not delete or ignore the historical reasoning**. Report the transition:

```text
candidate/open at T1
→ independent evidence at T2
→ promoted/closed/qualified at T3
```

## Query routing table

| User/agent question | Read first |
|---|---|
| “What is Strands?” | `systems/strands/README.md` |
| “How should I classify a Strands system?” | `systems/strands/CLASSIFICATION.md` |
| “What reusable lessons did Strands teach us?” | `systems/strands/ENGINEERING_RULES.md` |
| “Does Strands support modern MCP?” | `systems/strands/PROTOCOLS.md` |
| “What exactly was executed for MCP?” | `quarries/strands-mcp-2026-07-28-compatibility.md` |
| “Why were concurrency/budget/enforcement fields added?” | `quarries/runtime-semantics-strands-langgraph-openai.md` |
| “Where did this claim come from?” | `systems/strands/EVIDENCE.md` |
| “What did we originally observe from Strands?” | `quarries/strands-agents.md` |
| “Which exact upstream source/snapshot?” | `mining-site/S-109-strands-agents.md` |
| “What remains unknown?” | `systems/strands/README.md` + `mk/MK1/UNKNOWNS.md` |
| “Can MK1 close now?” | `STATUS.md` + `mk/MK1/GATES.md` |

## Evidence discipline

When answering from this package:

1. preserve the pinned snapshot/date when making version-sensitive claims;
2. distinguish framework capability from deployed-application behavior;
3. distinguish source-owned CI from independent reproduction;
4. keep `UNKNOWN` when the concrete application/deployment is not described;
5. never use marketing labels as evidence;
6. prefer normalized engineering semantics over framework vocabulary;
7. cite the evidence layer when a claim is contested, protocol-specific or version-sensitive;
8. treat `systems/strands/` as current synthesis, not as replacement for provenance.

## Freshness / update trigger

Re-open the package when any of these materially change:

```yaml
triggers:
  - Strands repository/runtime architecture changes
  - session/concurrency semantics change
  - budget/cancellation semantics change
  - intervention/steering enforcement semantics change
  - MCP dependency range or protocol support changes
  - A2A revision/auth/transport becomes executable and pinned
  - Python/TypeScript provider parity materially changes
  - independent benchmark evidence changes multi-agent conclusions
```

When updating, preserve previous receipts and explicitly record the state transition rather than rewriting history silently.
