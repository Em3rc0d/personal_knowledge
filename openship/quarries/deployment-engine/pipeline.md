# Quarry — Deployment Engine

## Shared sequence

`OBSERVED / confidence: high`

The shared deploy pipeline models a lifecycle approximately as:

```text
preflight
  ↓
activate new workload
  ↓
readiness / health gate
  ↓
resolve routing target
  ↓
register/swap route
  ↓
retire previous workload
```

Cancellation is checked around mutating boundaries and the result distinguishes `ready`, `failed` and `cancelled`.

## Overlap path

When old and new workloads can coexist:

```text
OLD keeps serving
      ↓
start NEW
      ↓
health NEW
      ↓
switch route to NEW
      ↓
retire OLD
```

A failure before route switch leaves the previous workload untouched. This supports low/zero-impact rollback semantics.

## Non-overlap path

When old and new contend for a fixed resource such as one host port:

```text
retain+stop OLD
      ↓
start NEW
      ↓
health NEW
      ↓
route NEW
      ↓
retire retained OLD
```

On failure, the new workload must release the contested resource before the previous one is reactivated.

## Readiness vs routing

`OBSERVED / confidence: high`

Workload health is treated as deployment-critical. Routing/TLS failures after a healthy workload can be accumulated as warnings/action-required instead of automatically turning the whole deployment into failure.

## Reusable candidate patterns

`INSPIRED`

1. **Route last, retire last** — do not remove the known-good workload before the replacement passes readiness and can receive traffic when overlap is possible.
2. **Retain before destructive stop** — in non-overlap systems, preserve enough state to restore the old release.
3. **Separate workload truth from edge truth** — an application can be healthy while DNS/TLS/routing needs remediation.
4. **Make rollback semantics explicit in the runtime contract** — rollback must not be an emergent side effect.

## Known risks

- Shared state between build, runtime env, route state and deployment records can diverge.
- Fixed-port deployments cannot provide the same zero-downtime guarantees as isolated/overlap runtimes.
- "best effort" routing requires a strong UI/state model so users do not confuse `ready` with `publicly reachable`.
