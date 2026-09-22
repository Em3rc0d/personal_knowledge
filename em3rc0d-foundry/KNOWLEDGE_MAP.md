# EM3RC0D Foundry — Knowledge Map

## Read this first

- Current state: STATUS.md
- Execution plan: ROADMAP.md
- Authority and provenance: REPOSITORY_CONTRACT.md
- Machine retrieval contract: LLM_CONTEXT.md
- MK0 closure: mk/MK0/GATES.md

## Source

- mining-site/SOURCES.md — source registry.
- mining-site/S-001-railly-skills.md — exact Railly corpus receipt.
- ../research-corpora/railly-skills-2026-09-22/upstream/ — untouched source snapshot.

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

## Retrieval rule

Do not load the raw 1,323-file corpus into an ordinary execution context.

Use progressive disclosure:

    current question
      → Knowledge Map
      → relevant quarry
      → specific upstream file
      → raw run/case only when the claim needs it

This is itself one of the portable mechanisms learned from the source: compiled knowledge and active procedure should reduce context, not duplicate the entire evidence corpus.
