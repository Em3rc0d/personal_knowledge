# MK1 — Closure Gates

Status: **OPEN / IN PROGRESS**

MK1 closes only when the classification model survives pressure across materially different system families.

## Closure checklist

- [ ] every engineering family has at least one normalized classification record;
- [ ] control, capability, side-effect, state/memory and human-control axes remain framework-independent;
- [ ] P0 examples have capability-composition records;
- [ ] retries/errors/termination are normalized for representative loop families;
- [ ] memory examples use lifecycle dimensions rather than `memory=true`;
- [ ] protocol examples are revision-aware;
- [ ] multi-agent examples carry admission hypotheses and baseline/benefit fields;
- [ ] every material unknown remains explicit;
- [ ] duplicate or overlapping dimensions are resolved;
- [ ] the schema can classify a new external system without inventing a new top-level category;
- [x] concurrency semantics survived cross-runtime pressure testing without a framework-specific top-level category;
- [x] budget enforcement boundaries survived cross-runtime pressure testing without collapsing to a generic `bounded=true` flag;
- [x] intervention enforcement ownership survived cross-runtime pressure testing without equating guardrails/HITL/steering;
- [x] Strands MCP compatibility is pinned to revision `2026-07-28` with modern-lifecycle execution evidence and explicit auth/cancellation qualifications;
- [ ] classification records distinguish architecture description from production certification;
- [ ] MK2 contract families can be derived from MK1 without reopening basic terminology disputes.

## Pressure-test questions

Before closure, ask:

1. Can a deterministic S4 workflow and an autonomous S0 research agent both be described without implying one is more mature?
2. Can generated code be represented separately from permission to execute it?
3. Can an in-memory checkpoint and a cross-session semantic memory be represented without both becoming `memory=true`?
4. Can human review exist while dispatcher enforcement remains `UNKNOWN`?
5. Can a timeout after a mutating request be represented as `unknown outcome` rather than ordinary retryable failure?
6. Can legacy MCP and current MCP implementations be differentiated by revision rather than protocol name alone?
7. Can multi-agent topology be represented without implying measured benefit?
8. Can an implementation be fully classified while still being explicitly unverified for production?
9. Can durable state exist while concurrent writers remain unsafe or require explicit reducer/locking semantics?
10. Can two systems with the same numeric turn budget be distinguished when one checks before dispatch and another only at a later loop boundary?
11. Can blocking deterministic authorization be distinguished from parallel/model-mediated validation that may trip after work has already begun?
12. Can protocol interoperability be recorded as supported while auth policy and remote-effect rollback remain explicitly unproven?

If the answer to any is no, MK1 remains open.

## Cross-runtime gate receipt — 2026-09-16

Strands Agents, LangGraph and OpenAI Agents SDK were compared as independent runtime families.

Result:

```text
CONCURRENCY SEMANTICS        PASS → promoted under state
BUDGET ENFORCEMENT BOUNDARY  PASS → promoted under termination
INTERVENTION OWNER/BOUNDARY  PASS → promoted under human_control
TOP-LEVEL FRAMEWORK AXIS     NOT NEEDED
SCHEMA REVISION              mk1-draft-2026-09-16.1
```

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

This gate does not close MK1; it closes only the three schema questions surfaced by the Strands pressure test.

## Strands × MCP protocol gate — 2026-09-16

The Strands protocol record was pressure-tested against MCP `2026-07-28` rather than represented as `MCP=true`.

Result:

```text
PINNED MCP REVISION               2026-07-28
MODERN NEGOTIATION                PASS / UPSTREAM EXECUTED
LEGACY initialize REJECTED        PASS / REGRESSION FIXTURE
STREAMABLE HTTP                   PASS / UPSTREAM EXECUTED
TOOLS + STRUCTURED RESULTS        PASS / UPSTREAM EXECUTED
MRTR INPUT-REQUIRED               PASS / UPSTREAM EXECUTED
PROMPTS / RESOURCES               PRESENT IN PINNED MODERN FIXTURE
TOOLS LIST-CHANGED                PASS / UPSTREAM EXECUTED
TRACE CONTINUITY                  PASS / UPSTREAM E2E RECEIPT
AUTH ADAPTER                      SUPPORTED / NOT EXTERNAL-OAUTH CERTIFIED
REMOTE SIDE-EFFECT ROLLBACK       NOT IMPLIED BY CANCELLATION
INDEPENDENT LOCAL RE-RUN          BLOCKED BY ENVIRONMENT NETWORK
```

Evidence: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md).

This closes the **Strands core interoperability unknown at the source-evidence level**. It does not make protocol support a security or transactional-safety certificate, and the broader MK1 protocol gate remains open until representative protocol records are consistently revision-aware.

## Exit decision semantics

Closing MK1 will promote:

- stable vocabulary;
- orthogonal dimensions;
- classification schemas;
- normalized records and evidence-state discipline.

It will **not** yet certify operational policies. Those belong to MK2.

## State transition

```text
MK1 PASS
   ↓
freeze schema version for MK2 input
   ↓
open MK2 operationalization work
   ↓
derive contracts / schemas / checklists / test obligations
```

Until every gate closes:

```text
MK1 = IN PROGRESS
MK2 = BLOCKED
```
