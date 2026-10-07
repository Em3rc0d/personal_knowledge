# DOGFOOD-001 — Current Work Contract

Status: **F1 ACTIVE · VERCEL WEB SLICE PASS**  
Target repository: `Em3rc0d/Future-Wardrobe`

## Outcome

Resume Future Wardrobe RC1 at the earliest invalid evidence node and close release evidence without reopening already-valid product/design/architecture decisions.

## Exact product base

```text
repo: Em3rc0d/Future-Wardrobe
RC1 branch: astra/release-rc1
RC1 SHA: a80f1aacc4936ce6329f0e71b499d371086be6fa
PR: #8 OPEN / DRAFT
ENGINEERING_READY: NO
RELEASE_READY: NO
```

## Reused state

No current evidence has invalidated:

- product scope;
- durable domain/media/privacy invariants;
- frozen 3D decision;
- production architecture;
- RC1 product plan.

Do not replay those stages unless new evidence contradicts them.

## Current Product Graph position

```text
RESEARCH / FRAME       REUSE
BRAINSTORM             REUSE
DESIGN                 REUSE
ARCHITECTURE           REUSE
PLAN / RC1 SCOPE       REUSE
BUILD                   PARTIAL
TEST / PROVE            ACTIVE
  ├─ Vercel web         PASS / BOUNDED
  ├─ GitHub Actions     PRE_EXECUTION_FAILURE
  ├─ Railway worker     OPEN / STALE
  ├─ Supabase staging   OPEN / CURRENTLY INACTIVE
  └─ mobile/provider    OPEN
INDEPENDENT REVIEW      NOT REACHED
HUMAN PROMOTION         BLOCKED
DELIVER                 BLOCKED
```

## Closed F1 slice — Vercel web

F1 branch:

`foundry/dogfood001-f1-vercel-web`

Final exact SHA:

`f443743eb41226fb799624a146eddf7ceb9aa1f6`

Bounded diff:

- root `vercel.json`;
- root `next@16.3.4` declaration;
- matching root lockfile importer.

Executed result:

- frozen lockfile: PASS;
- build scope: `pnpm --filter @wardrobe/web build`;
- preview: READY;
- root HTTP: 200;
- `/api/health`: 200 / `configured:true`.

Receipt:

`DOGFOOD-001-F1-VERCEL.md`

## Current earliest unresolved execution boundary

> **Railway media-worker exact-RC1 reconciliation**

Known from B0:

- Railway project `future-wardrobe-rc1` exists;
- service `media-worker` exists;
- no current successful live deployment;
- configured source SHA `c7da191...` is behind RC1 `a80f1aa...`;
- historical failed/removed deployments exist.

## Next slice goal

Determine the **smallest safe Railway action** required to prove or reject worker deployability for exact RC1 state.

Before mutation:

1. re-read current Railway service config and latest deployment state;
2. inspect exact RC1 worker Docker/start/health contracts only as needed;
3. identify whether source/config/environment drift, build failure or healthcheck failure is the earliest worker boundary;
4. produce one exact proposed action.

Do not redeploy merely because the service is stale.

## Current authority

Authorized and completed:

- create F1 Vercel test branch;
- perform bounded Vercel-preview mutation;
- execute preview verification.

Not currently authorized:

- Railway redeploy;
- Supabase mutation/restoration;
- production alias/promotion;
- PR #8 merge;
- production release;
- mobile/EAS release.

## Evidence rule

Historical receipts remain valid only for their exact state.

A provider's current state is revalidated before promotion.

A READY web preview does not imply full engineering readiness.

## Non-goals

- redesign Future Wardrobe;
- reopen the stack;
- merge the divergent historical preview branch;
- collapse all release surfaces into one synthetic readiness score.
