# Quarry — NirDiamant/GenAI_Agents

> Status: **MK0 evidence — NOT CANON**  
> Upstream snapshot: `4c95ae14cc2462c442b5c064cccd74430d02bc46`  
> Observed: `2026-09-07`  
> Source: https://github.com/NirDiamant/GenAI_Agents

## 1. Why this source matters

`GenAI_Agents` is a broad pedagogical corpus spanning basic LLM chains, graph workflows, tool-using agents, multi-agent examples, RAG, MCP, memory, HITL, content generation, research, testing and evaluation.

Its value for `personal_knowledge` is not that every notebook is production-grade. Its value is that the repository exposes many **architectural shapes and failure surfaces in one place**, making it useful for building a framework-independent taxonomy.

The README advertises 55 tutorials and its principal numbered table currently reaches 54 entries; the newer minimal while-loop tutorial exists outside that numbered table. The catalog is strongly concentrated around LangGraph, with additional LangChain, PydanticAI, AutoGen, CrewAI, OpenAI Swarm, LightRAG, Ollama, MCP and custom examples.

### Initial source classification

```text
PEDAGOGICAL BREADTH       HIGH
FRAMEWORK DIVERSITY       MEDIUM
LANGGRAPH CONCENTRATION   HIGH
PRODUCTION EVIDENCE       UNEVEN
DEDICATED TEST COVERAGE   LOW / RECENTLY IMPROVING
VERSION COHERENCE         UNEVEN
VALUE AS PATTERN QUARRY   HIGH
VALUE AS CANON            LOW WITHOUT NORMALIZATION
```

## 2. Repository-level observations

### Q-OBS-001 — Tutorials are the product; shared runtime is not

**OBSERVED**

The repository is organized primarily as independent Jupyter notebooks rather than as one cohesive deployable agent runtime. The central README acts as a catalog and `all_agents_tutorials/` is the dominant source area.

**INFERENCE**

Patterns must be extracted at the level of architecture/contracts, not imported as a shared application architecture.

---

### Q-OBS-002 — Framework/version drift is structurally possible

**OBSERVED**

The root `requirements.txt` pins an older LangChain/LangGraph stack (`langchain==0.2.16`, `langgraph==0.2.18`, `openai==1.43.0`, `autogen==0.3.0`), while a recent HITL test explicitly expects a notebook-pinned `langgraph==0.2.76` for its integration slice.

The repository enabled Dependabot in August 2026, but the root environment still cannot be treated as proof that every notebook executes together.

**INFERENCE**

A tutorial corpus needs **per-slice executable environment evidence**. A global requirements file is insufficient when notebook generations span changing APIs.

**Candidate rule**

> Reproducibility belongs to the artifact under test: pin the runtime/dependencies relevant to that slice and prove execution, rather than trusting a repository-wide dependency list.

---

### Q-OBS-003 — Notebook validation checks hygiene, not executability

**OBSERVED**

`scripts/validate_notebook.py` enforces:

- nbformat 4 shape;
- cleared code outputs/execution counts;
- a preceding markdown heading for code cells;
- required tutorial sections;
- valid local image references that do not escape repository root.

Dedicated unit tests cover malformed notebooks and validation behavior.

The validator does **not** execute notebook code, resolve dependencies, invoke external integrations or verify outputs.

**INFERENCE**

Documentation quality gate and runtime correctness gate are orthogonal.

**Candidate rule**

> `structurally valid` → `executable` → `behaviorally correct` → `reliable` → `production-suitable` are separate claims requiring separate evidence.

---

### Q-OBS-004 — Automated tests exist, but only for selected recent slices

**OBSERVED**

The inspected `tests/` directory contains dedicated suites for:

- notebook contribution validation;
- HITL approval agent behavior;
- trace-based agent evaluation.

No repository-wide GitHub Actions workflow was visible under `.github/` at the pinned snapshot; `.github/` contains funding and Dependabot configuration.

**INFERENCE**

The newer slices show stronger engineering discipline than the corpus as a whole, but the repository does not provide inspected evidence that every notebook continuously passes.

**Do not infer**

