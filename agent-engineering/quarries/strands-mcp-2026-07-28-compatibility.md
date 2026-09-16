# Strands Agents × MCP `2026-07-28` — Compatibility Receipt

Status: **SUPPORTED BY PINNED SOURCE + EXECUTED UPSTREAM CI / NOT INDEPENDENTLY RE-RUN LOCALLY**  
Observed: **2026-09-16**

## Question

Does the pinned Strands Agents Python SDK evidence support real interoperability with the MCP `2026-07-28` protocol revision, or only legacy MCP naming/API compatibility?

## Pinned inputs

| Input | Receipt |
|---|---|
| Strands repository | `strands-agents/harness-sdk` |
| Strands snapshot | `a9361c54ca190117d5801dd09a1ab8d6d3d9bf20` |
| Python release observed | `python/v1.56.0` |
| MCP contract | `2026-07-28` |
| Strands MCP dependency at snapshot | `mcp>=1.23.0,<2.2` |
| MCP 2.x detection | capability probe: `hasattr(ClientSession, "discover")` |
| Transport fixture | in-process `MCPServer` over Streamable HTTP |

Primary Strands source: [`../mining-site/S-109-strands-agents.md`](../mining-site/S-109-strands-agents.md).

## Historical failure that had to be closed

A prior Strands state could import/operate against MCP 1.x while failing against servers that spoke only the `2026-07-28` lifecycle. The important regression shape was not merely renamed Python symbols: the old path attempted the legacy `initialize` handshake, while the new protocol moved connection negotiation to `server/discover` and removed protocol-session lifecycle assumptions.

The current pinned source contains a dedicated compatibility layer and integration fixture designed specifically to prevent that regression.

## 1. Dependency evidence

**OBSERVED** — `strands-py/pyproject.toml` at the pinned snapshot declares:

```text
mcp>=1.23.0,<2.2
```

The same file documents that the normal test matrix resolves to MCP 2.x and that a separate override forces MCP 1.x for backwards-compatibility coverage.

**SUPPORTED** — MCP 2.x is therefore no longer an accidental unsupported install path at this snapshot; it is inside the declared dependency contract and test matrix.

Qualification: acceptance of a version range is not by itself interoperability evidence. The runtime lifecycle and behavior must still be exercised.

## 2. Protocol-aware compatibility layer

**OBSERVED** — `strands.tools.mcp._compat` detects MCP 2.x by capability rather than parsing a package version:

```text
MCP_V2 := ClientSession exposes discover
```

The source explicitly describes `ClientSession.discover` as the 2.x replacement for the removed initialization handshake.

The compatibility layer also contains 2.x-specific behavior for:

- modern session negotiation;
- snake_case result/model fields;
- Streamable HTTP transport differences;
- multi round-trip input requests;
- prompts/resources reads;
- list pagination;
- tool result error and structured-content mapping;
- modern list-changed subscription behavior;
- finalized task-extension behavior.

**SUPPORTED** — this is protocol-semantic adaptation, not merely import aliasing.

## 3. Strongest fixture: reject legacy initialization

**OBSERVED** — the pinned source contains:

```text
strands-py/tests_integ/mcp/test_mcp_client_v2.py
```

The fixture runs MCP 2.x's own `MCPServer` in-process over Streamable HTTP.

Crucially, the server application is wrapped so that any request whose method is the legacy `initialize` handshake receives HTTP `405`.

Therefore this assertion shape matters:

```text
Strands MCPClient connects successfully
AND
server refuses initialize
```

A client that merely fell back to the legacy lifecycle cannot pass the fixture.

**SUPPORTED** — successful connection proves the tested path negotiates the modern lifecycle rather than accidentally succeeding through legacy compatibility.

## 4. Behaviors exercised by the pinned fixture

The current pinned integration file exercises more than connection setup.

### Negotiation

- connect to a server that only accepts the modern lifecycle;
- obtain server instructions after negotiation.

