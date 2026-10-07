# Quarry — personal_knowledge Readiness Audit

Observed: 2026-10-07  
Status: **NON-CANONICAL / repository audit**

## Purpose

Determine what Knowledge Foundry may safely consume today without pretending every domain has equal maturity.

## Structural findings

| Domain | Current state | Foundry input posture |
|---|---|---|
| `agent-engineering` | MK1 active; MK0 closed; bounded Strands package solidified | `ELIGIBLE_WITH_LIMITATIONS` for explicitly solidified/promoted slices only |
| `jett-engineering-method` | MK1 active; MK0 internal canon foundation closed | `ELIGIBLE_WITH_LIMITATIONS` for MK0 foundation / explicitly stable contracts |
| `em3rc0d-foundry` | STATUS says MK0 closed + MK1 dogfood admitted; README/LLM metadata stale | `BLOCKED_METADATA` until routing metadata is synchronized |
| `content-strategy` | MK0 active; hypotheses/profile-specific evidence | `RESEARCH_ONLY` by default |
| `web-design` | MK0 active; operational rules not certified | `RESEARCH_ONLY` by default |
| `ux-laws` | MK0 active; source/original evidence and licensing gaps open | `RESEARCH_ONLY` |
| `openship` | MK0 active; cross-check/threat-model/documentation-drift work open | `RESEARCH_ONLY` |
| `research-corpora` | evidence preservation layer | never direct instructional canon |

## Gap A — control-plane asymmetry

`agent-engineering` and `em3rc0d-foundry` have full control-plane files:

- ROADMAP;
- REPOSITORY_CONTRACT;
- KNOWLEDGE_MAP;
- LLM_CONTEXT.

Other domains are intentionally lighter.

Conclusion: do **not** require identical folder shapes. Knowledge Foundry should rely on the Domain Input Contract rather than "file exists" heuristics.

## Gap B — Source Intake adoption debt

The JEM Source Intake Contract is newer than several domain registries.

Older registries often omit some independent dimensions such as:

- access state;
- capture state;
- verification state;
- promotion state;
- supported/not-supported claims;
- exact observation boundary.

Conclusion: missing fields are `UNKNOWN`. Do not retroactively infer them from a URL or a source-list entry.

## Gap C — status drift

`em3rc0d-foundry/STATUS.md`:
`MK0 CLOSED · MK1 DOGFOOD ADMITTED`.

But:

- `em3rc0d-foundry/README.md` says MK0 active;
- `em3rc0d-foundry/LLM_CONTEXT.md` says `current_mk: MK0`;
- root README describes it as currently MK0.

This can misroute humans/agents and should be synchronized against STATUS/ROADMAP.

## Gap D — repository licensing posture

No root LICENSE file exists.

This means Knowledge Foundry must not infer open-source/open-content reuse rights for our own repository material, while third-party corpora retain their own licenses.

## Gap E — educational evidence missing

Before this audit, the repo contained no dedicated evidence package for:

- retrieval/spaced learning;
- worked examples;
- assessment validity/reliability/fairness;
- UDL;
- WCAG 2.2 as educational-delivery baseline;
- course-content rights licensing;
- learner-pilot data boundaries.

These gaps are being patched as S-002 through S-006 and corresponding architecture/quarry artifacts.

## Dogfood implication

Do not choose an entire domain as "the course source".

Choose a **bounded eligible slice**, pin its revision, and compile a capability from that slice.
