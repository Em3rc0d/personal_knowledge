# MK1 — Closure Gates

Status: **OPEN / IN PROGRESS**  
Execution plan: [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md)

MK1 closes only when the classification model survives pressure across materially different system families and produces a frozen input package for MK2.

## Gate dashboard

| Gate | State | Evidence / blocker |
|---|---|---|
| G1 representative family records | **PARTIAL** | REC-001, REC-002, REC-013, REC-014 materialized; high-capability/egress/memory/eval/multi-agent gaps remain |
| G2 framework-independent axes | **PARTIAL / STRONG** | Strands + LangGraph + OpenAI cross-runtime pass; more representative records still required |
| G3 P0 capability composition | **PARTIAL** | REC-001 has shell composition; generated-code/browser and egress records still open |
| G4 retry/error/termination normalization | **PARTIAL** | REC-001 + Strands cover distinct boundaries; more consequential/high-capability paths required |
| G5 memory lifecycle | **OPEN** | Strands supports separation, but dedicated representative memory record still required |
| G6 protocol revision awareness | **PARTIAL / STRONG** | REC-013 + Strands MCP complete; A2A receipt remains open |
| G7 multi-agent admission/baseline | **OPEN** | topology exists; benefit/baseline evidence contract not yet executed |
| G8 material UNKNOWN visibility/routing | **PARTIAL** | registers exist; closure routing not yet complete |
| G9 duplicate/overlap audit | **PARTIAL** | three Strands-derived overlaps resolved; final schema freeze audit pending |
| G10 external-system fit | **PARTIAL / STRONG** | Strands/LangGraph/OpenAI pressure supports current schema; broader record set pending |
| G11 architecture ≠ production certification | **PARTIAL / STRONG** | materialized records explicitly separate them; must hold across final set |
| G12 MK2 derivability | **OPEN** | handoff contract defined; frozen schema/record set not yet available |

## Closed subgates

- [x] concurrency semantics survived cross-runtime pressure testing without a framework-specific top-level category;
- [x] budget enforcement boundaries survived cross-runtime pressure testing without collapsing to a generic `bounded=true` flag;
- [x] intervention enforcement ownership survived cross-runtime pressure testing without equating guardrails/HITL/steering;
- [x] Strands MCP compatibility is pinned to revision `2026-07-28` with modern-lifecycle execution evidence and explicit auth/cancellation qualifications;
- [x] a canonical system-package layer exists and preserves evidence/history separation;
- [x] MK1 normalized record registry/template exists;
- [x] MK1→MK2 handoff contract exists as blocked design input.

These subgates reduce uncertainty; they do **not** imply MK1 closure.

## Remaining closure checklist

- [ ] every required engineering family has at least one normalized classification record or an explicit `COVERED_BY` decision;
- [ ] P0/high-blast-radius examples include capability-composition and side-effect records;
- [ ] retries/errors/termination are normalized for representative loop and consequential families;
- [ ] a dedicated memory example uses lifecycle dimensions rather than `memory=true`;
- [ ] A2A has a revision/auth/transport/execution receipt sufficient for protocol classification;
- [ ] multi-agent example carries admission hypothesis + simpler baseline + measured benefit/cost evidence;
- [ ] every material UNKNOWN is closed, routed forward, out-of-scope or explicitly blocks MK1;
- [ ] duplicate/overlapping dimensions pass final audit;
- [ ] schema can classify the representative set without a framework-name top-level category;
- [ ] architecture descriptions remain separate from production certification across the final set;
- [ ] MK2 contract families can be derived from frozen MK1 semantics without reopening terminology;
- [ ] frozen schema revision is declared in `SCHEMA_HISTORY.md`;
- [ ] MK1 `CLOSURE.md` exists with exact record set and handoff receipt.

## Pressure-test questions

Before closure, all must be answerable without hidden assumptions:

1. Can a deterministic S4 workflow and an autonomous S0 research agent both be described without implying one is more mature?
2. Can generated code be represented separately from permission to execute it?
3. Can an in-memory checkpoint and cross-session semantic memory be represented without both becoming `memory=true`?
4. Can human review exist while dispatcher enforcement remains `UNKNOWN`?
5. Can a timeout after a mutating request be represented as `unknown outcome` rather than ordinary retryable failure?
6. Can legacy MCP and current MCP implementations be differentiated by revision rather than protocol name alone?
7. Can multi-agent topology be represented without implying measured benefit?
8. Can an implementation be fully classified while still explicitly unverified for production?
9. Can durable state exist while concurrent writers remain unsafe or require reducer/locking semantics?
10. Can two systems with the same numeric turn budget be distinguished when enforcement happens at different boundaries?
11. Can blocking deterministic authorization be distinguished from parallel/model-mediated validation that may trip after work begins?
12. Can protocol interoperability be supported while auth policy and remote-effect rollback remain unproven?
13. Can a system expose a feature without the classification pretending every application enables or configures it?
14. Can an UNKNOWN remain visible without being forced into the nearest enum merely to complete a record?

If any answer is no, MK1 remains open.

## Cross-runtime gate receipt — 2026-09-16

Strands Agents, LangGraph and OpenAI Agents SDK were compared as independent runtime families.

```text
CONCURRENCY SEMANTICS        PASS → promoted under state
BUDGET ENFORCEMENT BOUNDARY  PASS → promoted under termination
INTERVENTION OWNER/BOUNDARY  PASS → promoted under human_control
TOP-LEVEL FRAMEWORK AXIS     NOT NEEDED
SCHEMA REVISION              mk1-draft-2026-09-16.1
```

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

## Strands × MCP protocol gate — 2026-09-16

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

This closes one current MCP implementation path; it does not close the separate A2A gate.

## Active specialized gates

- A2A protocol evidence: [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md)
- multi-agent benefit/admission: [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md)
- representative record coverage: [`records/README.md`](./records/README.md)
- schema freeze procedure: [`SCHEMA_HISTORY.md`](./SCHEMA_HISTORY.md)

## Exit decision semantics

Closing MK1 promotes:

- stable vocabulary;
- orthogonal classification dimensions;
- frozen schema revision;
- normalized representative records;
- evidence-state/UNKNOWN discipline;
- explicit handoff package.

It does **not** certify operational policies or production readiness. Those belong to MK2+.

## State transition

```text
remaining records + protocol + multi-agent evidence
        ↓
UNKNOWN reconciliation
        ↓
schema freeze audit
        ↓
MK1 CLOSURE.md
        ↓
MK2 HANDOFF_CONTRACT activation
        ↓
MK2 OPEN
```

Until every blocking gate passes:

```text
MK1 = IN PROGRESS
MK2 = BLOCKED
```
