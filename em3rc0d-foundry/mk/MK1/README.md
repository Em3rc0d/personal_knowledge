# EM3RC0D Foundry — MK1

Status: **ACTIVE — MULTI-DOGFOOD**

MK1 exists to test the generated Foundry model against real work.

Pressure tests:

1. `DOGFOOD-001` — Future Wardrobe RC1; currently HOLD on over-quota/inactive external infrastructure after bounded Vercel PASS.
2. `DOGFOOD-002` — em3rc0d Portfolio; B0/F1/F2/F3 reached HUMAN REVIEW with two exact-head green, unmerged portfolio PRs.

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
- `DOGFOOD-002-PORTFOLIO-B0.md` — portfolio baseline and one-file evidence-sync slice.
- `DOGFOOD-002-STATE.json` — compact exact-state record for DOGFOOD-002.
- `DOGFOOD-002-F2-REENTRY.md` — bounded compact re-entry sufficiency check.
- `DOGFOOD-002-F3-CLAIM-AUDIT.md` — public flagship claim audit with KEEP/CORRECT dispositions.

## Constraint

Do not expand MK1 schemas speculatively.

Only add a field/artifact when DOGFOOD-001 demonstrates a consumer for it.
