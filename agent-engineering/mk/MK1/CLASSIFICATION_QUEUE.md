# MK1 — Classification Queue

Status: **ACTIVE — FIRST SET COMPLETE**

MK1 began with systems already supported by strong MK0 evidence, then expands into independent pressure tests before schema freeze.

## First classification set — COMPLETE

| ID | System | Result |
|---|---|---|
| R-001 | minimal while-loop agent | CLASSIFIED |
| R-002 | HITL approval agent | CLASSIFIED / TEST-SUPPORTED |
| R-003 | trace-evaluation harness | CLASSIFIED / TEST-SUPPORTED |
| R-004 | E2E testing agent | CLASSIFIED |
| R-005 | self-healing code agent | CLASSIFIED |
| R-006 | HR messaging agent | CLASSIFIED WITH UNKNOWN |
| R-007 | social publishing agent | CLASSIFIED WITH UNKNOWNS |
| R-008 | document-intake agent | CLASSIFIED WITH UNKNOWNS |
| R-009 | DataScribe | CLASSIFIED WITH UNKNOWN |
| R-010 | self-improving/reflection example | QUALIFIED |
| R-011 | memory-enhanced conversational agent | SOURCE CLAIM QUALIFIED |
| R-012 | multi-agent collaboration system | CLASSIFIED / TAXONOMY COUNTEREXAMPLE |
| R-013 | MCP tutorial | LEGACY PROTOCOL CLASSIFICATION |

Records: [`records/`](./records/)

## P0 completion additions

The original first set omitted two MK0 P0 call paths. They were added before declaring P0 classification coverage complete:

| ID | System | Result |
|---|---|---|
| R-014 | ShopGenie outbound email | CLASSIFIED WITH UNKNOWNS |
| R-015 | Car Buyer browser agent | CLASSIFIED WITH AUTHORITY QUALIFICATION |

This means all nine P0 call-path families from the MK0 verification quarry now have normalized MK1 records.

## Cross-source pressure test

| ID | Source | System | Result |
|---|---|---|---|
| R-016 | `Agent_Memory_Techniques@b7f7240e...` | Conversation Buffer Memory | PASS — existing schema sufficient |

This is the first record outside the primary `GenAI_Agents` mining site.

## Why the first set mattered

It covered the dimensions most likely to expose overlap or ambiguity:

- deterministic vs model-directed control;
- shell/generated-code/browser authority;
- external messaging/publication/data egress;
- dispatcher-enforced HITL;
- state/checkpoint/persistence;
- memory lifecycle;
- retry and unknown-outcome semantics;
- trace vs outcome evaluation;
- multi-agent topology;
- protocol version drift.

It produced material schema refinements documented in [`PRESSURE_TESTS.md`](./PRESSURE_TESTS.md).

## Classification workflow

```text
select system
    ↓
pin source + snapshot
    ↓
collect implementation/test evidence
    ↓
fill classification schema
    ↓
mark unsupported fields UNKNOWN
    ↓
identify dimension overlap/conflict
    ↓
pressure-test normalization rules
    ↓
compare against another system family/source
    ↓
refine schema only when evidence requires it
```

## Next pressure-test queue

Before MK1 closure, prioritize cases not sufficiently exercised by R-001..R-016:

1. C1 model-routed workflow;
2. C3 open-horizon agent;
3. dynamic multi-agent delegation;
4. durable cross-session memory with identity/isolation/retention;
5. authenticated transactional browser;
6. production-oriented system from `agents-towards-production`;
7. unknown-outcome mutating timeout/reconciliation case;
8. at least one independent source/framework outside the NirDiamant corpus.

## Engineering-family coverage

Current records cover at least one representative of:

- single-step deterministic LLM task;
- graph workflow;
- model-tool loop;
- retrieval/document system;
- state/memory system;
- evaluator/critic loop;
- generated-code/browser system;
- external-mutating system;
- multi-agent/multi-role system;
- protocol/integration system.

Coverage does not equal closure: topology extremes and independent-source pressure remain open.

## Admission rule for new top-level dimensions

Do not add a new top-level axis because one framework exposes a new class or field.

A new dimension should be introduced only when:

1. existing axes cannot represent a material engineering difference without distortion;
2. the difference affects behavior, risk, reliability, evaluation or reproducibility;
3. at least two independent examples or one strong counterexample justify the distinction;
4. the new dimension does not duplicate another field under a different name.

## Output expectation

MK1 ends with a stable schema plus normalized records/pressure tests sufficient for MK2 to derive operational contracts without re-litigating basic vocabulary.
