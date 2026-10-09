# MK1 — Primer recibo de normalización (8 fixtures)

Date: 2026-10-07 America/Lima.
Class: `OBSERVED` (input JSON counts) + `GENERATED` (mapping). Source: `SRC-PV-001` at commit `756290289742535eb0ac3817548f152e9759cc70`.
Status: **PARTIAL FIXTURE / NOT A FULL-CORPUS NORMALIZER**.

## Method

Read all 513 input records from the pinned dataset to validate identity uniqueness and original categories, then map only 8 selected records from Q-003 (one flagged/unflagged pair per category). The underlying post bodies and author-created videos were not inspected. These are catalog-facing records, not verified original works. No prompt body or audiovisual work is copied.

## Structural checks (dataset-level)

- `rows`: **513**
- unique `slug` keys: **513**
- duplicate `slug` keys: **0**
- category counts after deterministic mapping: `MOTION=317` · `EXPLAINER=67` · `INTERACTIVE=70` · `SCENE_3D=59`
- all selected fixture slugs resolved: **8/8**

## Fixture mapping

| ID (`SRC-PV-001:<slug>`) | Category | Source partial | Normalized coverage | Catalog tech tags | Original access | Runtime | Rights | Reproduction |
|---|---|---|---|---|---|---|---|---|
| `0xevinho-436195` | `MOTION` | `false` | `CATALOG_UNMARKED` | `canvas, particles, pixel` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `0xrapzz-433554` | `MOTION` | `true` | `CATALOG_PARTIAL` | `canvas, svg, gsap` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `0xnfrith-068999` | `EXPLAINER` | `false` | `CATALOG_UNMARKED` | `svg, gsap` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `konstantinsaifo-501736` | `EXPLAINER` | `true` | `CATALOG_PARTIAL` | `threejs, shader` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `0xchuckstock-879327` | `INTERACTIVE` | `false` | `CATALOG_UNMARKED` | `threejs, shader, playable` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `0xpai-eth-635565` | `INTERACTIVE` | `true` | `CATALOG_PARTIAL` | `canvas, pixel, playable` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `alexalbert-274839` | `SCENE_3D` | `false` | `CATALOG_UNMARKED` | `threejs, shader, canvas` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |
| `0xsolty-735200` | `SCENE_3D` | `true` | `CATALOG_PARTIAL` | `shader, webgl` | `BLOCKED` | `UNKNOWN` | `UNKNOWN` | `NOT_TESTED` |

`original_post_access=BLOCKED` is supported by the eight fetch-failure receipts documented in [Q-003](../../quarries/Q-003-original-post-access-audit.md); the field describes **access**, not validity or creator identity. `technology_evidence=CATALOG_TAG` and `original_claim_verification=UNVERIFIED` apply to all eight. External media rights default `UNKNOWN`.

## Adversarial review requirements

1. Take one `CATALOG_UNMARKED` entry and verify it does **not** become "full prompt" or "originally verified".
2. Take one `CATALOG_PARTIAL` entry and verify nobody infers its precise missing instructions.
3. Create a synthetic unknown tech tag and route to `UNKNOWN_TAG` without dropping the record.
4. Confirm duplicate prompt text across multiple authors does not collapse `record_id`.
5. Confirm no renderer or resource license is inferred from technique tags.
6. Record a denied rights case and prevent rehosting external media.

## Finding

The scoped mapping is deterministic for the current eight rows and preserves missing evidence. However, **no standalone normalizer, semantic-clustering review or full-schema compliance test has been implemented**. MK1 remains **OPEN** until broader coverage, negative fixtures and review.
