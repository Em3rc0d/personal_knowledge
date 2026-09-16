# S-112 — Agent2Agent (A2A) Protocol

Status: **REGISTERED / OFFICIAL**  
Observed: **2026-09-16**

## Source identity

| Field | Value |
|---|---|
| ID | `S-112` |
| System | Agent2Agent (A2A) Protocol |
| Type | open protocol specification / official repository |
| Documentation | https://a2a-protocol.org/ |
| Specification | https://a2a-protocol.org/dev/specification/ |
| Repository | https://github.com/a2aproject/A2A |
| Repository snapshot observed | `afda8316c64951a2ecb2a0d3d10867405d2b4095` |
| Latest repository release observed | `v1.0.1` — 2026-05-28 |
| Protocol compatibility version | `1.0` |
| Major specification release | `v1.0.0` — 2026-03-12 |
| Previous major/minor line relevant here | `0.3` |
| License | Apache-2.0 |
| Use here | revision-aware distributed-agent interoperability pressure test |
| Authority | official A2A protocol source |

## Version semantics

The current specification identifies the released protocol as **1.0**. A2A protocol compatibility is identified by `Major.Minor`; patch versions do not define a distinct wire-compatibility version.

At observation time the repository's latest patch release is `v1.0.1`, while the protocol compatibility line remains `1.0`.

The `v1.0.0` release explicitly contains breaking changes relative to `0.3`, including a broad refactor separating the application protocol from transport bindings and multiple message/API/security shape changes.

Therefore:

```text
A2A SDK 0.3.x
!=
automatic A2A 1.0 compatibility
```

## Core current semantics inspected

### Agent Card

The Agent Card is the self-describing discovery document for an agent. Current fields/surfaces include:

- identity/name/description;
- supported interfaces and endpoints;
- protocol version per interface;
- capabilities;
- security schemes/requirements;
- input/output modes;
- skills;
- optional signatures/extensions.

Discovery metadata is **not authorization**.

### Tasks / messages

A2A supports direct messages and stateful tasks. Tasks have explicit lifecycle states and identifiers; messages can be associated with tasks and contexts.

Important current states include terminal and interrupted states such as:

- completed;
- failed;
- canceled;
- rejected;
- input required;
- auth required.

A runtime/application must still decide what those states mean for external side effects.

### Protocol versioning

Current clients send the A2A protocol version (`1.0`) with requests. A 0.3 client may be assumed when the version header is absent under current backward-compatibility semantics.

This makes protocol revision a first-class interoperability fact.

### Standard bindings

Current A2A defines standard bindings for:

- JSON-RPC;
- gRPC;
- HTTP+JSON / REST.

Agents declare supported interfaces/bindings in their Agent Card. Transport support must be classified separately from the abstract protocol.

### Authentication / authorization

A2A uses standard web/application security patterns.

Authentication requirements are declared in the Agent Card. Credentials are generally acquired and transmitted outside the A2A message body through the relevant transport/security mechanism.

Authorization remains application/agent policy. The protocol requires resource/task access checks but does not define one universal authorization model.

Therefore:

```text
agent discovered
!=
authenticated caller
!=
authorized task/action
```

### Cancellation

A2A exposes task cancellation as a protocol operation/state transition.

No general transactional rollback guarantee follows from a task becoming `canceled`.

Domain rule remains:

```text
protocol cancellation != external side-effect rollback
```

## Strands relevance

The pinned Strands snapshot currently studied by this domain (`a9361c54...`) uses A2A SDK **0.3.x** in both Python and TypeScript paths:

```text
Python:     a2a-sdk >=0.3.0,<0.4.0
TypeScript: @a2a-js/sdk ^0.3.10
```

That means its A2A implementation must be classified against the **0.3 protocol family**, not silently promoted to current A2A `1.0` compatibility.

Processed comparison: [`../quarries/strands-a2a-version-drift.md`](../quarries/strands-a2a-version-drift.md).

## Promotion boundary

Use `S-112` to:

- pin current A2A protocol semantics;
- detect version drift;
- classify discovery/task/auth/transport/cancellation boundaries;
- pressure-test MK1 protocol fields.

Do not use `S-112` alone to:

- certify a framework implementation as A2A 1.0 compatible;
- certify cross-vendor interoperability;
- infer authorization from Agent Card discovery;
- infer rollback from cancellation;
- infer exactly-once task execution;
- infer production security/SLOs.
