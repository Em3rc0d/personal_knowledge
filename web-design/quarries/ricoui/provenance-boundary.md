# RICOUI Quarry — Provenance Boundary

## Objective

Prevent source-derived observations from silently becoming authoritative domain facts.

## Required lineage

```text
external source
    ↓
source record
    ↓
evidence / observation
    ↓
inference
    ↓
adopted design rule
    ↓
generated artifact
```

## Example

```yaml
id: WD-RICOUI-001
claim: DESIGN.md is the canonical document in RICOUI's document model
provenance:
  type: OFFICIAL
  source: SRC-RICOUI
status: EVIDENCE
```

A derived rule would be recorded separately:

```yaml
id: WD-DS-001
rule: A substantial website should maintain one canonical semantic design contract.
provenance:
  type: INSPIRED
  derived_from:
    - source: SRC-RICOUI
      evidence: WD-RICOUI-001
status: CANDIDATE
```

## Confidence

Use confidence only where uncertainty matters:

```yaml
confidence: high
```

or, if numerical scoring is later formalized, according to a documented calibration scheme. Arbitrary pseudo-precision such as `0.94` must not be used unless the scoring semantics are defined.

## Promotion rule

A quarry statement may be promoted only when:

1. provenance is explicit;
2. the source supports the claim at the stated level;
3. inference is separated from observation;
4. copyright/licensing boundaries are respected;
5. applicability limits are documented;
6. contradictions are resolved or carried forward explicitly.
