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


## Motion v1.3 reproducibility update — merged 2026-10-08

- [NINFA PR #6](https://github.com/Em3rc0d/NINFA/pull/6) was **merged into main**, squash SHA `5d09d76c673c1141067ad228cc103373539290fc`.
- [Versioned local finishing module](https://github.com/Em3rc0d/NINFA/tree/main/tools/motion-v13) and [UAT engineering proof](https://github.com/Em3rc0d/NINFA/blob/main/docs/contracts/decisions/MOTION_V1_3_LOCAL_FINISHING_2026-10-08.md) now exist. Unlike prior source-recovery uncertainty, this **newly authored** finishing code is actually versioned, and exact tested source/fixtures/test SHA matched GitHub blobs.
- The existing clean video can be reused for local audio/caption revision, avoiding re-rendering hundreds of original frames. FFmpeg finishing produced `dia01` 17.5 seconds / 525 frames in 4.65s and `dia02` 23.6 seconds / 708 frames in 5.93s in the assistant Linux environment. Full dia01 repeats were byte-identical SHA `2bb1af34c5da6e4291597ba0a53762f5bd206c6a67fdc8dcbeeed6dc6c86e752`. Hash-gated cached review was measured at 1.15s vs 4.80s fresh on that host. **16/16 local Python tests passed.**
- **Critical boundary:** It is an **AV finisher**, NOT a generic scene-to-video renderer, full NINFA production factory, Windows/WSL2 certification, prodAgentic adapter, or publishing service. Only English, `ILLUSTRATIVE_POC` and `release=BLOCKED`; neither EMERCOD voice assets nor owner audio files are committed. No cloud rendering, GitHub Actions or paid APIs.
- Does not close the parent programmatic-video MK1 source-normalization or integrated VideoRenderPort gates. This is **observed narrow engineering evidence**, not a universal video standard certification.


## Motion v1.4 bounded Scene Engine — merged 2026-10-08

- [NINFA PR #7](https://github.com/Em3rc0d/NINFA/pull/7) **MERGED to main**, squash commit `85945c90d72b86e96e553182177495f8e1e40973`. [Actual versioned renderer](https://github.com/Em3rc0d/NINFA/tree/main/tools/motion-v14) now exists and produces **clean silent** videos compatible with Motion v1.3's verified visual input format.
- Three **bounded original composition families**: `cache_race` (uses same-host NINFA v1.3 actual 4.80s/1.15s measurement, source-locked), `circuit_breaker` (DEMO/no live calls), `source_lineage` (DEMO/no independent verification). Six-second 1080×1920, H.264, 30fps, 180-frame review exports verified for each.
- **20/20 offline Python tests PASS**, source/tests/fixtures Git blobs exact-matched to local working copies, all three visual outputs satisfy Motion v1.3 `assert_visual`, sampled frames differ over time. No raw voice or MP4 was committed.
- **Scope:** English-only NINFA; `release_state=BLOCKED`; no audio source ingestion or actual owner v1.4 UAT, no generic AI scene generation, no cross-account prodAgentic implementation, no actual destination safe-zone/host security certification, no cloud/Actions/paid APIs. **Does not close parent MK1 catalog gates.**

## v1.4 → v1.3 owner-voice technical integration — 2026-10-08

- [NINFA PR #8 MERGED](https://github.com/Em3rc0d/NINFA/pull/8), squash commit `402d0f505f74849b7f6c9292e2632aaca1b42ca2`. A [single-command local review runner](https://github.com/Em3rc0d/NINFA/blob/main/tools/motion-v14/run_review.py) now composes strict local v1.4 scene manifests, a **private owner voice** and manually timed subtitles via existing v1.3 finishing. No personal audio, final MP4 or private file paths in Git.
- Demonstrated on the earlier owner-narrated **Parallel Execution** script (not a new experiment): novel continuous 23.6s animation + v1.3 finishing; 1080x1920 H264/AAC 708 decoded frames; `ILLUSTRATIVE_POC` and on-video DEMO, local 0.34/0.14s simulated sleep measurements only. The owner has the resulting private playable review file.
- **26/26 offline Python tests PASS**. GitHub blob hashes matched exactly with locally exercised scene engine, unit tests, integration runner, integration test and two manifests; two successive runs confirmed cached visual and finished MP4 reuse without new FFmpeg render. Zero API spend / media Actions / posting.
- This is **NARROW END-TO-END ENGINEERING PROOF**, not generic new-story visualization, word-level auto sync, cross-tenant publishing, real benchmark replication, Windows/WSL2 certification, OS-level security proof or owner UAT acceptance of this new visual.
- NINFA content approval and provider publication remain **BLOCKED**. prodAgentic VideoRenderPort RFC and programmatic-video MK1 normalization remain OPEN.
