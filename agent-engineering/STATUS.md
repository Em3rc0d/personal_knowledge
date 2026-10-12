# Agent Engineering — Status

Updated: **2026-10-12**  
Role: **canonical live dashboard**

> Historical reasoning belongs in quarries/MK receipts. `STATUS.md` answers only **where the domain is now**.

## Domain state

```text
DOMAIN                     agent-engineering
CURRENT MK                 MK1 — Normalize & Classify
STATE                      IN PROGRESS
SCHEMA                     mk1-draft-2026-09-16.1 / ACTIVE DRAFT
MK0                        ✅ CLOSED
MK1                        🟡 ACTIVE
MK2                        🔒 BLOCKED / DESIGN SEEDED
MK3+                       🔒 BLOCKED
```

## Control plane

```text
HUMAN ENTRYPOINT           README.md
LIVE STATUS                STATUS.md
EXECUTION ORDER            ROADMAP.md
REPOSITORY CONTRACT        REPOSITORY_CONTRACT.md
HUMAN KNOWLEDGE MAP        KNOWLEDGE_MAP.md
LLM ROUTER                 LLM_CONTEXT.md
SYSTEM PACKAGE CONTRACT    systems/PACKAGE_SPEC.md
MK1 CLOSURE PLAN           mk/MK1/CLOSURE_PLAN.md
MK2 HANDOFF CONTRACT       mk/MK2/HANDOFF_CONTRACT.md
```

## MK1 dashboard

| Workstream | State | Current artifact |
|---|---|---|
| Strands canonical package | ✅ SOLIDIFIED | [`systems/strands/`](./systems/strands/) |
| concurrency semantics | ✅ PROMOTED | schema `state` qualifiers |
| budget enforcement semantics | ✅ PROMOTED | schema `termination` qualifiers |
| intervention owner/boundary | ✅ PROMOTED | schema `human_control` qualifiers |
| Strands × MCP `2026-07-28` | ✅ SUPPORTED / QUALIFIED | [`systems/strands/PROTOCOLS.md`](./systems/strands/PROTOCOLS.md) |
| normalized record infrastructure | ✅ READY | [`mk/MK1/records/`](./mk/MK1/records/) |
| representative record set | ✅ ALL FAMILIES MATERIALIZED / FINAL AUDIT PENDING | 12 materialized/qualified (including [REC-012](./mk/MK1/records/REC-012-external-agent-scaling.md)) + 2 `COVERED_BY` |
| A2A classification-shape gate | ✅ PASS / QUALIFIED | [`quarries/strands-a2a-version-drift.md`](./quarries/strands-a2a-version-drift.md) |
| Strands A2A `1.0` compatibility | ⚠️ NOT ESTABLISHED / ROUTED DEBT | system freshness/interoperability debt, not hidden as PASS |
| multi-agent baseline | ✅ G7 PASS / QUALIFIED_UPSTREAM | [real LLM studies and checked outcome CSV](./quarries/multiagent-external-scaling-evidence.md) · own model inference NOT RUN |
| UNKNOWN reconciliation | 🟡 U-MK1-001 QUALIFIED; U-002/U-003 still OPEN | [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md) |
| schema freeze audit | 🟡 ENUM FORMAT RECHECK PASS / FULL FREEZE HOLD | [0/394 scalar mismatches](./mk/MK1/audits/ENUM_NORMALIZATION_RECHECK_2026-10-12.md); [PA-06 authority / remaining C5–C6 review](./mk/MK1/audits/FULL_REPRESENTATIVE_AUDIT_2026-10-12.md) |
| MK1 closure receipt | 🔒 NOT YET | future `mk/MK1/CLOSURE.md` |
| MK2 activation | 🔒 BLOCKED | [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md) |

## Representative-record state

```text
MATERIALIZED / QUALIFIED
REC-001  minimal while-loop / model-tool loop / shell
REC-002  HITL approval / protected dispatcher
REC-003  trace evaluation / outcome-vs-trajectory
REC-004  generated code + browser + host blast radius
REC-007  external publication / dry-run / idempotency
REC-008  document/file data egress
REC-009  database authority / least privilege
REC-010  reflection/adaptation vs persistent improvement
REC-011  state/persistence vs memory lifecycle contrast
REC-013  MCP revision drift
REC-014  Strands Agents canonical classification

COVERED_BY
REC-005  covered by REC-004 + REC-003
REC-006  covered by REC-002 + REC-007

QUALIFIED / SOURCE-REPORTED
REC-012  representative multi-agent baseline/admission evidence; external S-118 + S-119; local LLM NOT RUN
```

