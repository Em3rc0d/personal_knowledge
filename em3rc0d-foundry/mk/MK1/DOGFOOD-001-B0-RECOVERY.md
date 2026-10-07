# DOGFOOD-001 — B0 Recovery Baseline

Date: 2026-10-07  
Target: `Em3rc0d/Future-Wardrobe`  
Mode: **READ-ONLY RECOVERY**  
Verdict: **RECOVERED / NOT RELEASE-READY**

## Baseline question

Can a trustworthy next action be reconstructed from the pre-Foundry Future Wardrobe state without replaying closed product/design/architecture work?

## Exact repository identity

```text
main
686160ff6ccca52943b6b39ef787a9efb045be87

astra/release-rc1
a80f1aacc4936ce6329f0e71b499d371086be6fa

astra/release-rc1-vercel-preview
84e0f4291b13ddf05eb6c9697c0127edc7b53560

PR #8
OPEN / DRAFT
ENGINEERING_READY=NO
RELEASE_READY=NO
```

These identities exactly match the DOGFOOD-001 admission receipt from 2026-09-22. No repository-head drift was observed.

## Material recovery surfaces inspected

B0 required **43 distinct material source/state surfaces** before the trustworthy next action was clear.

They included:

- repository metadata, branches, trees, compare state, commits, issue/PR state;
- current RC1 and preview branch manifests/config;
- release contract/checklist/receipts/runbooks;
- current GitHub Actions runs and job step state;
- current Vercel project, deployments and failing RC1 build log;
- current Supabase project state;
- current Railway project/service/config/deployments.

This count is an observed coordination-cost input, not a quality score.

## Recovery elapsed time

`UNKNOWN`

A wall-clock timer was not started at the beginning of B0. Do not reconstruct a duration after the fact.

This means F2 may compare artifact count and reconstruction burden against B0, but exact elapsed-time comparison is unavailable for this first baseline.

## Historical evidence that remains reusable

### Product / design / architecture

No new evidence invalidated the frozen RC1 product definition or durable invariants.

Reuse:

- Level A Visual Wardrobe Memory scope;
- real interactive 3D requirement;
- exact garment-ID outfit truth;
- private-source / derived-media separation;
- edit vs variation identity semantics;
- Next + Expo + Supabase + worker architecture;
- source-domain/product contracts already captured in MK0/RC1 docs.

Disposition: **REUSE / DO NOT REPLAY**.

### Supabase historical evidence

The 2026-09-10 receipt remains evidence that, at that exact observation boundary:

- migrations applied;
- 12 private tables had RLS enabled;
- buckets were private;
- A/B read isolation passed.

Disposition: **REUSE AS HISTORICAL EXACT-STATE EVIDENCE**, not current operational health.

## Drift / invalidation found

### D1 — Supabase staging state changed

Historical receipt:

`future-wardrobe-rc1-staging = ACTIVE_HEALTHY`

Observed 2026-10-07:

`mcpygkebzetgzauelgjf = INACTIVE`

Impact:

- historical migration/RLS evidence remains valid for its old state;
- hosted continuation gates cannot be treated as currently runnable without restoring/revalidating the staging environment;
- current staging health claim is invalidated.

### D2 — Railway worker is not live and is stale relative to RC1

Observed Railway project:

`future-wardrobe-rc1`

Service:

`media-worker`

Current state:

- latest live-status deployment is FAILED;
- later deployments are REMOVED;
- no current public deployment URL;
- configured source commit is `c7da191...`, behind RC1 head `a80f1aa...`;
- one empty staged environment patch remains visible.

Impact:

`WORKER_DEPLOYMENT_READY = NO`

Historical “trial state” prose is not reused as current diagnosis. Current provider state is the authority.

### D3 — Vercel gives new executable evidence

Current project is linked to `Em3rc0d/Future-Wardrobe`.

Observed:

- production deployment from `main@686160f`: READY;
- exact `astra/release-rc1@a80f1aa`: ERROR;
- `astra/release-rc1-vercel-preview@84e0f42`: READY.

The exact RC1 deployment reached dependency installation and build execution. It failed because the root `pnpm run build` builds the mobile workspace and:

```text
@wardrobe/mobile
expo export --platform all
→ web support requested
→ react-native-web not installed
→ build exit 1
```

The Vercel project UI is configured for Node 24.x, but the repository engine forces Node 22.x during the build. This produced a warning, not the observed build failure.

### D4 — Preview branch contains a reusable deployment mechanism

The READY preview branch contains:

`vercel.json`

that narrows Vercel to:

```text
framework: nextjs
buildCommand: pnpm --filter @wardrobe/web build
outputDirectory: apps/web/.next
```

This is useful evidence that Vercel should build only the web delivery surface.

However the preview branch:

- is historically divergent from RC1;
- contains unrelated code differences;
- uses `pnpm install --no-frozen-lockfile`, which conflicts with the RC1 lockfile discipline.

Therefore:

**DO NOT MERGE THE PREVIEW BRANCH WHOLESALE.**

Mine the minimal deployment mechanism and re-verify it against exact RC1 state.

### D5 — GitHub Actions failure remains pre-execution

For exact RC1 head `a80f1aa...`:

- latest push run: failure;
- latest PR run: failure;
- each contains 14 jobs;
- every inspected job has `steps=[]`.

Therefore the current evidence still supports:

`GITHUB_ACTIONS = PRE_EXECUTION_CI_FAILURE`

It does **not** support application-test failure.

## Product Graph re-entry

```text
RESEARCH / FRAME       REUSE
BRAINSTORM             REUSE
DESIGN                 REUSE
ARCHITECTURE           REUSE
PLAN / RC1 SCOPE       REUSE
BUILD                   PARTIAL / existing implementation
TEST / PROVE            FIRST INVALID NODE
INDEPENDENT REVIEW      NOT REACHED
PACKAGE / EVIDENCE      PARTIAL
HUMAN PROMOTION         BLOCKED
DELIVER                 BLOCKED
```

### Earliest incomplete / invalidated node

> **TEST / PROVE — deployment and environment reproduction boundary**

Do not return to product brainstorming, visual direction or architecture.

## B0 coordination metrics

```yaml
material_source_surfaces_opened: 43
repository_head_drift: 0
drift_prone_state_classes_checked:
  - repository identity
  - PR state
  - CI execution
  - Vercel deployment
  - Supabase staging health
  - Railway worker health
  - deployment configuration
  - preview-vs-RC1 divergence
stale_or_changed_external_states: 3
contradictory_canonical_product_decisions_found: 0
stages_reused: 5
first_partial_stage: BUILD
first_invalid_stage: TEST_PROVE
human_decisions_during_b0: 0
future_wardrobe_mutations_during_b0: 0
rework_loops_during_b0: 0
recovery_elapsed_time: UNKNOWN
```

## B0 verdict

The recovery did **not** need to replay Future Wardrobe product definition, UX design or architecture.

It did require a broad manual reconciliation across repo prose, GitHub, Vercel, Supabase and Railway.

This is exactly the coordination burden F1/F2 must reduce.

## Exact next action

Create a minimal F1 release-reconciliation slice from exact RC1 head.

The first mutation must:

1. preserve all product/domain/architecture decisions;
2. port only the proven **web-only Vercel build boundary** from the preview branch;
3. retain frozen-lockfile discipline rather than copying `--no-frozen-lockfile`;
4. verify a preview built from the exact F1 source identity;
5. record whether the Vercel failure is closed before moving to Railway/Supabase/device gates.

No Future Wardrobe mutation is authorized by this B0 receipt itself.