- “tests directory exists” ⇒ “all tutorials are tested”;
- “Dependabot exists” ⇒ “compatibility is continuously certified”.

---

## 3. Taxonomy pressure test: what is an agent?

The upstream calls a wide range of systems “agents”: simple QA chains, deterministic state graphs, model-routed workflows, tool loops, multi-agent systems and specialized pipelines.

Community issues #4 and #91 explicitly challenge this terminology. The exact definitions suggested by issue authors are not authoritative, but the ambiguity they expose is real.

### Official contrast

Anthropic's *Building Effective Agents* distinguishes:

```text
WORKFLOW
LLMs/tools orchestrated through predefined code paths

AGENT
LLM dynamically directs its process and tool use
```

### Proposed MK1 dimensions

Do **not** classify systems with a single `agent=yes/no` flag. Normalize along orthogonal axes:

| Dimension | Example values |
|---|---|
| Control authority | deterministic code / model-routed / model-directed |
| Horizon | single call / bounded multi-step / open-ended |
| Environment | read-only / mutable sandbox / external mutable systems |
| Tool authority | none / fixed sequence / model-selected |
| State | stateless / transient structured / checkpointed / durable |
| Memory | none / session / episodic / semantic / external knowledge |
| Side effects | none / reversible / consequential |
| Human control | none / review-after / approval-before / editable action |
| Evaluation | answer-only / outcome / trace / regression suite |
| Topology | single model / router-workers / parallel workers / peer agents |

### Candidate rule

> “Agent” is a control-system property, not a framework constructor or marketing label.

Using `create_react_agent()` does not automatically make a system more agentic than a custom loop; conversely, a custom runtime can be model-directed without a framework-specific “agent” API.

## 4. Minimal agent loop — useful core, dangerous simplifications

The recent `agent_while_loop_from_scratch.ipynb` is one of the strongest pedagogical slices because it strips abstraction away.

### What it demonstrates well

**OBSERVED**

The example has:

- one model;
- tool definitions;
- a repeated model → tool → result cycle;
- explicit `MAX_TURNS` hard stop;
- a record of previously failed exact calls;
- a guard that blocks repeating an identical failed call;
- tool results/errors reintroduced into subsequent model context.

**SUPPORTED principle**

A model-facing instruction such as “do not repeat a failed action” is softer than enforcing the invariant in executable runtime logic.

This aligns with general safety/reliability engineering: if violating a rule is unacceptable, the model should not possess unilateral authority to violate it.

### What must be qualified

The tutorial's “transcript is the agent's entire mind” framing is useful for its minimal example but too narrow as a general model.

Current agent context may include:

- system/developer instructions;
- tool definitions and schemas;
- structured runtime state;
- transcript/history;
- retrieved documents;
- checkpoints;
- external memory/store contents;
- environment observations;
- policy metadata.

**Normalized principle**

> The model acts from the context projected into a turn; the agent system may maintain substantially more state than the model sees at once.

### Security counterexample

The minimal tutorial exposes a model-callable `run_command` tool that uses shell execution. This is pedagogically effective for showing agency, but **must not become our production pattern**.

**Candidate security rule**

> General shell/code execution is a high-blast-radius capability. Prefer narrow tools; when code execution is required, constrain filesystem, network, credentials, command surface, resources and side effects with a sandbox/policy boundary.

## 5. Tool design / ACI

Across the repository, tools bridge probabilistic model decisions and deterministic APIs/files/data.

### Durable extraction

A tool contract is more than its function signature:

```text
identity / purpose
input schema
validation
authorization
risk level
side-effect semantics
idempotency
error taxonomy
retryability
time/cost budget
output schema
provenance / evidence
observability receipt
```

### Repository signal

Issue #129 asks for a consistent error model that distinguishes model, tool, parsing, timeout and downstream failures and expresses retryability.

This is a strong **design pressure signal**, but not evidence that every upstream example lacks such handling.

### Official contrast

Anthropic's tool-engineering guidance independently supports treating tools as an Agent-Computer Interface and evaluating tool ergonomics with realistic tasks, held-out cases, tool-call/error counts, latency and token use.

