# DOGFOOD-001 — Future Wardrobe RC1 Recovery and Closure

Status: **ADMITTED FOR MK1 DOGFOOD**
Selected: 2026-09-22
Foundry role: first real EM3RC0D adaptation trial
Target repository: `Em3rc0d/Future-Wardrobe`

## Why Future Wardrobe

Future Wardrobe is intentionally selected over a clean greenfield project for the first Foundry run because it already contains the failure mode the Foundry claims to solve: substantial prior work, multiple artifacts/branches, a live draft release candidate, partial evidence, external environment blockers, visual/product concerns and stale-state risk.

A greenfield project would test planning and generation. Future Wardrobe tests **recovery, exact-state routing, evidence reuse/invalidation and truthful promotion**, which are more diagnostic for MK1.

PocketFinances remains a useful later comparator for greenfield/product-creation behavior. It is not used as DOGFOOD-001.

## Current external identity

Observed through GitHub on 2026-09-22:

- default branch: `main`
- main HEAD: `686160ff6ccca52943b6b39ef787a9efb045be87`
- active RC1 branch: `astra/release-rc1`
- RC1 HEAD: `a80f1aacc4936ce6329f0e71b499d371086be6fa`
- preview branch: `astra/release-rc1-vercel-preview`
- preview HEAD: `84e0f4291b13ddf05eb6c9697c0127edc7b53560`
- open draft PR: #8, “RC1 execution: private wardrobe core, resumable ingestion and real GLB studio”
- PR #8 remains draft and explicitly reports `ENGINEERING_READY=NO` and `RELEASE_READY=NO`.

The PR body is historical evidence, not current truth. Every drift-prone claim must be revalidated before reuse.

## Dogfood mission

Do **not** redesign Future Wardrobe from zero.

The mission is:

> Recover the exact current RC1 state, determine the earliest incomplete or invalidated product node, close only evidence that can actually be closed, and produce a truthful next promotion decision without replaying already-valid work.

The product outcome may legitimately be:

- release candidate ready for human/physical gate;
- blocked by a real external credential/device/provider dependency;
- returned to an earlier design/architecture/build node by new evidence;
- held because the remaining coordination cost exceeds current product value.

“Ship at all costs” is not the objective.

## Foundry mechanisms under test

DOGFOOD-001 tests these candidate mechanisms:

1. **Current-state recovery**
   - repo/branch/PR/deployment/evidence reconciliation;
   - historical prose treated as lead, not truth.

2. **Work Contract + machine manifest**
   - exact source and artifact identity;
   - acceptance/non-goals/invariants;
   - action-specific authority;
   - stage receipts.

3. **Earliest-incomplete re-entry**
   - do not replay closed MK0/RC1 decisions unless evidence invalidates them.

4. **Dependency-aware evidence reuse**
   - preserve prior proof only when state, contract, environment, method revision and dependency cone permit it.

5. **Explicit invalidation**
   - new build/design/runtime evidence reopens only affected downstream nodes.

6. **Conditional gates**
   - visual, resilience, security, performance and device gates run only when their claims/risk trigger them.

7. **Independent final review**
   - builder output is not final promotion evidence.

8. **Exact-action human promotion**
   - local-write, commit, push, PR, merge, release, deployment and external communication remain separate permissions.

9. **Case → reusable-capital disposition**
   - the run ends by deciding what should become a pattern, procedure, reusable primitive, design rule, test/eval, gap or no-change.

## Baseline / comparison

This is a prospective before/after operating comparison, not a claim of randomized causal evaluation.

### Baseline B0 — pre-Foundry recovery burden

Before Foundry-specific artifacts are introduced into Future Wardrobe:

- inventory the current sources required to reconstruct state;
- count materially drift-prone claims that require revalidation;
- record contradictory/stale claims;
- record how many prior artifacts must be opened before a trustworthy next action is known;
- measure elapsed recovery time;
- record repeated decisions/research that had to be reconstructed.

The existing PR body, repo docs, branch topology and historical notes form the baseline workflow.

### Foundry run F1

Use the candidate Product Graph and Artifact Model to:

- produce one compact current Work Contract;
- create exact-state stage receipts;
- route to earliest incomplete node;
- preserve/reject old evidence explicitly;
- finish with one exact next action or truthful external blocker.

### Follow-up F2

At the next separate working session, recover the same project from Foundry artifacts.

Compare against B0:

- time to trustworthy next action;
- number of files/sources needed;
- stale claims detected before mutation;
- repeated decisions avoided;
- evidence reused safely;
- unnecessary stages replayed;
- escaped defects/rework;
- human clarifications required.

## Coordination-cost measurements

Record at minimum:

- recovery elapsed time;
- number of source artifacts opened;
- number of drift-prone claims checked;
- number of stale/contradictory claims found;
- number of stages reused;
- number of stages invalidated;
- number of conditional gates triggered vs skipped;
- number of agent/reviewer passes;
- number of human decisions;
- number of external blockers;
- number of rework loops;
- final exact next action;
- reusable-capital candidates produced.

Do not collapse these into one synthetic score during MK1.

## Success criteria

DOGFOOD-001 is useful if it demonstrates at least one of:

- materially faster F2 recovery than B0;
- a stale claim caught before causing mutation;
- valid prior evidence reused without replay;
- invalid prior evidence rejected because identity/dependency changed;
- a conditional gate catches a real issue without forcing unrelated ceremony;
- a clear authority boundary prevents an unintended external action;
- a reusable asset emerges from real work and survives review.

## Kill / simplify conditions

The candidate Foundry mechanism should be removed, simplified or demoted when:

- maintaining the artifact costs more than reconstructing the state it replaces;
- the same fact must be duplicated manually across multiple “sources of truth”;
- a gate repeatedly produces no decision-relevant evidence;
- a manifest field is never used to route, invalidate, verify or promote;
- agent orchestration adds passes without changing findings/evidence;
- an abstraction cannot explain a real Future Wardrobe transition;
- a reusable asset exists only because the framework wants one.

The Foundry itself is under test.

## Mutation boundary

The first phase is read-only recovery and baseline capture.

No Future Wardrobe source mutation, merge, release, deployment or external communication is implied by selecting the project for dogfood.

Mutation begins only after the recovered Work Contract and exact next stage are explicit and the applicable authority is granted.

## MK relationship

Selecting and instrumenting this trial satisfies MK0 G6.

DOGFOOD-001 execution belongs to MK1 because it is the first pressure test of normalization, work profiles, receipts, authority and invalidation against real work.
