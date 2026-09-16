# Strands Agents — Evidence Map

Status: **CANONICAL PROVENANCE MAP**  
Observed baseline: **2026-09-16**

This file answers **“why do we believe the canonical Strands view?”** without duplicating all raw evidence.

## Evidence chain

```text
S-109 source receipt
        ↓
strands-agents quarry
        ↓
MK1 Strands pressure test
        ↓
independent runtime crosscheck
        ↓
MK1 schema promotion
        ↓
Strands × MCP 2026-07-28 execution receipt
        ↓
systems/strands/ canonical current view
```

## Primary receipts

### Source identity — S-109

Path: [`../../mining-site/S-109-strands-agents.md`](../../mining-site/S-109-strands-agents.md)

Carries:

- canonical Strands docs/repository identity;
- pinned repository snapshot;
- observed release versions;
- source authority/qualification;
- inspected source slices;
- legal/reuse boundary;
- links into processed evidence.

Use when verifying **which Strands version/source** a claim refers to.

### Detailed Strands quarry

Path: [`../../quarries/strands-agents.md`](../../quarries/strands-agents.md)

Carries the broad processed source observations covering:

- SDK/platform identity;
- core model-driven loop;
- Graph/Swarm/Workflow/agents-as-tools;
- conversation/state/session/memory distinctions;
- tools and host-process permission boundary;
- hooks/plugins/steering;
- structured output;
- observability/evaluation;
- MCP/A2A presence;
- deployment posture;
- original candidate dimensions and unknowns.

Use when auditing the **raw processed reasoning** behind the current synthesis.

Important: this quarry preserves historical candidate state. Some candidates/unknowns were later resolved. Prefer this system package for current status.

### MK1 Strands pressure test

