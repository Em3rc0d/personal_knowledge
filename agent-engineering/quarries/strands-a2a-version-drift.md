# Strands Agents × A2A — Version-Drift / Interoperability Receipt

Status: **SUPPORTED / QUALIFIED / REVISION-DRIFT IDENTIFIED**  
Observed: **2026-09-16**

## Question

What does “Strands supports A2A” actually mean at the pinned Strands snapshot, and can that support be treated as current A2A `1.0` interoperability?

## Pinned inputs

| Input | Receipt |
|---|---|
| Strands repository | `strands-agents/harness-sdk` |
| Strands snapshot | `a9361c54ca190117d5801dd09a1ab8d6d3d9bf20` |
| Strands Python A2A dependency | `a2a-sdk>=0.3.0,<0.4.0` |
| Strands TypeScript A2A dependency | `@a2a-js/sdk ^0.3.10` |
| A2A official source | `S-112` |
| Current A2A compatibility line | `1.0` |
| Latest A2A repository release observed | `v1.0.1` |
| A2A 1.0 major release | `v1.0.0` — breaking changes from 0.3 |

## Executive result

```text
Strands A2A capability                SUPPORTED
Strands Python protocol family        0.3.x
Strands TypeScript protocol family    0.3.x
A2A current protocol family           1.0
Strands 0.3 integration fixtures      PRESENT
A2A 0.3 invocation/streaming          COVERED BY FIXTURE SOURCE
A2A 0.3 Graph integration             COVERED BY FIXTURE SOURCE
Specific successful fixture CI run    NOT VERIFIED IN THIS PASS
Independent execution                 NOT RUN
A2A 1.0 compatibility                 NOT ESTABLISHED
Version drift                         MATERIAL / EXPLICIT
```

The correct current statement is therefore:

> The pinned Strands SDK exposes real A2A client/server integration against the A2A **0.3** SDK family. Current A2A protocol compatibility is **1.0**, so A2A 1.0 support must not be inferred without a migration/execution receipt.

## 1. Dependency receipt

### Python

At the pinned snapshot, `strands-py/pyproject.toml` declares:

```text
A2A extra → a2a-sdk >=0.3.0,<0.4.0
```

### TypeScript

At the same snapshot, `strands-ts/package.json` uses:

```text
@a2a-js/sdk ^0.3.10
```

The current upstream Strands default branch inspected during this pass still exposes the TypeScript `0.3.10` dependency family, so the finding is not merely an old archived-package artifact.

## 2. Current A2A revision

Official A2A sources identify the released protocol compatibility line as **1.0**.

Current specification semantics use `Major.Minor` for protocol compatibility. Patch versions do not define a new wire compatibility version.

The official repository's `v1.0.0` release is explicitly a breaking release relative to `0.3`, including changes to protocol bindings, request/message shapes, push-notification configuration, OAuth flows and other protocol structures.

A later `v1.0.1` patch release contains bug fixes while remaining in protocol compatibility line `1.0`.

Therefore:

```text
0.3 implementation
+
current spec 1.0
≠
current-compatible implementation
```

## 3. Strands A2A client surface

The pinned Python source provides `A2AAgent`, which:

- resolves/fetches a remote Agent Card;
- caches card metadata;
- invokes a remote agent synchronously/asynchronously;
- streams A2A protocol events;
- converts terminal/interrupted task states into Strands result semantics;
- accepts a configurable A2A `ClientConfig` / HTTP client for authentication/transport settings.

The source explicitly notes that authenticated card discovery can use a caller-provided HTTP client configured for mechanisms such as SigV4, OAuth or bearer tokens.

This is an implementation surface, not a guarantee that every remote endpoint is authenticated/authorized correctly.

## 4. Strands A2A server surface

Pinned documentation exposes `A2AServer` / TypeScript server integration.

Observed semantics include:

- Agent Card at `/.well-known/agent-card.json`;
- JSON-RPC handling in the documented server path;
- streaming support;
- task/context-oriented conversation behavior;
- per-context `agent_factory` as the recommended isolation model;
- bounded server context cache (`max_contexts`);
- task store / queue / push notification extension points.

### Critical security qualification

The docs explicitly warn:

```text
context_id is not an authentication boundary
```

A caller that knows another context ID can attach to that conversation unless the deployment adds authenticated identity enforcement at the transport/gateway layer.

Therefore:

```text
conversation isolation by key
!=
authenticated tenant isolation
```

## 5. Concurrency semantics

Pinned Strands docs expose two materially different A2A server modes.

### Recommended `agent_factory`

A dedicated agent is created/reused per `context_id`, allowing independent contexts to execute concurrently.

### Deprecated shared `agent`

A single agent is reused across contexts, with state swapped under a lock. This serializes requests and creates stronger coupling between context handling and the shared instance.

This supports the MK1 rule that protocol/server support must still describe:

- invocation concurrency;
- writer/state model;
- isolation key;
- lock/serialization behavior.

## 6. Interrupt / `input_required` semantics

