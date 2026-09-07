# MK1 — Classification Records

Status: **ACTIVE / EVIDENCE-BACKED NORMALIZATION**

This directory contains one normalized record per representative system. Records are architecture/evidence descriptions, not production certifications.

## Record contract

Each record should:

1. pin source and snapshot;
2. classify control separately from topology;
3. enumerate reachable capabilities, not only intended use;
4. distinguish observed vs reachable side effects;
5. preserve `UNKNOWN` for unsupported material facts;
6. state evidence basis and quarry/source paths;
7. record schema pressure discovered by the example;
8. avoid framework names as top-level architecture classes.

## First classification set

| ID | System | State |
|---|---|---|
| R-001 | Minimal while-loop agent | CLASSIFIED |
| R-002 | HITL approval agent | CLASSIFIED |
| R-003 | Trace-evaluation harness | CLASSIFIED |
| R-004 | E2E testing agent | CLASSIFIED |
| R-005 | Self-healing code agent | CLASSIFIED |
| R-006 | HR messaging agent | CLASSIFIED WITH UNKNOWNS |
| R-007 | Social publishing agent | CLASSIFIED WITH UNKNOWNS |
| R-008 | Document-intake agent | CLASSIFIED WITH UNKNOWNS |
| R-009 | DataScribe | CLASSIFIED WITH UNKNOWNS |
| R-010 | Self-improving / reflection example | QUALIFIED |
| R-011 | Memory-enhanced conversational agent | CLASSIFIED |
| R-012 | Multi-agent collaboration system | CLASSIFIED / TAXONOMY COUNTEREXAMPLE |
| R-013 | MCP tutorial | LEGACY PROTOCOL CLASSIFICATION |

## Evidence hierarchy

```text
source/test observation
  > source documentation claim
  > inference with premises
  > unsupported assumption
```

Unsupported assumptions are not silently converted into fields; they remain `UNKNOWN`.

## Important pressure-test discoveries

The first records already require two distinctions now encoded in MK1:

- `observed side effect` vs `reachable side effect`;
- `model count/topology` vs `control authority`.

A deterministic five-step multi-role workflow is not model-directed merely because two role agents participate. Likewise, a harmless shell demo is not low-authority merely because the observed command was benign.