Path: [`../../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](../../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)

Carries the first normalized attempt to classify Strands against the framework-independent MK1 model.

It is historically important because it deliberately refused to promote three Strands-specific observations directly into the schema:

- concurrency semantics;
- budget enforcement boundary;
- intervention enforcement owner.

Use when auditing **why schema promotion required independent confirmation**.

### Cross-runtime semantic validation

Path: [`../../quarries/runtime-semantics-strands-langgraph-openai.md`](../../quarries/runtime-semantics-strands-langgraph-openai.md)

Sources:

- S-109 Strands Agents;
- S-110 LangGraph;
- S-111 OpenAI Agents SDK.

Carries independent confirmation that the three Strands candidates are reusable engineering distinctions rather than framework accidents.

Final promotion:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Use when justifying the current MK1 schema fields.

### MCP `2026-07-28` compatibility receipt

Path: [`../../quarries/strands-mcp-2026-07-28-compatibility.md`](../../quarries/strands-mcp-2026-07-28-compatibility.md)

Carries the protocol-specific execution evidence for:

- MCP 2.x dependency contract;
- `server/discover` modern lifecycle;
- explicit legacy-`initialize` rejection fixture;
- Streamable HTTP interoperability;
- tools/list and tools/call;
- structured content/error mapping;
- multi-round-trip input requests;
- prompts/resources;
- list-changed subscriptions;
- task-extension boundary;
- trace continuity;
- auth qualification;
- cancellation qualification;
- upstream CI receipts;
- failed/blocked independent local rerun receipt.

Use when making any concrete claim about current Strands ↔ MCP `2026-07-28` interoperability.

## Normalized canon dependencies

### Current MK1 schema

Path: [`../../mk/MK1/CLASSIFICATION_SCHEMA.md`](../../mk/MK1/CLASSIFICATION_SCHEMA.md)

Current revision: `mk1-draft-2026-09-16.1`.

Strands helped pressure-test this schema, but the schema is framework-independent.

### Current dimension semantics

Path: [`../../mk/MK1/DIMENSIONS.md`](../../mk/MK1/DIMENSIONS.md)

Use for the authoritative meaning of normalized fields such as state concurrency, human-control enforcement and termination budgets.

### Current normalization rules

Path: [`../../mk/MK1/NORMALIZATION_RULES.md`](../../mk/MK1/NORMALIZATION_RULES.md)

Use when deciding whether a Strands feature name should become a normalized field. Default answer: classify the underlying engineering semantics, not the framework vocabulary.

### Current gates and unknowns

- gates: [`../../mk/MK1/GATES.md`](../../mk/MK1/GATES.md)
- unknown register: [`../../mk/MK1/UNKNOWNS.md`](../../mk/MK1/UNKNOWNS.md)
- domain status: [`../../STATUS.md`](../../STATUS.md)

These decide what is still open even if older quarries describe the same item as a candidate or UNKNOWN.

## Claim → evidence matrix

| Canonical claim | Evidence | State |
|---|---|---|
| Strands is an in-process SDK/harness, not a mandatory hosted control plane | S-109 + Strands quarry | **SUPPORTED** |
| Core Agent execution is model-directed inside runtime-owned mechanics | Strands quarry + pressure test | **SUPPORTED** |
| Workflow/Graph/Swarm/agents-as-tools are materially different topologies | Strands quarry + pressure test | **SUPPORTED** |
| framework identity is not taxonomy | Strands topology evidence + MK1 normalization | **SUPPORTED** |
| conversation, invocation state, session persistence and long-term memory are distinct | Strands quarry | **STRONGLY SUPPORTED** |
| host-process authority materially determines tool blast radius | Strands quarry/source security guidance | **STRONGLY SUPPORTED** |
| persistence does not imply concurrency safety | Strands + LangGraph + OpenAI runtime crosscheck | **CROSS-RUNTIME SUPPORTED** |
| budgets require enforcement-boundary semantics | Strands + LangGraph + OpenAI runtime crosscheck | **CROSS-RUNTIME SUPPORTED** |
| interventions require enforcement owner/boundary | Strands + LangGraph + OpenAI runtime crosscheck | **CROSS-RUNTIME SUPPORTED** |
| output/trajectory/session evaluation are separate surfaces | Strands Evals evidence | **SUPPORTED** |
| Strands Python interoperates with MCP `2026-07-28` modern lifecycle at pinned snapshot | MCP compatibility receipt + upstream CI | **SUPPORTED / UPSTREAM-EXECUTED** |
| MCP trace continuity works in tested modern path | MCP trace receipt | **UPSTREAM E2E TESTED** |
| MCP external OAuth policy is universally correct | no sufficient evidence | **NOT CLAIMED** |
| remote cancellation rolls back side effects | no sufficient evidence | **NOT CLAIMED** |
| A2A current revision/auth/transport is fully pinned and executed | incomplete receipt | **UNKNOWN / OPEN** |
| Graph/Swarm is generally better than a simpler architecture | no benchmark evidence | **NOT CLAIMED** |
| every Strands app is production-ready | impossible from framework evidence alone | **NOT CLAIMED** |

## Evidence-state vocabulary

Use the domain reasoning states consistently:

```text
SOURCE CLAIM   source says it
OBSERVED       directly visible in code/test/artifact
INFERRED       derived from observations; premises must be visible
SUPPORTED      evidence is sufficient for the scoped claim
QUALIFIED      supported only with explicit boundaries/limitations
CONTRADICTED   evidence rejects the claim as stated
UNKNOWN        material evidence is missing
```

Repository provenance labels remain complementary:

```text
OFFICIAL | OBSERVED | INFERRED | INSPIRED | GENERATED
```

## Freshness rule

All current Strands facts in this package are anchored to:

```text
snapshot: a9361c54ca190117d5801dd09a1ab8d6d3d9bf20
observed: 2026-09-16
```

If a future Strands release changes runtime semantics, protocol ranges, orchestration behavior or API guarantees:

1. create/update the source receipt with the new snapshot;
2. preserve previous evidence as historical;
3. rerun relevant pressure gates;
4. update this package only after evidence is reconciled;
5. never silently reinterpret the old snapshot as the new one.
