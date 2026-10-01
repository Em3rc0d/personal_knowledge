# EM3RC0D Foundry — Status

Updated: 2026-09-22
State: **MK0 CLOSED · MK1 DOGFOOD ADMITTED**

## Current truth

| Surface | State |
|---|---|
| Railly/skills raw snapshot | PASS — exact upstream tree preserved |
| Upstream provenance and MIT license | PASS |
| Repository structural inventory | PASS |
| Core Foundry governance | DISTILLED |
| 20 registered skill contracts | DISTILLED by functional family |
| Eval/trigger contracts | DISTILLED |
| Promotion rounds and lifecycle history | DISTILLED |
| Compiled knowledge layer | DISTILLED |
| Work-item manifest / exact-state machinery | DISTILLED |
| Review gate catalog | DISTILLED at architecture/rule-family level |
| Cases corpus | INVENTORIED + representative lessons traced |
| Run corpus | INVENTORIED by run family; not every historical run re-narrated |
| Railly-specific runtime dependencies | SEPARATED from portable mechanisms |
| Initial EM3RC0D Foundry model | GENERATED / not validated |
| First real EM3RC0D dogfood | FUTURE WARDROBE RC1 selected |
| MK0 closure | PASS |
| MK1 execution | READY TO START |

## Corpus identity

Source: Railly/skills
Commit: 77fdde3e8d7e13b7c27c7660f7c15619839e38af
Root tree: 701944bade5f718381446a7cd9224ed01ea1f952
Raw snapshot: ../research-corpora/railly-skills-2026-09-22/upstream/

## DOGFOOD-001

Target: `Em3rc0d/Future-Wardrobe`.

Observed GitHub state at admission:

- `main`: `686160ff6ccca52943b6b39ef787a9efb045be87`
- `astra/release-rc1`: `a80f1aacc4936ce6329f0e71b499d371086be6fa`
- `astra/release-rc1-vercel-preview`: `84e0f4291b13ddf05eb6c9697c0127edc7b53560`
- draft PR #8 remains open;
- PR body explicitly says `ENGINEERING_READY=NO` and `RELEASE_READY=NO`.

The selection does not grant mutation or release authority. First phase is read-only recovery and B0 baseline capture.

Dogfood contract: `mk/MK0/DOGFOOD-001-FUTURE-WARDROBE.md`.

## Why Future Wardrobe first

The first test should stress the claims that distinguish a Foundry from a template generator:

- recover a complex existing project;
- distinguish historical prose from current state;
- resume at the earliest valid node;
- reuse or invalidate exact-state evidence;
- route conditional risk/design gates;
- preserve human promotion boundaries.

PocketFinances remains useful as a later greenfield comparison after the recovery-oriented mechanisms survive DOGFOOD-001.

## What is not claimed

MK0 closure means the research/frame package is sufficient to run an experiment.

It does **not** mean:

- the Foundry architecture is validated;
- the Product Graph is final;
- all proposed artifacts are worth their cost;
- Future Wardrobe is engineering- or release-ready;
- Railly maturity transfers to EM3RC0D.

MK1 exists to falsify those assumptions on real work.
