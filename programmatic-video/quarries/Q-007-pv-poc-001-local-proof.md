# Q-007 — PV-POC-001: first local video render evidence

Observation date: **2026-10-07 America/Lima**.
Status: **OBSERVED / PASS_OUTPUT_ONLY / NOT A PRODUCTION RELEASE**.
Upstream trial archive: [NINFA experiment PR #2](https://github.com/Em3rc0d/NINFA/pull/2); product RFC [prodAgentic #71](https://github.com/Em3rc0d/prodAgentic/issues/71).

## Purpose and boundaries

An original, trusted local-Python compositing fixture was authored and run **in an assistant work container**. The user has a self-contained `PV-POC-001_reproducible.zip` archive with source, manifest, validation scripts, visual previews, receipt, and one MP4. That archive has not yet been persisted in GitHub; NINFA PR #2 holds a **hash-bound summary only**. The proof is bounded to our executing host, not the user's Windows/WSL2.

```text
original manifest
  -> Python / Pillow scene painter (trusted authored code)
  -> 300 RGB frames streamed to FFmpeg stdin
  -> libx264 H.264 MP4 + no audio
  -> ffprobe output gate + SHA256
  -> second independent run
  -> byte comparison + 7 negative cases + temporal-frame checks
```

## Input and execution metadata

| Attribute | Observation |
|---|---|
| Scenes | 3 synthetic original scenes; 90 + 120 + 90 frame allocations |
| Media/third party | No fetched clips, external images, music, logos or prompt code |
| Canvas | 1080×1920 portrait; 30 FPS, 300 frames, 10 s |
| Rendering tools | Python, Pillow 12.3.0, FFmpeg 7.1.5-0+deb13u1/libx264, ffprobe |
| Host | Linux x86_64, 5 logical CPUs, approx. 5.8 GiB RAM |
| Font | System Lato (Debian `fonts-lato` OFL-1.1); not redistributed |
| FFmpeg flags | `libx264`, `ultrafast`, `-crf 20`, 2 threads, `yuv420p`, faststart, fixed `creation_time` |
| POC elapsed (render function) | run 1: 19.68 seconds; run 2: 25.24 seconds |
| Peak RSS | run 1: 131.7 MiB; run 2: NOT MEASURED |
| Video file size | 771,848 bytes |
| Video content | video-only, H.264, 1080×1920, 30/1 FPS, 300 decoded frames, 10.000000s |
| Exact repeat | two independent full renders binary-identical: **PASS** |
| Output SHA256 | `44aa178c3aac0baf76dacec93ade73c740d11d0cc8ab28e8d4018ac09d5fca98` |
| Source render.py SHA256 | `c36f1a7363d87fadc230915f2a5ecfa20138c017b0c1c25a21155c3c57139637` |
| Manifest SHA256 | `1b572e4ab3b640728251aedbd414674bc95c7de80c3bdd0d5551179b04ff2023` |

## Test matrix

| Gate | Outcome | Scope |
|---|---|---|
| FFprobe resolution, H264, 30fps, duration, count | PASS | Actual resulting MP4 |
| No audio | PASS | Single video stream |
| Repeatability exact bytes | PASS | Same container, two independent executions |
| Valid scene boundary and contiguous clock | PASS | Fixed 3-scene manifest |
| Reject overlapping scene, insufficient duration | PASS | Two negative fixtures |
| Reject unapproved third-party media/code/audio | PASS | Three negative fixtures |
| Reject FPS mismatch | PASS | One negative fixture |
| Reject out-of-safe-zone text | PASS | Runtime bounding-box assertion and negative test |
| Temporal motion | PASS | Sampled frame variance and observed static preview |
| Resource usage | MEASURED PARTIALLY | No sustained monitoring of second peak |
| Host-level no-egress and secrets isolation | **UNKNOWN** | Code contained no network calls, but OS-level policy **not dynamically certified** |
| UI safe zones for TikTok/Instagram | **NOT CERTIFIED** | Only conservative experimental bbox screen area |
| Human quality/editorial acceptance | **NOT CONDUCTED** | Needs owner assessment |
| Portability to user WSL2 | **NOT TESTED** | Environment-specific result |
| Stable Git-based code reproduction | **NOT YET** | Source in user-delivered ZIP; Git PR evidence only |
| prodAgentic runtime integration and scheduling | **NOT PERFORMED** | Separate authority gates |

## Important architectural learnings

1. A **simple 2D video can be composed without HyperFrames, Remotion, paid text-to-video APIs, GPUs, remote rendering or cloud deployments**, on the measured host. This is a narrow observation, not an evaluation of those alternative renderers.
2. NINFA's original **production documentation** and historical manifests are useful conceptually, but code for this pilot was authored newly rather than importing an alleged existing generic NINFA compositor.
3. The pilot's progress rail is intentionally nonessential. Required on-screen text is checked against explicit, conservative experimental safe-zone bounds. This is not proof of every social UI's actual overlays.
4. The OS/runtime isolation problem is **not solved** by safe trusted input; untrusted generated HTML/JS must remain blocked until an independent sandbox test.
5. The first render had a footer in a likely social overlay region; it was revised, then both final renders were rerun. **Only the final SHA** above is eligible as evidence.

## Gate decisions

- `ADOPT`: treat frame-based local video rendering as **feasible for this fixture**.
- `REVIEW`: acceptability of compositional quality for accounts and motion complexity; independent human approval needed.
- `HOLD`: product backend/VideoRenderPort integration, cost model, real publish/scheduling, temporal QA broad enough for arbitrary clips, authenticated asset store, and OS sandbox.
- `NO MK1 CERTIFICATION`: full catalog taxonomy/normalization remains open; this is an auxiliary experimental quarry, **not** permission to skip MK1.
- `NO CLOUD DEPLOYMENT`: container-only work, no payments or provider schedules.

## Reproduction package provenance

Artifact name: `PV-POC-001_reproducible.zip`, produced within the originating conversation and linked to its owner there, not an external GitHub release. For third-party re-review, archive matching scripts/manifest in the NINFA experiment branch and validate their SHA256 before running them on a different host. Do not use the Git-only receipt as a substitute for archived source/binary.
