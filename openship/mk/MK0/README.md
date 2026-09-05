# OpenShip MK0 — Mine & Frame

## Objective

Create a trustworthy baseline of OpenShip's product model, architecture, deployment mechanics, infrastructure adapters, security boundaries, agent interface and operational maturity.

## Pinned reference

```text
repo:    oblien/openship
version: v0.7.0
commit:  6510d3fd942473e54b6a41c2b1f99e0f2a483fd6
```

## Captured in this iteration

- monorepo/application/package map;
- control-plane composition model;
- Docker/Bare/Cloud runtimes;
- deployment overlap/non-overlap semantics;
- readiness vs routing separation;
- SSH as managed transport;
- local embedded vs shared/distributed state model;
- OpenResty/Nginx/TLS edge;
- API authorization and security trust boundaries;
- MCP tool projection;
- CI and release-gate evolution;
- representative real failure modes;
- documentation drift as an explicit caveat.

## Not yet closed

MK0 remains open until the domain has exhaustive critical-file coverage, explicit subsystem contracts, a complete high-blast-radius threat model and a provenance audit.

## Gate rule

```text
NOT ENOUGH:
"we understand the architecture"

REQUIRED:
evidence map
+ source-of-truth map
+ failure boundaries
+ trust boundaries
+ contradictions
+ provenance review
```
