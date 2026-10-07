# EM3RC0D Foundry — MK1

Status: **ACTIVE — DOGFOOD-001 / B0 CAPTURED**

MK1 exists to test the generated Foundry model against real work.

The first pressure test is Future Wardrobe RC1.

## Current experiment

`DOGFOOD-001 — Future Wardrobe RC1 Recovery and Closure`

Current phase:

```text
B0 recovery baseline      ✅ captured
F1 / Vercel web slice     ✅ PASS / bounded
F1 / Railway diagnosis    ✅ read-only complete
F1 / staging dependency   🔒 next exact action pending
F2 recovery test          🔒 waits on F1
MK1 verdict               🔒 waits on evidence
```

## Active artifacts

- `DOGFOOD-001-B0-RECOVERY.md` — observed recovery baseline.
- `DOGFOOD-001-WORK-CONTRACT.md` — compact current-state contract and exact next action.
- `DOGFOOD-001-STATE.json` — machine-readable state for later re-entry.
- `DOGFOOD-001-F1-VERCEL.md` — executed first F1 slice and bounded proof.
- `DOGFOOD-001-F1-RAILWAY-DIAGNOSIS.md` — read-only diagnosis of worker readiness/dependency boundary.

## Constraint

Do not expand MK1 schemas speculatively.

Only add a field/artifact when DOGFOOD-001 demonstrates a consumer for it.
