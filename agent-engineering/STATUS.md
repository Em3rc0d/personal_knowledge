# Agent Engineering — Status

Updated: **2026-09-16**  
Role: **canonical live dashboard**

> Historical reasoning belongs in quarries/MK receipts. `STATUS.md` stays intentionally focused on **where the domain is now**.

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

## Control-plane documents

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
| representative record set | 🟡 PARTIAL | [`mk/MK1/records/README.md`](./mk/MK1/records/README.md) |
| A2A reproducibility receipt | 🟡 OPEN | [`mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md`](./mk/MK1/A2A_EVIDENCE_REQUIREMENTS.md) |
| multi-agent baseline | 🟡 OPEN | [`mk/MK1/MULTI_AGENT_BASELINE_SPEC.md`](./mk/MK1/MULTI_AGENT_BASELINE_SPEC.md) |
| UNKNOWN reconciliation | 🟡 PARTIAL | [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md) |
| schema freeze audit | 🔒 BLOCKED BY ABOVE | [`mk/MK1/SCHEMA_HISTORY.md`](./mk/MK1/SCHEMA_HISTORY.md) |
| MK1 closure receipt | 🔒 NOT YET | future `mk/MK1/CLOSURE.md` |
| MK2 activation | 🔒 BLOCKED | [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md) |

## Materialized MK1 records

```text
REC-001  ✅ QUALIFIED  minimal while-loop / model-tool loop / shell
REC-002  ✅ QUALIFIED  HITL approval / protected dispatcher
REC-013  ✅ QUALIFIED  MCP revision drift / lifecycle semantics
REC-014  ✅ QUALIFIED  Strands Agents canonical classification
```

Registry and family coverage: [`mk/MK1/records/README.md`](./mk/MK1/records/README.md).

Highest-pressure records still missing:

```text
REC-004 generated-code/browser capability composition
REC-008 document/file data egress
REC-011 dedicated memory lifecycle
REC-003 trace-evaluation/critic pressure
REC-012 multi-agent after baseline evidence
```

## Resolved MK1 pressure tests

### Runtime semantics

Cross-source set:

- Strands Agents;
- LangGraph;
- OpenAI Agents SDK.

Result:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Evidence: [`quarries/runtime-semantics-strands-langgraph-openai.md`](./quarries/runtime-semantics-strands-langgraph-openai.md).

### Strands × MCP

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

Current view: [`systems/strands/PROTOCOLS.md`](./systems/strands/PROTOCOLS.md).  
Detailed receipt: [`quarries/strands-mcp-2026-07-28-compatibility.md`](./quarries/strands-mcp-2026-07-28-compatibility.md).

## Active MK1 blockers

MK1 cannot close until all `OPEN_MK1` items are resolved or explicitly routed.

```text
B1 representative family coverage
B2 A2A revision/auth/transport/execution receipt
B3 multi-agent baseline/admission evidence
B4 final schema overlap/freeze audit
B5 closure UNKNOWN routing
B6 MK1 CLOSURE.md
```

Executable dependency graph: [`mk/MK1/CLOSURE_PLAN.md`](./mk/MK1/CLOSURE_PLAN.md).

## Current UNKNOWN policy

Important uncertainty is not hidden inside prose.

Canonical register: [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md).

Closure states:

```text
OPEN_MK1
CLOSED
QUALIFIED
ROUTED_MK2
ROUTED_MK3_PLUS
ROUTED_MK5_PLUS
OUT_OF_SCOPE
```

Any material `OPEN_MK1` item blocks MK1 closure.

## Current system packages

### Strands Agents

Status: **CURRENT / QUALIFIED / SOLIDIFIED**

```text
systems/strands/
├── README.md
├── CLASSIFICATION.md
├── ENGINEERING_RULES.md
├── PROTOCOLS.md
├── EVIDENCE.md
└── LLM_CONTEXT.md
```

Pinned source snapshot:

```text
strands-agents/harness-sdk@a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
```

Current known protocol debt inside the package:

```text
A2A exact revision/auth/transport/execution receipt = OPEN
```

## MK2 state

MK2 design exists but is **not active canon**.

Activation requires:

```text
frozen MK1 schema
+ representative record coverage PASS
+ routed UNKNOWNs
+ protocol/multi-agent gates resolved
+ MK1 CLOSURE.md
```

Contract: [`mk/MK2/HANDOFF_CONTRACT.md`](./mk/MK2/HANDOFF_CONTRACT.md).

## Source/evidence anchors

```text
PRIMARY QUARRY SOURCE       NirDiamant/GenAI_Agents
PRIMARY SNAPSHOT            4c95ae14cc2462c442b5c064cccd74430d02bc46
MEMORY CROSS-SOURCE         Agent_Memory_Techniques@b7f7240e...
PRODUCTION CROSS-SOURCE     agents-towards-production@141b0679...
MCP CURRENT CONTRACT        2026-07-28
STRANDS SNAPSHOT            a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
```

Full registry: [`mining-site/SOURCES.md`](./mining-site/SOURCES.md).

## Next execution order

```text
1. materialize REC-004 generated-code/browser
2. materialize REC-008 data-egress
3. materialize REC-011 memory lifecycle
4. close A2A evidence contract
5. execute multi-agent baseline contract / REC-012
6. fill remaining non-redundant record pressure
7. reconcile UNKNOWNs
8. run schema freeze audit
9. create MK1 CLOSURE.md
10. activate MK2 handoff
```

This ordering is mirrored in [`ROADMAP.md`](./ROADMAP.md).

## Promotion state

```text
MK0 FRAME / EVIDENCE BASE    ✅ CLOSED
MK1 NORMALIZATION            🟡 IN PROGRESS
STRANDS SYSTEM PACKAGE       ✅ SOLIDIFIED
RUNTIME SEMANTICS CROSSCHECK ✅ COMPLETE
STRANDS MCP 2026-07-28       ✅ SUPPORTED / QUALIFIED
RECORD SET                   🟡 PARTIAL
A2A                          🟡 OPEN
MULTI-AGENT BASELINE         🟡 OPEN
SCHEMA FREEZE                🔒 NOT YET
MK2                          🔒 BLOCKED
CANON OPERATIONAL RULES      🔒 BLOCKED BY MK2+
```
