# Architecture

Defines how UX-law knowledge is represented, connected, queried and consumed by humans or agents.

## Target architecture

```text
Sources
  ↓
Mining Registry
  ↓
Quarry Dossiers
  ↓
Normalized Knowledge Graph
  ↓
Operational Rules
  ↓
Design-System Mappings
  ↓
Product / Agent Consumers
  ↓
Verification Evidence
```

## Architectural concerns

- stable law IDs;
- source/provenance links;
- relationships and conflicts;
- applicability predicates;
- confidence and evidence strength;
- machine-readable rule contracts;
- versioning across MKs;
- traceability from implementation back to evidence.

MK0 defines the boundaries; later MKs close the schemas.
