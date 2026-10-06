# Knowledge Foundry — LLM Context

## Role

This file tells an agent how to reason inside `knowledge-foundry/` without confusing productization with source truth.

## Read order

For current-state work:

1. `STATUS.md`
2. `ROADMAP.md`
3. `REPOSITORY_CONTRACT.md`
4. active `mk/*` artifacts
5. only then descend into quarries/sources when provenance is needed.

## Routing rules

- Technical truth belongs to the source domain.
- Educational design belongs here.
- Raw source evidence is never promoted directly into course claims.
- Prefer pointers to source-domain canon over duplication.
- A course draft is GENERATED until evidence promotes it.
- Pedagogical claims require learner/assessment evidence.
- Commercial claims require market evidence.
- License uncertainty blocks commercial promotion when reuse rights matter.

## Anti-inference rules

Do not infer:

- `popular source → correct source`;
- `correct source → teachable curriculum`;
- `good curriculum → effective course`;
- `effective course → commercial demand`;
- `MIT repository → every linked asset/source is MIT`;
- `paraphrased → free of licensing/provenance concerns`;
- `pilot passed once → reliable for all audiences`;
- `agent says complete → verified release`.

## Current MK

MK0 is active.

Do not write `MK0/CLOSURE.md`, activate MK1, or mark a product RELEASED unless the corresponding gates actually pass.
