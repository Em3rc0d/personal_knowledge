# Agent Engineering — Mining Sources

Registry of sources used to mine and challenge the `agent-engineering` domain.

A source is evidence, not canon. `quarries/` stores extracted observations; promotion requires independent reasoning and MK gates.

## Provenance vocabulary

- `OFFICIAL` — primary documentation/specification from the system owner or standards body.
- `OBSERVED` — behavior or artifact directly visible in source code, tests, repository metadata or reproducible execution.
- `INFERRED` — conclusion derived from multiple observations; must expose premises.
- `INSPIRED` — useful idea adapted from a source but not claimed as that source's rule.
- `GENERATED` — internally proposed taxonomy/rule awaiting evidence.

## S-001 — GenAI_Agents

| Field | Value |
|---|---|
| ID | `S-001` |
| Type | public GitHub repository / tutorial corpus |
| Repository | https://github.com/NirDiamant/GenAI_Agents |
| Owner | Nir Diamant |
| Snapshot | `4c95ae14cc2462c442b5c064cccd74430d02bc46` |
| Snapshot date observed | 2026-09-07 |
| Upstream last push at observation | 2026-09-04 |
| Primary language | Jupyter Notebook / Python |
| Use here | pattern quarry, examples, counterexamples, taxonomy pressure test |
| Authority | mixed; code/tests are primary for this repository, explanatory claims remain tutorial claims |
| Confidence | HIGH for repository facts; VARIABLE for general engineering claims |

### Legal boundary

The upstream repository uses a custom license that grants non-commercial use with attribution while reserving commercial rights to the licensor.

Implications for this knowledge base:

- do not copy or redistribute notebook implementation code;
- do not promote source prose verbatim;
- independently synthesize principles and record factual observations;
- keep upstream attribution and exact snapshot;
- treat code fragments only as evidence inspected in place, not reusable assets.

License: https://github.com/NirDiamant/GenAI_Agents/blob/main/LICENSE

### High-value upstream slices inspected

- root README / implementation catalog;
- root `requirements.txt`;
- `CONTRIBUTING.md`;
- `scripts/validate_notebook.py`;
- `tests/test_validate_notebook.py`;
- `all_agents_tutorials/agent_while_loop_from_scratch.ipynb`;
- `all_agents_tutorials/human_in_the_loop_approval_agent.ipynb`;
- `tests/test_hitl_approval_agent.py`;
- `all_agents_tutorials/trace_based_agent_evaluation.ipynb`;
- `tests/test_trace_based_agent_evaluation.py`;
- P0/P1 families covering generated code, shell, browser, database, external communication/publication, file egress, reflection, memory, research, multi-agent and MCP;
- representative memory/checkpoint patterns through repository code search;
- selected repository issues for failure/reproducibility signals.

### Upstream issues sampled

Issues are `OBSERVED` reports from community participants, not independently verified facts unless code/test evidence confirms them.

- #4 — challenges overbroad use of the term “agent”;
- #91 — similar taxonomy concern around workflows/functions vs agents;
- #95 — report that an internet-summary example consumed search titles rather than article contents;
- #129 — request for structured error taxonomy and retry semantics;
- #81 — compatibility/runtime failure report around a LangGraph tutorial;
- #92 — setup/build failure report.

## S-002 — Agent_Memory_Techniques

| Field | Value |
|---|---|
| ID | `S-002` |
| Type | public GitHub repository / specialized memory corpus |
| Repository | https://github.com/NirDiamant/Agent_Memory_Techniques |
| Snapshot | `b7f7240eb4d4510f3b45300a89126858a474b31d` |
| Snapshot date observed | 2026-09-07 |
| Use here | memory taxonomy pressure test and lifecycle vocabulary |
| Authority | specialized tutorial source; source code is primary for source-specific behavior, taxonomy remains a source model to normalize |
| License signal | README declares Apache-2.0 |

High-value evidence inspected:

- root README taxonomy;
- `docs/comparison.md` covering 30 techniques;
- explicit dimensions for family, persistence, retrieval and token-cost behavior.

Key use in `agent-engineering`:

- supports distinguishing short-term context from long-term semantic/episodic/procedural stores;
- shows persistence and retrieval strategy are independent dimensions;
- reinforces that `MemorySaver`, chat history, vector stores, cross-session memory and semantic knowledge must not collapse into one `memory=true` flag.

## S-003 — agents-towards-production

| Field | Value |
|---|---|
| ID | `S-003` |
| Type | public GitHub repository / production-oriented tutorial corpus |
| Repository | https://github.com/NirDiamant/agents-towards-production |
| Snapshot | `141b0679f11b48209f2b872419f78a3a13850e0d` |
| Snapshot date observed | 2026-09-07 |
| Use here | production-pattern comparison, not repository-wide certification |
| Authority | mixed tutorial source |

