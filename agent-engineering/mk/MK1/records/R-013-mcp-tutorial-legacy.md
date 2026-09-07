# R-013 — MCP Tutorial (Legacy Protocol Shape)

Status: **LEGACY PROTOCOL CLASSIFICATION**  
Primary source: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
Artifact: `all_agents_tutorials/mcp-tutorial.ipynb`  
Current contrast contract used by domain: MCP `2026-07-28`

## Normalized record

```yaml
identity:
  name: Model Context Protocol Tutorial
  evidence_state: CONTRADICTED

control:
  primary_authority: deterministic
  control_class: C0
  horizon: bounded_multistep
  topology: single_model
  model_count: integration-dependent

capabilities:
  reads: [MCP_TOOL_METADATA, MCP_TOOL_RESULTS]
  writes: [MCP_TOOL_INVOCATIONS]
  generated_code_execution: false
  shell: unknown
  browser: unknown
  database: unknown
  communication: unknown
  publication: unknown
  file_egress: unknown
  delegation: false
  capability_compositions:
    - protocol_discovery + tool_selection_or_call + remote_or_local_tool_authority

side_effects:
  observed_class: unknown
  reachable_class: unknown
  reversible: unknown
  external_mutation: unknown
  data_egress: unknown
  verification: protocol/tool response only; actual tool semantics determine effect

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: protocol/session dependent
  replay_semantics: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: n/a
  write_policy: n/a
  isolation_key: n/a
  retention_policy: n/a
  provenance: protocol responses are integration data, not semantic memory by default

human_control:
  level: unknown
  mode: unknown
  dispatcher_enforcement: unknown
  approval_binding: protocol does not itself imply approval

errors_and_retries:
  error_model: protocol_structured + implementation-dependent
  retry_owner: mixed
  retry_budget: unknown
  idempotency: tool-specific
  unknown_outcome_handling: tool/transport-specific

termination:
  success_predicate: integration/tool request completes
  terminal_failure_predicate: protocol/tool failure
  turn_budget: integration-dependent
  tool_budget: integration-dependent
  time_budget: integration-dependent
  cost_or_token_budget: integration-dependent
  oscillation_detection: integration-dependent
  cancellation: protocol/runtime revision dependent

evaluation:
  static_contracts: [protocol/message compatibility]
  unit_integration: [tutorial demonstration only]
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols:
  - name: MCP
    revision: legacy tutorial predating 2026-07-28 core
    role: client/server tutorial
    transport: stdio/session-oriented example
    capabilities: tool discovery + invocation
    auth_model: implementation-dependent
    extensions: unknown

security:
  trust_boundaries: [host_to_mcp_client, client_to_server, server_to_tool]
  least_privilege: unknown
  sandbox: unknown
  data_classification: tool-dependent
  authorization_boundary: NOT PROVIDED BY PROTOCOL DISCOVERY ALONE
  receipts: protocol request/response; tool-specific outcome receipt required separately

unknowns:
  - exact current migration path for each MCP SDK/language
  - authorization model of individual exposed tools
  - side-effect class of discovered tools
  - timeout/idempotency semantics of individual tools
```

## Evidence basis

The tutorial uses a session-oriented MCP client shape with `ClientSession`, explicit `initialize()`, tool discovery via `list_tools()` and protocol-mediated tool execution.

The domain's current MCP contrast (`2026-07-28`) uses a stateless core and removes the mandatory `initialize/initialized` lifecycle and core `Mcp-Session-Id`; capability/version information is carried differently and discovery is optional/revision-aware.

Primary quarry paths:

- `quarries/genai-agents-p0-p1-callpaths.md` P1-06;
- `quarries/cross-source-memory-production-mcp.md`.

## Classification result

The tutorial retains conceptual value for **protocol-mediated discovery/invocation**, but its lifecycle mechanics are a legacy integration example.

More importantly, this record proves that `MCP` is not an agent class and not an authorization guarantee. The actual tool capability/side effect can remain completely UNKNOWN until the exposed server/tool contract is inspected.

## MK2 handoff seed

Operational MCP contract must pin protocol revision, role, transport, capability set, extension set, auth/identity boundary, per-tool authorization, timeout/cancellation and side-effect/idempotency semantics.
