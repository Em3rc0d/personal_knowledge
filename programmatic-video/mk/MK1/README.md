# MK1 — Normalize & Classify

Status: **IN PROGRESS / NOT PROMOTED** (2026-10-07 America/Lima).

MK0 result: [PASS WITH LIMITATIONS](../MK0/CLOSURE.md). Only **source-discovery and first-party technical documentation** are eligible as source facts; claims about individual creator process remain excluded.

## Objective

Normalize research observations into stable, queryable concepts without importing third-party prompts as canonical workflows or converting collection labels into implementation truth.

## Slice 1

- [Taxonomy and contracts](TAXONOMY.md): record identity, provenance, rights, clocks/renderers and deduplication.
- [Fixture review](NORMALIZATION-RECEIPT.md): 8 records sampled and mapped to canonical statuses, with falsifiers and exceptions.
- [Cross-system audit](../../quarries/Q-005-content-ops-ninfa-integration-audit.md): Ninfa's documented video pipeline vs prodAgentic's existing PNG renderer; no migration certified.
- [NINFA code-level audit](../../quarries/Q-006-ninfa-code-reuse-audit.md): WAV/TTS module exists, general scene→MP4 executable not verified.
- [PV-POC-001 external sandbox proof](../../quarries/Q-007-pv-poc-001-local-proof.md): trusted authored Pillow/FFmpeg video exported twice with identical SHA; not a product or MK1 certificate.
- [PV-POC-003 Spanish neural voice proof](../../quarries/Q-008-piper-spanish-voice-poc.md): successful Piper GitHub Actions run; naturalness and product certification still open.
- [ADR-001 proposed ownership](ADR-001-VIDEO-OWNERSHIP-AND-REUSE.md): additive video port in prodAgentic; not accepted by prodAgentic's release authority.
- [Video handoff candidate](VIDEO-HANDOFF-CANDIDATE.md): typed request/result proposal, **not** an approved implementation or MK3 integration contract.
- Source data remains pinned to SHA `756290289742535eb0ac3817548f152e9759cc70`; do not mirror 513 prompts here.
- Any full-catalog machine normalization requires a follow-on proof and a decision about the maintenance burden.

## Boundaries

- `prompt_partial=false` means **CATALOG_UNMARKED**, never "complete confirmed".
- `tech_tags` are **catalog labels**, not reviewed original implementations.
- `post_url` is a pointer; direct contents may be `BLOCKED`.
- Rights/usage permission remain `UNKNOWN` unless checked for the actual media/asset.
- Videos marked "remake" require separate identity, lineage and rights from creator originals.
- MK1 taxonomies describe classification. They do not authorize executing prompts, installing renderers or autopublishing.

## MK1 acceptance gate

- [x] Minimal canonical field list and allowed values defined.
- [x] Identity and duplicate semantics separated.
- [x] Eight-fixture mapping documented across four categories and both partial flags.
- [ ] Review false-positive/false-negative errors on a broader sample (e.g. 24 diverse records) and refine heuristics.
- [ ] Validate a repeatable schema against every record WITHOUT copying raw protected material into `personal_knowledge`.
- [ ] Resolve explicit `UNKNOWN` routing for newly discovered tags, unclear reuse rights and source drift.
- [ ] Reviewer verifies that tests assert only catalog-level facts, not original-artifact truth.
- [ ] Record `CLOSURE.md` only after criteria pass.

Until those checks pass, MK1 is **OPEN**. Implementation is separately **BLOCKED** by runtime preflight.