### Candidate rule

> An agent should not infer retry policy from an arbitrary error string such as “try again”. The tool/runtime should expose structured error class + retryability + backoff/budget policy.

## 6. Retries and termination

The repository contains multiple retry patterns, from bounded `for attempt in range(...)` loops and Tenacity usage to explanatory TODOs suggesting retry logic.

The minimal agent tutorial also demonstrates a failure spiral caused when an error text encourages repeated action.

### Normalized retry model

```text
failure
  ↓
classify
  ├─ permanent / invalid request ─► fail / revise action
  ├─ authorization / policy ──────► block / escalate
  ├─ transient ──────────────────► bounded retry + backoff
  └─ unknown ────────────────────► fail-safe / bounded diagnostic path
```

### Candidate termination contract

Every autonomous loop should declare at minimum:

- success predicate;
- terminal failure predicate;
- max model turns;
- max tool calls;
- per-tool retry budget;
- wall-clock deadline;
- token/cost budget where relevant;
- repeated-action/oscillation detection;
- external cancellation path.

A fixed `MAX_TURNS` is a useful safety net, not a complete termination model.

## 7. Human-in-the-Loop and consequential actions

The recent HITL tutorial is one of the best-supported upstream slices because its behavior is exercised by dedicated tests.

### Strong observations

Tests demonstrate that:

- low-risk lookup can execute without approval;
- mutating refund requests pause before any side effect;
- direct dispatcher bypass is rejected;
- approve/reject/modify decisions have distinct behavior;
- modified arguments are revalidated;
- unexpected arguments are rejected;
- invalid numeric edge cases are rejected;
- audit events capture decisions/actions;
- LangGraph integration pauses and resumes using persisted thread state when the notebook-pinned version is present.

### Official contrast

Current LangGraph documentation independently prescribes persisted state for interrupt/resume and recommends a durable checkpointer in production rather than an in-memory saver.

### Portable invariants

```text
proposal
  ↓
validate schema
  ↓
classify risk
  ├─ low risk ───────► execute
  └─ review required
          ↓
     persist request
          ↓
       interrupt
          ↓
 approve / edit / reject
   │        │       │
   │        │       └──► terminate without side effect
   │        └──► revalidate edited action
   └────────────► authorization receipt
                     ↓
                  execute
                     ↓
                   audit
```

### Candidate rules

- Approval must occur **before** the consequential effect.
- Approval state must be durable if execution can outlive a process/session.
- Editing an action invalidates the prior validation result.
- The tool dispatcher should independently enforce authorization so bypassing orchestration does not bypass policy.
- Code before a resumable interrupt must be replay-safe/idempotent where the framework can rerun a node.

## 8. State, persistence, context and memory

Repository search shows recurring use of `MemorySaver`/in-memory state in several LangGraph tutorials, with some examples also using SQLite or stores.

This is useful pedagogically but must be normalized.

### Proposed vocabulary

```text
STATE
structured facts needed by the current execution

CHECKPOINT
serialized state at an execution boundary

PERSISTENCE
mechanism that makes checkpoints/state durable

CONTEXT
information projected into the model for one inference turn

SESSION MEMORY
information retained across turns/steps in one interaction scope

LONG-TERM MEMORY
information intentionally retained/retrieved across sessions

KNOWLEDGE / RAG
external source material retrieved because it may answer a task
```

### Candidate rule

> Do not call all persisted information “memory”. Persistence is an execution property; memory is a semantic/lifecycle policy.

## 9. Trace-based evaluation

The trace-evaluation tutorial is also backed by dedicated tests.

### What the upstream slice demonstrates well

Its deterministic evaluator separates checks for:

- expected tool sequence;
- tool arguments;
- evidence/claims;
- latency;
- execution errors.

The tests also cover:

- exceptions converted to failed traces without aborting the suite;
- contradictory claims losing evidence credit;
- extra tool calls violating expected trajectory;
- latency budget boundaries;
- suite-level quality gates for pass rate, tool accuracy and p95 latency.

### Why this should not be promoted unchanged

A deterministic trace score is only one evaluation layer.

