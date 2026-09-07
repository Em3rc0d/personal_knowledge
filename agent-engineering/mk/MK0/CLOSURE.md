# MK0 Closure — Agent Engineering

Date: 2026-09-07  
Decision: **CLOSE MK0 / OPEN MK1**

## Scope of this closure

MK0 is `Mine & Frame`. Closing it means the domain now has enough evidence, vocabulary, contradiction handling and risk framing to normalize new systems without trusting framework names or marketing labels.

It does **not** mean:

- every upstream notebook runs today;
- P0 systems are secure;
- candidate rules are production-certified;
- MK2 operational contracts exist;
- any source is promoted wholesale to canon.

## Evidence ledger

### Source space

- `S-001` GenAI_Agents pinned to `4c95ae14cc2462c442b5c064cccd74430d02bc46`;
- `S-002` Agent_Memory_Techniques pinned to `b7f7240eb4d4510f3b45300a89126858a474b31d`;
- `S-003` agents-towards-production pinned to `141b0679f11b48209f2b872419f78a3a13850e0d`;
- MCP current official revision fixed to `2026-07-28` for this closure;
- official agent/context/tool/HITL/eval guidance and scientific contradiction sources registered.

### Corpus inventory

- all 55 GenAI_Agents tutorial entries mapped into engineering families;
- framework concentration recorded rather than mistaken for evidence of best practice;
- P0/P1 priority queue established.

### P0 call-path evidence

Classification-level call paths now exist for:

- generated E2E code + browser execution;
- generated self-healing code execution;
- general shell tool loop;
- HR external messaging;
- social publication;
- SMTP outbound email;
- external document upload/conversion;
- database exploration with explicit upstream DML/no-safety-rails warning;
- browser scraping.

Where a lower-level detail was not proven, it remains `UNKNOWN` instead of being inferred.

### P1 claim qualification

- `self-improving` normalized to reflection/adaptation unless improvement is externally measured and persistent;
- memory semantics moved to lifecycle dimensions using a specialized source;
- research/fact-checking separated from evidence/provenance strength;
- multi-agent topology separated from demonstrated benefit;
- MCP tutorial lifecycle marked legacy relative to current `2026-07-28` core semantics.

### Risk / threat framing

A framework-independent threat model now covers:

- prompt injection → privileged action;
- generated code execution;
- shell authority;
- database writes;
- duplicate/replayed side effects;
- approval bypass;
- data egress;
- browser-session privilege;
- memory poisoning;
- multi-agent authority amplification;
- capability discovery vs authorization;
- unverified completion;
- retry/oscillation/cost exhaustion.

### MK1 readiness

A classification schema now exists for:

- control authority;
- horizon/topology;
- capabilities and capability composition;
- side-effect class;
- state/checkpoint/persistence;
- memory lifecycle;
- human control;
- error/retry ownership;
- termination;
- evaluation layers;
- protocol revision/contracts;
- security boundaries;
- reproducibility evidence;
- explicit unknowns.

## MK0 exit-gate review

### Gate 1 — high-impact source families sampled

**PASS**

P0 families were inspected at sufficient source depth to classify authority/blast radius. P1 claims were separately qualified.

### Gate 2 — every candidate rule has evidence path + adversarial question

**PASS at MK0 depth**

Candidate invariants are backed by source/test/official/scientific evidence and the threat model supplies adversarial fixtures.

### Gate 3 — terminology framework-independent

**PASS**

The MK1 schema does not require LangGraph, LangChain, AutoGen, CrewAI, MCP or any other framework as a top-level system class.

### Gate 4 — legal/provenance boundaries preserved

**PASS**

S-001 custom non-commercial license is recorded; extracted knowledge is independently phrased. Sources are pinned and typed.

### Gate 5 — UNKNOWN remains explicit

**PASS**

Examples include unresolved HR sender approval coverage, DataScribe exact mutation dispatcher, browser authenticated mutation reachability and production runtime certification.

### Gate 6 — MK1 can classify a new system without marketing labels

**PASS**

`mk/MK1/README.md` provides a framework-independent record/schema and closure criteria.

## Remaining unknowns — intentionally transferred forward

These no longer block MK0 because they require normalization, operationalization or execution evidence rather than mining/frame evidence:

- per-notebook executable dependency proof;
- exact runtime behavior under current model/provider versions;
- project-specific sandbox effectiveness;
- precise retries/idempotency for every tutorial;
- production-grade tenant isolation and secrets handling;
- benchmarked multi-agent gains;
- memory-quality metrics for each memory family;
- current MCP SDK migration details per language/runtime;
- system-specific deployment/rollback/SLO evidence.

They become MK1/MK2/MK5 concerns depending on type.

## Promotion decision

```text
MK0  Mine & Frame          ✅ CLOSED
MK1  Normalize & Classify  🟡 OPEN / IN PROGRESS
MK2  Operationalize        🔒 BLOCKED BY MK1
CANON RULE CERTIFICATION   🔒 NOT YET
```

## Final constraint

Closing MK0 promotes the **problem framing and evidence discipline**, not every candidate engineering rule.

`main` should only receive this closure after branch review confirms the documentation matches the evidence ledger and no source claim has silently become a fact.