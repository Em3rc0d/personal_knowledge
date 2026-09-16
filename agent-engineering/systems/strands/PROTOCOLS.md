# Strands Agents — Protocols & Interoperability

Status: **CURRENT REVISION-AWARE VIEW**  
Observed baseline: **2026-09-16**

This document separates protocol interoperability from the Strands runtime itself. A protocol adapter expands a system boundary; it does not automatically supply authorization, persistence, rollback, sandboxing or evaluation.

## Protocol summary

| Protocol | Strands pinned path | Current protocol line | Evidence state |
|---|---|---|---|
| MCP | MCP 2.x adapter path | `2026-07-28` | **SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED** |
| A2A Python | `a2a-sdk >=0.3.0,<0.4.0` | `1.0` | **SUPPORTED FOR 0.3 / CURRENT-REVISION DRIFT** |
| A2A TypeScript | `@a2a-js/sdk ^0.3.10` | `1.0` | **SUPPORTED FOR 0.3 / CURRENT-REVISION DRIFT** |

A protocol name alone is never the compatibility receipt.

# MCP

## Current classification

```yaml
name: MCP
revision: "2026-07-28"
strands_role: client / external capability consumer
source_snapshot: strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
python_release_observed: python/v1.56.0
evidence_state: SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED
```

## What is actually evidenced

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

## MCP evidence status by concern

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

## MCP cancellation boundary

Modern cancellation remains a control-plane fact, not a transactional guarantee.

Do not infer:

```text
request cancelled → external effect never happened
```

Consequential operations still require idempotency, verification, unknown-outcome handling and compensating logic where appropriate.

## MCP authentication / authorization boundary

Keep these layers separate:

```text
credential acquisition
≠ authenticated transport
≠ server authorization decision
≠ application business authorization
≠ safe side-effect semantics
```

# A2A

## Current classification

```yaml
name: A2A
strands_snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
python_dependency: a2a-sdk >=0.3.0,<0.4.0
typescript_dependency: @a2a-js/sdk ^0.3.10
strands_protocol_family: "0.3"
current_a2a_protocol_family: "1.0"
latest_a2a_repo_release_observed: v1.0.1
evidence_state: SUPPORTED_FOR_0_3 / VERSION_DRIFT / CURRENT_1_0_NOT_ESTABLISHED
```

## What Strands actually supports at the pinned snapshot

The pinned Strands SDK has real A2A-oriented implementation surfaces rather than a documentation-only claim.

### Client / remote agent

`A2AAgent` supports:

- Agent Card resolution and caching;
- synchronous invocation;
- asynchronous invocation;
- streaming remote execution;
- protocol event mapping to Strands result semantics;
- configurable A2A client/HTTP transport settings;
- authenticated HTTP client injection where the caller configures mechanisms such as bearer/OAuth/SigV4.

### Server

Pinned Strands documentation exposes A2A servers with:

- Agent Card at `/.well-known/agent-card.json`;
- documented JSON-RPC request handling;
- streaming support;
- task/context handling;
- per-context `agent_factory` as the recommended model;
- configurable task stores, queue managers and push-notification components.

### Multi-agent composition

Remote `A2AAgent` instances can participate in supported Graph patterns and can be wrapped as tools for orchestration.

Swarm does not support `A2AAgent` directly in the pinned docs.

## A2A integration fixture

The pinned Python repository includes:

```text
strands-py/tests_integ/a2a/test_multiagent_a2a.py
```

The fixture starts a local A2A server and covers:

- synchronous invocation;
- async invocation;
- streaming;
- non-streaming client configuration;
- a Graph combining a remote `A2AAgent` node with a local Strands `Agent`.

The Python integration-test workflow runs the broad `tests_integ` tree in its main integration scope.

Evidence must remain precise:

```text
fixture source present             YES
fixture located in integration set YES
workflow includes tests_integ      YES
specific successful A2A CI run     NOT VERIFIED IN THIS PASS
independent local rerun             NOT RUN
```

Do not convert the first three lines into the fourth.

