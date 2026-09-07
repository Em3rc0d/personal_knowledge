# GenAI_Agents — P0/P1 Call-Path Verification

> Status: **MK0 quarry evidence — NOT CANON**  
> Primary upstream: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
> Verification pass: 2026-09-07  
> Purpose: convert README-level triage into implementation-path evidence sufficient for MK0 classification.

## Evidence semantics

This document deliberately separates:

- **OBSERVED** — directly visible in source/tests at the pinned snapshot;
- **SOURCE CLAIM** — stated by upstream documentation/notebook text;
- **INFERRED** — engineering implication derived from observed evidence;
- **UNKNOWN** — a material detail not established by the inspected path;
- **DISPOSITION** — how `agent-engineering` should classify the pattern for MK1.

`call-path verified` means the consequential capability and its execution boundary are sufficiently established to classify the system. It does **not** mean the notebook was executed end-to-end or is production-safe.

---

# P0 — blast-radius families

## P0-01 — E2E Testing Agent

Artifact: `all_agents_tutorials/e2e_testing_agent.ipynb`

### Call path

```text
natural-language test request
  ↓
LLM converts request into structured actions
  ↓
workflow builds/extends Playwright Python script
  ↓
script stored in graph state
  ↓
Python exec(state["script"], ...)
  ↓
Playwright controls browser / observes DOM
  ↓
workflow continues until test path completes
```

### Evidence

**OBSERVED**

- `convert_user_instruction_to_actions` parses natural-language instructions into executable actions;
- `get_initial_action` initializes browser navigation/DOM retrieval;
- the notebook executes the accumulated `state["script"]` through Python `exec(...)`;
- Playwright is the execution substrate;
- the tutorial starts a local Flask app as its demonstration target.

### Engineering reading

The browser is not the primary security boundary. `exec(...)` promotes model-derived text into general Python execution inside the notebook process. The inherited capability set can include filesystem, environment, process and network access beyond the nominal browser task.

**DISPOSITION:** `R4 / generated-code execution`; generated test code must be treated as untrusted executable input.

**MK1 invariant seed:** generation and execution are separate authority domains.

---

## P0-02 — Self-Healing Codebase

Artifact: `all_agents_tutorials/self_healing_code.ipynb`

### Call path

```text
failing/target function
  ↓
LLM proposes replacement source code
  ↓
new_code string
  ↓
exec(new_code, namespace)
  ↓
replacement callable recovered from namespace
  ↓
subsequent workflow evaluates/uses revised function
```

### Evidence

**OBSERVED**

The implementation explicitly executes generated `new_code` with Python `exec(...)`.

### Qualification

Generate → test → revise is a useful repair pattern when the environment can objectively evaluate behavior. However, passing functional tests does not prove containment, absence of exfiltration, or suitability for promotion into a real codebase.

**DISPOSITION:** `R4 / generated-code execution`.

**MK1 invariant seed:** `generate → isolate → test → inspect evidence → promote`; never `generate → exec in trusted runtime → assume safe`.

---

## P0-03 — Minimal Agent While Loop

Artifact: `all_agents_tutorials/agent_while_loop_from_scratch.ipynb`

### Call path

```text
question + transcript
  ↓
model chooses tool
  ↓
run_tool(name, args)
  ├─ list_files
  ├─ read_file
  └─ run_command
          ↓
      subprocess.run(..., shell=True, timeout=60)
  ↓
tool result appended to transcript
  ↓
next model turn
```

### Positive controls

**OBSERVED**

- `MAX_TURNS` hard cap;
- exact failed-call registry;
- optional loop-level guard preventing the same failed call from being retried;
- command timeout.

### Boundary

The model-callable shell is still a general executor. The loop guard improves reliability but does not constrain command authority, filesystem scope, network scope, credentials or process privileges.

**DISPOSITION:** `R4-demo`; excellent harness pedagogy, unsafe default tool shape outside an isolated environment.

---

## P0-04 — HR AI Assistant / HR AI Agent

Artifacts:

- `all_agents_tutorials/HR_AI-Assistant.ipynb`
- `all_agents_tutorials/Hr_AI_Agent.ipynb`

### Call path of concern

