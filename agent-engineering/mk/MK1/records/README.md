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

## Current record set

| ID | System | State |
|---|---|---|
| R-001 | Minimal while-loop agent | CLASSIFIED |
| R-002 | HITL approval agent | CLASSIFIED / TEST-SUPPORTED |
| R-003 | Trace-evaluation harness | CLASSIFIED / TEST-SUPPORTED |
| R-004 | E2E testing agent | CLASSIFIED WITH SECURITY UNKNOWNS |
| R-005 | Self-healing code agent | CLASSIFIED WITH SECURITY UNKNOWNS |
| R-006 | HR messaging agent | CLASSIFIED WITH MATERIAL UNKNOWN |
| R-007 | Social publishing agent | CLASSIFIED WITH UNKNOWNS |
| R-008 | Document-intake agent | CLASSIFIED WITH UNKNOWNS |
| R-009 | DataScribe | CLASSIFIED WITH MATERIAL UNKNOWN |
| R-010 | Self-improving / reflection example | QUALIFIED — NOT PROVEN SELF-IMPROVING |
| R-011 | Memory-enhanced conversational agent | SOURCE CLAIM QUALIFIED |
| R-012 | Multi-agent collaboration system | CLASSIFIED / TAXONOMY COUNTEREXAMPLE |
| R-013 | MCP tutorial | LEGACY PROTOCOL CLASSIFICATION |
| R-014 | ShopGenie outbound email | CLASSIFIED WITH UNKNOWNS |
| R-015 | Car Buyer browser agent | CLASSIFIED WITH AUTHORITY QUALIFICATION |
| R-016 | External Conversation Buffer Memory | CROSS-SOURCE PRESSURE PASS |

## Coverage notes

- R-001..R-013 complete the original first classification queue.
- R-014/R-015 close the two P0 call-path gaps omitted from that initial queue.
- R-016 is the first classification outside the primary `GenAI_Agents` mining site, sourced from `Agent_Memory_Techniques`.

All nine MK0 P0 call-path families now have normalized records.

## Evidence hierarchy

```text
source/test observation
  > source documentation claim
  > inference with premises
  > unsupported assumption
```

Unsupported assumptions are not silently converted into fields; they remain `UNKNOWN`.

## Material pressure-test discoveries

The records caused concrete schema refinements:

1. `observed_class` and `reachable_class` are separate side-effect facts;
2. boolean-looking capability facts permit explicit `unknown`;
3. topology/model count and control authority are separate;
4. `deterministic_multi_role` represents fixed multi-role orchestration without implying model-directed control;
5. multi-agent records carry admission hypothesis, baseline, measured benefit and coordination-cost fields;
6. memory labels are normalized to scope/persistence/retrieval/write lifecycle evidence;
7. protocol support is revisioned, not boolean.

Detailed pressure-test ledger: [`../PRESSURE_TESTS.md`](../PRESSURE_TESTS.md).

## Current rule

A complete record can still be unsafe, unreliable, legacy or unresolved. Classification makes architecture explicit; certification remains a later MK concern.