The source advertises production-oriented topics including stateful workflows, memory, web search, Docker/FastAPI deployment, guardrails, scaling, browser automation, multi-agent coordination, observability and evaluation.

Important qualification:

- its pinned `.github/` directory contains funding, issue-template and Dependabot configuration but no visible GitHub Actions workflow;
- therefore `production-grade` / `production-ready` labels are source claims/tutorial-scope descriptions, not repository-wide certification.

## Official technical contrast

### S-101 — Anthropic: Building Effective Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/building-effective-agents
- published: 2024-12-19
- relevance:
  - distinguishes predefined workflows from model-directed agents;
  - recommends the simplest architecture that meets the task;
  - frames additional agentic complexity as latency/cost tradeoff;
  - emphasizes transparency and tool/ACI quality;
  - warns that frameworks can obscure underlying behavior.

### S-102 — Anthropic: Writing Effective Tools for Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/writing-tools-for-agents
- published: 2025-09-11
- relevance:
  - tool design is an agent-facing interface problem;
  - realistic held-out evaluation matters;
  - tool-call count, errors, runtime and token use complement outcome quality;
  - tool descriptions/schema/result shape materially affect behavior.

### S-103 — Anthropic: Effective Context Engineering for AI Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- published: 2025-09-29
- relevance:
  - context is a finite curated token budget;
  - context is broader than transcript/history;
  - context selection is a system-design concern.

### S-104 — Anthropic: Demystifying Evals for AI Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- published: 2026-01-09
- relevance:
  - separates tasks, trials, graders, traces/transcripts, outcomes and harnesses;
  - stochastic agents require repeated trials;
  - outcome and trajectory may require different graders;
  - automated evals should be complemented by production monitoring/human review.

### S-105 — LangGraph: Human-in-the-loop

- provenance: `OFFICIAL`
- URL: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- relevance:
  - policy-driven tool interruption;
  - approve/edit/reject decisions;
  - persisted graph state required to resume;
  - durable checkpointer recommended in production.

### S-106 — LangGraph: Interrupts

- provenance: `OFFICIAL`
- URL: https://docs.langchain.com/oss/python/langgraph/interrupts
- relevance:
  - dynamic pause/resume semantics;
  - `thread_id` identifies persisted execution;
  - pre-interrupt side effects must be replay-safe/idempotent.

### S-107 — LangGraph: Persistence

- provenance: `OFFICIAL`
- URL: https://docs.langchain.com/oss/python/langgraph/persistence
- relevance:
  - checkpoints underpin HITL, memory, time travel and fault recovery;
  - persistence/state durability is distinct from semantic memory.

### S-108 — Model Context Protocol specification

- provenance: `OFFICIAL`
- root: https://modelcontextprotocol.io/
- current specification revision for this pass: `2026-07-28`
- release source: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- relevance:
  - stateless protocol core;
  - mandatory legacy `initialize`/`initialized` and `Mcp-Session-Id` lifecycle removed from core;
  - per-request protocol/client metadata;
  - optional `server/discover`;
  - authorization hardening and formal extensions;
  - protocol interoperability remains distinct from runtime authorization/policy.

The `S-001` MCP tutorial remains a useful historical integration artifact, not a current `2026-07-28` lifecycle reference.

### S-109 — Strands Agents

- provenance: `OFFICIAL` + `OBSERVED`
- documentation: https://strandsagents.com
- repository: https://github.com/strands-agents/harness-sdk
- pinned snapshot: `a9361c54ca190117d5801dd09a1ab8d6d3d9bf20`
- observed: 2026-09-16
- release receipts: `python/v1.56.0`, `typescript/v1.18.0`
- license: Apache-2.0
- relevance:
  - modern in-process harness pressure test across model-directed/deterministic/mixed orchestration;
  - Graph, Swarm, Workflow and agents-as-tools;
  - explicit state/session/context/memory separation;
  - host-process capability boundary;
  - budget/cancellation/intervention enforcement pressure;
  - observability/eval/protocol adapters.
- detailed receipt: [`S-109-strands-agents.md`](./S-109-strands-agents.md)
- processed quarry: [`../quarries/strands-agents.md`](../quarries/strands-agents.md)
- MK1 pressure test: [`../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md`](../mk/MK1/STRANDS_AGENTS_PRESSURE_TEST.md)

### S-110 — LangGraph runtime semantics

- provenance: `OFFICIAL` + `OBSERVED`
- documentation: https://docs.langchain.com/oss/python/langgraph/
- repository: https://github.com/langchain-ai/langgraph
- pinned snapshot: `230927fb3a9ac9b2893a30322b4dfea7cdea9a8f`
- observed: 2026-09-16
- license: MIT
- relevance:
  - concurrent graph updates expose reducer/merge requirements;
  - interrupts persist/resume but can replay pre-interrupt code;
  - recursion limits are kill switches, not semantic success predicates;
  - tool-local interrupts can gate consequential dispatch.