```text
agent workflow
  ↓
ToolNode exposes:
  - candidate search
  - profile lookup
  - send_linkedin_message
  ↓
model/tool routing can select sender
  ↓
send_linkedin_message(...)
  ↓
HTTP POST containing recipient + generated message
```

### Evidence

**OBSERVED**

- `send_linkedin_message` is decorated as a tool;
- it is included in the same `ToolNode` as read-oriented candidate/profile tools;
- the sender performs an external HTTP POST;
- `NodeInterrupt` is present elsewhere for human review of generated job descriptions/interview questions.

### Boundary finding

**UNKNOWN:** the inspected source did not establish a single enforceable approval gate co-located with every outbound-message dispatch.

The presence of human interrupts elsewhere must not be generalized into “all consequential HR actions are HITL protected.”

**DISPOSITION:** `R3 / external communication`; split read tools from communication privileges and gate the actual sender when policy requires approval.

---

## P0-05 — Social Media Publishing Agent

Artifact: `all_agents_tutorials/social_media_publishing_agent_publora_langgraph.ipynb`

### Call path

```text
content request
  ↓
platform-specific generation
  ↓
deterministic length checks + LLM reviewer
  ↓
bounded revise loop
  ↓
publish stage
  ↓
create_post(content, platform_id, scheduled_time)
  ↓
external Publora API
```

### Positive controls

**OBSERVED**

- `DRY_RUN = True` by default;
- dry-run path creates drafts / avoids scheduling live publication;
- bounded revision count (`MAX_ITERS`);
- optional `Idempotency-Key` support in API wrapper;
- per-platform failures are isolated rather than aborting every publication.

### Qualification

Dry-run is a strong deterministic safety pattern because it changes the executable capability, not merely the prompt. It is not equivalent to human approval and must not be model-controlled.

**DISPOSITION:** `R3 / external publication`; positive reference for safe-mode + idempotency patterns.

---

## P0-06 — ShopGenie outbound email

Artifact: `all_agents_tutorials/ShopGenie.ipynb`

### Call path

```text
product research/comparison
  ↓
LLM-generated email metadata/body
  ↓
HTML template
  ↓
send_email(recipient, subject, body)
  ↓
SMTP + STARTTLS
  ↓
external delivery
```

### Evidence

**OBSERVED**

The final flow calls `send_email(...)`; that function establishes SMTP transport and sends generated recommendation output.

### Boundary finding

Transport encryption protects the channel, not authorization or duplicate-send semantics.

**UNKNOWN:** no idempotency/approval contract was established in the inspected call path.

**DISPOSITION:** `R3 / external communication`; generation and transmission are separate privileges.

---

## P0-07 — Document Intake Agent

Artifact: `all_agents_tutorials/document_intake_agent_langgraph.ipynb`

### Call path

```text
local document path
  ↓
convert_document(state)
  ↓
convert_file(path, to="md")
  ↓
POST conversion job metadata
  ↓
PUT original file bytes to presigned upload URL
  ↓
poll remote conversion status
  ↓
GET converted bytes
  ↓
markdown becomes grounded-answer input
```

### Positive controls

**OBSERVED**

- optional idempotency-key header support;
- explicit HTTP timeouts on transfer operations;
- deterministic conversion function before downstream grounded QA.

### Boundary finding

Conceptually “reading/converting a file” is actually **data egress** across a trust boundary.

**UNKNOWN:** the inspected static path did not establish a complete global deadline/cancellation policy or data-classification/retention policy.

**DISPOSITION:** `R3 / confidentiality + data egress`.

---

## P0-08 — DataScribe database exploration

Artifact: `all_agents_tutorials/database_discovery_fleet.ipynb`

### Source-level warning

**SOURCE CLAIM / OBSERVED notebook text**

The notebook explicitly warns that it is untested, has no safety rails, may attempt `INSERT`, `UPDATE` and `DELETE`, must not be used on production data, and recommends using a `READONLY` database user.

### Engineering meaning

The strongest control proposed by the tutorial itself is therefore outside the model/workflow: database credentials with read-only privileges.

This is a high-value lesson even though the precise lower-level query dispatcher was not fully reconstructed in this pass:

> authorization at the database principal is stronger than asking a model to generate only safe SQL.

