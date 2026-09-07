# MK1 — Classification Queue

Status: **ACTIVE**

MK1 begins with systems already supported by strong MK0 evidence, then expands across the remaining engineering families.

## First classification set

Priority order:

1. minimal while-loop agent;
2. HITL approval agent;
3. trace-evaluation harness;
4. E2E testing agent;
5. self-healing code agent;
6. HR messaging agent;
7. social publishing agent;
8. document-intake agent;
9. DataScribe;
10. self-improving/reflection example;
11. representative memory agent;
12. representative multi-agent system;
13. MCP tutorial as a legacy protocol example.

## Why this set comes first

It covers the dimensions most likely to expose overlap or ambiguity:

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
compare against another system family
    ↓
refine schema only when evidence requires it
```

## Expansion families

After the first set, cover at least one representative system from each family:

- single-call/deterministic LLM task;
- graph workflow;
- model-tool loop;
- retrieval/document system;
- state/memory system;
- evaluator/critic loop;
- generated-code/browser system;
- external-mutating system;
- multi-agent system;
- protocol/integration system.

## Admission rule for new top-level dimensions

Do not add a new top-level axis because one framework exposes a new class or field.

A new dimension should be introduced only when:

1. existing axes cannot represent a material engineering difference without distortion;
2. the difference affects behavior, risk, reliability, evaluation or reproducibility;
3. at least two independent examples or one strong counterexample justify the distinction;
4. the new dimension does not duplicate another field under a different name.

## Output expectation

MK1 should end with a stable schema plus normalized records/pressure tests sufficient for MK2 to derive operational contracts without re-litigating basic vocabulary.
