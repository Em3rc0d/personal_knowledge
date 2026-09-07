# Cross-Source Check — Memory, Production and MCP

> Status: **MK0 quarry evidence — NOT CANON**  
> Date: 2026-09-07

## Sources pinned

| ID | Source | Snapshot / revision | Role |
|---|---|---|---|
| S-001 | `NirDiamant/GenAI_Agents` | `4c95ae14cc2462c442b5c064cccd74430d02bc46` | broad agent-pattern corpus |
| S-002 | `NirDiamant/Agent_Memory_Techniques` | `b7f7240eb4d4510f3b45300a89126858a474b31d` | specialized memory corpus |
| S-003 | `NirDiamant/agents-towards-production` | `141b0679f11b48209f2b872419f78a3a13850e0d` | production-oriented corpus |
| S-108 | Model Context Protocol | `2026-07-28` | current official protocol contract |

This pass exists to prevent one broad tutorial repository from becoming the authority for every subdomain.

---

## 1. Memory — move from label to lifecycle contract

### S-001 pressure

The general GenAI corpus contains examples named `memory-enhanced`, LangGraph `MemorySaver` usage, checkpointers and stores. Those examples are useful but heterogeneous.

### S-002 specialized contrast

The dedicated memory corpus organizes 30 techniques across distinct families:

- short-term context management;
- long-term storage;
- cognitive memory architectures;
- retrieval/routing;
- memory frameworks;
- evaluation/production.

Its comparison matrix independently separates:

- persistence;
- retrieval mechanism;
- token-cost behavior;
- intended lifecycle/use case.

### Normalized conclusion

`memory` must not be a boolean property.

MK1 should classify memory with at least:

```yaml
semantic_role: conversation | episodic | semantic | procedural | working | shared | external_knowledge
scope: turn | session | cross_session | user | project | shared_team
persistence: none | process | local_durable | remote_durable
write_policy: explicit | automatic | model_selected | background_consolidation
retrieval_policy: recency | semantic | lexical | graph | time | hybrid | tool_selected
isolation_key: none | session | user | tenant | project
retention_policy:
update_conflict_policy:
forgetting_or_decay:
provenance:
evaluation:
```

### Canon candidate

> Persistence answers **whether information survives**. Memory answers **what is intentionally retained and later recalled, for whom, under what lifecycle and retrieval policy**.

A checkpoint can persist without being semantic memory. A vector store can be durable memory but is not runtime state. RAG can retrieve knowledge without representing a user's memory.

---

## 2. Production — source claim vs demonstrated readiness

### S-003 value

`agents-towards-production` is materially more relevant than S-001 for production concerns. Its stated tutorial scope includes:

- stateful workflows;
- vector memory;
- real-time search/data integrations;
- Docker deployment;
- FastAPI endpoints;
- guardrails/security;
- GPU/cloud scaling;
- browser automation;
- multi-agent coordination;
- observability;
- evaluation;
- user interfaces.

Those are the correct **classes of concern** when moving from demo to operated system.

### Important negative evidence

At the pinned snapshot, `.github/` contains:

- `FUNDING.yml`;
- `ISSUE_TEMPLATE.md`;
- `dependabot.yml`.

No repository-wide GitHub Actions workflow is visible there.

Therefore:

```text
"production-oriented tutorial"
        !=
"repository-wide reproducibly tested production system"
```

### Normalized production-readiness model

A later MK should require evidence across separate dimensions rather than a `production_ready=true` label:

```yaml
runtime_reproducibility:
configuration_and_secrets:
authentication_authorization:
least_privilege:
data_governance:
idempotency_and_replay:
fault_tolerance:
timeouts_retries_cancellation:
persistence_and_recovery:
observability:
evaluation_regression_gates:
security_testing:
deployment_and_rollback:
capacity_and_cost:
incident_operability:
```

### Canon candidate

> Production readiness is an evidence vector, not a tutorial category.

No sister repository, vendor integration or framework name can promote an individual agent to production-ready without evidence for the relevant operational dimensions.

---

## 3. MCP — protocol revision is part of architecture

### S-001 tutorial shape

The MCP notebook uses the older stateful lifecycle:

```text
create ClientSession
  ↓
initialize()
  ↓
list_tools()
  ↓
tool calls over established session
```

This was a valid historical MCP teaching shape.

### S-108 current official revision

The MCP `2026-07-28` release changed the core lifecycle substantially:

- core protocol is stateless request/response;
- mandatory `initialize` / `initialized` handshake removed;
- `Mcp-Session-Id` removed from core lifecycle;
- each request is self-describing;
- protocol version travels per request;
- client identity/capability metadata travels with requests;
- optional `server/discover` supports capability discovery when desired;
- method/tool routing becomes HTTP-header visible;
- list responses can be deterministic/cacheable;
- authorization is hardened;
- extensions are first-class;
- long-running/interactivity capabilities move through extensions / multi-round-trip patterns;
- protocol features now have explicit deprecation lifecycle.

### Normalized MCP integration contract

MK1 must not store merely:

```yaml
mcp: true
```

It needs something closer to:

```yaml
protocol: MCP
revision: 2026-07-28
transport:
role: host | client | server
capabilities_exposed:
extensions:
auth_model:
identity_model:
trust_boundary:
policy_owner:
allowed_tools_resources_prompts:
timeouts_and_cancellation:
observability:
```

### Security distinction

MCP standardizes interoperability and capability exposure. It does **not** answer whether a particular model/user is authorized to invoke a consequential tool.

```text
discoverable capability
    !=
authorized capability
    !=
approved action
```

### Canon candidate

> Protocol interoperability and execution authorization are orthogonal contracts.

---

## 4. Source-specialization rule

This cross-check establishes a reusable evidence principle:

```text
broad corpus
   ↓ discovers pattern
specialized source
   ↓ refines domain vocabulary
current official contract
   ↓ constrains versioned behavior
independent empirical evidence
   ↓ challenges generalization
our test/evidence gate
   ↓ decides promotion
```

Examples:

- GenAI_Agents discovers memory examples; dedicated memory sources define a stronger memory quarry.
- GenAI_Agents demonstrates MCP concepts; current MCP specification defines current wire/lifecycle semantics.
- agents-towards-production expands operational concerns; actual production readiness still requires project-specific evidence.

## 5. MK0 disposition

The previously open cross-source blockers are now resolved at **Mine & Frame** depth:

- memory semantics have a specialized comparison source;
- production claims have a specialized comparison source and explicit qualification;
- MCP has been checked against the current `2026-07-28` protocol revision;
- remaining implementation/runtime certification belongs to MK2+ rather than MK0.

No source here is promoted wholesale to canon.