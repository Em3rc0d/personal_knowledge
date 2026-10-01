# S-114 — midudev/mcp-higgsfield-landing

Status: **REGISTERED / OBSERVED**  
Observed: **2026-10-01**

## Source identity

| Field | Value |
|---|---|
| ID | `S-114` |
| System | Arko landing / Higgsfield MCP workflow |
| Type | public GitHub repository / worked multimodal agent workflow |
| Repository | https://github.com/midudev/mcp-higgsfield-landing |
| Repository snapshot observed | `31b75c6f4aa068ef32c9e92dd30b9910b3118e66` |
| Primary artifact | Astro landing with AI-generated walkthrough media |
| Generator path | Claude Code + Higgsfield MCP + Kling 3.0, as described by the repository |
| Runtime stack | Astro 7, Tailwind CSS 4, GSAP ScrollTrigger, Lenis, sharp |
| Deployment | static assets through Cloudflare Workers |
| License signal | no root license file was visible in the observed repository root |
| Use here | reproducible agent-workflow, artifact-provenance and evidence-cost pressure test |
| Authority | source-specific implementation evidence; not an authoritative general agent standard |

## Evidence inspected

- `README.md` and `PROMPTS.md`;
- `.agents/skills/landing-page-design/SKILL.md`;
- `src/scripts/world.ts`, `Stage.astro`, `Stop.astro` and `src/data/arko.ts`;
- `package.json`, `wrangler.jsonc` and generated video asset metadata.

Observed media sizes:

- desktop walkthrough `recorrido.mp4`: 12,207,386 bytes;
- mobile walkthrough `recorrido-m.mp4`: 5,854,836 bytes;
- cinemagraph `0.mp4`: 614,780 bytes;
- cinemagraph `5.mp4`: 567,779 bytes.

## Core observations

### 1. MCP is a build-time capability, not the production product

The repository uses Higgsfield through MCP to generate media during construction. The deployed experience consumes ordinary static media assets.

    generative capability
          ↓
    materialized artifact
          ↓
    deterministic web runtime

This isolates production availability, latency and per-visitor cost from the generative provider when content does not need to be generated per request.

### 2. Durable skill and execution recipe are separated

The repository distinguishes a reusable design skill, project-specific prompts, MCP/tool capability, generated artifacts and deterministic product code.

Useful normalization:

    SKILL            = reusable policy / durable know-how
    EXECUTION RECIPE = task-specific ordered procedure
    CAPABILITY       = MCP/tool/provider operation
    ARTIFACT         = materialized output
    RUNTIME          = deterministic consumer of artifacts

This is stronger than treating one large prompt as the whole system.

### 3. Expensive generation is cost-aware and retry-scoped

The recipe asks for cost inspection before generation and for retrying only a failed clip rather than rerunning the whole batch.

Candidate general pattern:

    estimate cost
    → generate bounded batch
    → validate each artifact
    → retry only failed units

### 4. Stochastic output is normalized by deterministic transforms

Generated clips are joined and transcoded with ffmpeg before entering the application.

    stochastic generation
            ↓
    deterministic normalization
            ↓
    stable artifact contract

The product runtime does not need to understand provider job semantics.

### 5. Human invariants constrain agent execution

The prompts specify exact input images/crops, ordered transitions, aspect ratio, duration, forbidden additions, resolutions, CRF targets, crossfade length, seek strategy, mobile behavior and reduced-motion behavior.

Reusable pattern:

    human intent
    → explicit invariants
    → agent execution
    → observable artifacts
    → validation

### 6. Seek reliability is purchased with transfer cost

The walkthrough is encoded with every frame as a keyframe (`-g 1`) so scroll-driven seeking can be immediate. The observed desktop/mobile files are approximately 12.2 MB and 5.85 MB respectively.

    seek determinism ↑
    compression efficiency ↓

Do not generalize this choice without a media/performance budget.

### 7. Runtime has degraded-mode behavior

Observed implementation includes `preload="none"`, delayed/interaction-triggered video loading, still-image fallbacks, lazy loading, a mobile media variant and `prefers-reduced-motion` behavior.

Generated media enhances the experience without becoming the only usable state.

## Missing provenance layer

The repository versions prompts and final artifacts, but the inspected snapshot does not expose a machine-readable per-generation manifest tying every output to all generation inputs and provider metadata.

Candidate fields:

    artifact_id
    provider
    model
    model_revision
    generation_id
    prompt_sha256
    input_artifact_sha256
    parameters
    estimated_cost
    actual_cost
    generated_at
    output_sha256
    transform_chain
    validation_receipt

This is an **INFERRED / GENERATED** improvement proposal, not an upstream feature claim.

## Promotion boundary

Use S-114 to support:

- separation of durable skill from task-specific recipe;
- build-time capability → materialized artifact → runtime decoupling;
- cost-aware generation and scoped retries;
- deterministic post-processing after stochastic generation;
- artifact provenance requirements;
- human-authored invariants before agent execution;
- performance tradeoffs for media-heavy workflows;
- degraded-mode design for generated assets.

Do not use S-114 alone to:

- certify Higgsfield, Kling, Claude Code, Astro or Cloudflare reliability;
- claim exact generative reproducibility;
- infer that this landing is production-ready for every traffic profile;
- generalize `-g 1` as a universal video strategy;
- copy upstream code or prose where licensing permission has not been established;
- treat a polished demo as evidence of complete workflow governance.
