# Quarry — Security & Trust Boundaries

## Primary trust boundary

`OFFICIAL / OBSERVED`

OpenShip's own security guide identifies `apps/api` and `packages/adapters` as the most security-sensitive surfaces. The dashboard is explicitly treated as a client rather than as an enforcement boundary.

## High-blast-radius capabilities

- Docker socket access on self-hosted Compose installs.
- Root/elevated remote execution over SSH.
- package/system installation;
- edge configuration and port 80/443 control;
- private repository credentials;
- encrypted project secrets;
- deployment-trigger webhooks;
- MCP/automation actions.

Compromise of the control plane can therefore imply compromise of managed workloads/hosts. This is inherent to the product category and must be designed around explicitly.

## Upstream golden invariants

Summarized from `SECURITY_GUIDE.md`:

1. Remote-exec arguments must be shell-quoted through the controlled escaping primitive rather than interpolated raw.
2. Zero-auth behavior must have a single authoritative gate.

Supporting controls observed/documented include:

- SSH private key permissions;
- pinned `known_hosts` / strict host checking;
- credentials encrypted at rest;
- secrets not returned through normal API views;
- HMAC validation of raw webhook bodies;
- route-level permission tags;
- organization scoping;
- cloud-mode floors around host filesystem/local command access.

## Secret storage

`OBSERVED`

Stored secrets use an encrypted envelope based on AES-256-GCM with key material derived from the auth secret. Serialized responses expose presence flags rather than secret values.

## Important failure evidence

Recent issues demonstrate why representation boundaries are critical:

- UI masked secret state can diverge from persisted intent.
- build-time secret values and runtime secret values can diverge if the wrong representation is passed downstream.
- image-variable interpolation can silently resolve to an unintended tag.

## Reusable candidate rules

`INSPIRED`

1. **Masked representation must never be accepted as canonical secret state.**
2. **Transport errors must not be converted into resource-state conclusions.**
3. **Privileged execution should be capability-scoped and auditable.**
4. **Agent access should terminate at an authorized control-plane operation, not at raw root shell access.**
5. **Every value crossing build/runtime/routing boundaries needs one canonical resolved representation and provenance.**

## Open question for MK1

Could a host-side restricted agent replace broad Docker-socket/root-SSH authority while preserving OpenShip's DX? This is an inspired design question, not a claim about upstream direction.