Pinned documentation maps Strands interrupt handling into A2A task interruption semantics.

For Python:

- a tool/hook interrupt moves the task to `input_required`;
- pending interrupt identifiers are exposed in a structured `DataPart`;
- the client responds on the same task with the matching interrupt ID;
- unmatched/duplicate/invalid responses are rejected before the agent resumes;
- a normal conversational message is rejected while an interrupt remains pending.

This is stronger than a generic “human can reply” feature because it introduces an explicit binding identifier.

Qualification: protocol/task binding still does not prove that every external side effect surrounding the interrupt is replay-safe or transactional.

## 7. Integration-fixture evidence

The pinned repository contains:

```text
strands-py/tests_integ/a2a/test_multiagent_a2a.py
```

The fixture starts a local A2A server subprocess and covers:

- synchronous `A2AAgent` invocation;
- async invocation;
- streaming invocation;
- non-streaming client configuration;
- a Strands `Graph` containing both a remote `A2AAgent` node and a regular local `Agent` node.

The repository's Python integration-test workflow includes the whole `tests_integ` tree in its main integration scope.

### Evidence qualification

This pass verified:

```text
fixture source              PRESENT
fixture in integration tree PRESENT
integration workflow scope  tests_integ
specific successful CI run  NOT VERIFIED
independent local run       NOT RUN
```

Do not convert “fixture exists in CI scope” into “this exact fixture passed on this exact snapshot” without a run receipt.

## 8. Authentication / authorization boundary

Current A2A 1.0 semantics declare security schemes/requirements in the Agent Card and rely on standard web security mechanisms. Authorization remains application-defined.

Pinned Strands exposes client transport customization for authenticated requests and server customization hooks, but the basic server examples do not establish a universal authenticated deployment.

Important domain distinction:

```text
Agent Card says security scheme
!=
credential successfully acquired
!=
caller authenticated
!=
action authorized
```

## 9. Task cancellation

A2A defines task cancellation/state transitions. Strands' A2A surface can represent task completion/interruption states.

However:

```text
task canceled
!=
remote business side effect rolled back
```

Exactly-once, idempotency and compensating actions remain tool/application responsibilities.

## 10. Schema consequence

The existing MK1 protocol shape can represent the evidence without a new top-level dimension:

```yaml
protocols:
  - name: A2A
    revision: "0.3"
    role: client + server
    transport: HTTP / JSON-RPC path in pinned Strands implementation
    capabilities:
      - Agent Card discovery
      - synchronous/async invocation
      - streaming
      - task/context handling
      - input_required interrupt flow
      - Graph remote-agent node integration
    auth_model: transport/application configured; context_id is not auth
    execution_evidence:
      fixture_source: PRESENT
      ci_scope: PRESENT
      specific_ci_pass: NOT_VERIFIED
      independent_run: NOT_RUN
    compatibility:
      current_a2a_1_0: NOT_ESTABLISHED
```

No `A2A=true` boolean can preserve this information adequately.

## 11. MK1 gate decision

The **classification/evidence-shape gate can pass in qualified form** because:

1. exact protocol family is pinned (`0.3`);
2. implementation dependencies are pinned;
3. client/server/discovery/task/streaming/concurrency/auth boundaries are evidenced;
4. integration fixture source exists;
5. absence of a specific CI execution receipt is explicit;
6. current `1.0` version drift is identified rather than hidden;
7. the current MK1 schema represents the difference without framework-specific fields.

What remains open is not “what does A2A mean?” but:

> **Strands A2A 1.0 migration/interoperability execution evidence.**

That becomes system freshness/compatibility debt, not a reason to pretend the existing 0.3 receipt is current 1.0 conformance.

## 12. Reusable rules strengthened

### Rule A — Protocol support is revision-specific

```text
supports A2A 0.3
!=
supports A2A 1.0
```

### Rule B — Discovery keys are not identity boundaries

`context_id`, task ID or Agent Card discovery data must not be treated as authenticated tenant identity unless the security layer explicitly binds them.

### Rule C — Distributed-agent interoperability expands trust boundaries

Adding a remote agent adds at least:

- remote endpoint identity;
- remote capabilities;
- credential/auth boundary;
- task state;
- network failure/unknown outcome;
- cancellation semantics;
- remote side-effect authority.

### Rule D — Integration fixture ≠ verified CI pass

Preserve the difference among:

```text
fixture exists
fixture is in CI scope
specific run passed
independent reproduction passed
```

## Promotion decision

For the pinned Strands snapshot:

```text
A2A 0.3 implementation          SUPPORTED / SOURCE + FIXTURE EVIDENCE
A2A 0.3 execution receipt       QUALIFIED — specific CI pass not verified
A2A 1.0 compatibility           OPEN / NOT ESTABLISHED
MK1 protocol classification     PASS / QUALIFIED
```

This is sufficient to close the broad MK1 **A2A classification-shape** unknown while preserving A2A 1.0 migration as explicit version-drift debt.
