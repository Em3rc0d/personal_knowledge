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
- therefore `production-grade` / `production-ready` labels are treated as source claims and tutorial scope descriptions, not evidence that the whole repository is continuously integration-tested or certified.

This source is useful for MK1/MK2 architecture and operational pattern mining, but it cannot retroactively make `S-001` examples production-ready.

## Official technical contrast

### S-101 — Anthropic: Building Effective Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/building-effective-agents
- published: 2024-12-19
- relevance:
  - distinguishes predefined **workflows** from model-directed **agents**;
  - recommends the simplest architecture that meets the task;
  - frames additional agentic complexity as a latency/cost tradeoff;
  - emphasizes transparency and Agent-Computer Interface/tool quality;
  - warns that frameworks can obscure underlying behavior.

### S-102 — Anthropic: Writing Effective Tools for Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/writing-tools-for-agents
- published: 2025-09-11
- relevance:
  - tool design is an agent-facing interface design problem;
  - realistic eval tasks and held-out evaluation matter;
  - collect tool-call count, errors, runtime and token use in addition to outcome quality;
  - tool descriptions/schema and result shape materially affect agent behavior.

### S-103 — Anthropic: Effective Context Engineering for AI Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- published: 2025-09-29
- relevance:
  - context is a finite, curated token budget;
  - context is broader than transcript/history;
  - context selection is part of system design, not merely prompt wording.

### S-104 — Anthropic: Demystifying Evals for AI Agents

- provenance: `OFFICIAL`
- URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- published: 2026-01-09
- relevance:
  - separates tasks, trials, graders, traces/transcripts, outcomes and harnesses;
  - stochastic agents require repeated trials;
  - outcome and trajectory may require different graders;
  - automated evals should be complemented by production monitoring and human review.

### S-105 — LangGraph: Human-in-the-loop

- provenance: `OFFICIAL`
- URL: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- relevance:
  - policy-driven tool interruption;
  - approve/edit/reject decisions;
  - persisted graph state required to resume;
  - persistent database-backed checkpointer recommended in production.

### S-106 — LangGraph: Interrupts

- provenance: `OFFICIAL`
- URL: https://docs.langchain.com/oss/python/langgraph/interrupts
- relevance:
  - dynamic pause/resume semantics;
  - `thread_id` identifies persisted execution;
  - pre-interrupt side effects must be idempotent because node execution can replay.

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
  - introduces a stateless protocol core;
  - removes the core `initialize` / `initialized` handshake and `Mcp-Session-Id` lifecycle used by older MCP examples;
  - requests carry protocol version, client identity/capabilities metadata and routing information;
  - `server/discover` is optional for upfront capability discovery;
  - list results become cacheable/deterministic;
  - authorization is hardened;
  - extensions become a formal mechanism, including long-running/task-style capabilities;
  - MCP remains an interoperability/capability protocol, not a substitute for runtime policy, authorization, persistence or evaluation.

The `S-001` MCP tutorial is therefore retained as a useful legacy learning artifact for tool discovery/execution concepts but is **not** a current lifecycle reference for MCP `2026-07-28`.

## Scientific literature

### S-201 — ReAct

- paper: *ReAct: Synergizing Reasoning and Acting in Language Models*
- Yao et al., ICLR 2023
- URL: https://arxiv.org/abs/2210.03629
- provenance: external scientific evidence
- relevance: interleaving model reasoning/planning with environment actions can improve interactive task solving and provide inspectable trajectories.

### S-202 — Reflexion

- paper: *Reflexion: Language Agents with Verbal Reinforcement Learning*
- Shinn et al., NeurIPS 2023
- URL: https://arxiv.org/abs/2303.11366
- provenance: external scientific evidence
- relevance: textual reflection can improve later trials when coupled to feedback and episodic memory; it is not equivalent to model-weight learning.

### S-203 — Limits of intrinsic self-correction

- paper: *Large Language Models Cannot Self-Correct Reasoning Yet*
- Huang et al., ICLR 2024
- URL: https://arxiv.org/abs/2310.01798
- provenance: external scientific evidence
- relevance: intrinsic self-correction without external feedback is unreliable and can degrade reasoning performance.

### S-204 — AgentBench

- paper: *AgentBench: Evaluating LLMs as Agents*
- Liu et al., ICLR 2024
- URL: https://arxiv.org/abs/2308.03688
- provenance: external scientific evidence
- relevance: agent capability requires evaluation in interactive environments, not only static language benchmarks.

### S-205 — Multi-agent failure taxonomy

- paper: *Why Do Multi-Agent LLM Systems Fail?*
- Cemri et al., 2025
- URL: https://arxiv.org/abs/2503.13657
- provenance: external scientific evidence
- relevance: identifies failure classes spanning system/specification design, inter-agent misalignment, verification and termination; multi-agent complexity is not free performance.

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

Specialization and scope also matter. A dedicated memory corpus may be a better taxonomy quarry for memory than a general agents corpus, while the current MCP specification outranks an older tutorial's protocol lifecycle.

No single source automatically wins every dispute. The hierarchy indicates default evidentiary weight; applicability, recency, methodology and reproducibility must still be examined.