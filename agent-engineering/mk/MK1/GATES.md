# MK1 — Closure Gates

Status: **OPEN / IN PROGRESS**  
Execution plan: [`CLOSURE_PLAN.md`](./CLOSURE_PLAN.md)

MK1 closes only when the classification model survives representative system pressure and produces a frozen, auditable input package for MK2.

## Gate dashboard

| Gate | State | Evidence / blocker |
|---|---|---|
| G1 representative family records | **PASS EXCEPT MULTI-AGENT** | 11 materialized/qualified + 2 `COVERED_BY`; REC-012 still open |
| G2 framework-independent axes | **STRONG / FINAL AUDIT PENDING** | tutorial families + Strands/LangGraph/OpenAI pressure fit current schema without framework-name axis |
| G3 P0 capability composition | **PASS / QUALIFIED** | REC-001, REC-004, REC-007, REC-008, REC-009 reconstruct high-risk authority/effect paths |
| G4 retry/error/termination normalization | **PASS FOR REPRESENTATIVE NON-MULTI-AGENT SET / QUALIFIED** | loop, mutation, egress, publication and runtime cases preserve retry/idempotency/unknown-outcome boundaries |
| G5 memory lifecycle | **PASS / QUALIFIED** | REC-011 + REC-014 distinguish state/checkpoint/persistence/memory/knowledge |
| G6 protocol revision awareness | **PASS / QUALIFIED** | MCP current/legacy records + Strands A2A 0.3 vs current A2A 1.0 version drift |
| G7 multi-agent admission/baseline | **OPEN / BLOCKING** | REC-012 requires actual baseline/benefit evidence |
| G8 material UNKNOWN visibility/routing | **PARTIAL / FINAL PASS PENDING** | register exists; closure routing follows REC-012 |
| G9 duplicate/overlap audit | **PARTIAL** | candidate overlaps surfaced; final freeze audit pending |
| G10 external-system fit | **STRONG / FINAL AUDIT PENDING** | broad representative set fits current schema; REC-012 remains the final missing family |
| G11 architecture ≠ production certification | **PASS / STRONG** | all materialized records explicitly separate classification from production certification |
| G12 MK2 derivability | **OPEN / BLOCKED BY FREEZE** | handoff contract exists; frozen schema/closure receipt do not |

## Closed subgates

- [x] concurrency semantics survived cross-runtime pressure without a framework-specific top-level category;
- [x] budget enforcement boundaries survived cross-runtime pressure without collapsing to `bounded=true`;
- [x] intervention enforcement ownership survived cross-runtime pressure without equating guardrails/HITL/steering;
- [x] Strands MCP is pinned to `2026-07-28` with modern-lifecycle execution evidence and explicit auth/cancellation qualifications;
- [x] generated-code/browser capability composition is materialized in REC-004;
- [x] data-egress/confidentiality pressure is materialized in REC-008;
- [x] database effective authority is materialized in REC-009;
- [x] evaluation separates trajectory/outcome/repeated evidence in REC-003;
- [x] reflection/adaptation is separated from demonstrated persistent improvement in REC-010;
- [x] memory lifecycle is represented without `memory=true` in REC-011;
- [x] A2A support is revision-aware: pinned Strands `0.3.x` is not silently promoted to current A2A `1.0` compatibility;
- [x] A2A classification shape fits the current protocol schema in qualified form;
- [x] canonical system-package, normalized-record and MK1→MK2 handoff contracts exist.

These subgates do **not** imply MK1 closure.

## Remaining closure checklist

- [ ] REC-012 contains admission hypothesis + simpler baseline + measured outcome/cost/termination evidence;
- [ ] final representative-set review confirms all `COVERED_BY` decisions hide no distinct schema pressure;
- [ ] every material UNKNOWN is closed, qualified, routed forward or declared out-of-scope;
- [ ] final cross-dimension audit resolves overlap questions including egress/confidentiality and memory lifecycle placement;
- [ ] schema can classify the complete representative set without framework-name top-level categories;
- [ ] MK2 contract families map to frozen MK1 semantics without reopening basic terminology;
- [ ] frozen schema revision is declared in `SCHEMA_HISTORY.md`;
- [ ] MK1 `CLOSURE.md` names the exact frozen revision, record set, qualifications and handoff.

