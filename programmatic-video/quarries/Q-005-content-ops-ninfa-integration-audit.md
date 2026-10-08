# Q-005 — Cross-repository capability audit: content-seller, NINFA, prodAgentic

Date: 2026-10-07 America/Lima.
Status: **QUARRY_ONLY / ARCHITECTURAL CANDIDATE**. This is not a cross-repository release decision.
Source type: internal repository code/docs, observed on default branches. All statements refer to bounded files inspected; do not treat README promises as runtime test evidence.

## Why this audit

Avoid building an independent "Video Factory" when the estate already contains an audiovisual pipeline and a governed social-content runtime. The right problem is the **missing reusable, verifiable video output contract**, not acquiring 513 prompts.

## Source matrix (directly inspected)

| Source ID | Repo / paths | Observation | Boundary |
|---|---|---|---|
| PV-INT-01 | `Em3rc0d/NINFA`: `README.md`, `docs/MEDIA_STORAGE_POLICY.md`, `docs/VOICE_CLONE_CHATTERBOX.md`, `content/CONTENT_STATUS.md` | README claims full local production, local narration, scene manifests + motion/diagrams + FFmpeg, two completed full episodes; TTS Chatterbox has measured CPU and GTX 1650 runtime in docs | `DOCUMENTED IMPLEMENTATION / REPRODUCIBLE MODULE API NOT VERIFIED`; does not prove generic isolated render CLI |
| PV-INT-02 | `Em3rc0d/prodAgentic`: `README.md`, `backend/domain/rendering/models.py`, `backend/domain/rendering/ports.py`, `backend/application/rendering/r4_service.py`, `mk1/STATUS.md`, `mk1/build/r4/CERTIFICATION_GRAPH.json` | Existing profile → content → VisualSpec → rendered assets → QA → approval model; `RenderContentType.PNG` and renderer request `single_image/carousel/infographic`; `RendererPort.render()` returns page bytes; MP4 contract not found in inspected renderer surfaces | STATIC RENDER/PNG, not video; release certification not inferred from implementation |
| PV-INT-03 | `Em3rc0d/content-seller`: `README.md`, `mk1/README.md`, `mk1/integration/PRODAGENTIC.md`, `mk1/arch/SYSTEM_INVARIANTS.md` | Editorial/evidence/novelty/certification authority for LinkedIn, Content Seller and Logan, with `prodAgentic` as execution plane. Existing no-repeat, anti-cross-profile-leakage, critical copy preservation, consent/gate semantics | No code or private editorial dataset copied here; its A3 autonomy remains distinct from renderer quality |

## Critical finding

```text
content-seller                   prodAgentic                      NINFA
editorial intelligence          current social runtime          independent YouTube media project
topic + novelty + claims        Profile/VisualSpec/PNG          scene manifests + audio + FFmpeg
autonomy/quality gates           approval/export/QA              local video production evidence
       |                               |                              |
       +-------- versioned inputs -----+                              |
                                       |---- potential video port ----+
                                              (NOT INTEGRATED)
```

**Do not make NINFA the owner of all content identities.** Its Does It Automate? brand, 16:9 long-form voice/shorts decisions and media-company analytics are not generic production policy. For multi-profile production, `prodAgentic` owns runtime authority and routing; NINFA provides **candidate implementation patterns** or, only if tested, a reusable *local render adapter* extracted behind a stable interface.

A renderer is not a scheduler. Neither `NINFA` nor Programmatic Video owns TikTok browser sessions, external scheduling credentials, idempotent posting or provider reconciliation.

## Proven gap — positive and negative evidence

1. **Positive:** `prodAgentic` already has an explicit `RendererPort`, immutable `VisualSpec` lineage, digest/provenance, owned assets, and visual QA.
2. **Negative within scoped code:** `RenderContentType` only declares `PNG="image/png"`; `RendererRequestV1.format` enumerates static formats; the current renderer port returns `RenderedPageBytes`. Its contracts should **not be modified in-place** to smuggle MP4 into PNG assets.
3. **Positive (NINFA docs):** local narration, scenes and FFmpeg assembly are documented with real production episodes. The Chatterbox implementation is documented at `tools/chatterbox-local/`, but that is **TTS**, not proof of a reusable generic video engine.
4. **Unknown:** location, entrypoint, tests, portability and runtime isolation of NINFA's general scene/video renderer (source-level extraction audit still required).
5. **Unknown:** whether a third-party framework such as HyperFrames materially improves results over Ninfa's existing FFmpeg workflow. No proof yet.
6. **Unknown:** TikTok Studio native scheduling adapter availability. Manual/browser-session scheduling should stay a separate authorized step; "export MP4" never means "scheduled".

## Options and choice

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Create a new Video Factory product | independence | duplicates NINFA and prodAgentic responsibilities; adds cost/maintenance | REJECT for now |
| Put all content logic inside NINFA | existing AV workflow | leaks Does It Automate? editorial policies, couples unrelated accounts to YouTube project | REJECT |
| Copy NINFA code into prodAgentic wholesale | quick apparent integration | source drift, hidden deps, rights and security risks | REJECT |
| Introduce a **video adapter contract in prodAgentic**, backed first by proven local assembly patterns | consistent approval/QA, keeps identities isolated, single control plane | needs repo/source audit, video-specific schema/QA; not a trivial PNG extension | **PREFERRED CANDIDATE**, not yet authorized |
| HyperFrames/Remotion spike only after gap evidence | potentially stronger motion design | additional dependency, licensing and sandbox cost | CONDITIONAL |

## Principle of minimum change

```text
Content Seller approved content + immutable ProfileVersion
    ↓
prodAgentic: VideoStoryboard candidate (new type, not overload current VisualSpec)
    ↓
VideoRenderPort (isolated worker / CLI, renderer-agnostic)
    ↓
NINFA-inspired local FFmpeg scene pipeline OR another measured backend
    ↓
VideoArtifactReceipt + MP4 + preview frames + quality checks
    ↓
prodAgentic existing authority gates (adapted for video)
    ↓
human approved export / separately authorized scheduling
    ↓
content-seller metrics and learnings
```

"Existing authority gates adapted for video" does **not** mean static QA already covers time-based clipping, subtitles, flicker, audio, duration, codecs or aspect changes.

## Source and confidentiality discipline

- No NINFA brand identity, voice sample, media assets, transcripts or third-party content become generic default renderer fixtures.
- No private content-seller repository files or unpublished editorial assets are copied into this public knowledge domain.
- This document includes only interface-level observations and public-repository code facts needed to avoid duplicate architecture.
- No changes made to NINFA, prodAgentic or content-seller source from this research.

## Required next evidence

- Source-level read-only inventory of NINFA scene composition/FFmpeg entrypoints, versions, tests, external assumptions and actual licensing.
- Exact prodAgentic render lifecycle audit for video extension seams; ensure S5 PNG result and existing API remain compatible.
- Workstation preflight (WSL2/Docker, Chrome, FFmpeg, CPU/GPU) in an **authorized** environment.
- One fictional, no-publishing 9:16 Content Seller explainer experiment with original shapes/text/optional silent audio.
- Negative tests: network denied, font/asset missing, renderer timeout, invalid output, anti-duplicate editorial gate, wrong brand profile.
- Human evaluation and measured resource cost before integrating with release candidate.
