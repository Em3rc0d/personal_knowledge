# Agent Engineering — Status

Updated: 2026-09-07

## Current gate

```text
DOMAIN                    agent-engineering
CURRENT MK                MK1
STATE                     IN PROGRESS
MK0                       CLOSED / STRUCTURED EVIDENCE PACKAGE
MK1                       ACTIVE / 16 NORMALIZED RECORDS
MK2                       BLOCKED / DESIGN PACKAGE SEEDED
PRIMARY MINING SITE       NirDiamant/GenAI_Agents
UPSTREAM SNAPSHOT         4c95ae14cc2462c442b5c064cccd74430d02bc46
MEMORY CROSS-SOURCE       Agent_Memory_Techniques@b7f7240e...
PRODUCTION CROSS-SOURCE   agents-towards-production@141b0679...
MCP CONTRACT              2026-07-28
LICENSE BOUNDARY          RECORDED / S-001 NON-COMMERCIAL CUSTOM LICENSE
P0 CALL PATHS             9/9 NORMALIZED INTO MK1 RECORDS
FIRST CLASSIFICATION SET  13/13 COMPLETE
EXTERNAL PRESSURE TEST    R-016 PASS
SCHEMA REFINEMENTS        OBSERVED/REACHABLE EFFECT + MULTI-AGENT ADMISSION
REUSABLE RULES            CANDIDATE / NORMALIZATION IN PROGRESS
CANON RULE CERTIFICATION  BLOCKED BY MK1/MK2+
```

## MK progression

| MK | Objective | State | Package |
|---|---|---|---|
| MK0 | Mine source, establish vocabulary, provenance, claims, evidence, contradictions and candidate rules | **✅ CLOSED** | [`mk/MK0/`](./mk/MK0/) |
| MK1 | Normalize taxonomy and classify architectures, state, tools, control and failure modes | **🟡 IN PROGRESS** | [`mk/MK1/`](./mk/MK1/) |
| MK2 | Convert findings into operational contracts, checklists, schemas and tests | **🔒 BLOCKED / DESIGN SEEDED** | [`mk/MK2/`](./mk/MK2/) |
| MK3 | Integrate agent engineering with Jett Engineering Method, security and project workflows | BLOCKED | — |
| MK4 | Automate static checks, eval harness templates and evidence gates | BLOCKED | — |
| MK5+ | Certify rules against independent agent systems and production-like fixtures | BLOCKED | — |

## MK1 milestone

The original first classification queue is complete and all MK0 P0 call paths now have normalized records.

```text
R-001..R-013  original first set       ✅ COMPLETE
R-014         ShopGenie SMTP gap        ✅ CLASSIFIED
R-015         Car Buyer browser gap     ✅ CLASSIFIED
R-016         external memory source    ✅ PRESSURE PASS
```

Records: [`mk/MK1/records/`](./mk/MK1/records/)

Pressure-test ledger: [`mk/MK1/PRESSURE_TESTS.md`](./mk/MK1/PRESSURE_TESTS.md)

Closure gates: [`mk/MK1/GATES.md`](./mk/MK1/GATES.md)

## Material normalization results

### 1. Observed effect != reachable authority

R-001/R-004/R-005 showed that a benign run can execute on a shell/general-Python substrate capable of materially stronger effects.

The schema now records:

```yaml
side_effects:
  observed_class:
  reachable_class:
```

### 2. Multi-agent topology != control authority

R-012 uses multiple named roles but follows a fixed code-defined five-step sequence with one shared model client.

Normalized result:

```text
control = C0 deterministic
topology = deterministic_multi_role
```

The schema now includes explicit multi-agent admission hypothesis, baseline, measured benefit and coordination-cost fields.

### 3. Memory label != lifecycle evidence

R-011's upstream “long-term memory” uses in-process dictionaries keyed by `session_id`.

Normalized result:

```text
scope = session
persistence = process
```

R-016 independently confirmed that the same lifecycle axes cleanly classify Conversation Buffer Memory from `Agent_Memory_Techniques`.

### 4. HITL presence != dispatcher authorization

- R-002: H4 dispatcher enforcement is supported by dedicated tests.
- R-006: outbound HR sender authorization remains `UNKNOWN` despite interrupts elsewhere.

### 5. Safe mode is an authority boundary

R-007 shows that trusted `DRY_RUN` configuration changes executable publication capability rather than merely asking the model to behave safely.

### 6. Infrastructure authorization outranks intent

R-009 DataScribe is materially different under a read-only database principal versus write-capable credentials.

### 7. Protocol name != protocol contract

R-013 records the MCP tutorial as a legacy protocol lifecycle relative to the domain's current `2026-07-28` contract.

## Current record coverage

The normalized record set now covers:

- deterministic single-step LLM behavior;
- model-tool loop;
- graph/workflow orchestration;
- HITL/consequential actions;
- trace evaluation infrastructure;
- generated code execution;
- shell authority;
- browser retrieval;
- external messaging/publication;
- file-byte data egress;
- database authority;
- reflection/adaptation;
- memory lifecycle;
- deterministic multi-role/multi-agent presentation;
- MCP/versioned protocol integration;
- one cross-source memory implementation.

## Current UNKNOWN discipline

Material unknowns remain explicit in individual records and registers. Important examples include:

- sandbox/network/secret bounds for generated-code and shell systems;
- universal outbound-send approval in HR;
- external-send idempotency/reconciliation;
- remote document-retention/data-classification policy;
- exact DataScribe mutation dispatcher/filter path;
- authenticated browser mutation reachability;
- measured multi-agent benefit;
- durable cross-session memory behavior;
- per-language MCP migration/runtime details.

Canonical registers:

- [`mk/MK0/UNKNOWNS.md`](./mk/MK0/UNKNOWNS.md)
- [`mk/MK1/UNKNOWNS.md`](./mk/MK1/UNKNOWNS.md)
- [`mk/MK2/UNKNOWNS.md`](./mk/MK2/UNKNOWNS.md)

## MK1 closure blockers

MK1 remains open. Still required:

1. C1 model-routed workflow;
2. C3/open-horizon agent;
3. dynamic multi-agent delegation;
4. durable cross-session memory with identity/isolation/retention;
5. authenticated transactional browser;
6. explicit unknown-outcome mutation + reconciliation/idempotency case;
7. production-oriented pressure test from `agents-towards-production`;
8. at least one independent source/framework outside the NirDiamant corpus;
9. final overlap review and schema revision freeze.

## Documentation architecture

README files remain indexes. Substantive knowledge is split by responsibility.

```text
mk/MK0/   evidence/framing/closure package
mk/MK1/   schema + dimensions + rules + records + pressure tests + gates
mk/MK2/   blocked design scaffolding for operationalization
```

## Promotion state

```text
MK0 FRAME / EVIDENCE BASE   ✅ CLOSED
MK1 NORMALIZATION           🟡 IN PROGRESS — FIRST RECORD MILESTONE COMPLETE
MK2 OPERATIONALIZATION      🔒 BLOCKED / DESIGN SEEDED
CANON RULE CERTIFICATION    🔒 BLOCKED
CURRENT BRANCH MERGE        🔒 PENDING REVIEW
```

A record being complete means the architecture/evidence state is explicit. It does **not** certify security, reliability or production readiness.
