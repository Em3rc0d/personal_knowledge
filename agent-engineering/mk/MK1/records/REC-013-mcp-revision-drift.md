# REC-013 — MCP Revision Drift / Integration Record

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-013
name: Legacy MCP tutorial vs current MCP 2026-07-28 contract
schema_revision: mk1-draft-2026-09-16.1
classification_scope: protocol revision/lifecycle pressure test
source_receipts:
  - S-001
  - S-108
primary_quarries:
  - quarries/cross-source-memory-production-mcp.md
evidence_state: SUPPORTED / QUALIFIED
production_certification: false
```

## Why this is one MK1 record

This record is intentionally a **revision-drift comparison**, not a claim that the old tutorial is “wrong”.

The legacy tutorial is evidence of a valid historical MCP integration shape. The current MCP specification is evidence that `MCP=true` cannot safely represent protocol architecture without revision/lifecycle semantics.

## Classification

```yaml
identity:
  name: MCP legacy/current lifecycle comparison
  source: S-001 tutorial + S-108 official MCP specification
  snapshot:
    tutorial: NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46
    current_protocol_revision: "2026-07-28"
  evidence_state: SUPPORTED

control:
  primary_authority: deterministic
  horizon: bounded_multistep
  topology: single_model | mixed
  model_count: application-dependent

capabilities:
  reads:
    - protocol-discovered tools/resources/prompts depending implementation
  writes:
    - protocol-exposed consequential actions may exist depending server
  generated_code_execution: false
  shell: false
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: unknown
  capability_compositions:
    - discoverable remote capability + model/runtime invocation authority + remote server permissions

side_effects:
  class: unknown
  reversible: unknown
  external_mutation: application/server-dependent
  data_egress: unknown
  verification: protocol response does not by itself prove external business outcome for consequential tools

state:
  runtime_state: structured
  checkpointing: unknown
  persistence_backend: protocol does not define application persistence
  replay_semantics: application-defined
  invocation_concurrency: protocol/application-defined
  writer_model: unknown
  concurrency_conflict_semantics: application/server-defined
  locking: unknown

memory:
  semantic_role: []
  scope: none | unknown
  persistence: none | unknown
  retrieval_policy: protocol resources are not automatically semantic memory
  write_policy: not defined by protocol
  isolation_key: application/auth scope dependent
  retention_policy: application/server dependent
  provenance: protocol-exposed content/resources require source-specific provenance

human_control:
  level: unknown
  mode: unknown
  dispatcher_enforcement: unknown
  enforcement_owner: application/infrastructure/server policy dependent
  enforcement_boundary: MCP interoperability does not define whether a user/model is authorized to invoke a consequential capability
  approval_binding: application-defined

errors_and_retries:
  error_model: structured | protocol-defined + application-specific
  retry_owner: runtime | client | server | mixed
  retry_budget: application-defined
  idempotency: tool/server-defined
  unknown_outcome_handling: application/server-defined; protocol support does not imply safe retry

termination:
  success_predicate: protocol request completion is not necessarily semantic business success
  terminal_failure_predicate: protocol/application error
  turn_budget: application-defined
  turn_budget_enforcement: application-defined
  tool_budget: application-defined
  tool_budget_enforcement: application-defined
  time_budget: transport/runtime-defined
  time_budget_enforcement: application/transport-defined
  cost_or_token_budget: application-defined
  cost_or_token_budget_enforcement: application-defined
  overshoot_semantics: application-defined
  oscillation_detection: application-defined
  cancellation: protocol/application revision dependent
  cancellation_effective_boundary: remote side-effect rollback is not implied

evaluation:
  static_contracts:
    - protocol revision/lifecycle compatibility
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols:
  - name: MCP
    revision: legacy stateful tutorial path
    role: client
    transport: tutorial-specific
    capabilities:
      - create ClientSession
      - initialize
      - list_tools
      - invoke tools over established session
    auth_model: tutorial/application-specific
    extensions: legacy/tutorial-specific

  - name: MCP
    revision: "2026-07-28"
    role: client/server/host depending implementation
    transport: implementation-specific; core revision includes stateless request/response semantics
    capabilities:
      - per-request protocol version / client metadata
      - optional server/discover
      - deterministic/cacheable list behavior where specified
      - formal extensions
    auth_model: hardened/current spec; concrete authorization remains deployment-specific
    extensions: first-class / revision-aware

security:
  trust_boundaries:
    - model/runtime
    - MCP client/host
    - remote/local MCP server
    - authentication/authorization layer
    - exposed tool/resource/prompt implementation
  least_privilege: application-required
  sandbox: unknown
  data_classification: application/server-specific
  receipts:
    - discoverable capability is explicitly not treated as authorized capability

reproducibility:
  model_receipt: not protocol-defined
  dependency_receipt: implementation-specific
  external_api_receipt:
    tutorial_snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
    protocol_revision: "2026-07-28"
  execution_evidence: this record is a source/spec revision comparison; Strands provides a separate upstream-executed modern MCP record

unknowns:
  - exact runtime compatibility of arbitrary legacy tutorial implementations with current protocol revision
  - concrete auth/authorization policy for each deployment
  - tool idempotency and retry semantics
  - remote side-effect state after timeout/cancellation
  - transport-specific behavior for a concrete implementation
```

## Material revision difference

Legacy tutorial shape:

```text
ClientSession
  ↓
initialize()
  ↓
list_tools()
  ↓
invocations over established session
```

Current `2026-07-28` core contract changes the lifecycle materially, including removal of the mandatory legacy core initialization/session assumptions and movement toward self-describing/stateless request semantics with optional discovery and formal extensions.

Therefore:

```text
protocol name equality
!=
lifecycle compatibility
```

## Security distinction

The record intentionally preserves:

```text
discoverable capability
    !=
authorized capability
    !=
approved consequential action
```

MCP solves interoperability/capability exposure. The agent system still owns policy, authorization, risk classification, HITL, side-effect verification and retry safety.

## Relationship to Strands MCP receipt

This record proves why revision-aware classification is required.

The stronger executable current example lives separately in:

- `systems/strands/PROTOCOLS.md`;
- `quarries/strands-mcp-2026-07-28-compatibility.md`.

That receipt verifies a current implementation path against MCP `2026-07-28` using upstream execution evidence. It does not erase the historical value of this legacy/current comparison.

## Production-certification boundary

This record does not certify any MCP server/client as secure, authorized, universally interoperable, idempotent or production-ready.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: false
normalization_issue: confirms protocol records require revision/role/transport/auth/extensions and must remain independent from authorization and side-effect policy
```

## Evidence

- [`../../../quarries/cross-source-memory-production-mcp.md`](../../../quarries/cross-source-memory-production-mcp.md)
- [`../../../mining-site/SOURCES.md`](../../../mining-site/SOURCES.md)
- current executable Strands comparison: [`../../../systems/strands/PROTOCOLS.md`](../../../systems/strands/PROTOCOLS.md)
