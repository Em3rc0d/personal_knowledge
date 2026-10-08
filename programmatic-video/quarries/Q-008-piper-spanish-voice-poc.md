# Q-008 — PV-POC-003: TTS neuronal Piper en español

Fecha local de ejecución: 2026-10-07 (Lima; logs UTC: 2026-10-08 04:32).
Estado: **TECHNICAL PASS / OWNER NATURALNESS NOT ACCEPTED / VOICE REJECTED FOR PRODUCTION / PRODUCT INTEGRATION NOT DONE**. Follow-up after owner listened: Piper `es_MX-claude-high` **did not fully satisfy** voice naturalness expectations. No claim that Piper as a family is universally inadequate; this specific voice fails this account's quality gate.

## Need and blocker discovery

PV-POC-002 proved synchronous 3-scene audiovisual assembly but eSpeak Spanish Latin American synthesis was audibly robotic (owner confirmation). The assistant's local runtime had no Piper, Kokoro, Chatterbox, ONNX weights or network DNS to download a neural model. The installed connected Descript app responded **Insufficient AI credits** to a minimal 3-sentence generation request. **No Descript output was made, no purchase or upgrade attempted**.

Instead of treating unavailable TTS as pass, an isolated [NINFA draft PR #3](https://github.com/Em3rc0d/NINFA/pull/3) adds GitHub Actions plus a small fixed-data, trusted Python/Pillow-free audio/video proof. Existing NINFA `main` and prodAgentic release code remain unmodified.

## Actual execution

- [GitHub Actions successful run ID 37727885129](https://github.com/Em3rc0d/NINFA/actions/runs/37727885129): `synthesize-and-render`, status `completed/success`.
- [Review artifact ID 11528507578](https://github.com/Em3rc0d/NINFA/actions/runs/37727885129/artifacts/11528507578), retained seven days; contains model-free WAVs, MP4, SRT and receipt.
- Runner OS `ubuntu-24.04`, Python 3.11, `piper-tts==1.3.0`, CPU inference with Piper `es_MX-claude-high` (VITS neural, Mexican/Latin American Spanish). Model downloaded from pinned `v1.0.0` and checked against SHA `3ef40a71ea63852cd8ab7e6fa7d2ecdcfa67a0b47c9c48e3f10e02ee02083ea0`.
- Sentences kept verbatim: `De una idea, nace un video.`; `Primero el guion, luego el diseño y el render.`; `Y al final, validamos el resultado.`.
- Scene starts `0.15`, `3.13`, `7.02` seconds. Voice takes `2.450`, `3.297`, `2.798` seconds; **tempo factors all 1.0**.
- Master WAV `narracion-neuronal.wav` SHA `08140a4f4283093a9cb7a857c093664a7c814e05f69f2a86b9d553850b4b59a2`.
- CI video: 1080×1920, H.264/AAC, 30 FPS, 300 frames, 10 seconds, SHA `5175469b4ee54ce58a2019e3f65ccf1eab9d7537772982a3849e4df389c92e6b`.
- The GH artifact was downloaded into the assistant container using the GitHub app. For **visual continuity with PV-POC-002**, the exact neural master WAV was then muxed with the original clean animated video and safely placed ASS captions. Remuxed 10s H.264/AAC 300-frame SHA `4d7c28b3efb3de0532cfcb22767cd511259f05593244f07138f1f924337fd4ef`, 989,324 bytes. Measured mean -17.3 dBFS, max -2.0 dBFS, with mono 48kHz audio. This remix is available to owner in sandbox, plus reproducible ZIP. It is **not identical** to GitHub's simpler graphics.
- The ZIP archive integrity check passed.

## Evaluation

| Gate | Status |
|---|---|
| Fetch/download real neural model with verified hash | **PASS** GitHub-hosted runner only |
| TTS separate scene WAVs with nonzero RMS and original text | **PASS** |
| Voice timing unaltered, fitting exact 10s POC | **PASS** |
| Playable verified 1080×1920, 300 frames H264/AAC and external WAV | **PASS** |
| Original animation reused for delivered local video | **PASS** |
| No paid voice API | **PASS**; GitHub Actions hosted minutes subject to account terms |
| Neural speech sounds human/natural | **NOT ACCEPTED by owner** for publication; technically synthesized ≠ editorial quality accepted |
| Accent/treatment of technology words in Peru | **NOT EVALUATED** |
| TikTok platform safe zone certified | **NOT CERTIFIED** (experimental conservative layout only) |
| Security for untrusted code/OS-level no-egress | **NOT CERTIFIED** |
| Product contract adapter in prodAgentic | **NOT IMPLEMENTED** |
| TikTok or other scheduling/publishing | **NOT PERFORMED** |

## Boundaries and next gate

1. The owner reviewed the pilot and reported that the voice was still not satisfactory. **Do not promote this Piper voice to production.** Revisit only with a different evaluated voice path, explicitly budgeted and independently quality-gated.
2. If approved, evaluate voice choice versus 1–2 different **authorized** model voices, evaluate pronunciation substitutions for abbreviations and editorial pacing; do not necessarily adopt one voice for all brands.
3. Keep `piper-tts` GPL-3-or-later package and voice dataset/model licensing separately reviewed before redistribution; this test only runs in a transient CI worker and does not commit model binaries.
4. Preserve current PNG render contract. After owner approval and release authority, create additive `VideoRenderPortV0` with allowed audio sources, timings, receipt and temporal QA.
5. No new application, provider subscriptions or social scheduling implied.
6. **Resource policy amendment:** GitHub Actions served as a *one-time experimental runner*, **not a TTS backend or ongoing production worker**. The NINFA experimental workflow was modified to `workflow_dispatch` only (no `push` or `pull_request` automatic triggers) in branch `experiment/pv-poc-003-piper-voice`. Even where public standard runners have free minutes, do not design the business around CI artifacts/retention, shared compute, abuse limits or account quota assumptions.

Related [Q-007](Q-007-pv-poc-001-local-proof.md) and [NINFA PR #3](https://github.com/Em3rc0d/NINFA/pull/3).
