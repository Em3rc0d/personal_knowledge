# MK1 — A2A Evidence Requirements

Status: **OPEN GATE SPECIFICATION**

## Purpose

Define the minimum evidence required before this domain can represent an A2A integration as a reproducible, revision-aware protocol record rather than a feature claim such as `A2A supported`.

This is an **evidence contract**, not an A2A tutorial and not a security certification.

## Current state

For the current Strands knowledge package:

```text
A2A framework capability          OBSERVED
exact protocol revision           UNKNOWN
implementation/version receipt    OPEN
transport receipt                 OPEN
identity/discovery receipt        OPEN
authentication/authz boundary     OPEN
invocation/task lifecycle         OPEN
cancellation semantics            OPEN
trace continuity                  OPEN
execution interoperability        OPEN
```

The gate remains open until a pinned path is studied.

## Required receipt identity

Every A2A receipt must pin:

```yaml
protocol:
  name: A2A
  specification_revision:
  specification_source:
implementation:
  framework_or_sdk:
  repository:
  snapshot_or_release:
  language:
role:
  client: true | false
  server: true | false
  remote_agent: true | false
observed_date:
```

If the protocol revision cannot be established, the record remains `QUALIFIED/UNKNOWN` and cannot close this gate.

## Required semantic dimensions

### 1. Discovery / identity

Determine what identifies a remote agent and how capabilities are discovered.

Record, where applicable:

- agent/card/descriptor representation;
- endpoint identity;
- capability declaration;
- version or extension negotiation;
- cache/freshness semantics;
- trust assumptions around advertised capabilities.

Do not treat metadata discovery as authorization.

### 2. Transport

Record the actual tested transport/path rather than `network` generically.

Examples of evidence questions:

- HTTP/streaming/SSE/WebSocket/other?
- request-response vs long-lived stream?
- TLS assumptions?
- proxy/gateway boundary?
- timeouts/reconnect behavior?

Only claim what the pinned implementation exercises.

### 3. Authentication and authorization

Separate:

```text
authentication: who/what is the caller?
authorization: is this caller allowed to invoke this agent/action?
```

Record:

- credential/token mechanism;
- credential owner/issuer;
- where verification occurs;
- where action-level authorization occurs;
- whether delegated identity is preserved;
- whether remote agent capability claims influence authorization.

If the test path is unauthenticated, state that directly.

### 4. Invocation / task lifecycle

Reconstruct the protocol lifecycle relevant to work execution:

```text
discover/resolve remote agent
→ create/send request/task
→ intermediate status/messages/artifacts
→ terminal status
→ result/artifact retrieval
```

Identify:

- task/request identifiers;
- terminal states;
- streaming/update semantics;
- retry/resume behavior;
- duplicate request behavior if known;
- how unknown outcome is represented.

### 5. Cancellation

Record:

- how cancellation is requested;
- which component owns it;
- when it becomes effective;
- whether remote work may already have executed;
- whether cancellation is acknowledged;
- what state is terminal afterward;
- whether side-effect rollback is guaranteed.

Default domain rule:

```text
protocol cancellation != transactional rollback
```

Do not weaken it without direct evidence.

### 6. Failure semantics

At minimum pressure-test or inspect:

- unreachable remote agent;
- malformed/unsupported request;
- remote execution error;
- timeout after request dispatch;
- disconnect during streaming;
- duplicate/retried request;
- authorization failure when auth exists;
- remote terminal failure vs unknown outcome.

The record may preserve UNKNOWNs; it must not collapse all failures into a generic exception.

### 7. Observability / trace continuity

If tracing exists, record:

- correlation/request/task ID;
- trace/context propagation mechanism;
- client span;
- remote/server span;
- whether parent/trace continuity is actually tested;
- whether logs/receipts can reconstruct the remote action.

Absence of tracing does not block protocol classification, but it remains an operational qualification.

### 8. Extensions / optional capabilities

Record optional protocol extensions separately from core revision support.

```text
core compatible
!=
every extension supported
```

Each material extension should identify:

- name/revision;
- role;
- execution evidence;
- compatibility assumptions.

## Execution evidence hierarchy

Preferred evidence strength:

```text
independent reproducible fixture
> pinned upstream integration test + execution receipt
> pinned source/test inspection
> official documentation claim
> marketing/feature list
```

MK1 can accept a qualified source-owned CI receipt when independent execution is impossible, provided the limitation is explicit, as done for the current Strands MCP receipt.

## Minimum executable fixture

A useful fixture should exercise at least:

```text
1. discover/resolve remote agent
2. send one deterministic request/task
3. receive terminal result/artifact
4. verify correlation/task identity
5. exercise one failure path
6. exercise cancellation or explicitly show why unavailable
7. record auth mode
8. emit reproducibility receipt
```

Where streaming/task updates are central to the implementation, include at least one intermediate update path.

## Receipt output shape

```yaml
protocols:
  - name: A2A
    revision:
    role:
    transport:
    discovery:
    capabilities: []
    authentication:
    authorization_boundary:
    task_lifecycle:
    cancellation:
    failure_semantics:
    observability:
    extensions: []
    execution_evidence:
      source_snapshot:
      fixture:
      upstream_ci:
      independent_run:
    unknowns: []
```

## Gate pass condition

This MK1 gate passes when one relevant A2A path is sufficiently pinned and classified to demonstrate that the current schema can represent distributed-agent interoperability without reducing it to `A2A=true`.

The gate does **not** require:

- universal A2A compatibility;
- every framework implementation;
- penetration testing;
- production SLOs;
- exactly-once semantics;
- remote side-effect rollback.

Those belong to deployment/project evidence or later MKs.

## Promotion consequence

If the A2A receipt fits the existing protocol schema, no schema change is required.

If a material semantic difference cannot be represented, apply the normal MK1 admission rule before changing the schema:

1. material engineering impact;
2. existing dimensions cannot represent it cleanly;
3. independent evidence/counterexample;
4. no duplicate dimension.

## Expected current target

Strands is the natural first candidate because its current package already records A2A as an unresolved protocol surface. This is a work-order choice, not a claim that Strands defines A2A semantics.
