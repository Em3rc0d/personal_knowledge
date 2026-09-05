# OpenShip Quarries

Quarries contain extracted evidence and structured observations from the pinned OpenShip snapshot.

They are **not automatically canonical patterns**. Promotion path:

```text
quarry observation
  → contradiction / boundary review
  → normalized concept
  → reusable rule
  → testable contract
```

## Current quarry families

- `architecture/` — control-plane and package boundaries.
- `deployment-engine/` — sequencing, readiness, rollback and cancellation.
- `runtimes/` — Docker/Bare/Cloud abstraction.
- `operations/` — SSH, embedded/remote state and queues.
- `edge/` — routing, OpenResty, TLS and degradation.
- `security/` — trust boundaries, secrets and high-blast-radius actions.
- `mcp/` — agent-facing tools and authorization.
- `ci-cd/` — tests, release gates and operational learning.
