# EM3RC0D Foundry — Candidate Knowledge Graph

Provenance: GENERATED + INSPIRED
Status: MK0 candidate.

## Goal

Extend Railly’s compiled skill knowledge into a general reusable-capital graph.

## Candidate node classes

### Evidence

- source;
- observation;
- run;
- artifact;
- external review;
- production observation;
- market signal.

### Work knowledge

- case;
- decision;
- assumption;
- gap;
- contradiction.

### Transferable knowledge

- pattern;
- antipattern;
- invariant;
- heuristic;
- failure shape.

### Reusable capital

- skill/procedure;
- code primitive;
- UI component;
- product shell;
- design rule/token set;
- architecture pattern;
- test harness;
- evaluation;
- deployment recipe;
- observability recipe;
- research method;
- documentation template.

### Product entities

- work item;
- product;
- version/release;
- user-facing capability.

## Candidate relationship types

From evidence to knowledge:

- originates;
- applies;
- evaluates;
- transfers;
- contradicts;
- rejects;
- supersedes.

From knowledge to reusable capital:

- motivates;
- supports;
- constrains;
- contradicts;
- supersedes;
- implements.

From reusable capital to product:

- used-by;
- generated-by;
- validated-on;
- failed-on;
- replaced-by.

## Relationship state

Candidate lifecycle:

- candidate;
- active;
- contradicted;
- superseded;
- stale;
- deprecated.

Status must not erase historical edges.

## Evidence strength

A relationship needs:

- provenance;
- exact source handle;
- date/state identity when drift-prone;
- claim boundary;
- visibility;
- confidence only when meaningful.

Do not transform “mentioned in file” into “applied”.

## Promotion destinations

When a case closes, exactly one primary knowledge disposition should be selected:

- link existing pattern;
- create candidate pattern;
- create/update reusable asset candidate;
- add deterministic guard;
- add eval;
- record coverage gap;
- no change.

Unlike the source, EM3RC0D may need a second dimension for asset type because not every reusable lesson is procedural.

## Generated projections

Future compiler may generate:

- compact index;
- coverage matrix;
- provenance graph;
- asset dependency graph;
- maturity gaps;
- stale links;
- transfer map.

These are projections, not authored truth.

## Runtime boundary

Ordinary product-building agents should query:

- current Work Contract;
- relevant active asset;
- compact index when retrieval is needed.

They should not automatically receive:

- all cases;
- all failed proposals;
- all raw runs;
- private telemetry;
- unrelated product history.

Evolution agents/reviewers may access broader Foundry context under explicit scope.

## Key invariant

The knowledge graph exists to reduce rediscovery while preserving uncertainty.

If compilation makes weak evidence look stronger, the graph has failed.
