# DOGFOOD-001 — F1 Railway Read-Only Diagnosis

Date: 2026-10-07  
Target: `Em3rc0d/Future-Wardrobe`  
Stage: `TEST / PROVE`  
Boundary: `RAILWAY_MEDIA_WORKER_EXACT_RC1_RECONCILIATION`  
Mode: **READ-ONLY**  
Verdict: **BLOCKED BEFORE REDEPLOY — DEPENDENCY TARGET / AVAILABILITY MUST BE RESOLVED**

## Current Railway identity

```text
project: future-wardrobe-rc1
project_id: 2576649b-944c-437b-bb56-9ecd03a19887
environment: production
environment_id: 50b549ca-dd48-4d42-bd85-7e4a69c91c6b
service: media-worker
service_id: cca16b81-86ee-4b9d-8b90-20d2b01c02e3
state: OFFLINE
```

Current service config:

- repo: `Em3rc0d/Future-Wardrobe`;
- branch: `astra/release-rc1`;
- configured commit: `c7da19173a6f8f7f36f4930f7359e5e61fab7acb`;
- Dockerfile: `services/media-worker/Dockerfile`;
- start command: `services/media-worker/entrypoint.sh`;
- healthcheck: `/ready`;
- healthcheck timeout: 300s;
- region: `sfo`, one replica.

## Correction to B0 wording

B0 called the Railway source SHA stale relative to RC1.

That is true for **repository identity**, but a dependency-cone comparison from `c7da191...` to RC1 `a80f1aa...` shows that the only worker-relevant changed file is:

`services/media-worker/README.md`

No executable worker code, Dockerfile, package manifest, media contract, observability package, root package manifest or lockfile changed in that interval.

Therefore the more precise statement is:

> Railway source identity is behind RC1, but no executable worker-code drift was observed in the inspected dependency cone.

Do not use source age alone as the worker failure diagnosis.

## Historical Railway execution evidence

The historical failed deployment `e837cbff-82bf-44f5-8ba2-770701590ebf` shows:

- Docker build completed;
- `pnpm install --frozen-lockfile` passed;
- media-worker TypeScript build passed;
- image was built and pushed;
- Railway began healthchecking `/ready`;
- repeated readiness attempts failed for the full retry window;
- final result: `1/1 replicas never became healthy` / `Healthcheck failed`.

Therefore:

```text
WORKER_BUILD = HISTORICAL PASS
WORKER_STARTUP_OR_READINESS = HISTORICAL FAIL
```

No deploy/runtime log was available that isolates the exact internal readiness error.

Later `c7da191...` deployments are currently `REMOVED`; their available metadata does not prove that they ever reached healthy runtime.

## Current worker readiness contract

Exact RC1 worker code exposes two distinct health surfaces:

### `/health`

Process liveness.

Returns HTTP 200 while the Node worker health server is running.

### `/ready`

Dependency readiness.

It returns HTTP 200 only after a worker loop successfully:

1. probes the selected background-removal provider;
2. calls Supabase `worker_read`;
3. processes the operational worker path;
4. reaches `ready = true`.

The worker README explicitly states:

> readiness at `/ready` requires both the local background-removal engine and the Supabase worker loop to be operational.

Railway is currently configured to use `/ready`, not `/health`.

This is a deliberate stronger readiness contract, not an accidental endpoint mismatch.

## Current Supabase dependency state

Canonical RC1 staging authority:

`future-wardrobe-rc1-staging / mcpygkebzetgzauelgjf`

Current Supabase provider state:

`INACTIVE`

The deployment runbook orders:

```text
1. verify migrations on isolated staging
2. deploy compatible worker
3. deploy web staging
...
```

Therefore a healthy staging backend is a precondition to a clean worker-readiness proof.

## Railway target identity limitation

Railway confirms that the service has:

- `SUPABASE_URL`;
- a Supabase service/secret-key variable.

However connector access is OAuth-redacted and does not expose the values.

Therefore current evidence cannot prove that Railway's `SUPABASE_URL` points to:

`https://mcpygkebzetgzauelgjf.supabase.co`

This remains **UNKNOWN**.

Do not infer the target from project naming.

## Why redeploy is not the next safe action

A blind redeploy would combine unresolved variables:

- current official staging is INACTIVE;
- actual Railway Supabase target is UNKNOWN;
- historical failure was readiness, not build;
- worker executable code is effectively unchanged since the later configured commit.

That would produce weak evidence: a failure could be dependency availability, target misconfiguration, rembg startup/resource behavior or another readiness cause.

Foundry should not spend a deployment merely to rediscover that ambiguity.

## Exact next action

Before any Railway redeploy:

1. restore or otherwise make the **official Future Wardrobe staging project** `mcpygkebzetgzauelgjf` active;
2. verify the intended Railway `SUPABASE_URL` target is that exact staging project without exposing credentials;
3. only then redeploy the worker from an explicitly pinned source identity;
4. observe both `/health` and `/ready` and capture runtime logs;
5. classify any remaining failure as:
   - process/startup;
   - rembg provider;
   - Supabase/RPC;
   - resource/healthcheck;
   - configuration.

Steps 1–2 require external configuration/mutation authority and are **not executed by this read-only diagnosis**.

## Candidate design question surfaced

Railway currently uses dependency readiness (`/ready`) as its deployment healthcheck.

Possible alternative for later review:

- Railway platform healthcheck → `/health`;
- separate operational monitor → `/ready`.

That could prevent external dependency outages from making a valid process undeployable.

But the existing alerting contract explicitly treats `/ready` unhealthy for five minutes as an operational alert, and one case is insufficient to change the deployment contract.

Disposition: **REVIEW CANDIDATE, NOT A CHANGE**.

## What this proves

- the historical Railway failure was post-build readiness;
- current worker executable drift is not supported as the cause;
- current official Supabase staging is unavailable;
- current Railway Supabase target cannot be verified from redacted connector state;
- redeploying now would not isolate the failure.

## What this does not prove

- that Supabase inactivity caused the historical healthcheck failure;
- that rembg startup was healthy or unhealthy in the failed deployment;
- that current Railway variables are wrong;
- that `/ready` should be replaced as Railway's healthcheck;
- that the worker would pass after staging restoration.
