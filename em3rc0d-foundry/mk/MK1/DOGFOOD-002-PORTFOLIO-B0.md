# DOGFOOD-002 — em3rc0d Portfolio B0

Date: 2026-10-07  
Target: `Em3rc0d/em3rc0d-portfolio`  
Mode: **READ-ONLY RECOVERY + DOC-ONLY SAFE SLICE**  
Verdict: **B0 PASS / F1 DOC-SYNC OPEN**

## User constraint

Do **not** touch the user's latest/pre-existing working branch.

Operational interpretation used for this experiment:

- no existing branch is mutated, rebased or force-pushed;
- B0 reads only `main` and current production evidence;
- any mutation must occur on a newly created `foundry/*` branch from stable `main`;
- no merge or production deployment is authorized by B0.

## Exact baseline

```text
repo: Em3rc0d/em3rc0d-portfolio
stable branch: main
main SHA: 514e9acea5ae1692c62ccfd86f0eace7ed886357
production Vercel deployment: dpl_4iTZn73nKAQvLKGsqQCgVSMEfQ6S
production state: READY
deployment git ref: main
deployment git SHA: 514e9acea5ae1692c62ccfd86f0eace7ed886357
production origin: HTTP 200
latest exact-main quality run: 36730970268 / SUCCESS
```

The exact-main quality run executed:

- `npm ci`;
- lockfile reproducibility check;
- Next production build;
- payload budget;
- responsive/accessibility/interaction/scene contracts;
- route/link/metadata/structured-data/share-image release smoke.

## Production posture

Current production and repository source are aligned:

```text
main@514e9ac...
      =
Vercel production source@514e9ac...
      =
latest exact-main quality run source@514e9ac...
```

No runtime defect or deployment drift was observed during B0.

## Drift found

`PROJECT_STATE.md` still represented the original V2 production closeout as if it were current production authority:

```text
bed2449a...
dpl_8NkJD...
```

That evidence remains valid for the original V2 release event, but current production has advanced substantially.

Comparison:

```text
bed2449... → 514e9ac...
46 commits ahead
```

The later production lineage includes material runtime/content evolution such as localized routing, current project identities, cinematic portfolio work and related release checks.

Therefore:

> current production truth had advanced while one current-state document still pointed at historical exact-state authority.

## Earliest invalid node

This project does **not** currently re-enter at product DESIGN, BUILD or runtime TEST.

The first invalid node is:

> **EVIDENCE / CURRENT-STATE SYNCHRONIZATION**

The correct action is not to redesign or rebuild the portfolio.

## Safe F1 slice

A new branch was created from current stable `main`:

`foundry/dogfood002-project-state-sync`

No pre-existing branch was modified.

The slice changes exactly one file:

`PROJECT_STATE.md`

Purpose:

1. point current production authority to `main@514e9ac...`;
2. record current Vercel production deployment;
3. record the exact-main quality run;
4. preserve the original V2 release proof as historical evidence rather than rewriting it;
5. explicitly prevent historical lab metrics from being silently attributed to later production revisions.

Draft PR:

`Em3rc0d/em3rc0d-portfolio#39`

No merge is authorized by this receipt.

## Why this is a useful Foundry pressure test

DOGFOOD-001 tested a degraded release with external dependencies.

DOGFOOD-002 tests the opposite:

- production is healthy;
- code does not need repair;
- historical evidence is valuable;
- current-state documentation drifted.

A Foundry that always responds to stale evidence by changing code would be unsafe.

Expected behavior:

```text
healthy runtime
+ exact current deployment
+ stale current-state document
        ↓
evidence repair only
        ↓
no product mutation
```

## Foundry mechanisms under pressure

Observed useful:

- exact-state evidence;
- historical vs current truth separation;
- earliest-invalid-node routing;
- minimal mutation surface;
- user branch ownership as authority boundary;
- claim <= evidence.

## What this does not prove

- that every current portfolio claim is externally verified;
- that historical V2 lab metrics still hold numerically on current production;
- that the newest/pre-existing feature branches are obsolete or safe to delete;
- that PR #39 should be merged automatically;
- that Foundry reduces recovery time quantitatively.

## Next observation

Wait for PR #39 hosted gates.

If they pass, DOGFOOD-002 has a clean candidate result:

```text
current-state drift
→ one-file evidence repair
→ existing branches untouched
→ runtime unchanged
→ hosted verification green
```

If they fail, investigate the exact failing gate without widening the slice.


## Promotion addendum

The B0 diagnosis was subsequently promoted through bounded slices:

- PR #39 → `d573bf449e077c417ead25a5a80ec35bd036063e`;
- PR #40 → `5a0da2dd633d47530e8d88150428e717584480d6`;
- PR #41 → `c898d743817d0fc6b8d9548444b166810c76ce83`.

Final observed production after the promotion sequence:

- `main@c898d743817d0fc6b8d9548444b166810c76ce83`;
- Vercel `dpl_4r3uvZA3nMbJFfiTXbFzha5pHX3G`;
- state `READY`.

The original B0 baseline remains historical evidence and is not rewritten as though these later promotions had already happened.
