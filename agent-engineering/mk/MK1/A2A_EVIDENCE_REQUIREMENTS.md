# MK1 — A2A Evidence Requirements

Status: **GATE SATISFIED / QUALIFIED FOR PINNED STRANDS 0.3 PATH**  
Current receipt: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md)

## Purpose

Define the minimum evidence required before this domain may represent an A2A integration as a revision-aware protocol record rather than a feature claim such as `A2A supported`.

This remains a reusable **evidence contract**, not an A2A tutorial and not a security certification.

## Current gate result

For the pinned Strands snapshot:

```text
Strands snapshot                  a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
Python A2A dependency             >=0.3.0,<0.4.0
TypeScript A2A dependency         ^0.3.10
implementation protocol family    0.3
current official A2A family       1.0
client/server roles               established
Agent Card/discovery              established
invoke/stream/task shape          established
state/concurrency boundary        established / qualified
security/auth boundary            established / qualified
integration fixture source        present
integration workflow scope        present
specific successful A2A CI run    NOT VERIFIED
independent execution             NOT RUN
A2A 1.0 compatibility             NOT ESTABLISHED
MK1 classification-shape gate     PASS / QUALIFIED
```

The gate is satisfied because the current MK1 protocol model can faithfully represent both **what is supported** and **what is not proven** without collapsing to `A2A=true`.

A2A `1.0` migration/interoperability remains explicit system-version/freshness debt. It must not be reported as current compatibility until new evidence exists.

## Required receipt identity

Every future A2A receipt must pin:

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

If protocol revision cannot be established, the record remains `QUALIFIED/UNKNOWN` and cannot satisfy this evidence contract.

## Required semantic dimensions

### 1. Discovery / identity

Record, where applicable:

- Agent Card/descriptor representation;
- endpoint identity;
- capability declaration;
- version or extension negotiation;
- cache/freshness semantics;
- trust assumptions around advertised capabilities.

Metadata discovery is not authorization.

### 2. Transport

Record the actual implementation path, including where known:

- binding/transport;
- request-response vs streaming behavior;
- TLS/proxy/gateway assumptions;
- timeouts/reconnect behavior.

Only claim what the pinned implementation supports/evidences.

### 3. Authentication and authorization

Separate:

```text
authentication: who/what is the caller?
authorization: is this caller allowed to invoke this agent/action?
```

Record credential mechanism, verification boundary, action authorization and delegated identity behavior where evidenced.

An isolation/correlation key such as `context_id` must not be treated as authenticated identity unless the security layer explicitly binds it.

### 4. Invocation / task lifecycle

Reconstruct the relevant lifecycle:

```text
discover/resolve remote agent
→ create/send request/task
→ intermediate status/messages/artifacts
→ terminal/interrupted state
→ result/artifact retrieval
```

Identify task/request IDs, streaming semantics, terminal states, retry/resume behavior and unknown outcomes where known.

### 5. Cancellation

Record how cancellation is requested, which component owns it, when it becomes effective and what terminal state follows.

Default invariant:

```text
protocol cancellation != transactional rollback
```

Do not weaken this without direct evidence.

### 6. Failure semantics

Inspect/pressure-test relevant cases such as:

- unreachable remote agent;
- malformed/unsupported request;
- remote execution error;
- timeout after dispatch;
- disconnect during streaming;
- duplicate/retried request;
- authentication/authorization failure;
- terminal failure vs unknown outcome.

UNKNOWNs are valid; collapsing all failures into one generic exception is not.

### 7. Observability / trace continuity

If tracing exists, record correlation/task IDs, context propagation and whether client/server trace continuity is actually tested.

Absence of tracing does not block classification, but remains an operational qualification.

### 8. Extensions / optional capabilities

Record optional extensions separately from core revision support:

```text
core protocol support != every extension supported
```

## Execution evidence hierarchy

```text
independent reproducible fixture
> pinned upstream integration test + execution receipt
> pinned source/test inspection
> official documentation claim
> marketing/feature list
```

Crucially:

```text
fixture exists
!=
fixture lies in CI scope
!=
specific CI run passed
!=
independent reproduction passed
```

The current Strands receipt preserves those levels separately.

## Minimum executable fixture for stronger future receipts

A stronger execution receipt should exercise at least:

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

Where streaming/task updates are material, include an intermediate update path.

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

## Gate pass semantics

The MK1 gate passes when one relevant A2A path is sufficiently pinned/classified to prove the current schema can represent distributed-agent interoperability without reducing it to `A2A=true`.

The current Strands 0.3 receipt satisfies that requirement **in qualified form**.

The gate does not require:

- universal A2A compatibility;
- current/future revision compatibility without evidence;
- every framework implementation;
- penetration testing;
- production SLOs;
- exactly-once semantics;
- remote side-effect rollback.

## Current non-claim

Do not infer:

```text
MK1 A2A gate PASS / QUALIFIED
→ Strands A2A 1.0 compatible
```

The latter remains **NOT ESTABLISHED**.

## Promotion consequence

The current receipt fits existing protocol semantics, so no framework-specific or A2A-specific top-level dimension is required.

If a future A2A revision exposes a material distinction the frozen schema cannot represent, apply the normal MK1/revision-reopen discipline rather than silently patching downstream MK2 artifacts.
