# KU-003 — Portfolio production-state synchronization

Date: 2026-10-07  
Consumer: `EM3RC0D Foundry / DOGFOOD-002`  
Outcome: `HELPED`  
Confidence: `high`

## Problem

Continue Foundry dogfood without using over-quota Supabase/Railway infrastructure and without touching the user's latest/pre-existing portfolio branch.

## Knowledge used

| Knowledge | Reuse |
|---|---|
| earliest-invalid-node routing | prevented unnecessary redesign/build work |
| exact-state evidence | aligned current main, Vercel production and CI identity |
| historical/current evidence separation | preserved original V2 release proof without treating it as current |
| authority boundaries | translated “do not touch my latest branch” into no mutation of any existing branch |
| bounded mutation | reduced F1 to one documentation file |

## What was reused

Foundry rules were used to decide **not** to modify product code.

The project was already healthy:

- production source = current `main`;
- Vercel production = READY;
- exact-main hosted quality = SUCCESS;
- production origin = HTTP 200.

The first invalid node was evidence synchronization, not software execution.

## Work avoided

```yaml
product_redesign_avoided: true
runtime_code_change_avoided: true
existing_branch_mutation_avoided: true
new_backend_infrastructure_required: false
supabase_required: false
railway_required: false
time_saved: UNKNOWN
```

## Friction / stale knowledge

`PROJECT_STATE.md` still presented the original V2 release identity `bed2449...` as current production authority even though production had advanced to `514e9ac...`.

Historical release evidence itself was not wrong; its routing as current truth was stale.

## Knowledge returned

DOGFOOD-002 adds evidence for this candidate rule:

> A healthy product can re-enter Foundry at EVIDENCE rather than BUILD; stale current-state documentation should not trigger runtime mutation.

It also strengthens:

> user-owned/pre-existing branches are authority boundaries; create isolated experimental branches instead of borrowing or rewriting them.

These remain observed mechanisms, not universal law from one case.

## Evidence

- portfolio baseline: `main@514e9acea5ae1692c62ccfd86f0eace7ed886357`;
- Vercel production: `dpl_4iTZn73nKAQvLKGsqQCgVSMEfQ6S` READY;
- exact-main quality run: `36730970268` SUCCESS;
- safe branch: `foundry/dogfood002-project-state-sync`;
- F1 head: `afbc85682f4c7285d2b5ce9c1677c07f82661149`;
- draft PR: `Em3rc0d/em3rc0d-portfolio#39`;
- changed files: exactly `PROJECT_STATE.md`.

## Interpretation

This receipt supports that existing knowledge materially constrained the action and prevented unnecessary source/runtime changes.

It does not yet prove faster recovery quantitatively.

## Disposition

- `KEEP` — earliest-invalid-node routing.
- `KEEP` — historical/current evidence separation.
- `KEEP` — branch ownership/authority boundary.
- `KEEP` — minimal mutation rule.
- `NO_CHANGE` — no new framework or automation.


## Promotion addendum

The final PR #39 head was `f7deb278377ba7e57eb23bd425e787262ad44ccb`, with Portfolio CI `37697919701` PASS and V2 Experience Quality `37697919696` PASS.

It was promoted as squash commit `d573bf449e077c417ead25a5a80ec35bd036063e`.

Promotion did not require runtime source changes.
