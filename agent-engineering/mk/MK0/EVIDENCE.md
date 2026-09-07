# MK0 — Evidence Ledger

Status: **CLOSED MK0 EVIDENCE MAP**

This file summarizes the evidence families that justified the MK0 closure. Raw/source-level observations remain in `mining-site/` and `quarries/`; this file is the MK-level map, not a copy of every quarry.

## Primary source space

### S-001 — GenAI_Agents

Pinned snapshot: `4c95ae14cc2462c442b5c064cccd74430d02bc46`

Evidence mined:

- 55-tutorial normalized inventory;
- framework concentration quantified rather than treated as best-practice evidence;
- minimal model → tool → observation loop;
- HITL approval path + dedicated tests;
- trace-evaluation harness + dedicated tests;
- generated-code/browser/shell high-blast-radius paths;
- external messaging, publication and data-egress paths;
- reflection, memory, research, multi-agent and MCP claims;
- issue/reproducibility signals kept below implementation/tests in evidentiary weight.

Detailed quarries:

- [`../../quarries/genai-agents.md`](../../quarries/genai-agents.md)
- [`../../quarries/genai-agents-inventory.md`](../../quarries/genai-agents-inventory.md)
- [`../../quarries/genai-agents-risk-scan.md`](../../quarries/genai-agents-risk-scan.md)
- [`../../quarries/genai-agents-p0-p1-callpaths.md`](../../quarries/genai-agents-p0-p1-callpaths.md)

## Specialized cross-source pressure tests

### S-002 — Agent_Memory_Techniques

Pinned snapshot: `b7f7240eb4d4510f3b45300a89126858a474b31d`

Used to pressure-test the overloaded term `memory` and separate short-term context, long-term stores, cognitive memory, routing/retrieval, frameworks and production/evaluation concerns.

### S-003 — agents-towards-production

Pinned snapshot: `141b0679f11b48209f2b872419f78a3a13850e0d`

Used to expand production concerns such as deployment, security guardrails, observability, APIs, scaling and operationalization while preserving the qualification that `production-grade` remains a source claim unless independently demonstrated.

Cross-source quarry:

- [`../../quarries/cross-source-memory-production-mcp.md`](../../quarries/cross-source-memory-production-mcp.md)

## MCP official contract pressure test

MCP official revision used at closure: **`2026-07-28`**.

The upstream GenAI_Agents MCP notebook represents an older lifecycle/session model. MK0 therefore preserves it as a useful legacy learning artifact rather than a current protocol contract.

## Official / scientific pressure tests

The registered evidence set covers:

- workflow vs agent/control authority;
- tool/ACI design;
- context engineering;
- HITL/persistence/replay;
- agent evaluation and repeated trials;
- ReAct-style acting loops;
- Reflexion and limits of intrinsic self-correction;
- interactive agent benchmarking;
- multi-agent failure modes.

Canonical source registry:

- [`../../mining-site/SOURCES.md`](../../mining-site/SOURCES.md)

## P0 call-path families classified at MK0 depth

- generated E2E code + browser execution;
- self-healing generated code execution;
- general shell tool loop;
- HR outbound messaging;
- social publication;
- SMTP outbound email;
- external document upload/conversion;
- database exploration with explicit upstream write-capability warning;
- browser scraping / browser authority.

`CLASSIFIED AT MK0 DEPTH` means authority/blast-radius can be normalized. It does not mean production-safe or exhaustively runtime-certified.

## P1 claims qualified

- `self-improving` → reflection/adaptation unless persistent improvement is measured;
- memory → lifecycle dimensions rather than a boolean;
- research/fact-checking → evidence/provenance contract rather than node naming;
- multi-agent → topology requiring measurable benefit against a simpler baseline;
- MCP → revisioned interoperability contract, not automatic authorization/runtime architecture.

## Evidence graph

```text
GenAI_Agents
  ├─ inventory
  ├─ P0 call paths
  ├─ P1 claim qualification
  ├─ HITL/tests
  └─ trace-eval/tests
        │
        ├── pressure-tested by Agent_Memory_Techniques
        ├── pressure-tested by agents-towards-production
        ├── pressure-tested by MCP 2026-07-28
        └── pressure-tested by official/scientific sources
                    │
                    ▼
             MK0 framing closure
                    │
                    ▼
           MK1 normalization schema
```

## Evidence hierarchy retained

```text
reproducible observed behavior / tests
        +
current official contract/spec
        +
peer-reviewed or strong empirical evidence
        >
repository README claim
        >
community issue / anecdote
        >
marketing label
```

Applicability, recency, methodology and reproducibility still matter; the hierarchy is a default weighting, not a mechanical score.