## Pressure-test questions

Before closure, all must be answerable without hidden assumptions:

1. Can deterministic S4 and autonomous S0 systems be described without treating autonomy as maturity?
2. Can generated code be represented separately from permission to execute it?
3. Can a checkpoint and cross-session semantic memory be represented without both becoming `memory=true`?
4. Can human review exist while dispatcher enforcement remains `UNKNOWN`?
5. Can timeout-after-mutation be represented as unknown outcome rather than ordinary retryable failure?
6. Can legacy/current protocol implementations be differentiated by revision rather than protocol name alone?
7. Can A2A 0.3 support be represented while A2A 1.0 compatibility remains explicitly unproven?
8. Can multi-agent topology be represented without implying measured benefit?
9. Can an implementation be fully classified while explicitly unverified for production?
10. Can durable state exist while concurrent writers remain unsafe or require reducer/locking semantics?
11. Can equal numeric budgets have different enforcement/overshoot semantics?
12. Can deterministic authorization be distinguished from model-mediated/parallel validation?
13. Can protocol interoperability be supported while authorization and rollback remain unproven?
14. Can framework capability remain distinct from concrete deployment configuration?
15. Can an UNKNOWN remain visible rather than forced into the nearest enum?

If any answer is no, MK1 remains open.

## Cross-runtime gate receipt — 2026-09-16

```text
CONCURRENCY SEMANTICS        PASS → state
BUDGET ENFORCEMENT BOUNDARY  PASS → termination
INTERVENTION OWNER/BOUNDARY  PASS → human_control
TOP-LEVEL FRAMEWORK AXIS     NOT NEEDED
SCHEMA REVISION              mk1-draft-2026-09-16.1
```

Evidence: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md).

## Strands × MCP gate — 2026-09-16

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

## Strands × A2A gate — 2026-09-16

```text
STRANDS PYTHON A2A SDK            >=0.3.0,<0.4.0
STRANDS TYPESCRIPT A2A SDK        ^0.3.10
PINNED PROTOCOL FAMILY            0.3
CURRENT A2A PROTOCOL FAMILY       1.0
CLIENT/SERVER/DISCOVERY SHAPE     SUPPORTED
SYNC/ASYNC/STREAM FIXTURE         PRESENT
GRAPH REMOTE-AGENT FIXTURE        PRESENT
INTEGRATION WORKFLOW SCOPE        PRESENT
SPECIFIC A2A CI PASS              NOT VERIFIED
INDEPENDENT RERUN                 NOT RUN
A2A 1.0 COMPATIBILITY             NOT ESTABLISHED
MK1 CLASSIFICATION SHAPE          PASS / QUALIFIED
```

Evidence: [`../../quarries/strands-a2a-version-drift.md`](../../quarries/strands-a2a-version-drift.md).

This gate proves revision-aware representability. It does **not** certify Strands as A2A `1.0` compatible.

## Active specialized gate

The only remaining evidence gate requiring a new representative experiment is:

- multi-agent benefit/admission → [`MULTI_AGENT_BASELINE_SPEC.md`](./MULTI_AGENT_BASELINE_SPEC.md)

Supporting/frozen-audit artifacts:

- record coverage → [`records/README.md`](./records/README.md)
- UNKNOWN routing → [`UNKNOWNS.md`](./UNKNOWNS.md)
- schema freeze procedure → [`SCHEMA_HISTORY.md`](./SCHEMA_HISTORY.md)
- A2A evidence contract/receipt semantics → [`A2A_EVIDENCE_REQUIREMENTS.md`](./A2A_EVIDENCE_REQUIREMENTS.md)

## Exit decision semantics

Closing MK1 promotes:

- stable vocabulary;
- orthogonal classification dimensions;
- frozen schema revision;
- representative normalized records;
- evidence-state/UNKNOWN discipline;
- explicit MK2 handoff package.

It does **not** certify operational policy, production readiness or universal protocol compatibility.

## State transition

```text
REC-012 multi-agent baseline
        ↓
UNKNOWN reconciliation
        ↓
cross-dimension + schema freeze audit
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
