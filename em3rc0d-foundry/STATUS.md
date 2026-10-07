# EM3RC0D Foundry — Status

Updated: 2026-10-07
State: **MK0 CLOSED · MK1 ACTIVE / MULTI-DOGFOOD**

## Current truth

| Surface | State |
|---|---|
| Railly/skills raw snapshot | PASS — exact upstream tree preserved |
| Upstream provenance and MIT license | PASS |
| Core Foundry governance | DISTILLED |
| Initial EM3RC0D Foundry model | GENERATED / under dogfood |
| MK0 closure | PASS |
| DOGFOOD-001 target | Future Wardrobe RC1 |
| B0 read-only recovery | PASS / CAPTURED |
| B0 Work Contract | CAPTURED |
| B0 machine state | CAPTURED / candidate schema |
| Earliest invalid node | TEST / PROVE — deployment/environment reproduction |
| F1 Vercel web slice | PASS / BOUNDED |
| F1 branch | `foundry/dogfood001-f1-vercel-web@f443743...` |
| Railway read-only diagnosis | COMPLETE |
| Railway executable drift | NONE OBSERVED — README-only since configured SHA |
| Historical worker build | PASS |
| Historical worker readiness | FAIL |
| Current canonical Supabase staging | INACTIVE |
| Railway Supabase target | UNKNOWN — OAuth-redacted |
| Next F1 boundary | Reactivate canonical staging + verify Railway target identity |
| Supabase/Railway mutation authority | PENDING |
| F2 recovery comparison | BLOCKED BY F1 |
| DOGFOOD-001 execution | HOLD — Supabase/Railway over quota / staging inactive |
| DOGFOOD-002 target | em3rc0d-portfolio |
| DOGFOOD-002 B0 | PASS |
| DOGFOOD-002 earliest invalid node | EVIDENCE / CURRENT-STATE SYNCHRONIZATION |
| DOGFOOD-002 safe branch | `foundry/dogfood002-project-state-sync` |
| DOGFOOD-002 runtime mutation | NONE |
| DOGFOOD-002 hosted gates | Portfolio CI PASS · V2 Experience Quality PASS |
| DOGFOOD-002 PR #39 | MERGED → `d573bf449...` |
| DOGFOOD-002 F2 compact re-entry | PASS / BOUNDED |
| DOGFOOD-002 F3 claim audit | PASS / 2 KEEP · 1 CORRECT |
| Portfolio PR #39 | MERGED · exact-head gates PASS |
| Portfolio PR #40 | MERGED → `5a0da2dd...` · rebased exact-head gates PASS |
| Portfolio PR #41 | MERGED → `c898d743...` · snapshot-safe authority model |
| DOGFOOD-002 production | `main@c898d743...` · Vercel `dpl_4r3uv...` READY |
| DOGFOOD-002 state | PROMOTED / BOUNDED COMPLETE |
| DOGFOOD-002 next boundary | NONE until new evidence or fresh timed recovery |
| MK1 verdict | OPEN |

## DOGFOOD-001 exact source state

Observed 2026-10-07:

- Future Wardrobe `main`: `686160ff6ccca52943b6b39ef787a9efb045be87`
- RC1: `astra/release-rc1@a80f1aacc4936ce6329f0e71b499d371086be6fa`
- preview: `astra/release-rc1-vercel-preview@84e0f4291b13ddf05eb6c9697c0127edc7b53560`
- PR #8 remains OPEN / DRAFT;
- `ENGINEERING_READY=NO`;
- `RELEASE_READY=NO`.

These repository identities are unchanged from DOGFOOD admission.

## B0 current-state findings

### Reused without replay

No current evidence invalidated the frozen product definition, durable domain invariants, RC1 scope or production architecture.

Therefore:

```text
RESEARCH / FRAME   REUSE
BRAINSTORM         REUSE
DESIGN             REUSE
ARCHITECTURE       REUSE
PLAN / RC1 SCOPE   REUSE
BUILD              PARTIAL
TEST / PROVE       FIRST INVALID NODE
```

### GitHub Actions

Exact RC1 head was rechecked.

Latest push and PR quality runs each expose 14 failed jobs with no executed workflow steps.

Current interpretation:

