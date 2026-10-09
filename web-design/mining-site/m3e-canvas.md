# M3E Canvas — external source study

- Source: https://github.com/lnkiai/m3e-canvas
- Reviewed: 2026-10-09
- Status: RESEARCH REFERENCE; not a dependency or endorsed implementation
- Provenance: OFFICIAL for upstream README and agent.md claims; OBSERVED for inspected source files; INSPIRED for EM3RC0D proposals.
- Confidence: high for cited structure; limited for runtime security, accessibility, portability and visual fidelity (not independently tested).

## Scope and observed mechanisms

Upstream describes a browser-based Material 3 Expressive screen editor producing prompts for coding agents. It supports screens, groups, navigation actions, theme axes, interactive previews, prompt generation, PNG export, JSON project import/export, and optional model-assisted annotations.

Inspected upstream files (default branch as observed on 2026-10-09):
- [README](https://github.com/lnkiai/m3e-canvas/blob/main/README.md): user-facing capabilities and static build.
- [lib/project.ts](https://github.com/lnkiai/m3e-canvas/blob/main/lib/project.ts): JSON document shape checks, save/read.
- [lib/prompt.ts](https://github.com/lnkiai/m3e-canvas/blob/main/lib/prompt.ts): natural-language prompt derivation from structured design.
- [lib/share.ts](https://github.com/lnkiai/m3e-canvas/blob/main/lib/share.ts): shareable filtered JSON compressed to URL fragment.
- [lib/tidy.ts](https://github.com/lnkiai/m3e-canvas/blob/main/lib/tidy.ts): placement, grouping and ordering heuristics.
- [lib/tokens.ts](https://github.com/lnkiai/m3e-canvas/blob/main/lib/tokens.ts): model primitives and design tokens.
- [public/agent.md](https://github.com/lnkiai/m3e-canvas/blob/main/public/agent.md): documented agent-facing JSON format.
- [package.json](https://github.com/lnkiai/m3e-canvas/blob/main/package.json): Next.js, React, TypeScript, Motion, Tailwind and Vitest.

## Portable lessons (INSPIRED, not an upstream contract)

1. Represent UI design in structured, validated, versioned data rather than in a prompt or screenshot.
2. Derive previews and agent instructions from the same snapshot; generation must be reproducible or record its nondeterminism.
3. Preserve interactions and state alongside geometry/tokens, including responsive intent.
4. Place schema validation, migrations, compatibility checks and independent review at artifact boundaries.
5. Record provenance and confidence for extracted design decisions.

## Boundaries / failure modes

- A natural-language prompt is lossy and not a normative specification.
- Two frame dimensions do not guarantee adaptive design coverage.
- A URL-fragment share link is not access control; recipients can read embedded data, and link exposure remains possible.
- Browser-stored BYOK credentials require provider-specific security review.
- The upstream agent guide advises not verifying generated documents; EM3RC0D rejects that policy and demands validation.
- Passing unit tests does not demonstrate generated-code fidelity or accessibility.
- No dependency, fork, skill installation, build pipeline or Foundry runtime change is authorized by this study.

## Destination

See [Design Contract → Foundry](../../em3rc0d-foundry/architecture/DESIGN_CONTRACT_TO_FOUNDRY.md) for the bounded architecture candidate. The canonical design contract is an EM3RC0D synthesis, **not** M3E Canvas's JSON schema.
