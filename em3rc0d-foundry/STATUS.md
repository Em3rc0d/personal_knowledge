# EM3RC0D Foundry — Status

Updated: 2026-09-22
State: **MK0 ACTIVE**

## Current truth

| Surface | State |
|---|---|
| Railly/skills raw snapshot | PASS — exact upstream tree preserved |
| Upstream provenance and MIT license | PASS |
| Repository structural inventory | PASS |
| Core Foundry governance | DISTILLED |
| 20 registered skill contracts | DISTILLED by functional family |
| Eval/trigger contracts | DISTILLED |
| Promotion rounds and lifecycle history | DISTILLED |
| Compiled knowledge layer | DISTILLED |
| Work-item manifest / exact-state machinery | DISTILLED |
| Review gate catalog | DISTILLED at architecture/rule-family level |
| Cases corpus | INVENTORIED + representative lessons traced |
| Run corpus | INVENTORIED by run family; not every historical run re-narrated |
| Railly-specific runtime dependencies | SEPARATED from portable mechanisms |
| Initial EM3RC0D Foundry model | GENERATED / not promoted |
| First real EM3RC0D dogfood cycle | NOT STARTED |
| MK0 closure | OPEN |

## Corpus identity

Source: Railly/skills
Commit: 77fdde3e8d7e13b7c27c7660f7c15619839e38af
Root tree: 701944bade5f718381446a7cd9224ed01ea1f952
Raw snapshot: ../research-corpora/railly-skills-2026-09-22/upstream/

Observed repository tree at the pinned commit:

- 1,323 files total.
- foundry/: 1,013 files, approximately 18 MB.
- cases/: 113 files.
- skills/: 101 files.
- scripts/: 42 files.
- subagents/: 4 files.
- www/: 24 files.
- foundry/maturity.json currently registers 20 skills.

Historical prose in NORTH.md says 19 registered skills. The machine-readable maturity registry at the pinned commit contains 20. For current catalog count, the registry wins; the discrepancy is preserved as evidence that prose can lag state.

## What “distilled” means here

The full repository tree was inventoried. The architecture and control model were derived by directly reading:

- root direction/governance documents;
- all registered SKILL.md contracts;
- their trigger/eval contracts where present;
- high-value reference contracts for shaping, proof and review;
- Foundry maturity, cases, rounds, knowledge and proposal-impact surfaces;
- work-item, knowledge, validation, usage-receipt and installation scripts;
- representative case/run families and corpus-level counts.

MK0 does **not** claim that every one of the hundreds of historical run reports has been manually paraphrased line by line. Those artifacts remain retrievable raw evidence. The distillation preserves their role and the recurring mechanisms they support without duplicating the full corpus.

## Current blocker

The primary MK0 blocker is no longer source understanding. It is **adaptation validation**:

Which proposed EM3RC0D Foundry mechanisms survive contact with a real EM3RC0D product without adding more coordination cost than they save?

That answer requires dogfood, not more speculative architecture.
