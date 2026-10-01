# Reproducible Multimodal Agent Workflows

Source basis: [S-114](../mining-site/S-114-midudev-higgsfield-landing.md)

Status: **QUARRY / NON-CANONICAL**

## Thesis

A useful agent workflow is not a prompt. It is a governed path from intent to materialized, inspectable artifacts.

    SPEC
      ↓
    SKILL / POLICY
      ↓
    EXECUTION RECIPE
      ↓
    CAPABILITIES
      ↓
    STOCHASTIC GENERATION
      ↓
    DETERMINISTIC NORMALIZATION
      ↓
    ARTIFACT MANIFEST
      ↓
    PRODUCT RUNTIME
      ↓
    VALIDATION
      ↓
    PROMOTION / CERTIFICATION

S-114 demonstrates most of this path in a compact worked system. The manifest/certification layer is the main missing opportunity.

## Separation of concerns

### Skill

Durable, reusable decision policy: design constraints, accessibility policy, structural rules and review heuristics. It should survive replacement of one specific project.

### Execution recipe

Ordered task-bound procedure: prepare inputs, invoke capabilities, validate units, retry bounded failures, normalize outputs, integrate and verify. Ordering and parameters affect results, so the recipe should be versioned like code.

### Capability

External or local operation an agent can invoke: generation, image transformation, ffmpeg, browser verification or deployment. Capability availability is not workflow correctness.

### Artifact

Materialized output with stable identity: image, video, JSON, build, report or deployment bundle. Accepted artifacts should remain usable even if the generating provider later becomes unavailable.

## Artifact-first architecture

Prefer:

    provider job
    → materialized artifact
    → checksum + metadata
    → deterministic consumer

over a live generative runtime dependency when content does not need to be fresh per user request.

Benefits include provider isolation, lower runtime latency/cost, cacheability, independent QA and rollback.

## Stochastic-to-deterministic boundary

Generative systems produce variable outputs. Narrow that variability before the artifact crosses into the product contract.

    generate
    → inspect
    → reject/retry bounded failures
    → deterministic transform
    → validate shape/size/hash
    → publish

Deterministic normalization does not make source generation reproducible; it makes the artifact interface stable.

## Cost-aware orchestration

Candidate rules:

1. estimate cost before expensive batches where possible;
2. define bounded batch size;
3. assign logical artifact IDs before generation;
4. record per-unit results;
5. retry failed units only;
6. avoid regenerating accepted artifacts without an explicit invalidation reason.

## Human invariants vs agent discretion

Human/spec should own objective, forbidden outcomes, source-of-truth inputs, cost budget, format, acceptance criteria and promotion authority.

Agent discretion may cover implementation sequencing inside the recipe, provider-prompt wording, bounded retries, local optimization and deterministic assembly mechanics.

The goal is not maximal autonomy; it is useful execution under explicit invariants.

## Provenance manifest

Prompts alone are insufficient provenance for generated artifacts.

Minimum candidate contract:

    artifact_id: stable logical ID
    source_ids: upstream evidence/input IDs
    provider: generation provider
    model: model family
    model_revision: exact revision when exposed
    generation_id: provider job/run ID
    prompt_sha256: hash of exact prompt
    input_artifact_sha256: hashes of binary inputs
    parameters: normalized generation parameters
    cost_estimate: preflight estimate
    cost_actual: observed amount when exposed
    created_at: timestamp
    output_sha256: final output hash
    transform_chain: tool/version/parameters
    validation_receipt: accepted|rejected|qualified + checks

If a provider does not expose a field, store `UNKNOWN`; do not fabricate precision.

## Performance as an artifact constraint

An artifact can be visually correct and still operationally unsuitable. Generated-media acceptance should include transfer bytes, decode memory, LCP interaction, mobile variants, reduced-motion behavior, lazy/deferred load, cacheability and failure fallback.

`Looks correct` is not sufficient evidence.

## Graceful degradation

    premium generated experience
            ↓ unavailable / reduced motion
    optimized still or simpler deterministic experience
            ↓
    core content + primary action remain usable

## Failure and invalidation model

Explicit invalidation reasons should include changed upstream input, changed factual content, failed validation, performance-budget breach, legal/licensing constraint, product-contract change, or an intentional provider/model revision experiment.

Do not regenerate merely because a workflow is being rerun.

## Candidate workflow unit

    Workflow Package
    ├── scope / objective
    ├── inputs contract
    ├── skill / policy
    ├── execution recipe
    ├── capability requirements
    ├── cost policy
    ├── artifact schema
    ├── provenance manifest
    ├── validation gates
    ├── degraded mode
    └── promotion criteria

This turns prompt collections into inspectable engineering assets.

## Evidence state

Supported by S-114: skill/recipe separation, build-time generative capability, materialized outputs, deterministic assembly, cost preflight in the recipe, scoped retries and runtime fallback/performance handling.

Generated proposals requiring further pressure tests: universal manifest schema, workflow-package schema, certification levels, provider-independent cost policy and generalized artifact invalidation protocol.