**UNKNOWN:** exact reachable mutation path and parser/statement filtering behavior were not fully established from the available source view.

**DISPOSITION:** `R4 if write-capable credentials; R1 under enforced read-only principal`.

The risk rating is determined by **actual DB privilege**, not by the intended “schema exploration” use case.

---

## P0-09 — Car Buyer browser scraping

Artifact: `all_agents_tutorials/car_buyer_agent_langgraph.ipynb`

### Evidence

**OBSERVED**

- uses a Playwright-compatible browser API (`patchright.async_api.async_playwright`);
- browser is used for dynamic web scraping/retrieval;
- browser lifecycle is managed by workflow code.

### Boundary

The inspected pattern is primarily retrieval-oriented. A browser engine itself is still a high-capability substrate; risk rises materially if authentication, arbitrary navigation, downloads, form submission or mutation are exposed to model control.

**UNKNOWN:** no evidence in the inspected path established authenticated mutating browser actions.

**DISPOSITION:** current sampled behavior `R1`, underlying browser capability `R4-capable`; classify authority by allowed actions/origins rather than library choice.

---

# P1 — epistemic / reliability families

## P1-01 — Self-Improving Agent

Artifact: `all_agents_tutorials/self_improving_agent.ipynb`

### Evidence

**SOURCE CLAIM**

Upstream describes a response generator, chat-history manager, reflection mechanism and a “learning system” that incorporates reflection insights into future responses.

**OBSERVED/QUALIFIED**

The mechanism is a reflection/revision/adaptation loop; the inspected source does not establish parameter learning or a benchmark proving persistent capability improvement across a held-out task distribution.

### Normalization

```text
reflection        != learning
revision          != durable adaptation
better one run    != demonstrated improvement distribution
```

**DISPOSITION:** classify as `reflection/adaptation pattern`, not as proven self-improving system.

---

## P1-02 — Memory-enhanced agents

Representative artifacts:

- `memory_enhanced_conversational_agent.ipynb`
- `memory-agent-tutorial.ipynb`
- multiple LangGraph examples using `MemorySaver` / stores

### Cross-source finding

The dedicated `Agent_Memory_Techniques` repository provides a materially better taxonomy: short-term, long-term, cognitive, retrieval/routing, frameworks and evaluation/production, with explicit persistence and retrieval dimensions.

Therefore the generic GenAI corpus is retained as implementation examples, not as canonical memory semantics.

### Normalization

For MK1, every memory claim must state:

```yaml
scope: turn | session | cross-session | shared
write_policy:
retrieval_policy:
persistence:
isolation_key:
retention:
forgetting/update_semantics:
provenance:
evaluation:
```

**DISPOSITION:** replace “uses memory” with a lifecycle contract.

---

## P1-03 — Scientific Paper Agent / Systematic Review

Artifacts:

- `scientific_paper_agent_langgraph.ipynb`
- `systematic_review_of_scientific_articles.ipynb`

### Positive patterns

**OBSERVED/SOURCE CLAIM**

The corpus includes structured scholarly retrieval/document processing, retry mechanisms, stateful workflows and quality/improvement nodes.

### Epistemic boundary

A node called `quality`, `review` or `fact-check` is not independently authoritative if it is another LLM over the same evidence.

Research-grade completion needs stronger contracts:

- source identity and retrieval receipt;
- evidence actually provided to the model, not only source URL/title;
- claim-to-source linkage;
- exclusion/selection criteria where systematic review is claimed;
- deterministic metadata checks where possible;
- uncertainty and unresolved-conflict handling;
- human verification for high-stakes synthesis.

**DISPOSITION:** useful research-orchestration patterns; do not promote “research rigor” from node names alone.

---

## P1-04 — Journalism Assistant

Artifact: `journalism_focused_ai_assistant_langgraph.ipynb`

### Evidence

The tutorial combines web retrieval with fact-checking/bias-analysis style stages and retry handling around search.

### Qualification

The earlier repository issue around the internet-summary example — where titles rather than article contents could be summarized — demonstrates why **intended source ≠ observed evidence**.

**DISPOSITION:** journalism/fact-checking workflows require content-level provenance receipts and claim-level evidence, not source labels alone.

---

