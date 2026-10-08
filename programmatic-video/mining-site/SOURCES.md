# Programmatic Video — Source Registry (MK0)

Observation date: **2026-10-07 America/Lima**.
Policy: `jett-engineering-method/SOURCE-INTAKE-CONTRACT.md`. Each record separates access, capture, verification and promotion. `VERIFIED` never means that a tool performed as advertised; it applies only to explicitly bounded documentation or file contents inspected.

## SRC-PV-001 — Awesome Opus 5.5 Videos (seed)

| Field | Recorded |
|---|---|
| input_pointer | https://github.com/Em3rc0d/awesome-opus5-5-videos |
| resolved_identity | `Em3rc0d/awesome-opus5-5-videos`, public repo, `main` |
| pinned_commit | `756290289742535eb0ac3817548f152e9759cc70` |
| latest_commit_utc | `2026-10-08T02:12:38Z` (2026-10-07 21:12 Lima) |
| inspected | `README.md`, `data/videos.json`, 3 `prompts/*.md`, `LICENSE`, commit history |
| access_state | ACCESSIBLE |
| capture_state | REPRODUCIBLE (exact GitHub commit, relevant files) |
| verification_state | VERIFIED for file contents/counts; INCONCLUSIVE for video-generation attribution or independent recreations |
| promotion_state | QUARRY_ONLY |
| provenance | OBSERVED for files, INFERRED for implications |
| confidence | HIGH for counts/structure; LOW for creator/process authenticity |

**Supported:** data records 513 entries, categorical labels, linked URLs, prompt strings, missing-context flags; README advertises original vs remake on Skillry; repository contains MIT text with copyright `yihui-dev`.

**Not supported:** that 513 original videos were independently validated, that prompts are executable without creator environment, that `prompt_partial=false` proves completeness, that linked remakes have been measured, that third-party creative assets are MIT.

**Drift trigger:** any updated dataset/prompt, withdrawn creator post, changed label/licensing. Record a new commit rather than overwrite this observation.

## SRC-PV-002 — HyperFrames (candidate renderer)

- Owner/publisher: HeyGen, `heygen-com/hyperframes`.
- Identity: https://github.com/heygen-com/hyperframes
- Documentation: https://hyperframes.heygen.com/introduction
- Source type: first-party code/docs.
- Access: ACCESSIBLE; capture: PARTIAL (README/documentation sections).
- Verification: VERIFIED for vendor's stated CLI/local seekable HTML-to-MP4 pipeline; runtime determinism UNVERIFIED.
- Promotion: QUARRY_ONLY. Provenance: OFFICIAL (project claims) / not independently tested.
- Claimed mechanics: HTML/CSS/JS compositions, browser frame capture, FFmpeg encoding, local CLI, agent-oriented authoring.
- License reported by repository: Apache-2.0; **verify exact dependency/license versions at implementation time**.
- Risks: evolving interfaces, headless Chromium/GPU, FFmpeg CPU cost, browser asset fetching, security of generated JS.

## SRC-PV-003 — Remotion (candidate renderer)

- Publisher: Remotion.
- Identity: https://www.remotion.dev/docs ; render CLI: https://www.remotiondocs.com/docs/cli/render
- First-party license: https://github.com/remotion-dev/remotion/blob/main/LICENSE.md
- Access: ACCESSIBLE; capture: PARTIAL.
- Verification: VERIFIED for documented React/composition-to-video CLI and differentiated licensing, not for runtime behavior.
- Promotion: QUARRY_ONLY. Provenance: OFFICIAL.
- Important: license is **not universally free/unrestricted**: individuals and certain small organizations may qualify; ineligible businesses require Company License. Criteria/version must be rechecked before commercial integration.
- Risks: React/runtime coupling, browser encode load, license/telemetry policy changes, agent-generated dependencies.

## SRC-PV-004 — MDN Canvas captureStream

- Publisher: Mozilla Developer Network (documentation of web standard).
- Identity: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream
- Access: ACCESSIBLE; capture: PARTIAL.
- Verification: VERIFIED only for documented real-time canvas `MediaStream` semantics.
- Promotion: QUARRY_ONLY. Provenance: OFFICIAL documentation.
- Boundary: real-time capture API is **not** a complete deterministic batch render, container mux/MP4 delivery, nor a general timeline/editor.

## SRC-PV-005 — FFmpeg reference

- Publisher: FFmpeg project.
- Identity: https://ffmpeg.org/ffmpeg-filters.html
- Access: ACCESSIBLE; capture: PARTIAL.
- Verification: VERIFIED for documented scale/filter mechanics.
- Promotion: QUARRY_ONLY. Provenance: OFFICIAL documentation.
- Boundary: codec availability, executable version, licensing/build flags, latency and output consistency remain **UNTESTED**.

## Rights discipline

- MIT on `SRC-PV-001` code/documentation does **not** assert ownership over externally hosted posts, individual videos, audio, fonts, trademarks or remakes.
- Do not rehost source audiovisual artifacts or copy prompts wholesale. Use attributable links for study; create our own synthetic assets for experiments.
- A visible logo, audio track, screenshot or character needs independent rights review for commercial reuse.
- The linked Skillry site provides a comparison interface; it is not a source of neutral benchmark measurements.

## Follow-ups

- Inspect and record a stratified set of original X posts and any exact instructions/context visible (some access may be blocked).
- Recheck licensing before introducing a runtime into a commercial product.
- Pin candidate renderer, browser binary and FFmpeg versions before reproducibility tests.
