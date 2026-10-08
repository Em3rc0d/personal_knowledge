# CONTEXT_ROUTER — Minimal entrypoint for LLMs

Purpose: find the **smallest authoritative evidence** for the current question; do not preload the entire repository.

## Route by question

| Need | Open first | Expand only when necessary |
|---|---|---|
| Engineering process, provenance, gates | `jett-engineering-method/README.md` | `SOURCE-INTAKE-CONTRACT.md`, relevant phase |
| Agent systems / current state | `agent-engineering/STATUS.md` | `LLM_CONTEXT.md`, specific system/MK, then quarry/source |
| Product and repository foundry | `em3rc0d-foundry/LLM_CONTEXT.md` | `STATUS.md`, exact dogfood state |
| Education / knowledge compilation | `knowledge-foundry/LLM_CONTEXT.md` | `STATUS.md`, MK or architecture |
| Web design / UX | `web-design/README.md` / `ux-laws/README.md` | relevant design or test contract |
| Deployment & infra patterns | `openship/README.md` | exact architecture/quarry |
| Programmatic videos | `programmatic-video/STATUS.md` | MK0, source/experiment contract |
| Content and distribution | `content-strategy/STATUS.md` | campaign/test or quarry |
| Observed reuse and context cost | `knowledge-usage/README.md` | receipts or retrieval pilot |

If path/subject is unknown, use filesystem filename/heading search **locally**, not a broad load into model context. Optional deterministic helper: [`knowledge-usage/retrieval/retrieve.py`](./knowledge-usage/retrieval/README.md).

## Stop / expand rules

1. **Answer from the current authority**, not historical quarries. For priority use ROADMAP; for state use STATUS; for system semantics use current system package. Historical sources explain *why*, not necessarily *what is current*.
2. Read **one exact document or intact section at a time**. Carry only the quoted evidence, path, revision/observation date and material UNKNOWNs into the prompt. Do not compress away negations, conditions, permission boundaries, source identity or conflicting evidence.
3. If the question requires proof, freshness, legal/security claims or contradictory evidence, **expand** to the specific quarry, receipt, source, test or live system. Excerpt search results are pointers, not vetted facts.
4. If relevant evidence is missing, contradictory or over budget, say **UNKNOWN / NEEDS_EXPANSION**; never claim resolution from an incomplete excerpt.
5. Reuse known pinned source evidence, but revalidate drift-prone live facts (PRs, releases, deployment status) before a current claim.
6. Keep queries and outputs scoped to the task. Do not call paid models, vector databases or background workers just to find a file.

**Cost evidence:** less Markdown text loaded can reduce potential context burden; only model/provider usage metadata can establish billed-token savings. Keep input/output/cache/tool overhead and answer-quality metrics separate. No numeric saving is promised by this router.

Authority contract: [`README.md`](./README.md) · [`knowledge-usage/retrieval/README.md`](./knowledge-usage/retrieval/README.md).
