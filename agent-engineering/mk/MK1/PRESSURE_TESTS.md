# MK1 — Pressure Tests

Status: **ACTIVE**  
Purpose: record where real classification evidence validates, breaks or refines the normalized schema.

## PT-01 — Observed effect vs reachable authority

**Trigger:** R-001 minimal shell loop, R-004 E2E generated code, R-005 self-healing code.

**Problem discovered**

A benign observed execution can coexist with a broadly privileged execution substrate.

Example:

```text
observed: list/read/test action
reachable: shell / arbitrary Python / broad browser-host authority
```

**Result: SCHEMA CHANGED**

`side_effects.class` was split into:

- `observed_class`;
- `reachable_class`.

Boolean capability fields also gained explicit `unknown` states.

---

## PT-02 — Multi-agent topology vs control authority

**Trigger:** R-012 History/Data Collaboration System.

**Observation**

The source uses two named role agents, but `solve()` executes five code-defined steps in a fixed `for` loop and both roles share one model client.

**Result: PASS + SCHEMA CHANGED**

- control remains `C0 deterministic`;
- topology is `deterministic_multi_role`;
- a dedicated `multi_agent` block now records admission hypothesis, baseline, measured benefit and coordination cost.

Conclusion:

```text
multiple roles/models != model-directed control
```

---

## PT-03 — Memory label vs lifecycle evidence

**Trigger:** R-011 upstream Memory-Enhanced Conversational Agent.

**Observation**

The source describes short-term + long-term/cross-session behavior, while implementation uses in-process dictionaries and `ChatMessageHistory` keyed by `session_id`.

**Result: PASS / SOURCE CLAIM QUALIFIED**

Normalized classification:

```text
scope: session
persistence: process
```

The schema represented the implementation without using `memory=true` or accepting the source label as fact.

---

## PT-04 — External cross-source classification

**Trigger:** R-016 `Agent_Memory_Techniques` Conversation Buffer Memory.

**Goal**

Test schema outside the primary `GenAI_Agents` mining site.

**Result: PASS**

The external implementation fit existing axes:

- C0 deterministic;
- session/process memory;
- full-buffer retrieval policy;
- S1 local state;
- content egress to model API;
- explicit token/context growth concern.

No new top-level dimension was required.

---

## PT-05 — HITL node vs enforceable authorization

**Trigger:** R-002 HITL Approval vs R-006 HR Messaging.

**Result: PASS**

The schema distinguishes:

- H4 dispatcher-enforced authorization with tests;
- human interrupts elsewhere in a workflow while sender authorization remains `UNKNOWN`.

Conclusion:

```text
human review exists != consequential dispatcher is gated
```

---

## PT-06 — Safe mode changes capability

**Trigger:** R-007 Social Publishing.

**Result: PASS**

Trusted `DRY_RUN` configuration produces a real authority distinction:

- draft/reversible behavior: observed S2;
- live publication: reachable S3.

This is stronger than a prompt asking the model not to publish.

---

## PT-07 — Intent vs infrastructure authorization

**Trigger:** R-009 DataScribe.

**Result: PASS**

The system can be classified conditionally by actual database principal:

```text
read-only principal   -> read authority
write-capable principal -> consequential mutation authority
```

Prompt intent does not override database permissions.

---

## PT-08 — Protocol name vs protocol revision

**Trigger:** R-013 MCP tutorial.

**Result: PASS**

The schema represents the tutorial as a legacy MCP lifecycle while retaining current MCP `2026-07-28` as the contrast contract.

No `MCP=true` boolean is treated as sufficient integration evidence.

---

## PT-09 — Classification vs evaluation infrastructure

**Trigger:** R-003 trace-evaluation harness.

**Result: PASS**

The schema can classify a deterministic supporting harness without forcing it into an `agent` category. This validates that the domain models the full agent system/ecosystem, not just model loops.

---

# Pressure tests still required before MK1 closure

MK1 remains **IN PROGRESS**. The following materially different cases should still be tested:

1. **C1 model-routed workflow** where the model selects one of bounded code-defined routes;
2. **C3 open-horizon agent** with semantic termination rather than only a fixed step list;
3. **dynamic multi-agent delegation** where model decisions create/route work rather than deterministic role sequencing;
4. **durable cross-session memory** with real persistence, identity/isolation and retention;
5. **authenticated transactional browser** with real mutation authority;
6. **production-oriented external system** from `agents-towards-production` to pressure security/reproducibility/observability fields;
7. **unknown-outcome mutating timeout** with explicit reconciliation/idempotency semantics;
8. **new independent source/framework** beyond the NirDiamant corpus before freezing the schema for MK2.

## Current disposition

```text
FIRST CLASSIFICATION SET      COMPLETE
PRIMARY P0 CALL PATHS         COMPLETE
EXTERNAL MEMORY PRESSURE      PASS
SCHEMA REVISIONS              2 MATERIAL REFINEMENTS
MK1 CLOSURE                   NOT YET
MK2 ACTIVATION                BLOCKED
```