Canonical registry: [`mk/MK1/records/README.md`](./mk/MK1/records/README.md).

## Resolved protocol pressure

### MCP

Pinned contract: **MCP `2026-07-28`**.

```text
core interoperability       SUPPORTED / UPSTREAM-EXECUTED
modern lifecycle            REGRESSION-TESTED
legacy initialize fallback  REJECTED BY FIXTURE
Streamable HTTP             UPSTREAM-EXECUTED
MRTR/prompts/resources      SUPPORTED BY PINNED FIXTURE
list-changed                UPSTREAM-EXECUTED
trace continuity            UPSTREAM E2E TESTED
auth adapter                SUPPORTED / deployment auth separate
remote rollback             NOT IMPLIED
independent local rerun     ENVIRONMENT-BLOCKED
```

### A2A

Pinned Strands snapshot:

```text
Python A2A SDK              >=0.3.0,<0.4.0
TypeScript A2A SDK          ^0.3.10
current A2A protocol line   1.0
0.3 implementation          SUPPORTED / QUALIFIED
integration fixture source  PRESENT
specific successful CI run  NOT VERIFIED
independent rerun           NOT RUN
A2A 1.0 compatibility       NOT ESTABLISHED
```

Result: the **MK1 classification-shape gate passes in qualified form** because revision, role, transport/task shape, auth boundary, concurrency and evidence limitations are representable without `A2A=true`. A2A `1.0` migration remains explicit version-drift debt.

Current view: [`systems/strands/PROTOCOLS.md`](./systems/strands/PROTOCOLS.md).  
Receipt: [`quarries/strands-a2a-version-drift.md`](./quarries/strands-a2a-version-drift.md).

## Active MK1 blockers

```text
B1 full record enum lexical normalization ✅ 0/394 mismatches, 12 blocks checked
B2 PA-06 nested actor effective authority / semantic evidence still OPEN
B3 remaining U-MK1-002/U-MK1-003 UNKNOWN routing
B4 cross-dimension / C5–C6 re-audit and schema freeze decision
B5 MK1 CLOSURE.md
```

A2A `1.0` compatibility is **not silently closed**; it is no longer a taxonomy blocker because the current schema can faithfully represent the version drift and incomplete execution evidence.

Executable dependency graph: [`mk/MK1/CLOSURE_PLAN.md`](./mk/MK1/CLOSURE_PLAN.md).

## MK2 state

MK2 design exists but is **not active canon**.

Activation requires:

```text
frozen MK1 schema
+ representative record coverage PASS
+ multi-agent gate PASS
+ routed UNKNOWNs
+ MK1 CLOSURE.md
```

Contract: [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md).

## Next execution order

```text
1. audit per-child authority (PA-06), using variant-aware normalized records (scalar check PASS)
2. reconcile remaining OPEN_MK1 questions
3. rerun cross-dimension + schema freeze audit; PA-01 appendix decision recorded, PA-06 remains OPEN
4. decide freeze vs explicit new draft revision
5. create MK1 CLOSURE.md only on PASS
6. activate MK2 handoff only after closure
```

## Promotion state

```text
MK0 FRAME / EVIDENCE BASE    ✅ CLOSED
MK1 NORMALIZATION            🟡 IN PROGRESS
STRANDS SYSTEM PACKAGE       ✅ SOLIDIFIED
RUNTIME SEMANTICS CROSSCHECK ✅ COMPLETE
STRANDS MCP 2026-07-28       ✅ SUPPORTED / QUALIFIED
RECORD SET                   ✅ REPRESENTED / FINAL AUDIT PENDING
A2A CLASSIFICATION SHAPE     ✅ PASS / QUALIFIED
A2A 1.0 COMPATIBILITY        ⚠️ NOT ESTABLISHED
MULTI-AGENT BASELINE         ✅ PASS / QUALIFIED_UPSTREAM
SCHEMA FREEZE                🔒 NOT YET
MK2                          🔒 BLOCKED
CANON OPERATIONAL RULES      🔒 BLOCKED BY MK2+
```
