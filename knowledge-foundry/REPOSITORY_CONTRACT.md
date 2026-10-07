# Knowledge Foundry — Repository Contract

## Purpose

This contract prevents educational productization from corrupting the source-of-truth structure of `personal_knowledge`.

## Authority model

| Question | Authority |
|---|---|
| Is a technical claim true? | Source domain canon |
| Why do we believe it? | Source domain evidence/quarries/mining-site |
| How should it be taught? | Knowledge Foundry |
| Is a product pedagogically demonstrated? | Knowledge Foundry pilot/evaluation evidence |
| Is it commercially viable? | Commercial evidence, not technical canon |
| Can external text/assets be reused? | Source license + explicit usage boundary |

## Non-negotiable rules

1. **No canon duplication.** Knowledge Foundry links to domain canon instead of cloning it.
2. **No quarry-to-course shortcut.** Non-canonical research cannot silently become instructional truth.
3. **No source laundering.** Paraphrasing copyrighted or restricted material does not erase provenance/licensing obligations.
4. **No popularity-as-proof.** Stars, views, likes and reputation are discovery signals, not technical or pedagogical evidence.
5. **No draft-as-product.** A generated curriculum is not a validated course.
6. **No technical-truth/pedagogy collapse.** Correct information can still be taught badly.
7. **No pedagogical-truth/commercial-truth collapse.** A useful course may still have no market.
8. **No silent mutation upstream.** Knowledge Foundry does not rewrite other domain canon as a side effect.
9. **Unknown remains UNKNOWN.**
10. **Promotion requires evidence.**

## Provenance classes

Use the monorepo classes:

- `OFFICIAL`
- `OBSERVED`
- `INFERRED`
- `INSPIRED`
- `GENERATED`

Educational artifacts must additionally identify whether source material is:

- `REFERENCE_ONLY` — may support claims; do not reproduce.
- `TRANSFORMABLE` — transformation permitted under known terms.
- `REUSABLE` — direct reuse permitted under known terms.
- `UNKNOWN_LICENSE` — commercial promotion blocked until resolved.

These labels are Knowledge Foundry operational metadata; they do not replace legal advice or the source license.

## Promotion path

```text
source/domain canon
      ↓
candidate
      ↓
draft educational artifact
      ↓
assessment + pilot evidence
      ↓
review
      ↓
promotion decision
      ↓
released product
```

## State model

Suggested product states:

`IDEA → DRAFT → PILOT → VALIDATED → RELEASED → MAINTENANCE → RETIRED`

`VALIDATED` means the declared pedagogical gate passed. It does not imply commercial success.

## Branch discipline

Follow the root repository convention:

`knowledge/<domain>-<mk>-<purpose>`

`main` remains canonical. Workspaces evolve on branches and merge only after their active MK gates and review requirements are satisfied.