### Tools

- list tools;
- invoke a tool;
- surface structured tool output;
- map MCP error results.

### Multi round-trip requests

For MCP 2.x / `2026-07-28`, server-initiated elicitation was replaced by input-required results and request-state echo/retry semantics.

The fixture verifies that Strands:

1. receives `InputRequiredResult`;
2. dispatches embedded input through the registered elicitation callback;
3. carries responses / request state into another round;
4. reaches a terminal result;
5. returns a clean error when no elicitation callback exists;
6. forwards a declined input response.

### Prompts and resources

The pinned fixture additionally exercises:

- prompt listing and retrieval;
- resource listing / templates;
- resource reads;
- input-required retry behavior for prompts;
- input-required retry behavior for resources.

### Tool-list change subscription

The fixture dynamically registers a new server tool, publishes a tools-list-changed event, and verifies that the Strands client refreshes its cached tool set and calls the registered change callback.

This matters because modern MCP requires a subscription/listen path for this behavior rather than assuming legacy unprompted notification delivery.

## 5. Upstream CI execution receipt

PR `strands-agents/harness-sdk#4129` introduced the dedicated MCP 2.x integration fixture.

**OBSERVED** — the PR is merged. Its CI run `33901746886` completed successfully.

Within that run, job:

```text
Python / MCP 2.x Compat
```

completed with `success`, including explicit steps:

```text
Install package, then force mcp 2.x over the pin
Verify import and version flag
Run MCP tests
Run mcp 2.x integration tests
```

The repository's CI gate also completed successfully.

**SUPPORTED** — the core `2026-07-28` negotiation/tool fixture has an actual upstream execution receipt, not only source-code existence.

### Evidence strength qualification

This is source-owned CI, not an independently reproduced run by this knowledge base. It is strong operational evidence about the upstream project, but it should not be labeled an external conformance certification.

## 6. Trace continuity evidence

PR `#4131` added an end-to-end MCP 2.x OpenTelemetry test.

Its fixture:

- runs Strands `MCPClient` against MCP 2.x's real in-process server over Streamable HTTP;
- opens a caller span;
- invokes a tool;
- verifies caller, client-dispatch and server spans share the same trace ID;
- verifies parent relationships across Strands' background-thread boundary.

The PR is merged and its CI workflow completed successfully.

**SUPPORTED** — trace continuity across the modern MCP client/server boundary is directly tested upstream rather than inferred from metadata injection alone.

Qualification: observability continuity does not authorize the tool call and does not prove every external MCP server exports or preserves traces.

## 7. Cancellation semantics

**OBSERVED** — current Strands compatibility code treats MCP 1.x and 2.x cancellation differently.

On MCP 1.x, Strands historically had to capture a request ID and send cancellation notification behavior itself. On MCP 2.x, the official dispatcher owns cancellation signaling for the active request; Strands avoids sending a duplicate hand-crafted cancellation notification.

**QUALIFIED** — this establishes the mechanism used by Strands, but does **not** prove rollback of a remote side effect already started by the server.

The domain rule therefore remains:

```text
protocol cancellation != transactional rollback
```

Classification must still describe cancellation as best-effort/cooperative when the remote operation's external effects cannot be proven reversible.

## 8. Authentication boundary

**OBSERVED** — the pinned Strands source includes MCP client-credentials OAuth support and version-aware construction for MCP 1.x vs 2.x. Unit tests cover the renamed MCP 2.x client-credentials interface.

However, the modern local interoperability fixture deliberately requires no external endpoint or credentials.

**QUALIFIED** — this proves Strands exposes and tests auth construction compatibility, but the local `2026-07-28` fixture is **not an authenticated authorization-conformance test**.

Therefore:

- transport/protocol interoperability: supported;
- auth adapter compatibility: supported at source/unit level;
- end-to-end OAuth authorization policy against an external protected MCP server: remains deployment-specific / not proven by this fixture.