- detailed receipt: [`S-110-langgraph-runtime-semantics.md`](./S-110-langgraph-runtime-semantics.md)

### S-111 — OpenAI Agents SDK runtime semantics

- provenance: `OFFICIAL` + `OBSERVED`
- documentation: https://openai.github.io/openai-agents-python/
- repository: https://github.com/openai/openai-agents-python
- pinned snapshot: `5f9899d584c5cfc879d3579352eb929fd4b34756`
- observed: 2026-09-16
- latest release observed: `v0.22.2` (2026-09-09)
- license: MIT
- relevance:
  - `max_turns`, tool timeouts and cancellation are distinct controls;
  - blocking vs parallel guardrails have different pre-effect guarantees;
  - agent/tool/handoff guardrails cover different paths;
  - local tool concurrency differs from provider-side parallel calls.
- detailed receipt: [`S-111-openai-agents-sdk-runtime-semantics.md`](./S-111-openai-agents-sdk-runtime-semantics.md)

### S-112 — Agent2Agent (A2A) Protocol

- provenance: `OFFICIAL`
- documentation: https://a2a-protocol.org/
- specification: https://a2a-protocol.org/dev/specification/
- repository: https://github.com/a2aproject/A2A
- repository snapshot observed: `afda8316c64951a2ecb2a0d3d10867405d2b4095`
- observed: 2026-09-16
- latest repository release observed: `v1.0.1` (2026-05-28)
- protocol compatibility line: `1.0`
- major `v1.0.0` release: 2026-03-12; explicitly breaking relative to `0.3`
- license: Apache-2.0
- relevance:
  - current revision-aware distributed-agent interoperability contract;
  - Agent Card discovery/identity/capability metadata;
  - task/message lifecycle and terminal/interrupted states;
  - standard JSON-RPC, gRPC and HTTP+JSON bindings;
  - security/auth declaration separated from application authorization;
  - cancellation does not imply transactional rollback;
  - provides the current-spec contrast proving Strands `0.3.x` support cannot be silently promoted to A2A `1.0` compatibility.
- detailed receipt: [`S-112-a2a-protocol.md`](./S-112-a2a-protocol.md)
- Strands comparison: [`../quarries/strands-a2a-version-drift.md`](../quarries/strands-a2a-version-drift.md)

### Cross-runtime promotion receipt

`S-109` + `S-110` + `S-111` jointly support:

```text
concurrency semantics        → state
budget enforcement semantics → termination
intervention owner/boundary  → human_control
```

Synthesis: [`../quarries/runtime-semantics-strands-langgraph-openai.md`](../quarries/runtime-semantics-strands-langgraph-openai.md).

### Protocol-version pressure receipt

`S-109` + `S-112` establish the current A2A version-drift fact:

```text
Strands pinned A2A SDK line  0.3.x
current A2A protocol line    1.0
compatibility                NOT ESTABLISHED without new evidence
```

This supports revision-aware classification; it does not certify current-version interoperability.

## Scientific literature

### S-201 — ReAct

- paper: *ReAct: Synergizing Reasoning and Acting in Language Models*
- Yao et al., ICLR 2023
- URL: https://arxiv.org/abs/2210.03629
- provenance: external scientific evidence
- relevance: reasoning/action interleaving in interactive task solving.

### S-202 — Reflexion

- paper: *Reflexion: Language Agents with Verbal Reinforcement Learning*
- Shinn et al., NeurIPS 2023
- URL: https://arxiv.org/abs/2303.11366
- provenance: external scientific evidence
- relevance: feedback + episodic memory can improve later trials under studied conditions; not model-weight learning.

### S-203 — Limits of intrinsic self-correction

- paper: *Large Language Models Cannot Self-Correct Reasoning Yet*
- Huang et al., ICLR 2024
- URL: https://arxiv.org/abs/2310.01798
- provenance: external scientific evidence
- relevance: intrinsic self-correction without external feedback is unreliable and may degrade reasoning.

### S-204 — AgentBench

- paper: *AgentBench: Evaluating LLMs as Agents*
- Liu et al., ICLR 2024
- URL: https://arxiv.org/abs/2308.03688
- provenance: external scientific evidence
- relevance: agent capability requires interactive-environment evaluation, not only static language benchmarks.

### S-205 — Multi-agent failure taxonomy

- paper: *Why Do Multi-Agent LLM Systems Fail?*
- Cemri et al., 2025
- URL: https://arxiv.org/abs/2503.13657
- provenance: external scientific evidence
- relevance: failure classes across system/spec design, inter-agent misalignment, verification and termination; multi-agent complexity is not free performance.

## Source hierarchy for promotion

When sources disagree:

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

Specialization, applicability and recency matter. Current protocol specifications outrank older tutorial lifecycle assumptions for claims about current protocol behavior.

No single source automatically wins every dispute; scope, methodology and reproducibility still determine what may be promoted.