`PRE_EXECUTION_CI_FAILURE`

This is not application-test failure and is not a PASS.

### Vercel

Current evidence:

- `main@686160f...` production deployment: READY;
- exact `RC1@a80f1aa...`: ERROR;
- exact preview branch `84e0f42...`: READY.

The exact RC1 Vercel build reaches package installation/build and fails when the root Turbo build invokes Expo mobile web export without `react-native-web`.

The READY preview branch contains a useful web-only Vercel build boundary, but the branch is materially divergent and must not be merged wholesale.

### Supabase

Historical staging receipt observed `ACTIVE_HEALTHY`.

Current connector state for `future-wardrobe-rc1-staging` / `mcpygkebzetgzauelgjf` is:

`INACTIVE`

Historical migration/RLS evidence remains historical exact-state evidence; current staging-operational readiness is invalidated.

### Railway

Current project/service exist, but:

- no successful current worker deployment is live;
- latest live-status deployment is FAILED;
- later deployments are REMOVED;
- service config references `c7da191...`, behind exact RC1 `a80f1aa...`.

Current interpretation:

`WORKER_DEPLOYMENT_READY=NO`

## Baseline coordination evidence

B0 required reconciliation across **43 material source/state surfaces**.

```yaml
material_source_surfaces_opened: 43
recovery_elapsed_time: UNKNOWN
future_wardrobe_mutations: 0
rework_loops: 0
human_decisions_during_b0: 0
```

Elapsed recovery time was not instrumented from the beginning and will not be invented retroactively.

## F1 Vercel slice result

The first F1 slice passed on exact state:

- branch: `foundry/dogfood001-f1-vercel-web`;
- SHA: `f443743eb41226fb799624a146eddf7ceb9aa1f6`;
- Vercel deployment: `dpl_HQ4CNiL9d9kg5guGesUg2Pta7DJY`;
- final state: `READY`;
- `pnpm install --frozen-lockfile`: PASS;
- build scope: `@wardrobe/web` only;
- root HTTP: 200;
- `/api/health`: 200 / configured=true.

Two intermediate failures were preserved as evidence: missing root Next identity, then a deliberate frozen-lockfile rejection after package metadata changed without its lock importer.

Receipt: `mk/MK1/DOGFOOD-001-F1-VERCEL.md`.

## Exact next action

F1 remains in `TEST / PROVE`.

The Railway boundary has now been diagnosed read-only.

Key result:

- configured Railway source SHA is behind RC1 by identity, but no executable worker-code drift was found;
- historical worker build passed;
- historical failure occurred at `/ready`;
- `/ready` deliberately depends on local background removal **and** the Supabase worker loop;
- canonical staging `mcpygkebzetgzauelgjf` is currently INACTIVE;
- current Railway `SUPABASE_URL` value cannot be verified because connector access is redacted.

The next unresolved boundary is therefore:

> **Reactivate canonical Supabase staging + verify Railway target identity before redeploy**

No merge, production alias, Railway redeploy, Supabase mutation, mobile release or product redesign is currently implied.

## Active artifacts

- `mk/MK0/DOGFOOD-001-FUTURE-WARDROBE.md` — experiment contract.
- `mk/MK1/README.md` — active MK1 experiment router.
- `mk/MK1/DOGFOOD-001-B0-RECOVERY.md` — baseline receipt.
- `mk/MK1/DOGFOOD-001-WORK-CONTRACT.md` — compact re-entry contract.
- `mk/MK1/DOGFOOD-001-STATE.json` — machine-readable exact state.
- `mk/MK1/DOGFOOD-001-F1-VERCEL.md` — bounded Vercel execution receipt.
- `mk/MK1/DOGFOOD-001-F1-RAILWAY-DIAGNOSIS.md` — read-only worker/dependency diagnosis.

## What is not claimed

- Foundry compounding is not yet demonstrated.
- B0 does not prove faster recovery.
- Future Wardrobe is not engineering-ready or release-ready.
- The Product Graph and Artifact Model are still candidates under pressure.
- F1 Vercel source mutation is bounded and verified; this does not promote full RC1 readiness.
- F2 is the first direct recovery-burden comparison against the new artifacts.


