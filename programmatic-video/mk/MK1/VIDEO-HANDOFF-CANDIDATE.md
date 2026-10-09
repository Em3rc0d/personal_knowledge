# MK1 Candidate — Video production handoff (NOT an implementation)

Status: **CANDIDATE / NOT CANON / NOT APPROVED FOR PRODUCT BUILD**. An independently authored local synthetic `PV-POC-001` has now rendered and repeated successfully; see [Q-007](../../quarries/Q-007-pv-poc-001-local-proof.md). That proof does **not** establish prodAgentic adapter integration or arbitrary-code sandbox safety.
Dependency: [Q-005 cross-repo audit](../../quarries/Q-005-content-ops-ninfa-integration-audit.md), [Q-006 code-level audit](../../quarries/Q-006-ninfa-code-reuse-audit.md), [ADR-001 proposed ownership](ADR-001-VIDEO-OWNERSHIP-AND-REUSE.md).
This contract is for a reviewable boundary. Final operational schemas belong to MK2/MK3, not MK1.

## Separation of responsibilities

1. `content-seller` — produces policy/evidence/novelty decisions, not final pixels.
2. `prodAgentic` — owns ProfileVersion-bound runtime, validation, adapter invocation, artifact custody, approval and handoff.
3. Local AV adapter — renders time-indexed scenes and encodes video (NINFA code is candidate, NOT yet extracted).
4. `NINFA` — continues to own its own channel/editorial identity; **its versioned shared repository has no general video renderer API verified in the inspected sources**. Reuse manifests and only optional audio/TTS after explicit hardening; no permission to import voice/assets/brand automatically.
5. `personal_knowledge` — method/evidence, not production runtime.

## New conceptual types (do NOT mutate current static models)

```text
ApprovedContentSpec + ProfileVersionDigest
    → VideoStoryboardV0
    → VideoRenderRequestV0
    → VideoRenderPort
    → VideoRenderResultV0
    → TemporalVideoQA
    → HumanReview
    → ApprovedVideoBundle
    → ExportReceipt (scheduling independently authorized)
```

### VideoRenderRequestV0 — candidate required fields

| Field | Purpose |
|---|---|
| `run_id`, `revision_id`, `idempotency_key` | existing identity/retry boundary |
| `profile_version_digest`, `content_spec_digest`, `video_storyboard_digest` | freeze editorial, account, visual authority |
| `canvas: 1080x1920`, `fps: 30`, `duration_frames: 300` | initial pilot configuration, not universal platform standard |
| `scenes[]` with start/end frames, per-scene text/assets | time-indexed storyboard |
| `safe_area_profile_id` | profile/channel-specific measured UI constraints |
| `assets[]: {content_hash, rights_state, origin, kind}` | approved/owned bytes only |
| `audio_policy`, `subtitle_policy` | explicit NONE/OWNED/LICENSED and synchronized timebase |
| `renderer_id/version`, `browser/ffmpeg versions` | reproducibility |
| `external_network_policy: DENY_BY_DEFAULT` | prevent arbitrary third-party requests |
| `budget: max_elapsed_s/ram_mb/output_mb` | bound cost/failure paths |
| `publish_authority: NONE` | render process may never schedule or publish |

### VideoRenderResultV0 — candidate minimum

- `status=SUCCEEDED|FAILED|BLOCKED`; failed runs must not return publishable success.
- Immutable MP4 artifact pointer, `sha256`, size, frame count, duration, frame rate, resolution, codec (observed with ffprobe).
- Source/renderer/asset digest manifest, environment and timings.
- QA results: critical text coverage, safe-area crops, keyframe and sampled-frame review, subtitles/audio synchronization, flashes, readability, brand consistency and asset rights.
- Failure labels, attempt identifiers and idempotency/reconciliation receipt.
- Export not scheduled; `approval_ref` generated only after separate human gate.

## Compatibility invariants

- Existing `RendererRequestV1`, `RenderResultV1`, `AssetV1` and PNG endpoints remain unchanged during pilot.
- New audio/video content types and artifact store must not assume image-byte caps or `page_index`.
- Scheduling/publishing is a separate stateful side effect with durable provider receipt. No blind retries on unknown external state.
- No cross-account/profile leaks: storyboard and assets must carry the frozen ProfileVersion digest.
- Content Seller novelty blocks re-use before output and after revisions; rendering quality cannot waive editorial/evidence failures.
- Local render adapter executes with no social credentials, no model API keys and no internet by default.

## Initial proof slice

**PV-POC-001**: 10-second silent, three-scene, 1080x1920, 30fps tech explainer; original shapes/copy, no account-specific logos, no PII/third-party media. This is a **synthetic capability test**, not a proposed real Content Seller publication or a schedule action.

Expected sequence:

1. Attempt to recover NINFA's local/off-repo video assembly entrypoint; if not recoverable, mark `NOT_AVAILABLE` and evaluate a minimal original deterministic local FFmpeg composition path. Record FFmpeg availability and exact versions before any run.
2. Test sandbox can reject external network/file/timeout issues.
3. Build one original storyboard from fixture (not from catalog source prompt).
4. Render MP4 twice, inspect ffprobe, keyframe crops and visually compare renders.
5. Run negative cases and record resources/timings.
6. Present QA result to human and decide `ADOPT|REVISE|REJECT`.
7. Only upon success propose an integration PR to prodAgentic's **active authorized integration branch**, after reviewing branch/release rules.

**Release condition:** Not `PASS` until output exists, tests demonstrate the claimed behavior and a human approves quality. Do not market "zero cost" when only API cost is zero.

## Unresolved decisions (must close before BUILD)

- Source recovery: no general video renderer module/CLI verified in current NINFA repository. A new **minimal independent sandbox prototype** now exists and passed narrow output tests; source is delivered to owner as reproducibility ZIP but not yet archived in Git. This does not change legacy NINFA renderer claims or authorize prodAgentic runtime implementation.
- Choice between adapting its assembly or using HyperFrames/Remotion (measured comparison only if justified).
- Host placement (local WSL2 worker), input/output exchange, artifact storage and size limits.
- Sandboxing on available OS and FFmpeg/Chromium versions; avoid coupling untrusted renderer to Chatterbox service (GPU startup compulsory on current scripts, broad port binding).
- Timing of prodAgentic R4 certification and branch authority for an additive video slice.
- Real safe-zone specification, accessibility and proof/review workflow per platform.
- Who authorizes any eventual TikTok Studio scheduling operation; no auto-scheduling in this POC.
