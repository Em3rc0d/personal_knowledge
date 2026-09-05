# OpenShip — Mining Sources

## Primary upstream

| Source | Type | Provenance | Purpose |
|---|---|---|---|
| https://github.com/oblien/openship | Repository | OFFICIAL | Canonical upstream |
| https://github.com/oblien/openship/tree/6510d3fd942473e54b6a41c2b1f99e0f2a483fd6 | Snapshot | OFFICIAL | Pinned study reference |
| https://github.com/oblien/openship/blob/main/README.md | Product/operations docs | OFFICIAL | Product contract and deployment modes |
| https://github.com/oblien/openship/blob/main/SECURITY_GUIDE.md | Security map | OFFICIAL | Trust boundaries and reviewer invariants |
| https://github.com/oblien/openship/blob/main/SECURITY.md | Disclosure policy | OFFICIAL | Security scope |
| https://github.com/oblien/openship/blob/main/package.json | Monorepo manifest | OBSERVED | Toolchain/workspaces |

## Architecture and runtime

- `packages/adapters/src/platform.ts` — platform composition/factory.
- `packages/adapters/src/runtime/docker.ts` — Docker runtime.
- `packages/adapters/src/runtime/bare.ts` — bare runtime.
- `packages/adapters/src/runtime/cloud.ts` — cloud runtime.
- `packages/adapters/src/runtime/deploy-pipeline.ts` — shared deployment lifecycle.
- `packages/adapters/src/types.ts` — shared build/deploy/resource types.
- `packages/core/src/` — pure/shared domain rules.
- `apps/api/src/lib/stack-detector.ts` — stack/package-manager detection.
- `apps/api/src/lib/deployment-runtime.ts` — runtime resolution helpers.

## Remote execution and operations

- `apps/api/src/lib/ssh-manager.ts` — connection authority/pooling.
- `apps/api/src/lib/ssh-tunnel.ts` — tunnel primitives.
- `packages/adapters/src/system/` — executors, checks, installers and system control.
- `packages/db/src/client.ts` — database client / PGlite handling.
- `packages/db/src/pglite-lock.ts` — embedded DB single-instance boundary.
- `apps/api/src/lib/job-runner/` — in-process/BullMQ job execution.

## Edge / routing / TLS

- `packages/adapters/src/infra/nginx.ts` — routing provider.
- `packages/adapters/src/infra/openresty-lua.ts` — OpenResty layout/Lua integration.
- `packages/adapters/src/system/proxy/` — edge detection/provisioning.
- `apps/edge/Dockerfile` — containerized edge.
- `docs/acme.md` — ACME behavior.

## API / MCP / authorization

- `apps/api/src/lib/secure-router.ts` — route metadata/security contract.
- `apps/api/src/lib/permission.ts` and `route-permission.ts` — authorization.
- `apps/api/src/modules/mcp/mcp-tools.ts` — tool generation.
- `apps/api/src/modules/mcp/mcp-server.ts` — MCP server.
- `apps/api/src/modules/mcp/mcp-dispatch.ts` — tool dispatch.
- `apps/api/test/modules/mcp/` — MCP isolation/filter tests.

## CI / release evidence

- `.github/workflows/ci.yml`
- `.github/workflows/release-gate.yml`
- `.github/workflows/release.yml`
- `.github/workflows/docker-images.yml`

## Representative failure evidence

These issues are snapshots of failure modes, not permanent claims about future versions.

- https://github.com/oblien/openship/issues/809 — Compose image-variable interpolation can resolve to an unintended `latest` tag.
- https://github.com/oblien/openship/issues/801 — secret runtime environment divergence reported on v0.6.9.
- https://github.com/oblien/openship/issues/800 — dashboard secret-save behavior reported on v0.6.9.
- https://github.com/oblien/openship/issues/807 — SSH `Unable to exec` transport error classification.
- https://github.com/oblien/openship/issues/700 — edge/project teardown failure path.
- https://github.com/oblien/openship/issues/718 — primary-domain invariant issue.
- https://github.com/oblien/openship/issues/719 — route ordering/tie-break behavior.
- https://github.com/oblien/openship/issues/720 — MCP metadata omission for a route.

## Documentation-drift evidence

`packages/adapters/docs/ARCHITECTURE.md` still contains a Traefik-oriented model in places, while current `platform.ts` composes Nginx/OpenResty/certbot. Treat architecture docs as evidence requiring code cross-check, not as sole authority.
