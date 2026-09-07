# GenAI_Agents — Normalized Inventory Seed

> Status: **MK0 inventory seed — NOT IMPLEMENTATION CERTIFICATION**  
> Upstream snapshot: `4c95ae14cc2462c442b5c064cccd74430d02bc46`  
> Observed: 2026-09-07

## Purpose

Translate the upstream tutorial catalog into `agent-engineering` dimensions instead of preserving categories such as Business/Creative/Analysis.

This table is intentionally conservative:

- `Framework` is upstream metadata.
- `Normalized family` is our initial classification by engineering concern.
- `Risk cue` is **triage**, not a verified risk rating.
- `Evidence state = README` means implementation details are still unverified.
- `INSPECTED` means source-level patterns were sampled in this MK0 pass; it still does not mean production-certified.

Risk cue vocabulary:

```text
R0  generation / no obvious external state
R1  external or local reads / retrieval
R2  local or reversible mutation / generated artifacts
R3  external mutation, communication, publication, or data egress
R4  broad code/shell/browser/environment authority
VAR capability-dependent; needs implementation inspection
```

## Catalog normalization

| # | Tutorial | Framework metadata | Normalized family | Risk cue | Evidence state |
|---:|---|---|---|---:|---|
| 1 | Simple Conversational Agent | LangChain / PydanticAI | conversation + session context | R0 | README |
| 2 | Simple Question Answering | LangChain | single-step QA | R0 | README |
| 3 | Simple Data Analysis | LangChain / PydanticAI | local data reasoning | R1 | README |
| 4 | Introduction to LangGraph | LangGraph | graph/workflow orchestration | R0 | README |
| 5 | Model Context Protocol tutorial | MCP | tool/resource interoperability | VAR | PARTIAL |
| 6 | ATLAS Academic Task System | LangGraph | multi-agent planning / research | R1 | README |
| 7 | Scientific Paper Agent | LangGraph | retrieval + document processing | R1 | PARTIAL |
| 8 | Chiron / Feynman Learning | LangGraph | adaptive workflow + checkpointing | R0/R1 | PARTIAL |
| 9 | Customer Support Agent | LangGraph | classification + response workflow | R0 | README |
| 10 | Essay Grading Agent | LangGraph | evaluator / multi-criterion scoring | R0 | README |
| 11 | Travel Planning Agent | LangGraph | planning + external information | R1 | README |
| 12 | GenAI Career Assistant | LangGraph | planning / retrieval / interaction loop | R1 | PARTIAL |
| 13 | Project Manager Assistant | LangGraph | decomposition + risk/task generation | R0 | README |
| 14 | Contract Analysis Assistant / ClauseAI | LangGraph | document analysis + memory/state | R1 | PARTIAL |
| 15 | E2E Testing Agent | LangGraph | generated code + browser execution | R4 | **INSPECTED** |
| 16 | GIF Animation Generator | LangGraph | media generation pipeline | R2 | README |
| 17 | TTS Poem Generator | LangGraph | text + speech generation | R2 | README |
| 18 | Music Compositor | LangGraph | media/file generation | R2 | README |
| 19 | Content Intelligence | LangGraph | research + content workflow | R1/R2 | PARTIAL |
| 20 | Business Meme Generator | LangGraph | image/content generation | R2 | README |
| 21 | Murder Mystery Game | LangGraph | interactive loop / state graph | R0 | PARTIAL |
| 22 | Memory-Enhanced Conversational | LangChain | session/long-term memory pattern | R0 | PARTIAL |
| 23 | Multi-Agent Collaboration | LangChain | multi-agent coordination | R0/R1 | PARTIAL |
| 24 | Self-Improving Agent | LangChain | reflection / revision | R0 | PARTIAL |
| 25 | Task-Oriented Agent | LangChain | deterministic task transformation | R0 | README |
| 26 | Internet Search Agent | LangChain | web retrieval + summarization | R1 | ISSUE-SAMPLED |
| 27 | Research Team | AutoGen | multi-agent research | R1 | README |
| 28 | Sales Call Analyzer | LangGraph | media ingestion + analysis | R1 | README |
| 29 | Weather Emergency System | LangGraph | real-time retrieval + decision support | R1 | README |
| 30 | Self-Healing Codebase | LangGraph | generated code execution + repair loop | R4 | **INSPECTED** |
| 31 | DataScribe | LangGraph | database discovery / query planning | R1/VAR | PARTIAL |
| 32 | Memory-Enhanced Email | LangGraph | memory + email triage/generation | R1/VAR | README |
| 33 | News TL;DR | LangGraph | news retrieval + summarization | R1 | README |
| 34 | AInsight | LangGraph | news aggregation / analysis | R1 | PARTIAL |
| 35 | Journalism Assistant | LangGraph | retrieval + fact-checking workflow | R1 | PARTIAL |
| 36 | Blog Writer | OpenAI Swarm | multi-agent content generation | R0/R2 | README |
| 37 | Podcast Generator | LangGraph | retrieval + generated audio | R1/R2 | README |
| 38 | ShopGenie | LangGraph | product research + outbound email | R3 | **INSPECTED** |
| 39 | Car Buyer Agent | LangGraph | browser/web scraping + decision support | R1→R4 | **INSPECTED** |
| 40 | Taskifier | LangGraph | decomposition / prioritization | R0 | README |
| 41 | Grocery Management | CrewAI | multi-agent inventory/task workflow | R2/VAR | README |
| 42 | LangGraph Inspector | LangGraph | graph QA / vulnerability inspection | R0 | PARTIAL |
| 43 | EU Green Deal Bot | LangGraph | regulatory knowledge QA | R1 | PARTIAL |
| 44 | Systematic Review | LangGraph | scholarly retrieval + synthesis | R1 | PARTIAL |
| 45 | Controllable RAG Agent | Custom / external repository | deterministic graph + RAG | R1 | EXTERNAL-LINK ONLY |
| 46 | HR AI Assistant | LangGraph | recruitment + external messaging + HITL | R3 | **INSPECTED** |
| 47 | ML & Data Science Assistant | LangGraph | agentic data/ML workflow | R2/VAR | PARTIAL |
| 48 | Art Tourguide with LightRAG | LightRAG + LangGraph | graph-RAG + interactive exploration | R1 | PARTIAL |
| 49 | Gutenberg Sage | LangGraph + Ollama | local-model RAG + subprocess lifecycle | R2 | **INSPECTED** |
| 50 | Contextual Quoting System | LangGraph | structured data + local DB + quoting | R1/R2 | **INSPECTED** |
| 51 | Document Intake Agent | LangGraph | file upload/transform + grounded QA | R3 | **INSPECTED** |
| 52 | Social Media Publishing Agent | LangGraph | external publication workflow | R3 | **INSPECTED** |
| 53 | Human-in-the-Loop Approval Agent | LangGraph | policy/approval + consequential-action pattern | R3-pattern | **INSPECTED + TESTS** |
| 54 | Trace-Based Agent Evaluation | Python | eval harness / trajectory scoring | R0 | **INSPECTED + TESTS** |
| 55 | Agent While Loop From Scratch | raw model API / Python | model-tool agent harness | R4-demo | **INSPECTED** |

