# Quarry — Edge, Routing and TLS

## Current observed edge

`OBSERVED / confidence: high`

The current implementation uses Nginx/OpenResty + certbot-oriented infrastructure. Self-hosted Compose can run a containerized OpenResty edge on ports 80/443; remote/legacy paths can reach edge infrastructure through an executor.

Routing is written only after the workload is available/readiness-approved in the main deployment flow.

## Degradation principle

`OBSERVED`

Several edge-host failures are intentionally treated as routing gaps rather than deployment failures. The platform can degrade to a no-op infra provider in cases where the workload can still run but edge configuration cannot be safely reached/applied.

## TLS

Certificates are provisioned through ACME/certbot flows. Domain verification and routing state are distinct from workload runtime state.

## Dynamic edge rules

OpenResty/Lua is used for edge-level behavior such as route rules; database state can be serialized/pushed into edge runtime state without requiring a full reload for every policy change.

## Documentation drift

`OBSERVED`

`packages/adapters/docs/ARCHITECTURE.md` contains older Traefik-oriented descriptions while current platform code uses Nginx/OpenResty/certbot. Code and runtime artifacts therefore outrank stale architecture prose when resolving current behavior.

## Reusable candidate rules

`INSPIRED`

1. Edge health and workload health need separate state machines.
2. An edge failure should fail a deployment only when public reachability is itself a hard deployment contract.
3. Routing configuration should be idempotent and serializable per target when shared files/state are mutated.
4. Documentation of infrastructure providers must be executable/verifiable or continuously checked for drift.
