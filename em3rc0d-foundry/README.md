# EM3RC0D Foundry

Status: **MK0 — Mine & Frame / active**

EM3RC0D Foundry is the operating system for turning evidence, design intelligence, reusable engineering assets and product work into a compounding product factory.

Its goal is not to maximize repositories, prompts, agent calls or lines of code. Its goal is to maximize **valuable product throughput** while preserving evidence, quality, reversibility and human authority.

## Founding source

The first external corpus is the exact snapshot of Railly/skills at commit 77fdde3e8d7e13b7c27c7660f7c15619839e38af, preserved at:

research-corpora/railly-skills-2026-09-22/upstream/

The raw snapshot is evidence, not EM3RC0D canon. This domain distills mechanisms from that corpus and combines them with the existing Jett Engineering Method, MK lifecycle, mining-site/quarry model, design provenance and product-validation discipline.

## Core thesis

A product factory compounds when the next product does not pay again for decisions already solved.

The target relation is:

    new product
    = reusable capital
    + domain-specific delta
    + current evidence

Reusable capital may be a procedure, code primitive, component, product shell, design rule, architecture pattern, test harness, deployment recipe, evaluation, or research method.

## Two coupled loops

### Product loop

    opportunity / problem / request
      → intake
      → research + frame
      → brainstorm
      → design
      → architecture
      → plan / slice
      → build
      → test + prove
      → independent review
      → package
      → human promotion
      → deliver
      → observe
      → record case

The loop resumes at the **earliest incomplete or invalidated state**. It does not replay completed phases merely because a new session starts.

### Knowledge loop

    source / real work
      → evidence
      → quarry / case
      → candidate lesson
      → pattern or reusable asset candidate
      → evaluation
      → human promotion
      → reusable capital
      → next product

A completed product must improve either the market evidence or the factory. Preferably both.

## Non-negotiable boundaries

- Raw evidence is not canon.
- A generated proposal is not a decision.
- A green test is not proof that the test can detect the defect.
- Delivery, technical verification and human judgment are independent.
- A builder is not the final reviewer of its own work.
- Installed runtime procedures must not silently become write destinations for Foundry knowledge.
- Telemetry and invocation counts are adoption signals, not evidence of quality.
- Missing evidence remains UNKNOWN.
- External side effects require authority for that exact action.
- A reusable asset is promoted only when the evidence justifies its maintenance cost.
- The smallest durable reusable outcome wins; a new skill or abstraction is not the default.

## Current MK0 mission

MK0 is not building a production Foundry runtime yet.

It is:

1. preserving the source corpus exactly;
2. decomposing Railly/skills by functional surface;
3. extracting mechanisms, boundaries, failure lessons and executable invariants;
4. separating portable principles from Railly/Vercel-specific implementation choices;
5. defining the first EM3RC0D Foundry architecture as GENERATED/INSPIRED knowledge;
6. leaving operational promotion blocked until real EM3RC0D dogfood evidence exists.

See:

- KNOWLEDGE_MAP.md
- REPOSITORY_CONTRACT.md
- STATUS.md
- ROADMAP.md
- mining-site/S-001-railly-skills.md
- quarries/railly-skills/
- architecture/
- mk/MK0/