Agent systems are stochastic and can solve a task through multiple valid trajectories. An exact expected tool sequence can therefore be appropriate for **policy/contract tests** but too brittle for every capability eval.

Current eval guidance distinguishes:

- task;
- trial;
- grader;
- transcript/trace;
- outcome;
- harness;
- suite.

### Normalized evaluation stack

```text
STATIC CONTRACT TESTS
schemas / permissions / deterministic invariants
        ↓
UNIT + INTEGRATION TESTS
runtime, tools, persistence, replay, side effects
        ↓
TRAJECTORY EVALS
calls, arguments, policy violations, loops, efficiency
        ↓
OUTCOME EVALS
external task state / correctness / user-visible result
        ↓
REPEATED TRIALS
variance / pass@k / stability
        ↓
REGRESSION GATES
quality + latency + cost + safety
        ↓
PRODUCTION OBSERVABILITY
real failures / feedback / drift
```

### Candidate rule

> Never allow a trajectory grader to award “success” when the external outcome contradicts it.

## 10. Reflection and “self-improvement”

The repository includes reflection/self-improvement patterns. This terminology requires scientific discipline.

### Scientific contrast

- **Reflexion** shows that linguistic feedback stored across trials can improve performance under studied conditions.
- **Large Language Models Cannot Self-Correct Reasoning Yet** finds that intrinsic self-correction without external feedback is unreliable and can degrade results.

### Normalized distinction

```text
REFLECTION
model produces critique/reasoning about prior attempt

REVISION LOOP
model generates another attempt using critique

FEEDBACK-DRIVEN ADAPTATION
revision uses external verifier/environment/human signal

LEARNING
persistent capability/parameter/policy change demonstrated across future tasks
```

### Candidate rule

> Do not label a reflection loop “self-improving” unless improvement is measured across an evaluation distribution and persists under a defined mechanism.

## 11. Multi-agent systems

The upstream includes multiple multi-agent examples and orchestration topologies.

### Scientific pressure test

Recent empirical work on multi-agent LLM systems identifies failure families including:

- specification/system-design failures;
- inter-agent misalignment;
- task verification and termination failures.

This supports a conservative baseline.

### Candidate admission test for multi-agent

Before adding another agent, require a falsifiable benefit hypothesis such as:

- independent subtasks can execute in parallel;
- context can be partitioned without destructive information loss;
- specialized tools/permissions require isolation;
- independent critique/verifier role materially improves outcomes;
- throughput improves enough to offset coordination cost.

Measure against a single-agent or deterministic baseline.

### Anti-pattern

```text
problem is hard
    ↓
add more agents
    ↓
more conversations
    ↓
assume better reasoning
```

More agents add tokens, latency, coordination state and new failure modes. Complexity must earn promotion through evidence.

## 12. MCP

The repository includes an MCP tutorial and frames MCP as a bridge between AI systems and external resources/tools.

### Qualification

MCP is highly relevant as an interoperability protocol, but it is **not** the whole agent architecture.

A complete agent system still needs decisions about:

- capability discovery;
- tool authorization;
- trust boundaries;
- context selection;
- runtime loop;
- retries/timeouts;
- side-effect policy;
- persistence;
- observability;
- evaluation.

### Candidate rule

> Protocol interoperability must not be confused with execution authorization.

A tool being discoverable through MCP does not imply the model should be allowed to invoke it without policy.

## 13. Retrieval and grounding failure signal

Issue #95 reports that an internet-summary tutorial appeared to give the model search titles rather than fetched article contents.

Whether or not the specific implementation was later corrected, the failure class is durable:

```text
retrieval API returns metadata
        ↓
application assumes document content
        ↓
LLM summarizes metadata
        ↓
fluent answer falsely appears grounded
```

### Candidate rule

> Provenance must identify what bytes/text the model actually received, not merely the URL or source the application intended to retrieve.

This maps directly to Jett Engineering Method: `intended evidence != observed evidence`.

## 14. Security model extracted from the corpus

The tutorial corpus demonstrates powerful tool access but is not itself a complete security specification.

### Required production boundary

