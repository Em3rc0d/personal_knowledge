# Railly Skills — System Architecture

Provenance: OBSERVED + INFERRED
Primary upstream: NORTH.md, README.md, foundry/, skills/, cases/, scripts/

## 1. The repository is a Foundry, not a prompt library

The installable skill is only the runtime tip.

Observed layers:

| Layer | Upstream surface | Responsibility |
|---|---|---|
| Direction | NORTH.md | product promise, bets, non-goals, success signals |
| Procedures | skills/ | compact runtime methods |
| Evidence | cases/, foundry/runs/ | retrievable work evidence |
| Live work state | foundry/missions/ | Issue Contracts and manifests |
| Knowledge | foundry/knowledge/ | patterns, provenance, gaps, impacts |
| Evolution | foundry/candidates/, foundry/rounds/ | proposals and promotion decisions |
| Registry | foundry/maturity.json | channel, type, maturity, decision |
| Enforcement | scripts/ | validators, compilers, identity checks |
| Execution roles | subagents/ | recon, implementation, review |
| Presentation | www/ | public catalog |

INFERRED: the architectural advantage comes from keeping these concerns separable. Evidence can grow without bloating runtime context; procedures can evolve without erasing their provenance.

## 2. Five planes

### Work plane

Owns progression of a bounded work item.

Key source:

- skills/.experimental/factory-loop/SKILL.md
- foundry/missions/
- scripts/lib/work-item-manifest.mjs

### Evidence plane

Owns what was actually observed and on which exact state.

Key concepts:

- repository/commit/dirty identity;
- command + environment;
- receipt;
- relevant paths;
- contract digest;
- skill revision;
- artifact;
- external/current-state recheck.

### Knowledge plane

Owns reusable conclusions without making them executable automatically.

Key source:

- foundry/knowledge/
- skills/record-a-case/
- foundry/candidates/2026-08-compiled-knowledge-layer/

### Procedure plane

Owns small callable methods with narrow trigger boundaries.

Important source rule from scripts/validate-skills.mjs:

- SKILL.md is capped at 120 lines;
- details are progressively disclosed through references/scripts;
- trigger fixtures distinguish positive and near-miss requests.

INFERRED: procedure compactness is an explicit context-budget mechanism.

### Governance plane

Owns whether a procedure exists in distribution and what its evidence supports.

Two independent axes:

- distribution channel: stable / candidate / experimental;
- evidence maturity: experimental / dogfooded / evaluated / validated / deprecated.

This prevents “easy to install” from meaning “proven”.

## 3. Source vs distribution

foundry/source-of-truth.md makes the canonical checkout the write location for Foundry artifacts.

Installed copies under agent directories are distribution artifacts. They may be read; they are not write destinations.

Portable mechanism:

    canonical authoring/evidence source
      ≠ runtime installation

This prevents local installed copies from silently fragmenting history.

## 4. Progressive disclosure

The compiled knowledge candidate explicitly separates:

- executing agent → promoted active procedure only;
- maintainer/proposer → compact knowledge index;
- deeper investigation → pattern/provenance page;
- dispute/proof → selected case/run evidence.

This architecture reduces cold start without flooding every task with history.

## 5. Failure-aware evolution

PAPERCUTS.md records workflow friction separately from:

- shipped-behavior issue;
- transferable case;
- active skill;
- promotion round.

That separation matters because operational friction, product defect and reusable method are different objects.

## 6. EM3RC0D implication

INSPIRED:

EM3RC0D Foundry should preserve this separation, but widen the reusable asset plane beyond skills. Product work can compile into code primitives, components, shells, design rules, tests and release recipes as well as procedures.