## P1-05 — Multi-agent systems

Representative artifacts:

- `multi_agent_collaboration_system.ipynb`
- `research_team_autogen.ipynb`
- ATLAS / career assistant / grocery / content systems

### Mining result

The corpus demonstrates routing, role specialization, shared state and delegation. It does not establish a general rule that multi-agent topology improves outcomes over a simpler baseline.

### MK1 admission contract

A multi-agent design must name a falsifiable reason:

- parallelizable independent work;
- permission/tool isolation;
- context partitioning;
- independent verifier role;
- specialization with measurable quality benefit;
- throughput/latency improvement.

Then compare against a single-agent or deterministic baseline.

**DISPOSITION:** topology is an engineering variable, not a maturity level.

---

## P1-06 — MCP tutorial

Artifact: `all_agents_tutorials/mcp-tutorial.ipynb`

### Upstream implementation shape

**OBSERVED**

The tutorial imports MCP `ClientSession`, creates a client session, calls `initialize()`, discovers tools with `list_tools()` and executes tools through the client.

### Current-protocol contradiction

Current MCP specification `2026-07-28` introduced a stateless protocol core and removed the core `initialize` / `initialized` handshake and `Mcp-Session-Id`. Requests are self-describing; optional `server/discover` replaces mandatory upfront handshake for clients that need capabilities.

Other current changes include:

- `MCP-Protocol-Version` per request;
- method/name routing headers;
- cacheable deterministic list responses;
- authorization hardening;
- formal extensions framework;
- tasks and multi-round-trip request mechanisms;
- explicit deprecation lifecycle.

### Disposition

The notebook remains useful for understanding **tool discovery and protocol-mediated tool execution**, but its lifecycle/transport mechanics are legacy relative to `2026-07-28`.

**MK1 rule:** MCP version is part of the integration contract. “Supports MCP” without protocol revision, transport/auth model and capability set is underspecified.

---

# P0/P1 closure matrix

| Family | Classification evidence | Remaining UNKNOWN that blocks later certification | MK0 status |
|---|---|---|---|
| generated E2E code + browser | direct `exec(state["script"])` | sandbox policy | CLOSED FOR CLASSIFICATION |
| self-healing generated code | direct `exec(new_code, ...)` | sandbox/promotion evidence | CLOSED FOR CLASSIFICATION |
| generic shell loop | direct `shell=True` dispatcher | isolation/least privilege | CLOSED FOR CLASSIFICATION |
| HR external messaging | sender tool + HTTP POST + ToolNode | universal send approval boundary | CLOSED; UNKNOWN PRESERVED |
| social publishing | create/schedule API + dry-run/idempotency | full human approval semantics | CLOSED FOR CLASSIFICATION |
| SMTP email | direct final send path | idempotency/approval | CLOSED; UNKNOWN PRESERVED |
| document conversion | actual external byte upload/poll/download | retention/global deadline | CLOSED; UNKNOWN PRESERVED |
| database exploration | explicit no-safety-rails + DML warning | exact mutation dispatcher path | CLOSED; UNKNOWN PRESERVED |
| browser scraping | Playwright-compatible retrieval | authenticated mutation reachability | CLOSED; UNKNOWN PRESERVED |
| self-improvement | reflection/learning claim | benchmarked persistent improvement | CLOSED AS QUALIFIED CLAIM |
| memory | generic examples + dedicated taxonomy contrast | per-example lifecycle detail | CLOSED FOR MK0; MOVES TO MK1 |
| research/fact-checking | retrieval/review workflows | claim-level provenance strength | CLOSED FOR MK0; MOVES TO MK1 |
| multi-agent | topology examples | measured baseline advantage | CLOSED AS QUALIFIED CLAIM |
| MCP | old session lifecycle vs 2026-07-28 | per-SDK migration/version details | CLOSED AS VERSIONED CONTRADICTION |

## MK0 conclusion from this pass

Every P0/P1 family now has enough evidence to answer the MK0 question: **what class of engineering problem is this, what authority exists, which claim is justified, and what remains UNKNOWN?**

That is sufficient to stop using upstream marketing/category labels as the ontology. It is intentionally insufficient to certify production safety or runtime reproducibility; those belong to later MKs.