## Concentration observation

The upstream numbered table has 54 entries. **40/54 (~74%) include LangGraph in their framework metadata**, including mixed `LightRAG + LangGraph` and `LangGraph + Ollama` entries.

The 55th recent while-loop tutorial intentionally strips the framework away.

### Interpretation

`GenAI_Agents` has high **use-case breadth**, but its implementation corpus is heavily centered on one orchestration family. Therefore:

- use it to discover patterns and failure surfaces;
- do not infer framework-independent best practice from frequency alone;
- validate portable rules against independent runtimes/frameworks and first-party specifications.

## Engineering-family view

The 55 examples can be collapsed into a smaller set of engineering concerns:

1. **Single-call / deterministic LLM tasks** — QA, transformations, classification.
2. **Graph workflows** — predefined nodes with conditional/model routing.
3. **Model-tool loops** — repeated observation/action cycles.
4. **Retrieval/document systems** — web, papers, RAG, structured documents.
5. **State/memory systems** — checkpoints, session memory, stores.
6. **Evaluation/critic loops** — grading, trace scoring, self-review.
7. **Generated-code/browser systems** — E2E and self-healing examples.
8. **External-mutating systems** — messages, email, social publication, data upload.
9. **Multi-agent systems** — research, academic, content, inventory.
10. **Protocol/integration systems** — MCP and external API/tool adapters.

This family view is more useful for MK1 than upstream content categories because it predicts runtime contracts and failure modes.

## Priority queue for source-level verification

### P0 — blast radius

- E2E Testing — sampled;
- Self-Healing Codebase — sampled;
- HR Assistant — sampled;
- Social Publishing — sampled;
- ShopGenie outbound email — sampled;
- Document Intake external upload — sampled;
- any database example with model-authored executable queries — still needs full call-path inspection;
- any browser agent with authenticated/mutating actions — still needs full call-path inspection.

### P1 — epistemic/reliability claims

- Self-Improving Agent;
- Memory-Enhanced agents;
- Systematic Review / Scientific Paper Agent;
- Journalism Assistant;
- multi-agent collaboration/research systems;
- MCP tutorial against current specification.

### P2 — lower-risk pedagogical patterns

- simple QA/conversation;
- content/media generation without external publication;
- decomposition/task planning;
- entertainment/state-machine examples.

## What this inventory does *not* certify

- that README metadata matches current runnable code;
- that risk cues are reachable in all execution paths;
- that a notebook's model/provider still exists or behaves equivalently;
- that dependencies install together;
- that a tutorial is secure, correct, or production-ready;
- that examples marked README-only lack safety controls.

Those claims require direct source inspection and, where material, execution evidence.