## 9. Tasks and extension boundary

The current source distinguishes:

- legacy experimental task behavior on MCP 1.x;
- finalized SEP-2663 task extension behavior on MCP 2.x.

**SUPPORTED** — protocol extensions must be classified separately from the core protocol revision. A system can be compatible with MCP `2026-07-28` core while individual extensions have their own support/version evidence.

This reinforces the MK1 schema rule:

```text
MCP=true
```

is insufficient. Record revision, role, transport, auth assumptions and extensions.

## 10. What this closes

The Strands quarry previously carried:

> exact current MCP `2026-07-28` execution compatibility not yet independently executed

That statement is now refined.

### Closed at source-evidence level

```text
modern lifecycle negotiation     SUPPORTED
legacy-initialize rejection      TESTED UPSTREAM
Streamable HTTP interoperability TESTED UPSTREAM
tools list/call                  TESTED UPSTREAM
structured result/error mapping  TESTED UPSTREAM
MRTR input-required              TESTED UPSTREAM
prompts/resources                TESTED UPSTREAM IN CURRENT PINNED FIXTURE
list-changed subscription        TESTED UPSTREAM
MCP 2.x trace continuity         TESTED UPSTREAM
```

### Still open / qualified

```text
independent local re-run in this environment  NOT EXECUTED
external protected-server OAuth E2E           DEPLOYMENT-SPECIFIC / OPEN
remote side-effect rollback after cancel      NOT IMPLIED
universal server interoperability              NOT CERTIFIED
future mcp >=2.2 compatibility                 OUTSIDE PINNED RANGE AT THIS SNAPSHOT
```

## 11. Local reproduction attempt receipt

A local execution was attempted on 2026-09-16.

Environment:

```text
Python 3.13.5
pytest installed
uvicorn installed
strands not installed
mcp not installed
container outbound DNS/network unavailable
```

The environment could not clone GitHub or install the missing packages because network resolution is disabled. No local test result is claimed.

This is recorded explicitly so `upstream CI PASS` is not silently transformed into `independent reproduction PASS`.

## 12. Classification consequence

For the pinned Strands snapshot, the MCP record can now be represented as:

```yaml
protocols:
  - name: MCP
    revision: "2026-07-28"
    role: client / tool consumer
    transport: Streamable HTTP tested upstream
    capabilities:
      - server/discover negotiation
      - tools/list
      - tools/call
      - structured content
      - input-required multi-round-trip
      - prompts
      - resources
      - list-changed subscription
      - task extension support
      - trace propagation
    auth_model: client-credentials adapter supported; deployment policy separate
    extensions:
      - SEP-2322 multi-round-trip input
      - SEP-2663 tasks where configured/supported
    execution_evidence:
      upstream_ci: PASS
      independent_local: NOT_RUN_ENVIRONMENT_BLOCKED
```

## 13. Engineering rule strengthened

**SUPPORTED**:

> Protocol compatibility is a vector of evidence, not a boolean.

At minimum distinguish:

```text
protocol revision
negotiation/lifecycle
transport
core request behavior
extensions
authentication/authorization
cancellation semantics
observability continuity
execution receipt
```

A green interoperability fixture does not automatically prove authorization correctness or transactional safety.

## Promotion decision

The Strands ↔ MCP `2026-07-28` compatibility debt is **closed for current source-level interoperability evidence** at the pinned snapshot.

It remains intentionally **qualified**, not certified universally:

- upstream CI execution exists;
- exact modern lifecycle is regression-tested;
- local independent reproduction was blocked by environment;
- authorization and remote-effect semantics remain deployment-specific.

This is sufficient to promote the Strands MCP record from `UNKNOWN execution compatibility` to **`SUPPORTED / UPSTREAM-EXECUTED / QUALIFIED`** without weakening the domain's evidence discipline.
