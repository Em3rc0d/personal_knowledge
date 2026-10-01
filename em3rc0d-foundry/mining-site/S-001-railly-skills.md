# S-001 — Railly Skills

Provenance: **OFFICIAL + OBSERVED**
Source type: public GitHub repository
Repository: https://github.com/Railly/skills
Pinned commit: 77fdde3e8d7e13b7c27c7660f7c15619839e38af
Pinned root tree: 701944bade5f718381446a7cd9224ed01ea1f952
Observed commit date: 2026-09-02
License: MIT
Local raw snapshot: ../../research-corpora/railly-skills-2026-09-22/upstream/

## Why this source matters

The repository is not only a catalog of agent prompts. It contains:

- installable procedures;
- phase routing;
- exact-state work manifests;
- deterministic validation machinery;
- evidence ledgers;
- behavior evaluations;
- promotion/deprecation history;
- compiled provenance;
- proposal-impact memory;
- large review/run corpora;
- runtime adapters and subagent role definitions.

It therefore provides a real, evolving example of a personal engineering Foundry.

## Tree inventory

At the pinned commit:

| Surface | Files | Approx. bytes | Function |
|---|---:|---:|---|
| foundry/ | 1,013 | 18,014,086 | runs, decisions, candidates, knowledge, missions, maturity |
| cases/ | 113 | 731,788 | case records + repo conventions |
| skills/ | 101 | 490,129 | 20 registered procedure packages |
| scripts/ | 42 | 195,779 | validators, compilers, manifests, eval tooling |
| subagents/ | 4 | 10,712 | recon / implementation / review role surfaces |
| www/ | 24 | 174,985 | public presentation |
| other root/config | remainder | | direction, license, marketplace, CI |

The cases directory contains 28 repository convention files plus historical/observational supporting files; raw file count must not be presented as a count of independently validated cases.

## Registered skills

The machine-readable maturity registry has 20 entries:

- stable: issue-intake, record-a-case, review-gate, solution-gate;
- candidate channel: trail-decisions, signature-repro;
- experimental channel: before-after, handoff, herdr-workstreams, quality-baseline, performance-proof, test-strength, resilience-audit, security-review, simplify, work-intake, workstream-reconcile, xref, software-factory, factory-loop.

Maturity is separate from distribution channel. The snapshot includes experimental, dogfooded and evaluated states; no blanket “all validated” claim is supported.

## High-value source surfaces directly inspected

Direction and governance:

- NORTH.md
- README.md
- PAPERCUTS.md
- CHANGELOG.md
- foundry/README.md
- foundry/SHAPING.md
- foundry/governance.md
- foundry/eval-protocol.md
- foundry/source-of-truth.md
- foundry/case-template.md
- foundry/maturity.json

State and knowledge:

- foundry/missions/
- foundry/knowledge/
- foundry/candidates/2026-08-compiled-knowledge-layer/
- foundry/candidates/2026-08-usage-receipts/
- foundry/rounds/

Procedures:

- all 20 registered SKILL.md files;
- core trigger/eval contracts;
- Review Gate gate/proof/report references;
- Solution Gate shaping, candidate-audit and temporal-contract references;
- Before After capture/visual references.

Executable machinery:

- scripts/work-item.mjs
- scripts/lib/work-item-manifest.mjs
- scripts/validate-skills.mjs
- scripts/validate-issue-contracts.mjs
- scripts/compile-knowledge.mjs
- scripts/validate-knowledge.mjs
- scripts/build-proposal-packet.mjs
- scripts/record-impact.mjs
- scripts/compile-usage-receipts.mjs
- scripts/skills-doctor.mjs
- scripts/aggregate-skill-eval.mjs
- supporting knowledge/audit libraries.

Corpus evidence:

- complete tree inventory of case and run families;
- case inventory and representative cases;
- promotion rounds;
- run-family distribution.

## Observed run families

The Foundry run corpus is heavily weighted toward review evidence. At the pinned tree:

- review-gate: 616 files;
- solution-gate: 149;
- security-review-eval: 38;
- resilience-audit: 21;
- xref: 18;
- proposal-impact: 15;
- test-strength: 15;
- spec: 8;
- before-after: 4;
- software-factory: 3;
- quality-baseline: 2.

These are artifact counts, not independent success counts.

## Source limitations

- Much evidence originates from one practitioner’s workflow and repositories.
- Several procedures are intentionally experimental.
- Some promotions are explicit human overrides with evidence debt.
- Tooling contains Railly/Vercel-specific runtime assumptions.
- Historical prose can lag machine state. Example: NORTH.md describes 19 registered skills while maturity.json at the pinned commit contains 20.
- A large run corpus demonstrates use and iteration but does not itself prove transfer or causal improvement.

## Legal boundary

MIT permits use, copying, modification and redistribution subject to preserving the copyright and permission notice in copies or substantial portions.

The raw snapshot preserves LICENSE verbatim.

## Freshness

This receipt is valid for the pinned commit. A later upstream refresh must be a new receipt or explicit superseding snapshot, not a silent overwrite.
