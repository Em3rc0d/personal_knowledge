# Strands Agents — Protocols & Interoperability

Status: **CURRENT REVISION-AWARE VIEW**  
Observed baseline: **2026-09-16**

This document separates protocol interoperability from the Strands runtime itself. A protocol adapter expands a system boundary; it does not automatically supply authorization, persistence, rollback, sandboxing or evaluation.

## MCP

### Current classification

```yaml
name: MCP
revision: "2026-07-28"
strands_role: client / external capability consumer
source_snapshot: strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
python_release_observed: python/v1.56.0
evidence_state: SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED
```

### What is actually evidenced

The pinned Python SDK declares `mcp>=1.23.0,<2.2` and contains explicit compatibility logic for the 1.x and 2.x protocol/runtime lines.

The strongest execution fixture uses MCP 2.x's own `MCPServer` over Streamable HTTP and wraps that server so a legacy `initialize` request receives HTTP `405`.

That matters because a client cannot pass this fixture by silently falling back to the legacy lifecycle.

The current evidence covers:

- modern lifecycle negotiation through `server/discover` semantics;
- tool listing;
- tool invocation;
- structured tool result propagation;
- MCP error result mapping;
- multi-round-trip input-required behavior;
- prompt listing/retrieval;
- resource listing/read/template behavior;
- input-required flows for prompts/resources;
- tools-list change subscription/refresh;
- finalized task-extension support paths;
- modern MCP trace continuity;
- upstream CI execution of the MCP 2.x compatibility/integration suite.

### Evidence status by concern

| Concern | Current state | Qualification |
|---|---|---|
| protocol revision awareness | **SUPPORTED** | pinned to `2026-07-28` for this knowledge pass |
| modern negotiation/lifecycle | **UPSTREAM TESTED** | fixture rejects legacy `initialize` |
| Streamable HTTP | **UPSTREAM TESTED** | in-process real MCP 2.x server |
| tools list/call | **UPSTREAM TESTED** | modern path |
| structured result/errors | **UPSTREAM TESTED** | modern models/fields |
| multi-round-trip input | **UPSTREAM TESTED** | callback + request-state retry |
| prompts/resources | **UPSTREAM TESTED** | including input-required flows in current pinned fixture |
| list-changed subscription | **UPSTREAM TESTED** | modern subscription/listen behavior |
| task extension | **SUPPORTED** | revision/extension-specific semantics; not core boolean |
| trace continuity | **UPSTREAM E2E TESTED** | caller/client/server trace-parent chain |
| client-credentials adapter | **SOURCE + UNIT SUPPORTED** | version-aware construction |
| protected external OAuth E2E | **OPEN / DEPLOYMENT-SPECIFIC** | not proven by local in-process fixture |
| remote cancellation | **MECHANISM SUPPORTED / QUALIFIED** | does not prove side-effect rollback |
| universal server compatibility | **NOT CERTIFIED** | fixture is representative, not universal conformance |
| local independent rerun | **NOT RUN** | environment lacked packages and outbound DNS/network |
| `mcp>=2.2` | **OUTSIDE PINNED RANGE** | do not infer future compatibility |

## MCP engineering interpretation

A high-quality protocol record cannot be:

```text
mcp: true
```

It should instead answer:

```text
which revision?
which role?
which lifecycle/negotiation path?
which transport?
which core operations?
which extensions?
which auth model?
which cancellation semantics?
which trace/observability behavior?
what execution receipt exists?
```

The Strands pass is now one of the strongest concrete examples in this repository of **protocol compatibility as a vector of evidence**.

## Cancellation boundary

The modern MCP runtime can propagate cancellation differently from the legacy line, but cancellation remains a control-plane fact, not a transactional guarantee.

Do not infer:

```text
request cancelled → external effect never happened
```

A remote server may already have started work or committed a mutation. Consequential operations still require idempotency, verification, unknown-outcome handling and compensating logic where appropriate.

## Authentication / authorization boundary

The framework exposes auth adapter support, including client-credentials construction, but this is distinct from proving a deployment's authorization policy.

Keep these layers separate:

```text
credential acquisition
≠ authenticated transport
≠ server authorization decision
≠ application business authorization
≠ safe side-effect semantics
```

## A2A

### Current classification

```yaml
name: A2A
revision: UNKNOWN
strands_role: remote-agent consumer/provider surfaces
evidence_state: FRAMEWORK CAPABILITY OBSERVED / REPRODUCIBILITY DEBT OPEN
```

The Strands evidence set shows A2A-oriented integration surfaces and remote-agent composition, but this knowledge base has not yet completed the same quality of protocol receipt established for MCP.

Still required before closing the A2A gate:

- exact protocol revision;
- transport receipt;
- auth model;
- client/server role matrix;
- failure/cancellation semantics;
- trace continuity where applicable;
- executable interoperability fixture;
- version-pinned execution receipt.

Until then, do not turn `supports A2A` into a reproducible integration claim.

## Other ecosystem boundaries

Official Strands material references additional ecosystem interfaces such as AG-UI and x402. They are not currently normalized as closed protocol records in this domain.

Their presence should be treated as ecosystem capability evidence only until a dedicated revision/role/transport/auth execution pass exists.

## Source chain

- canonical source receipt: [`../../mining-site/S-109-strands-agents.md`](../../mining-site/S-109-strands-agents.md)
- MCP execution receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md)
- MK1 protocol rules: [`../../mk/MK1/CLASSIFICATION_SCHEMA.md`](../../mk/MK1/CLASSIFICATION_SCHEMA.md)
- current open unknowns: [`../../mk/MK1/UNKNOWNS.md`](../../mk/MK1/UNKNOWNS.md)