## A2A version drift

Current official A2A uses protocol compatibility line **1.0**. The A2A `v1.0.0` release contains breaking changes relative to `0.3`.

Therefore the pinned Strands `0.3.x` SDK dependencies cannot be represented as current A2A 1.0 support without additional migration/execution evidence.

```text
Strands A2A 0.3 implementation
          !=
A2A 1.0 compatibility
```

This is now explicit version debt rather than an undifferentiated `A2A UNKNOWN`.

## A2A discovery / identity

Strands uses Agent Card discovery for remote metadata/capability information.

The server also uses client-supplied `context_id` for conversation state isolation.

Pinned Strands documentation explicitly warns:

```text
context_id is not an authentication boundary
```

A caller with another caller's context ID can attach to that conversation unless authenticated identity is enforced at the transport/gateway layer.

Therefore:

```text
context isolation key
!=
authenticated tenant identity
```

## A2A concurrency model

Pinned server documentation distinguishes:

### `agent_factory` — recommended

Dedicated agent instance per `context_id`; independent contexts can execute concurrently.

### single shared `agent` — deprecated

One agent is reused across contexts and protected by a lock while state is swapped, serializing requests.

This reinforces that distributed-agent protocol support still requires ordinary state/concurrency classification.

## A2A interrupt / input-required binding

Pinned Python documentation maps Strands interrupts into A2A `input_required` task state.

Pending interrupts carry server-generated IDs. Responses must return the matching ID on the same task, and invalid/unmatched/duplicate answers are rejected before execution resumes.

This gives stronger binding semantics than a free-form “human replied” flow.

It does not prove replay-safe external side effects around the interrupt.

## A2A authentication / authorization boundary

Current A2A 1.0 supports standard security-scheme declarations and standard web authentication mechanisms. Authorization remains application/agent policy.

Pinned Strands allows custom authenticated clients and server/gateway customization, but basic framework support does not establish one universal auth policy.

Keep separate:

```text
Agent Card discovery
≠ declared security scheme
≠ authenticated transport
≠ caller authorization
≠ permission for a consequential action
```

## A2A cancellation boundary

Task cancellation is a protocol/task-state concept.

Do not infer:

```text
task canceled
→ remote business mutation rolled back
```

Idempotency, exactly-once assumptions and compensation remain application responsibilities.

## A2A gate result

For MK1 classification purposes:

```text
protocol family pinned             PASS
client/server roles                PASS
Agent Card/discovery               PASS
transport/task shape               PASS for pinned 0.3 path
state/concurrency boundary          PASS / qualified
security boundary                  PASS / qualified
integration fixture source         PASS
specific CI execution receipt       NOT VERIFIED
independent execution               NOT RUN
current A2A 1.0 compatibility       OPEN / NOT ESTABLISHED
schema representability             PASS
```

The broad **A2A classification-shape gate is therefore PASS / QUALIFIED**.

Remaining debt is narrower:

```text
Strands A2A 1.0 migration + executable interoperability receipt
```

That is version/freshness debt, not justification for reporting `A2A=true` without revision.

# Other ecosystem boundaries

Official Strands material references additional ecosystem interfaces such as AG-UI and x402. They are not currently normalized as closed protocol records in this domain.

Treat them as ecosystem capability evidence until a dedicated revision/role/transport/auth execution pass exists.

# Source chain

- Strands source receipt: [`../../mining-site/S-109-strands-agents.md`](../../mining-site/S-109-strands-agents.md)
- A2A current protocol receipt: [`../../mining-site/S-112-a2a-protocol.md`](../../mining-site/S-112-a2a-protocol.md)
- MCP execution receipt: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md)
- A2A version-drift receipt: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md)
- MK1 protocol schema: [`../../mk/MK1/CLASSIFICATION_SCHEMA.md`](../../mk/MK1/CLASSIFICATION_SCHEMA.md)
- current UNKNOWNs: [`../../mk/MK1/UNKNOWNS.md`](../../mk/MK1/UNKNOWNS.md)