For agent-accessible operations, reason across:

| Surface | Required questions |
|---|---|
| Filesystem | what paths may be read/written? symlinks? traversal? |
| Shell/code | what commands/runtime? sandbox? CPU/time/memory? |
| Network | what hosts/protocols? SSRF? exfiltration? |
| Secrets | can model/tool outputs expose credentials? |
| Databases | read vs mutation? parameterized queries? transaction boundary? |
| External APIs | scopes? rate/cost limits? idempotency? |
| User content | prompt injection / untrusted instructions? |
| Side effects | reversible? approval? compensating action? |

### Candidate rule

> Prompt-level “do not do X” is defense-in-depth, not a security boundary.

## 15. What we should learn from the repository itself

Beyond agent implementation patterns, the repository's evolution teaches a meta-rule.

Recent additions strengthened:

- dependency maintenance through Dependabot;
- contribution hygiene through a notebook validator;
- behavior evidence for HITL;
- deterministic trace evaluation;
- explicit bounded-loop pedagogy.

This indicates a maturation path from **examples → contracts → tests/evals**.

That maturation path is more reusable than any individual notebook.

## 16. Claim disposition matrix

| Upstream idea/claim | Disposition | Reason |
|---|---|---|
| agent systems often reduce to repeated model/tool interaction | `SUPPORTED / QUALIFIED` | useful core loop, but runtime/context can be richer |
| prompt rule < runtime-enforced invariant | `SUPPORTED` | directly demonstrated and consistent with engineering boundaries |
| transcript is the entire agent mind | `QUALIFIED` | true only for minimal stateless projection; context/state can exist elsewhere |
| LangGraph state/checkpoints useful for HITL | `SUPPORTED` | source tests + official docs |
| in-memory checkpointing is sufficient generally | `REJECT FOR PRODUCTION` | official docs recommend durable persistence in production |
| deterministic trace scoring is an agent eval | `SUPPORTED AS LAYER` | useful but incomplete without outcomes/repeated trials |
| reflection means self-improvement | `CONTRADICTED AS GENERAL CLAIM` | external feedback/evidence needed; intrinsic self-correction unreliable |
| multi-agent is more capable by default | `REJECT` | added failure modes/cost; benefit must be measured |
| MCP solves agent integration architecture | `QUALIFIED` | protocol solves interoperability slice, not policy/runtime/eval |
| framework constructor defines “agent” | `REJECT` | model/control authority is more meaningful taxonomy |
| notebook validator proves tutorial works | `REJECT` | validator is structural, not execution evidence |
| root dependency pin proves reproducibility | `REJECT` | versions differ across newer tutorial slices |
| ready-to-use implementation == production-ready | `REJECT` | no equivalent evidence chain |

## 17. Candidate reusable artifacts for MK2

Do not build these until MK1 normalizes the taxonomy:

1. `AGENT_SYSTEM.md` architecture contract template;
2. tool contract schema;
3. action risk/approval matrix;
4. structured error + retryability schema;
5. termination/budget contract;
6. state/context/memory decision table;
7. HITL side-effect checklist;
8. agent eval manifest (`tasks / trials / graders / outcomes / metrics`);
9. trace event schema;
10. multi-agent admission checklist;
11. agent security threat-model template;
12. reproducibility receipt for model/framework/tool versions.

## 18. Open questions before MK0 closure

- How many upstream tutorials are truly model-directed vs deterministic workflows under our normalized taxonomy?
- Which tutorials can cause external side effects, and what approval/idempotency controls exist in each?
- Which examples use unrestricted generated code/shell/browser/database execution?
- How consistently are retries bounded and classified?
- Which examples have durable state vs in-memory-only demonstrations?
- How many have objective success predicates rather than model-judged completion?
- How many have runnable automated tests?
- Which MCP patterns predate/currently diverge from the current specification revision?
- Which memory patterns belong in `agent-engineering` versus a future dedicated memory subdomain/source?
- Which production engineering rules are better sourced from the upstream `agents-towards-production` sister repository rather than inferred here?

Until these are answered, **this quarry remains evidence, not canon**.
