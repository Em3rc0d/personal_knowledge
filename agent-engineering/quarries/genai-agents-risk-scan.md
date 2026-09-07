# GenAI_Agents — Capability & Risk Scan

> Quarry evidence — **NOT CANON**  
> Upstream: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`  
> Scan date: 2026-09-07

## Purpose

Pressure-test the tutorial corpus by looking specifically for capabilities that change blast radius: generated code, shell, browser control, external writes, persistence, polling/retries, approval gates and idempotency.

This is a static source scan. Presence of a code pattern does not prove it is reachable in every run, and absence from a search does not prove a capability is absent.

## Risk scale used here

```text
R0  pure generation / no external state
R1  read-only external/local data
R2  reversible or sandboxed local mutation
R3  external mutation / communication / publication
R4  general code/shell/browser capability or broad environmental authority
```

Risk level describes potential blast radius, not code quality.

## Findings

### RS-01 — Minimal agent exposes general shell execution

- artifact: `agent_while_loop_from_scratch.ipynb`
- observed capability: model-selectable command tool reaches `subprocess.run(..., shell=True, ...)`;
- positive control: hard turn cap and repeated-failure guard;
- risk: `R4` if generalized outside a disposable tutorial environment.

**Disposition**

Pedagogically valuable for exposing the agent loop. Reject as a production tool shape unless execution is sandboxed and narrowed by policy.

**Portable rule**

> A general executor is a capability boundary, not an ordinary tool. Scope filesystem, network, credentials, command surface, resources and side effects independently of the prompt.

---

### RS-02 — E2E testing executes generated Python and controls a browser

- artifact: `e2e_testing_agent.ipynb`;
- observed capability: LLM-generated Playwright script is executed dynamically with Python `exec(...)`;
- environment: browser automation against a target web application;
- risk: `R4`.

**Threat surfaces**

- arbitrary Python execution;
- browser session authority;
- credential/session leakage if real credentials are present;
- unintended navigation or external requests;
- filesystem/process access inherited by the notebook runtime.

**Portable rule**

> Generated E2E code should execute in an isolated, disposable environment with explicit network/credential scope. A test target does not make generated code intrinsically safe.

---

### RS-03 — Self-healing example executes generated replacement code

- artifact: `self_healing_code.ipynb`;
- observed capability: newly generated code is executed dynamically to obtain the repaired function;
- risk: `R4` when model output is not sandboxed.

**Useful pattern**

Generate → test → revise can be powerful where correctness is machine-verifiable.

**Required normalization**

Generate → **isolate** → test → inspect evidence → promote. Never equate successful execution with safe integration.

---

### RS-04 — Social publishing has real external mutation but includes safety switches

- artifact: `social_media_publishing_agent_publora_langgraph.ipynb`;
- observed capability: create/schedule social posts through an external API;
- observed controls:
  - `DRY_RUN = True` by default;
  - dry run creates drafts / avoids scheduling;
  - bounded self-revision count;
  - optional idempotency key support;
- risk: `R3` when scheduling/publishing is enabled.

**Positive extraction**

This is a better pattern than prompt-only caution: a deterministic execution-mode switch changes what the system can actually do.

**Portable rule**

> Externally visible mutations should support a safe preview/draft mode, idempotency, explicit promotion to live execution and auditable receipts.

---

### RS-05 — HR examples can send external messages

- artifacts: `Hr_AI_Agent.ipynb`, `HR_AI-Assistant.ipynb`;
- observed capability: HTTP POST to a message endpoint with recipients and generated message content;
- other source evidence: HR tutorials also contain human-interrupt patterns in parts of their workflow;
- risk: `R3`.

**Open verification question**

Does every outbound communication path share one enforceable approval/policy boundary, or can a lower-level sender be called independently?

This remains `UNKNOWN` until the full call graph is normalized.

---

### RS-06 — ShopGenie contains SMTP delivery

- artifact: `ShopGenie.ipynb`;
- observed capability: connects to an SMTP server with TLS and sends generated recommendation output;
- risk: `R3`.

**Portable rule**

> “Generate email” and “send email” are separate privileges. Content generation may be autonomous while transmission remains gated.

---

### RS-07 — Document intake uploads user file bytes to an external conversion service

- artifact: `document_intake_agent_langgraph.ipynb`;
- observed capability:
  - declare conversion job;
  - upload file bytes to a presigned object-storage URL;
  - poll job status;
  - download converted output;
- positive control: supports an optional idempotency key;
- risk: `R3` for confidentiality/data-egress, even though the operation is conceptually “conversion”.

**Important extraction**

A read/transform operation can still be security-sensitive when it moves private bytes across a trust boundary.

**Required contract**

```text
data classification
allowed destination/service
retention policy
size/type validation
malware/content boundary where relevant
idempotency
overall deadline / cancellation
provenance of returned bytes
```

The static scan observed a polling loop; the complete deadline/cancellation semantics must be verified before treating it as a reusable reliability pattern.

---

### RS-08 — Car buyer uses browser automation for scraping

- artifact: `car_buyer_agent_langgraph.ipynb`;
- observed capability: browser automation via a Playwright-compatible interface for scraping;
- risk: primarily `R1`, but browser runtimes can become `R4` if exposed as open-ended model-controlled navigation/actions.

**Portable rule**

> Browser capability risk depends on action authority, not on the word “scraping”. Restrict origin/domain, authentication context, allowed actions and downloads.

---

### RS-09 — Local structured storage appears in quoting/memory examples

- artifact: `contextual_quoting_agentic_system.ipynb`;
- observed capability: local SQLite database use;
- multiple LangGraph tutorials also use `MemorySaver`/in-memory stores;
- risk: normally `R1-R2`, but persistence semantics matter more than storage technology.

**Portable rule**

> Treat operational state, checkpoints, semantic memory and business data as different stores/contracts even when a demo puts them in one process.

---

### RS-10 — Some graph examples set explicit recursion limits

Observed `recursion_limit = 50`-style configuration in representative LangGraph tutorials including graph-inspection, AutoML/data-science and murder-mystery examples.

**Positive extraction**

Framework-level recursion limits are useful kill switches.

**Qualification**

A recursion limit alone does not define:

- success condition;
- retry policy;
- wall-clock deadline;
- tool-call budget;
- cost/token budget;
- repeated-state/oscillation detection.

**Portable rule**

> Runtime hard stops are mandatory safety nets; semantic termination contracts are still required.

---

### RS-11 — Idempotency appears in newer external-operation examples

Observed explicit idempotency-key support in:

- document conversion flow;
- social publishing API wrapper.

**Positive extraction**

This is a high-value production-oriented pattern because retries, pause/resume and agent uncertainty make duplicate side effects likely.

**Portable rule**

> Every retryable mutating tool should state its idempotency contract or compensating-action strategy.

## Cross-cutting capability matrix

| Artifact / family | Main capability | Risk | Positive controls observed | Main missing proof before canon |
|---|---|---:|---|---|
| minimal while-loop | general shell | R4 | max turns, repeat-failure guard | sandbox/least privilege |
| E2E testing | generated code + browser | R4 | workflow structure/reporting | isolated execution + network/secret bounds |
| self-healing code | generated code execution | R4 | test/revision concept | sandbox + promotion gate |
| social publishing | external publication | R3 | dry run, bounded revision, idempotency | full approval/audit semantics |
| HR assistant | outbound messages | R3 | HITL patterns exist | prove sender cannot bypass policy |
| ShopGenie | SMTP send | R3 | TLS transport | explicit send approval/idempotency |
| document intake | external file upload/transform | R3 | idempotency key | data-governance + overall deadline |
| car buyer | browser scraping | R1→R4 | task-specific flow | domain/action containment |
| quoting/database | local DB | R1/R2 | structured data | read/write permission taxonomy |
| graph loops | recursive execution | varies | recursion limits in samples | semantic termination + budgets |

## Security principles promoted as candidates

1. **Capability > label.** “Test”, “scrape”, “convert” or “assistant” does not determine risk; actual authority does.
2. **Separate generation from execution.** Model output is data until an execution boundary deliberately promotes it to action.
3. **Default safe mode for mutations.** Preview/draft/dry-run should be a deterministic mode when feasible.
4. **Idempotency is first-class.** Retryable writes require keys, deduplication or compensating transactions.
5. **Least privilege for browser/shell/code.** Narrow tools beat general executors unless generality is required and contained.
6. **Data movement is a side effect.** Uploading private files is consequential even if no public mutation occurs.
7. **Budgets exist at multiple levels.** Recursion/turn caps do not replace tool, time, token/cost and retry budgets.
8. **Human approval must gate the actual dispatcher.** UI review alone is insufficient.
9. **Execution receipts must outlive narration.** Record what was actually invoked, with validated args and external result identifiers.
10. **Threat models use real capabilities.** Classify filesystem, network, code, browser, database, communication and publication separately.

## New MK0 fixtures derived from this scan

Future operationalization should test at least these adversarial cases:

- generated code attempts filesystem/network access outside declared scope;
- browser action leaves allowed origin;
- a mutating tool is retried after timeout and would duplicate the side effect without idempotency;
- a reviewer edits arguments after approval request;
- low-level sender/dispatcher is invoked without workflow approval;
- external upload contains data not permitted to leave the trust boundary;
- agent repeats a semantically identical failed action using different textual arguments;
- graph hits recursion limit without producing a verified outcome;
- model reports success although external receipt is absent;
- a dry-run/live-mode flag is changed by model-controlled input rather than trusted configuration.

## Status

This scan materially strengthens the security/side-effect side of MK0, but it is not exhaustive across every notebook. `UNKNOWN` remains appropriate for unsampled execution paths.
