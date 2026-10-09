# EM3RC0D Foundry — Knowledge Map

## Read this first

- Current state: STATUS.md
- Execution plan: ROADMAP.md
- Authority and provenance: REPOSITORY_CONTRACT.md
- Machine retrieval contract: LLM_CONTEXT.md
- Active experiment: mk/MK1/README.md
- Current DOGFOOD-001 work contract: mk/MK1/DOGFOOD-001-WORK-CONTRACT.md
- Exact re-entry state: mk/MK1/DOGFOOD-001-STATE.json
- B0 recovery evidence: mk/MK1/DOGFOOD-001-B0-RECOVERY.md
- MK0 closure: mk/MK0/GATES.md

## Sources

- mining-site/SOURCES.md — source registry.
- mining-site/S-001-railly-skills.md — exact Railly corpus receipt.
- ../research-corpora/railly-skills-2026-09-22/upstream/ — untouched Railly source snapshot.
- ../research-corpora/em3rc0d-repositories-2026-10-01/ — pinned EM3RC0D repository-estate corpus and reproducible materialization contract.

## Current system synthesis

- systems/README.md — authority boundary for system cards.
- systems/SYSTEM-MAP.md — cross-system capability graph and integration hypotheses.
- systems/SYSTEM-REGISTRY.json — machine-readable system/edge registry.
- systems/*.md — one current source-derived card per repository/system.

System cards are synthesis, not a substitute for their pinned source receipt.

## Railly distillation

quarries/railly-skills/ is ordered by question:

1. 01-system-architecture.md — what the system is.
2. 02-lifecycle-and-routing.md — how work moves.
3. 03-contracts-manifests-and-reentry.md — how state survives sessions and changes.
4. 04-shaping-and-solution-selection.md — how it chooses what deserves implementation.
5. 05-execution-factory.md — how implementation becomes staged evidence.
6. 06-proof-review-and-risk.md — how tests, resilience, security and review work.
7. 07-cases-knowledge-and-learning.md — how work becomes reusable knowledge.
8. 08-evals-governance-and-maturity.md — how procedures earn promotion.
9. 09-runtime-context-and-coordination.md — how agents/runtimes are bounded.
10. 10-design-and-product-output.md — how visual evidence and presentation fit.
11. 11-executable-infrastructure.md — what scripts make the process enforceable.
12. 12-adaptation-matrix.md — keep/adapt/abstract/reject decisions for EM3RC0D.

## EM3RC0D architecture candidates

- architecture/FOUNDRY_MODEL.md
- architecture/PRODUCT_GRAPH.md
- architecture/KNOWLEDGE_GRAPH.md
- architecture/ARTIFACT_MODEL.md

These are GENERATED/INSPIRED during MK0. They are not yet a runtime specification.

## MK0 controls

- mk/MK0/README.md
- mk/MK0/GATES.md
- mk/MK0/UNKNOWNS.md
- mk/MK0/DISTILLATION_LEDGER.md

## MK1 dogfood

- `mk/MK1/README.md` — current experiment router.
- `mk/MK1/DOGFOOD-001-STATE.json` — compact exact state; preferred F2 re-entry surface.
- `mk/MK1/DOGFOOD-001-WORK-CONTRACT.md` — current outcome, boundary, acceptance and authority.
- `mk/MK1/DOGFOOD-001-B0-RECOVERY.md` — deep B0 evidence; open only when provenance/detail is required.
- `mk/MK1/DOGFOOD-001-F1-VERCEL.md` — executed Vercel web slice; exact failure/pass evidence.
- `mk/MK1/DOGFOOD-001-F1-RAILWAY-DIAGNOSIS.md` — current worker readiness/dependency evidence.

## Retrieval rule

Do not load a raw corpus into an ordinary execution context.

Use progressive disclosure:

    current question
      → Knowledge Map
      → system card or relevant quarry
      → source receipt
      → specific pinned upstream file
      → raw run/case only when the claim needs it

Compiled knowledge and active procedure should reduce context, not duplicate the entire evidence corpus.

## UI design contract research (candidate)

- [M3E Canvas evidence study](../web-design/mining-site/m3e-canvas.md) — upstream research, not canon.
- [Design Contract → Foundry](architecture/DESIGN_CONTRACT_TO_FOUNDRY.md) — GENERATED/INSPIRED architecture candidate; no runtime promotion.
