# MK0 — Mine & Frame

Status: **✅ CLOSED**  
Closure date: **2026-09-07**  
Closure receipt: [`CLOSURE.md`](./CLOSURE.md)

## Purpose

MK0 established the evidence-backed framing required to study agent systems without trusting framework names, tutorial categories or marketing labels.

This README is the **entrypoint/index** for the MK0 package. Detailed knowledge lives in focused artifacts below.

## Package map

| Artifact | Responsibility |
|---|---|
| [`SCOPE.md`](./SCOPE.md) | mission, problem statement, source frame, non-goals and MK boundaries |
| [`ONTOLOGY.md`](./ONTOLOGY.md) | initial system classes, core components and critical distinctions |
| [`INVARIANTS.md`](./INVARIANTS.md) | candidate invariant families and anti-pattern catalog |
| [`EVIDENCE.md`](./EVIDENCE.md) | MK-level evidence ledger and links to source/quarry evidence |
| [`UNKNOWNS.md`](./UNKNOWNS.md) | unresolved facts deliberately transferred to later MKs |
| [`GATES.md`](./GATES.md) | exit criteria, PASS results and promotion semantics |
| [`CLOSURE.md`](./CLOSURE.md) | historical closure receipt: why MK0 closed and what that decision means |

## What MK0 established

At closure, the domain could distinguish and reason about:

- deterministic workflows vs model-routed/model-directed control;
- prompt guidance vs enforceable runtime invariants;
- capabilities and capability composition;
- side effects and blast radius;
- state, checkpointing, persistence, context, memory and knowledge/RAG;
- Human-in-the-Loop and dispatcher enforcement;
- retries, idempotency, unknown outcomes and termination;
- model claims, traces, outcomes and evidence;
- evaluation layers and stochastic/repeated-trial requirements;
- reflection vs demonstrated learning;
- multi-agent topology vs measured benefit;
- protocol interoperability vs authorization;
- source claims vs observations/inference/UNKNOWN.

## Main evidence families

```text
GenAI_Agents@4c95ae14...
Agent_Memory_Techniques@b7f7240e...
agents-towards-production@141b0679...
MCP official revision 2026-07-28
official runtime/tool/context/HITL/eval guidance
scientific agent/reflection/multi-agent literature
```

Source registry: [`../../mining-site/SOURCES.md`](../../mining-site/SOURCES.md)  
Raw/processed evidence: [`../../quarries/`](../../quarries/)

## Promotion state

```text
MK0  Mine & Frame          ✅ CLOSED
MK1  Normalize & Classify  🟡 IN PROGRESS
MK2  Operationalize        🔒 BLOCKED / DESIGN SEEDED
CANON RULE CERTIFICATION   🔒 NOT YET
```

Closing MK0 promotes the **framing, vocabulary foundation and evidence discipline**. Candidate operational rules continue through MK1/MK2 before any certification claim.
