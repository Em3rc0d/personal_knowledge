# EM3RC0D Foundry — Roadmap

## MK0 — Mine & Frame

Status: **CLOSED 2026-09-22**

Goal: understand the source system completely enough to design our own Foundry without confusing copied implementation with validated principle.

### P0 — Preserve source

Status: PASS.

### P1 — Functional distillation

Status: PASS.

### P2 — Adaptation model

Status: PASS AS CANDIDATE MODEL.

Candidate/generated:

- Product Graph;
- Knowledge Graph;
- Artifact Model;
- authority model;
- exact-state evidence and invalidation;
- reusable-capital model.

### P3 — MK0 closure audit

Status: PASS.

DOGFOOD-001 selects Future Wardrobe RC1 and defines the first adaptation experiment.

## MK1 — Normalize, Classify & Dogfood

Status: **ACTIVE — DOGFOOD-001**

### P0 — DOGFOOD-001 B0 recovery baseline

Status: **PASS / CAPTURED 2026-10-07**

Target: `Em3rc0d/Future-Wardrobe`.

Executed read-only.

Measure:

- current source/artifact inventory;
- recovery time;
- drift-prone claims;
- stale contradictions;
- current exact state;
- earliest incomplete/invalidated node;
- evidence that appears reusable vs stale.

Result:

- repository identities unchanged from admission;
- product/design/architecture reused without replay;
- earliest invalid node = `TEST / PROVE`;
- Supabase staging operational state invalidated (`ACTIVE_HEALTHY → INACTIVE`);
- Railway worker currently not live and configured behind RC1;
- exact RC1 Vercel build failure isolated;
- GitHub Actions pre-execution failure revalidated;
- B0 artifact count = 43 material source/state surfaces;
- elapsed recovery time = `UNKNOWN` because it was not instrumented prospectively.

Artifacts: `mk/MK1/DOGFOOD-001-B0-RECOVERY.md`, `DOGFOOD-001-WORK-CONTRACT.md`, `DOGFOOD-001-STATE.json`.

### P1 — Normalize from real pressure

Status: **IN PROGRESS / MINIMUM STATE MATERIALIZED**

Only normalize schemas required by DOGFOOD-001:

- work/source taxonomy;
- product profile;
- authority levels;
- stage receipt;
- evidence class;
- invalidation/dependency relationship;
- reusable-asset disposition.

Do not normalize fields with no observed consumer.

### P2 — F1 execution

Status: **ACTIVE**

Slice 1 — **Vercel web deployment reconciliation**: **PASS / BOUNDED**.

Evidence:

- final F1 SHA `f443743eb41226fb799624a146eddf7ceb9aa1f6`;
- frozen lockfile PASS;
- web-only build PASS;
- Vercel preview READY;
- root + health endpoint HTTP 200.

Slice 2 — **Railway media-worker exact-RC1 reconciliation**: **READ-ONLY DIAGNOSIS COMPLETE**.

Result:

- no executable worker drift observed between configured SHA and RC1;
- historical build PASS;
- historical readiness FAIL;
- Railway healthcheck `/ready` requires Supabase worker-loop success;
- canonical staging is currently INACTIVE;
- actual Railway Supabase target is UNKNOWN because connector values are redacted.

Slice 3 candidate — **canonical staging reactivation + Railway target verification**: **NEXT / mutation authority pending**.

Do not redeploy the worker until this precondition is resolved.

Run Future Wardrobe from the recovered current node through the minimum justified workflow.

Apply conditional design, security, resilience, visual or device gates only when their claims trigger them.

### P3 — F2 recovery

Start a separate session/cycle from Foundry artifacts.

Compare recovery burden with B0.

### P4 — MK1 verdict

For every candidate mechanism:

- promote;
- revise;
- absorb;
- reject;
- defer.

Close MK1 only when the schema and Product Graph reflect real dogfood rather than S-001 imitation.

## MK2 — Operationalize

Only mechanisms surviving MK1 become code/automation candidates:

- Work Contract + machine manifest;
- deterministic validators;
- receipt writer/invalidation;
- current-state resolver;
- product/knowledge graph projections;
- reusable asset registry;
- eval harness;
- case capture;
- minimum runtime adapter.

Do not build an autonomous control plane.

## MK3 — Integrate

Connect:

- personal_knowledge;
- project repositories;
- design system;
- reusable code/component registries;
- release/deployment surfaces where justified;
- external feedback and usage evidence.

## MK4 — Automate

Only after repeated manual success:

- automatic exact-state routing;
- stale-evidence invalidation;
- artifact generation;
- routine receipt compilation;
- candidate surfacing.

No automatic procedure promotion.

## MK5+ — Certify / Refine

Establish repeated transfer evidence, failure injection, regression suites, external dogfood, product-impact metrics and pruning/deprecation policy.
