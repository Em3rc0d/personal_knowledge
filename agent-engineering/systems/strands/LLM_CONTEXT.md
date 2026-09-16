# Strands Agents — LLM Context Contract

Status: **MACHINE-ORIENTED CURRENT CONTEXT**  
Use: retrieval/routing guide for LLMs and agents reading `personal_knowledge`  
Observed baseline: `2026-09-16`

This file tells a machine reader **what is current, where evidence lives, and what must not be inferred**.

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
a2a_version_receipt: quarries/strands-a2a-version-drift.md
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
4. systems/strands/PROTOCOLS.md when protocol-related
5. systems/strands/EVIDENCE.md when provenance is required
6. quarries/mining-site only for audit/detail
```

For current domain/MK state:

```text
STATUS.md → ROADMAP.md → mk/MK1/GATES.md
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
  python_dependency: ">=0.3.0,<0.4.0"
  typescript_dependency: "^0.3.10"
  pinned_protocol_family: "0.3"
  current_official_protocol_family: "1.0"
  client_server_discovery_shape: SUPPORTED
  invoke_stream_task_fixture_source: PRESENT
  graph_remote_agent_fixture_source: PRESENT
  integration_workflow_scope: PRESENT
  specific_successful_ci_receipt: NOT_VERIFIED
  independent_rerun: NOT_RUN
  mk1_classification_shape: PASS_QUALIFIED
  a2a_1_0_compatibility: NOT_ESTABLISHED
```

## Preferred compact interpretation

> Strands is an in-process agent SDK whose core Agent loop is model-directed but runtime-bounded, while the same SDK also provides deterministic and mixed orchestration forms. Its tools inherit effective authority from the application/host boundary, its state/session/memory concepts are distinct, and intervention/budget/cancellation guarantees depend on enforcement boundaries. Strands is therefore an implementation and taxonomy pressure test, not a taxonomy, security boundary or production certificate by itself.

## Protocol anti-overclaim rules

For MCP:

```text
MCP modern-path support
!= every MCP server/revision compatible
!= deployment authorization correct
!= cancellation rolls back remote effects
```

For A2A:

```text
Strands A2A support
!= A2A 1.0 compatibility

A2A 0.3 fixture source exists
!= specific CI run passed
!= independent reproduction passed
```

Current safe A2A claim:

> The pinned Strands snapshot has A2A 0.3.x implementation/integration-fixture evidence. Current A2A is 1.0.x, and compatibility with that line is not established by this evidence set.

## Prohibited inferences

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
  - "A2A support means A2A 1.0 compatibility"
  - "A2A integration fixture in CI scope means a specific run passed"
  - "context_id is an authentication boundary"
  - "Graph, Swarm or multi-agent improves performance without a baseline"
  - "Python and TypeScript have permanent feature parity"
```

## Historical-state warning

Older documents intentionally preserve earlier gate state.

Examples:

- the first Strands pass held concurrency/budget/intervention fields as candidates;
- independent runtime evidence later promoted them into `mk1-draft-2026-09-16.1`;
- the original quarry carried MCP execution compatibility as open debt before the modern MCP receipt;
- earlier system docs described A2A as unknown before the `0.3 → 1.0` version-drift receipt.

When state differs across time, report the transition rather than rewriting history.

## Query routing table

| Question | Read first |
|---|---|
| What is Strands? | `systems/strands/README.md` |
| How is Strands classified? | `systems/strands/CLASSIFICATION.md` |
| What reusable lessons did it expose? | `systems/strands/ENGINEERING_RULES.md` |
| What is the MCP state? | `systems/strands/PROTOCOLS.md` → MCP receipt |
| What is the A2A state? | `systems/strands/PROTOCOLS.md` → `quarries/strands-a2a-version-drift.md` |
| Why were concurrency/budget/enforcement fields added? | `quarries/runtime-semantics-strands-langgraph-openai.md` |
| Where did a claim come from? | `systems/strands/EVIDENCE.md` |
| What was originally observed? | `quarries/strands-agents.md` |
| Which upstream snapshot? | `mining-site/S-109-strands-agents.md` |
| What remains unknown? | `systems/strands/README.md` + `mk/MK1/UNKNOWNS.md` |
| Can MK1 close now? | `STATUS.md` + `mk/MK1/GATES.md` |

## Evidence discipline

When answering from this package:

1. preserve pinned snapshot/date for version-sensitive claims;
2. distinguish framework capability from deployed-application behavior;
3. distinguish source inspection, CI scope, specific successful run and independent reproduction;
4. keep `UNKNOWN` when deployment/application evidence is absent;
5. never use marketing labels as evidence;
6. prefer normalized engineering semantics over framework vocabulary;
7. trace contested/version-sensitive claims into evidence;
8. treat `systems/strands/` as current synthesis, not as replacement for provenance.

## Freshness triggers

Re-open this package when any of these materially change:

```yaml
triggers:
  - Strands runtime architecture
  - session/concurrency semantics
  - budget/cancellation semantics
  - intervention/steering enforcement semantics
  - MCP dependency range/protocol support
  - A2A dependency/revision support, especially migration to 1.0+
  - Python/TypeScript feature parity
  - independent multi-agent benchmark evidence
```

Preserve previous receipts and explicitly record state transitions rather than silently rewriting history.
