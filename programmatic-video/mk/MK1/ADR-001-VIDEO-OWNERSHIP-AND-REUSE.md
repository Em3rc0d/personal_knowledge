# ADR-001 (candidate) — Ownership y reuse de video en Content Operations

State: **PROPOSED / REVIEW REQUIRED**, no autorizado para implementación.
Date: 2026-10-07 America/Lima.
Primary evidence: [Q-005](../../quarries/Q-005-content-ops-ninfa-integration-audit.md), [Q-006](../../quarries/Q-006-ninfa-code-reuse-audit.md), `prodAgentic/backend/domain/rendering/models.py` y `NINFA/tools/chatterbox-local/`.

## Decision proposal

**prodAgentic owns orchestration/authority; a local isolated video adapter owns render execution; NINFA remains its own YouTube media project and contributes research/manifest patterns and optional TTS only.** Content Seller owns editorial policies and novelty.

The new adapter must be **small, separate, testable**. We must not claim a full pre-existing NINFA video renderer. Local FFmpeg assembly is an implementation **candidate**, not approved architecture yet.

## Proposed boundary

```text
content-seller editorial authority/novelty
    -> prodAgentic ProfileVersion + approved ContentSpec
    -> VideoStoryboardV0 (separate from static VisualSpecV1)
    -> VideoRenderPortV0 / limited worker
        -> original typed scenes + local encoder
        -> optional licensed audio from isolated TTS port
    -> VideoArtifactReceiptV0 (hash + ffprobe + exact inputs)
    -> Temporal QA + human review
    -> export (not external scheduling)
    -> scheduling separately authorized only after certified provider integration
```

## Preserve what already works

1. `RendererRequestV1` and `RenderContentType.PNG` remain unchanged; existing stable static routes/tests remain compatible.
2. Keep `prodAgentic` ProfileVersion, ContentSpec, media source digests, authority/approval, and idempotency patterns as inspiration for **additive video-specific contracts**, not a blind schema migration.
3. NINFA owns the *Does It Automate?* brand, content, voice references, historical video decisions and its own channel analytics.
4. No user-facing fourth application, no new cloud worker, no new database by default. Existing prodAgentic UI should eventually expose video jobs **after acceptance**, not in the initial research slice.
5. Content Seller topic novelty/quality rules apply before renderer and after revisions. The renderer does not make editorial decisions.

## Do not do

- No import of Chatterbox Gradio or its voice directory into prodAgentic's backend process.
- No arbitrary third-party HTML/JS executed with network, filesystem or credential access.
- No reinterpretation of PNG `AssetV1` as MP4 or changing existing content-type enum in-place.
- No assumption that published video implies versioned renderer reuse.
- No binding of a video result to an approval receipt without distinct **temporal** QA.
- No scheduling/publishing during `PV-POC-001`; the external TikTok session is not a worker permission.

## Technical design candidates to compare after review

| Option | Preflight input | Success / fail |
|---|---|---|
| `FFmpeg + original vector/bitmap frames` | Python/Node/FFmpeg, frame-deterministic scene drawing, approved fonts, no browser | Favor for 3-scene typography POC if quality/pace acceptable |
| `HyperFrames` | pinned package, Chromium, FFmpeg, restricted runtime, license | Only adopt if current approach fails motion quality/performance and new surface clearly pays for itself |
| `Remotion` | React runtime, Node/browser, FFmpeg and for-profit license eligibility | Alternate; no automatic assumption of free enterprise use |
| `NINFA video renderer import` | actual code/CLI and tests from recovered historical setup | Remains **UNAVAILABLE / NOT LOCATED** pending explicit recovery |

## First POC contract gate (build blocked)

Input: 10 seconds, 30fps, 1080x1920, 3 original scenes, silent, no provider API, no account branding or sensitive data. 
Output: MP4 `video/mp4`, ffprobe codec/resolution/frame count (300 expected), SHA256, scene/frame QA, 2 repeat runs, machine profile, memory/elapsed-time receipt and one negative failure case.

Before build: resolve host environment, verified rights for font/assets, executable versions, sandbox no-egress/secrets, worker ownership, temp storage policy, and whether fixed 1080x1920 frame render is tractable on the observed machine.

## Cross-repository work item

- [prodAgentic issue #71 — VideoRenderPortV0 RFC](https://github.com/Em3rc0d/prodAgentic/issues/71): tracks product-side approval/preflight without modifying frozen R4 authorities.

## Promotion rules

**This ADR is not an accepted prodAgentic ADR**; adopting it requires review in prodAgentic's own governance after R4 branch/release authority is checked, a real test and rollback plan. No code or production authority changes have been made.

## Branch and release authority refresh

GitHub reports [prodAgentic PR #69](https://github.com/Em3rc0d/prodAgentic/pull/69) **merged** at `93be1c98c87f2544c96a700afaefb0ec41562258`; older repo status documentation still says pre-UAT/pending. No fresh exact-main release receipt or production rollout proof was inspected. **Do not claim R4 is certified or unmerged.** Verify exact runtime authority on current main before proposing where a video PR branches; this design remains an isolated research proposal.
