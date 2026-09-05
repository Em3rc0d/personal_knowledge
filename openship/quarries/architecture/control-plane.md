# Quarry — Control Plane Architecture

## Observation

`OBSERVED / confidence: high`

OpenShip separates application surfaces from infrastructure execution. Desktop, dashboard, CLI, REST and MCP converge on the same backend/control-plane model rather than each implementing deployment independently.

The adapters package exposes a `Platform` composed from responsibilities rather than from one concrete infrastructure product:

```text
Platform
├── RuntimeAdapter
├── RoutingProvider
├── SslProvider
├── SystemManager | null
├── CommandExecutor | null
└── localHost
```

`createPlatform()` resolves the combination for `cloud`, `selfhosted` or `desktop`.

## Architectural consequence

`INFERRED / confidence: high`

Docker is an implementation detail of one runtime, not the domain model. This reduces infrastructure coupling and allows service code to target contracts such as build/deploy/route instead of Docker-specific operations.

## Monorepo boundaries

Observed top-level applications:

```text
apps/
├── api
├── cli
├── dashboard
├── desktop
├── edge
├── email
└── web
```

Observed shared packages:

```text
packages/
├── adapters
├── core
├── db
├── db-email
├── onboarding
└── ui
```

Important separation:

- `core`: pure/shared decisions and data rules.
- `adapters`: infrastructure/runtime/system integrations.
- `api`: actual trust boundary/orchestration.
- `dashboard`: client; never authoritative for permission enforcement.

## Reusable candidate pattern

`INSPIRED`

**Contract-first control plane**: model workloads, routing, certificates, systems and execution as explicit capabilities, then compose target-specific adapters behind one orchestration layer.

### Applicability

Useful when the product must support more than one execution target or more than one operator surface.

### Failure mode to avoid

A nominal adapter architecture can still leak concrete runtime assumptions through `instanceof`, shell paths, port semantics or edge-specific state. MK1 must map those leaks before this pattern is promoted.
