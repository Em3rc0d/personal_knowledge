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

## Railway read-only diagnosis

Receipt:

`DOGFOOD-001-F1-RAILWAY-DIAGNOSIS.md`

Observed:

- Railway service is currently OFFLINE;
- configured source identity `c7da191...` is behind RC1;
- dependency-cone comparison shows no executable worker drift to RC1 — only `services/media-worker/README.md` changed;
- historical worker Docker/package build passed;
- historical deployment failed at `/ready`, not build;
- exact RC1 `/ready` requires both local background-removal readiness and a successful Supabase worker loop;
- canonical Supabase staging `mcpygkebzetgzauelgjf` is currently INACTIVE;
- Railway confirms `SUPABASE_URL` exists but OAuth redaction prevents verifying its value.

Therefore a blind Railway redeploy would not isolate the failure.

## Current earliest unresolved execution boundary

> **Official staging availability + Railway target identity**

## Next slice goal

Before any Railway redeploy:

1. restore/reactivate canonical staging `mcpygkebzetgzauelgjf`;
2. verify Railway targets that exact staging project without exposing credentials;
3. then redeploy from a pinned source identity;
4. capture `/health`, `/ready` and runtime evidence.

Supabase restoration and Railway configuration/redeploy are external mutations and remain authority-gated.

## Current authority

Authorized and completed:

- create F1 Vercel test branch;
- perform bounded Vercel-preview mutation;
- execute preview verification.

Not currently authorized:

- Supabase restoration/reactivation;
- Railway variable/config mutation;
- Railway redeploy;
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
