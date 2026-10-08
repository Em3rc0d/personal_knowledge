# Q-009 — Does It Automate? PV-POC-006 motion-direction contract handoff

Date: **2026-10-08 America/Lima**.
Source of truth: [NINFA merged PR #4](https://github.com/Em3rc0d/NINFA/pull/4), canonical [Shorts motion contract v1.0.0 on main](https://github.com/Em3rc0d/NINFA/blob/main/docs/contracts/DOES_IT_AUTOMATE_SHORTS_MOTION_V1.md), squash commit `c8ee078ee65b8c06e94317edbe4f70f088e87e8e` (2026-10-08).

## Decision and evidence

- User reviewed PV-POC-006 (10-second English motion-graphics video with user-recorded English voice) and explicitly preferred it over PV-POC-005: "Me gusta más." The direction was approved as a creative **candidate/reference**, **not** as a release-certified reusable template nor a publishable real experiment.
- Tested POC output in local assistant container: 1080×1920, 30 FPS, 300 video frames, H.264/AAC, 10.0 seconds; SHA-256 \`bc17ebb25da40252abc092afb420a97695ec9d0b0f80e50cfc152d1d98dfce98\`; voice remained private and not committed.
- Experiment uses custom graphic elements and illustrates concept → script → design → render → QA → output; mock UI does **not** verify actual product outcomes. No official Does It Automate? brand-logo binary was provided to this experimental render.
- Strong positive directional preference supports **meaningful visual state changes rather than static text posters**. It does not prove audience retention, compliance with measured YouTube/TikTok overlays, broad platform integration, or commercial success.
- NINFA's existing [FROZEN BRAND v1](https://github.com/Em3rc0d/NINFA/blob/main/docs/BRAND_IDENTITY.md) prevails: no invented/recolored/deprecated logo. Existing [CHANNEL_THESIS](https://github.com/Em3rc0d/NINFA/blob/main/docs/CHANNEL_THESIS.md) prevails: real evidence and original contradiction-driven editorial formats for real Shorts.

## Durable contract boundaries

The NINFA PR records:
1. English-only script, spoken narration, captions and onscreen content for the channel.
2. Motion semantics: observable *state transitions* or evidence, not motion decoration.
3. Dark tech/graphite/off-white/electric-cyan vocabulary subordinated to approved brand assets.
4. Human-owned voice as a quality anchor; approved local Chatterbox/Kokoro candidates, private voice references, no paid API or routine CI rendering.
5. Explicit \`ILLUSTRATIVE_POC\` vs \`EVIDENCE_BACKED\` vs \`MIXED_LABELED\`; no fake result passes, always evidence/attribution.
6. Conservative safe-zone POC margins only until destination measured; audio/caption/temporal/mobile QA independent.
7. No scheduled/uploaded/published claims without separate approval and provider state receipts.
8. No raw user voice, heavy video binary or user secrets in GitHub.
9. A machine-readable v1 schema, fixture and local standard-library Node validator with negative cases; PR remains draft until clean-checkout local execution/review.

## Scope in cross-system architecture

This is a **channel-specific NINFA direction**; it is neither a required style for Content Seller accounts nor an approved \`prodAgentic\` runtime interface. It does **not** close the MK1 catalog-normalization gates and does **not** imply \`VideoRenderPortV0\` is authorized or implemented. Reusable renderer interfaces must remain independent of account visuals and voice identities.

Document registration must keep the distinction:
\`owner approves direction\` ≠ \`every version of PV-POC-006 approved\` ≠ \`production certified\` ≠ \`provider scheduled/published\`.

## Status

- Direction: **OWNER-ACCEPTED AS REFERENCE**.
- Contract: **MERGED IN NINFA MAIN / VERSION 1.0.0 ACTIVE AS CREATIVE-DIRECTION POLICY**; this does **not** authorize actual video production, publication, or cross-account integration.
- Validator: **19/19 current semantic regression cases PASS** executed from GitHub's committed validator and fixture in an isolated V8 JS environment without GitHub Actions; Node CLI from a fresh checkout **not yet executed**. Unknown root/nested props were included in the evaluated rejection cases.
- Motion engine productization: **NOT APPROVED**.
- Social publishing/scheduling: **NOT PERFORMED**.
- Owner voice and reference audio: **NOT UPLOADED TO GITHUB**.
