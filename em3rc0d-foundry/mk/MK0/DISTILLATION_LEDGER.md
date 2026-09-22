# EM3RC0D Foundry — MK0 Distillation Ledger

Source: S-001 Railly/skills
Pinned commit: 77fdde3e8d7e13b7c27c7660f7c15619839e38af

## Coverage ledger

| Source surface | Directly inspected | Distilled destination | Status |
|---|:---:|---|---|
| NORTH.md | yes | 01, 07, 08 | done |
| README.md | yes | 01, 02 | done |
| PAPERCUTS.md | yes | 01, 11 | done |
| CHANGELOG.md | yes | cross-check | done |
| foundry/SHAPING.md | yes | 01, 07 | done |
| foundry/governance.md | yes | 07, 08 | done |
| foundry/eval-protocol.md | yes | 08 | done |
| foundry/case-template.md | yes | 07 | done |
| foundry/source-of-truth.md | yes | 01, 11 | done |
| foundry/maturity.json | yes | 08 | done |
| foundry/missions/* | yes | 03 | done |
| all registered SKILL.md | yes | 02–09 | done |
| skill trigger contracts | yes, core/all relevant families | 02, 08 | done |
| skill method evals | yes, core/risk families | 05, 06, 08 | done |
| review-gate gate catalog | yes | 06 | done |
| review proof obligations | yes | 06 | done |
| review run report contract | yes | 06, 11 | done |
| solution candidate audit | yes | 04 | done |
| solution failure-shape system | yes at catalog/method level | 04 | done |
| shaping orchestration | yes | 04, 09 | done |
| temporal contracts | yes | 04 | done |
| before-after references | yes | 10 | done |
| foundry/knowledge/* | yes | 07 | done |
| compiled knowledge candidate | yes | 07, 11 | done |
| usage receipt candidate | yes | 07, 09, 11 | done |
| promotion rounds 001–014 | yes | 08 | done |
| scripts/work-item.mjs | yes | 03, 11 | done |
| work-item manifest library | yes | 03, 11 | done |
| validate-skills | yes | 11 | done |
| knowledge compiler/validator | yes | 07, 11 | done |
| proposal packet/impact | yes | 07, 11 | done |
| usage compiler | yes | 07, 11 | done |
| skills doctor | yes | 11 | done |
| eval aggregator | yes | 08, 11 | done |
| textual match audit | yes | 07, 11 | done |
| subagents | yes | 09 | done |
| cases tree | complete inventory | 06, 07 | done |
| representative case logic | yes | 06–08 | done |
| foundry/runs tree | complete family inventory | 06–08 | done |
| every historical run file | no line-by-line paraphrase | raw corpus retained | intentionally not duplicated |
| www/ presentation | inventory + architecture role | 01, 10 | sufficient for MK0 |

## Why historical runs are not individually rewritten

The raw corpus contains hundreds of exact run artifacts, especially Review Gate. Rewriting every report into prose would:

- duplicate source;
- increase context;
- risk losing exact identity;
- turn retrieval evidence into narrative;
- provide little marginal value once recurring mechanisms are extracted.

The Foundry model learned from the source itself favors a compact compiled layer plus retrieval handles.

Therefore MK0 records the corpus structure and distilled mechanisms while retaining raw artifacts for claim-specific drill-down.

## Outstanding source drill-down

None required for the current MK0 architecture frame.

Future dogfood findings may reopen a specific upstream case, gate, eval or run as needed.