## DOGFOOD-002 — em3rc0d Portfolio

User constraint: do not touch the latest/pre-existing portfolio branch.

Implemented authority boundary:

- no existing portfolio branch mutated;
- baseline read from stable `main@514e9acea5ae1692c62ccfd86f0eace7ed886357`;
- current Vercel production is READY on the same SHA;
- exact-main V2 Experience Quality run `36730970268` is SUCCESS;
- production origin re-observed HTTP 200.

B0 found no runtime defect. The first invalid node was stale current-state evidence: `PROJECT_STATE.md` still pointed at the original V2 release identity `bed2449...` as current production authority.

An isolated branch `foundry/dogfood002-project-state-sync` changed only `PROJECT_STATE.md`. PR #39 passed exact-head gates and was promoted as squash commit `d573bf449e077c417ead25a5a80ec35bd036063e`.

This experiment specifically tests whether Foundry can choose **evidence repair instead of code change** when runtime truth is already healthy.


## DOGFOOD-002 F2 — compact re-entry

F2 was executed as an **artifact sufficiency check**, not as a fabricated independent-session timing benchmark.

Using the compact DOGFOOD-002 state plus current PR/check status was sufficient to recover:

- exact baseline/main identity;
- safe isolated branch;
- one-file mutation surface;
- both hosted gates PASS;
- PR #39 READY FOR REVIEW / MERGEABLE;
- runtime unchanged;
- merge authority still absent.

No product/design/runtime history needed to be reopened to determine the next safe action.

Current boundary:

> **Human review / promotion of PR #39**

This is a valid stop condition. Foundry must not invent another implementation task simply because a bounded slice is green.


## DOGFOOD-002 F3 — public flagship claim audit

The current runtime flagships were checked against current source/project truth.

### PlacaClara

`KEEP`

Fresh Vercel evidence shows production `READY` on exact current `main@9f6797c...`, so an older operational document saying SEO/funnel promotion was pending is stale and does not justify downgrading the current public claim.

### AutoPulse

`KEEP`

The portfolio's bounded field-tested/R&D language remains below the current AutoPulse evidence ceiling. Public v1 is still explicitly uncertified.

### ECHO

`CORRECT`

Portfolio wording overstated current execution by calling the MVP/replay runtime active.

Canonical ECHO state currently has corpus readiness fail-closed, `modeling_allowed=false`, Benchmark A/B/C locked, and replay/real-camera progression blocked until corpus certification.

Portfolio PR #40 corrected only `src/content/systems/echo.ts`.

After PR #39, it was rebased rather than inheriting old green status.

Final exact head:

`82d52ae1a5eaead9f80cfb739bd7164ac1131bef`

Fresh hosted gates:

- Portfolio CI `37700040054` — PASS;
- V2 Experience Quality `37700040031` — PASS.

It was promoted as squash commit `5a0da2dd633d47530e8d88150428e717584480d6`.

## DOGFOOD-002 promotion feedback

Promotion exposed one additional evidence defect: an exact SHA labeled permanent **current production authority** inside `PROJECT_STATE.md` invalidated itself when the documentation merge changed `main` and Vercel deployed the new head.

PR #41 corrected the authority model:

- current source authority = actual GitHub `main`;
- current deployment authority = latest Vercel `target=production` deployment from `main`;
- embedded SHAs/deployment IDs = bounded observations, not perpetual aliases.

PR #41 exact head `210d0937a5b3190bd7092f9dec5b812fc247ad09` passed Portfolio CI `37700520889` and V2 Experience Quality `37700520851`, then merged as `c898d743817d0fc6b8d9548444b166810c76ce83`.

Final observed production after DOGFOOD-002 promotion:

- portfolio `main@c898d743817d0fc6b8d9548444b166810c76ce83`;
- Vercel production `dpl_4r3uvZA3nMbJFfiTXbFzha5pHX3G`;
- state `READY`;
- deployment Git SHA exactly `c898d743...`.

## DOGFOOD-002 stop condition

DOGFOOD-002 is **PROMOTED / BOUNDED COMPLETE**.

No additional implementation slice is currently justified. The next meaningful test is a genuinely fresh, prospectively timed recovery. Until then Foundry should stop rather than manufacture more work.
