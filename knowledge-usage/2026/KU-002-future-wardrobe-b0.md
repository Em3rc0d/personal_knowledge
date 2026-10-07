# KU-002 — Future Wardrobe B0 recovery

Date: 2026-10-07  
Consumer: `EM3RC0D Foundry / DOGFOOD-001`  
Outcome: `PARTIAL`  
Confidence: `high`

## Problem

Recover the exact current state of Future Wardrobe RC1 and identify the earliest incomplete or invalid product node without replaying already-valid product, design or architecture work.

## Knowledge used

| Knowledge | Revision / observation boundary | Reuse type |
|---|---|---|
| `em3rc0d-foundry/mk/MK0/DOGFOOD-001-FUTURE-WARDROBE.md` | main observed 2026-10-07 | experiment / recovery contract |
| `em3rc0d-foundry/architecture/PRODUCT_GRAPH.md` | MK0 candidate | re-entry / stage routing |
| `em3rc0d-foundry/architecture/ARTIFACT_MODEL.md` | MK0 candidate | exact-state / artifact design |
| JEM claim + source discipline | current `personal_knowledge` | evidence boundary |
| `knowledge-usage/` rules | main observed 2026-10-07 | measurement discipline |

## What was reused

Existing knowledge prevented a full project redesign.

The recovery reused:

- the frozen product scope instead of reopening ideation;
- durable domain/media/privacy invariants;
- the existing production architecture unless executable evidence contradicted it;
- the re-entry rule to search for the first invalid node;
- exact-state evidence rules so historical receipts were not confused with current provider health.

The resulting route was:

```text
RESEARCH / FRAME   REUSE
BRAINSTORM         REUSE
DESIGN             REUSE
ARCHITECTURE       REUSE
PLAN / RC1 SCOPE   REUSE
BUILD              PARTIAL
TEST / PROVE       FIRST INVALID NODE
```

## Work avoided

```yaml
rediscovery_avoided:
  - RC1 product definition
  - Level A vs later capability scope
  - 3D product decision
  - core domain/media/privacy invariants
decision_reconstruction_avoided:
  - production architecture selection
  - source-vs-derived media ownership
  - outfit identity semantics
  - release evidence philosophy
research_avoided: "no broad new stack/product research was required to locate the current node"
rework_avoided: "no Future Wardrobe source mutation occurred before external drift was reconciled"
time_saved: UNKNOWN
```

No wall-clock baseline was started at B0 entry, so time saving is not claimed.

## Friction / stale knowledge

B0 still required **43 material source/state surfaces** to obtain trustworthy current state.

Material drift found:

1. Supabase staging was historically `ACTIVE_HEALTHY` but is currently `INACTIVE`.
2. Railway currently has no successful live media-worker deployment and its configured source SHA is behind RC1.
3. Exact RC1 Vercel deployment is `ERROR`; executable logs isolate a monorepo build failure at Expo mobile web export.
4. GitHub Actions exact-RC1 jobs still fail before any workflow step executes.

This demonstrates that repository prose alone is insufficient for operational truth.

## Knowledge returned

DOGFOOD-001 produced:

- `em3rc0d-foundry/mk/MK1/DOGFOOD-001-B0-RECOVERY.md`;
- `em3rc0d-foundry/mk/MK1/DOGFOOD-001-WORK-CONTRACT.md`;
- `em3rc0d-foundry/mk/MK1/DOGFOOD-001-STATE.json`;
- a concrete F1 route: **Vercel web deployment reconciliation**;
- a falsifiable F2 expectation: recover from the compact artifacts before opening deep sources.

It also produced one real reusable-capital candidate:

> a project re-entry state should distinguish historical evidence from current external-provider operational state.

That remains a candidate until more cases support it.

## Evidence

Future Wardrobe observations:

- `main@686160ff6ccca52943b6b39ef787a9efb045be87`;
- `astra/release-rc1@a80f1aacc4936ce6329f0e71b499d371086be6fa`;
- PR #8 OPEN / DRAFT;
- exact RC1 GitHub Actions jobs inspected with no executed steps;
- Vercel exact RC1 deployment ERROR and exact preview branch deployment READY;
- Supabase staging `mcpygkebzetgzauelgjf` currently INACTIVE;
- Railway project `future-wardrobe-rc1` currently lacks a successful live worker.

B0 mutated no Future Wardrobe source or external deployment.

## Interpretation

This receipt supports:

> Existing `personal_knowledge` materially constrained and routed the recovery, reused settled decisions, and caught stale operational claims before mutation.

It does **not** yet support:

- faster recovery than the pre-Foundry baseline;
- a quantified productivity gain;
- validation of the full Product Graph;
- validation of the full Artifact Model;
- Future Wardrobe engineering or release readiness.

The result is therefore `PARTIAL`.

F2 is the meaningful compounding test.

## Disposition

- `KEEP` — earliest-invalid-node re-entry rule.
- `KEEP` — exact-state + historical/current evidence separation.
- `KEEP` — compact Work Contract as F2 input candidate.
- `SIMPLIFY` — F2 should attempt recovery from the compact state before opening the 43 B0 surfaces.
- `AUTOMATE_CANDIDATE` — provider-state reconciliation only if repeated dogfood shows the same burden.
- `NO_CHANGE` — no new global framework or score.
