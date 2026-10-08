# MK1 — Taxonomy and Normalization Contract

Class: `GENERATED` candidate contract, not yet certified.
Input source: `SRC-PV-001` / `data/videos.json` at commit `756290289742535eb0ac3817548f152e9759cc70`.

## Three layers: do not collapse

```text
SOURCE RECORD      (what catalog actually says, OBSERVED)
NORMALIZED RECORD  (controlled labels + claims with provenance, GENERATED)
REPRODUCTION RUN   (separate experimentally measured execution, NOT CREATED)
```

The normalizer cannot create truth missing from the source. In particular, no "VIDEO_PROVEN" status is inferred from the record's existence.

## Minimal canonical record contract

| Field | Allowed values / semantics |
|---|---|
| `record_id` | `SRC-PV-001:<slug>`; stable only within pinned snapshot |
| `source_commit` | exact SHA |
| `catalog_category` | `MOTION | EXPLAINER | INTERACTIVE | SCENE_3D | OTHER` |
| `tagged_technologies` | array from allowlist `CANVAS,SVG,THREEJS,SHADER,GSAP,CSS,AUDIO,PARTICLES,PLAYABLE,PIXEL,AI_IMAGE,WEBGL,PHYSICS` or `UNKNOWN_TAG`; retain raw unknown tag |
| `prompt_coverage` | `CATALOG_PARTIAL` when `prompt_partial=true`; `CATALOG_UNMARKED` otherwise |
| `prompt_storage` | `UPSTREAM_POINTER_ONLY` by default; never mirror raw prompt into normalized canon |
| `original_post_access` | `POINTER_ONLY | ACCESSIBLE | BLOCKED | DEAD`; default `POINTER_ONLY`, `BLOCKED` for observed fetch failures |
| `original_claim_verification` | `UNVERIFIED | VERIFIED | CONTRADICTED | INCONCLUSIVE`; default `UNVERIFIED` |
| `media_rights` | `UNKNOWN | VERIFIED_PERMITTED | RESTRICTED | NOT_APPLICABLE`; default `UNKNOWN` |
| `technology_evidence` | `CATALOG_TAG | INSPECTED_REMAKE | INSPECTED_ORIGINAL_IMPLEMENTATION | EXPERIMENTALLY_REPRODUCED`; default `CATALOG_TAG` |
| `animation_clock` | `UNKNOWN | WALL_CLOCK | SEEKABLE_TIME | FRAME_FUNCTION`; default `UNKNOWN` |
| `renderer` | `UNKNOWN | HYPERFRAMES | REMOTION | CUSTOM_FFMPEG | OTHER`; catalog has no assumed renderer |
| `cost_evidence` | `UNKNOWN | MEASURED_LOCAL | MEASURED_CLOUD`; default `UNKNOWN` |
| `reproduction_status` | `NOT_TESTED | BLOCKED | PASS | PASS_WITH_LIMITATIONS | FAIL`; default `NOT_TESTED` |
| `inference_notes` | bounded hypotheses only, explicit provenance |
| `source_url` | original `post_url` pointer plus record's original repository path/version |

## Primary normalization rules

1. `category: motion → MOTION`; `explainer → EXPLAINER`; `interactive → INTERACTIVE`; `3d → SCENE_3D`. Unexpected value → `OTHER`, emit unknown-tag review.
2. `tech_tags` must be mapped one-by-one and retain the original token for unknowns. These are **tags attributed by the dataset**, not verifications of generated code.
3. `prompt_partial: false` maps to `CATALOG_UNMARKED`, **never** `FULL`.
4. A post `url` alone maps to `POINTER_ONLY`. A failed fetch with receipt can upgrade *access status* to `BLOCKED`, not verification to `CONTRADICTED`.
5. `source_commit` and `record_id` are mandatory; source edits create new snapshot/version records and do not silently mutate previous observations.
6. A renderer is not inferred from `threejs`/`gsap`/`canvas`; those describe techniques/runtimes, not the export stack.
7. Licensing can differ for catalog files, copied prompt text, creator video, remake, fonts, sound and code generated in our tests; do not use one boolean `licensed`.
8. `provenance` is per **claim**, not merely a per-file badge. A fact from dataset is `OBSERVED`; our class mapping is `GENERATED`; conclusions about likely video performance are `INFERRED`.
9. `reproduction_status` can advance only with an `experiment_receipt` referencing version, input, media, frame verification and test result.
10. Empty or strange prompt text does not invalidate identity: emit `QUALITY_REVIEW` if appropriate, never silently discard records.

## Identity, exact duplicate, and semantic relation

Three independent entities:

- `record_id`: one catalog entry, even if text repeats.
- `exact_text_cluster`: derived by lowercasing, whitespace normalization and limited final punctuation trim on source prompt text. Clustering is **diagnostic** and only within a pinned snapshot; never drops an entry.
- `semantic_family`: REVIEW_REQUIRED label after comparing prompt purpose, scene specification, inputs and differences. Identical text does not imply identical output; similar meaning does not imply interchangeable copyright or attribution.

Example: the recurring generic 15-second showreel prompt can group multiple entries by text, while preserving all author/URL/event identities.

## Anti-inference rules

```text
CATALOG_UNMARKED   != VERIFIED_COMPLETE
CATALOG_TAG        != INSPECTED_SOURCE_CODE
URL                != ACCESSIBLE_POST
REMAKE_VISIBLE     != INDEPENDENT_BENCHMARK
MIT_REPO_LICENSE   != EXTERNAL_VIDEO_LICENSE
NO_PAID_API        != ZERO_RENDER_COST
SAME_PROMPT_TEXT   != SAME_CREATOR_OR_OUTPUT
RENDERER_README    != OUR_RUNTIME_PASS
```

## Taxonomy tests required before closure

- All 513 records have `record_id`, non-null category mapping, explicit coverage and rights default.
- Number of transformed rows = input rows (no dedupe-based deletion).
- 4 catalog categories map deterministically; unknown values routed to review.
- One record in at most one *exact text cluster*, but repeated text across different identities is preserved.
- Replays from the same pinned commit produce identical classification records after excluding non-deterministic capture metadata.
- Both positive and negative fixtures for `BLOCKED`, unknown tag and denied asset rights.
- No generated record may state `VERIFIED` attribution from catalog-only inputs.

### Output position

MK1 can produce a compact derived manifest and fixtures; it does **not** need to store third-party prompts or source media.
