# Agent Engineering — Capability-Centered Threat Model

> Status: **MK0 architecture seed**  
> Purpose: make agent risk a function of real authority and trust boundaries rather than labels such as `assistant`, `test`, `scraper`, `MCP` or `workflow`.

This threat model is derived from the P0/P1 mining pass over `GenAI_Agents` plus current protocol/runtime guidance. It is not tied to one framework.

## 1. Security objective

An agent system is safe only when probabilistic model decisions are surrounded by deterministic controls that bound:

- what information can enter model context;
- what information can leave a trust boundary;
- which capabilities can be invoked;
- with which arguments and identity;
- under what authorization/approval state;
- how often and for how long;
- what external state can change;
- how effects are verified and audited.

The model is never the final security principal.

## 2. Protected assets

```text
SECRETS
API keys, OAuth tokens, session cookies, private keys, credentials

PRIVATE DATA
user files, messages, source documents, personal/business records

SYSTEM INTEGRITY
filesystem, processes, source tree, runtime, package environment

EXTERNAL STATE
email, social posts, tickets, orders, money-like operations, database writes

IDENTITY / AUTHORITY
user identity, service principal, tenant/user scope, delegated permissions

KNOWLEDGE INTEGRITY
retrieved evidence, memory, source provenance, policy documents

AVAILABILITY / BUDGET
wall-clock, tokens, API quota, compute, money, rate limits

AUDIT INTEGRITY
receipts, traces, approvals, external identifiers, evaluation records
```

## 3. Primary trust boundaries

### TB-01 — Untrusted input → context builder

Sources may include:

- user prompts;
- web pages;
- PDFs/documents;
- emails/messages;
- tool output;
- memory records;
- other agents' messages.

Risk: instructions embedded in data can be mistaken for authority.

### TB-02 — Model output → executable action

Model output is untrusted proposal data until validated.

High-risk promotions include:

- shell commands;
- generated Python/JavaScript;
- SQL;
- browser actions;
- API mutations;
- outbound communications.

### TB-03 — Agent runtime → external service

The runtime may cross organizational/data-governance boundaries through APIs, uploads, SMTP, browsers or MCP servers.

### TB-04 — Pause/approval → resume

Approval state must survive process/session boundaries without losing the exact action, arguments, reviewer identity and policy version.

### TB-05 — Memory write → future context

A bad or malicious memory write can become persistent future instruction/evidence poisoning.

### TB-06 — Agent ↔ agent

Another agent's message is not automatically trusted merely because it originates inside the system.

### TB-07 — Protocol discovery → authorization

Capability discovery (including MCP) says what exists, not what the current actor is allowed to execute.

## 4. Capability classes

| Capability | Typical blast radius | Default stance |
|---|---:|---|
| pure generation | low | allow within content policy |
| read-only local file/data | low-medium | scope path/data |
| external retrieval | medium | constrain origin, provenance |
| write local artifact | medium | workspace scope + review as needed |
| external file upload | high | classify data + approved destination |
| database query | medium→critical | read-only principal by default |
| external communication | high | explicit recipient/action policy |
| publication | high | draft/preview by default |
| browser automation | high | origin/action/session constraints |
| shell | critical | deny by default; isolate if required |
| generated code execution | critical | disposable sandbox only |
| financial/irreversible mutation | critical | pre-effect authorization + receipts |

A library or framework does not determine the class. The reachable action authority does.

## 5. Threat catalog

### T-01 — Prompt injection becomes action authority

**Path**

```text
untrusted document/web/tool output
  ↓
model context
  ↓
embedded instruction influences decision
  ↓
model invokes privileged tool
```

**Controls**

- separate data from policy/instructions;
- least-privilege tool exposure;
- deterministic authorization outside the model;
- sanitize/structure retrieved content where appropriate;
- require approval for consequential operations;
- evaluate with adversarial injected content.

---

### T-02 — Generated code escapes intended task

Observed pressure examples: E2E and self-healing tutorials execute model-derived code.

**Controls**

- run in disposable isolated environment;
- no host secrets;
- read-only or ephemeral filesystem;
- explicit network deny/allow list;
- CPU/memory/process/time quotas;
- promote artifacts only after external validation;
- never use successful execution as the sole safety signal.

---

### T-03 — General shell becomes universal bypass

A shell can indirectly reach files, network, processes and credentials even if each individual narrow tool would have been restricted.

**Controls**

- prefer narrow typed tools;
- deny generic shell in trusted production runtime;
- if required, isolate and constrain commands/working directory/network/credentials;
- record command + args + exit status + artifact receipt.

---

### T-04 — Database mutation through generated SQL

A system intended for analysis may emit destructive SQL.

**Controls**

- enforce read-only DB principal for analysis agents;
- separate read and write connections;
- statement allowlist/parser is defense-in-depth, not identity replacement;
- transaction limits/timeouts;
- rows/bytes/cost limits;
- audit query receipts;
- write tools require a distinct policy path.

---

### T-05 — Duplicate external side effects after retry/replay

Agents naturally retry; graph resumes can replay; timeouts can hide successful external writes.

**Controls**

- idempotency keys;
- operation identifiers;
- query-before-retry where supported;
- compensating action contract when true idempotency is impossible;
- retries owned by runtime/tool policy, not prose error strings;
- distinguish `unknown outcome` from `failed outcome`.

---

### T-06 — Human approval does not gate actual dispatcher

A UI or graph can show approval while a lower-level tool remains independently callable.

**Controls**

- dispatcher verifies authorization receipt;
- approval binds exact action + normalized args + policy version;
- edits invalidate prior validation;
- reject path cannot execute effect;
- audit reviewer identity and decision;
- tests attempt direct dispatcher bypass.

---

### T-07 — Data egress disguised as transformation

Example pressure: document conversion uploads bytes to an external service.

**Controls**

- classify content before egress;
- destination allowlist;
- explicit retention/deletion contract;
- tenant/user authorization;
- size/type limits;
- provenance of returned artifact;
- do not place unrestricted upload tools next to arbitrary local-file readers.

---

### T-08 — Browser session privilege leakage

A browser may carry cookies, SSO or authenticated state.

**Controls**

- dedicated ephemeral profile;
- no unrelated saved credentials;
- origin/domain allowlist;
- action allowlist;
- constrain downloads/uploads;
- separate read-only research browser from transactional browser;
- capture navigation/action receipts.

---

### T-09 — Memory poisoning

Bad information can persist and influence future sessions.

**Controls**

- memory-write policy separate from ordinary conversation;
- provenance and source identity;
- user/tenant/project isolation keys;
- confidence/validity timestamps;
- conflict/update semantics;
- delete/forget support;
- do not store untrusted instructions as policy;
- retrieval filters and memory evals.

---

### T-10 — Multi-agent authority amplification

Several agents can propagate one bad assumption or unauthorized plan while obscuring responsibility.

**Controls**

- per-agent capability/identity boundaries;
- explicit delegation contract;
- messages treated as claims, not authority;
- verifier independence where claimed;
- shared budget/termination policy;
- end-to-end owner of final side effect;
- baseline comparison before topology promotion.

---

### T-11 — Capability discovery confused with permission

Especially relevant to MCP/tool registries.

**Controls**

```text
discovered
  ↓
policy-filtered for actor/context
  ↓
model-visible
  ↓
selected
  ↓
argument validation
  ↓
authorization/approval
  ↓
execution
```

Never collapse these states.

---

### T-12 — Agent asserts success without external effect

**Controls**

- verify outcome using independent read/receipt;
- external IDs for writes;
- trace must distinguish proposal, attempted execution and confirmed effect;
- evaluation fails when narration conflicts with outcome.

---

### T-13 — Infinite retry / oscillation / cost exhaustion

**Controls**

- max model turns;
- max tool calls;
- per-tool retry budget;
- wall-clock deadline;
- token/cost budget;
- repeated semantic-action detection;
- cancellation;
- explicit terminal failure state.

## 6. Required tool contract for consequential capabilities

```yaml
name:
purpose:
risk_class:
input_schema:
output_schema:
actor_identity:
required_permissions:
validation:
side_effect: none | reversible | consequential
idempotency:
retryable_errors:
non_retryable_errors:
timeout:
cancellation:
approval_policy:
data_egress:
allowed_resources:
receipt_schema:
observability:
```

A tool that cannot answer these fields is not ready to be classified as a safe consequential capability.

## 7. Fail-closed invariants

1. **No authorization evidence → no consequential execution.**
2. **Unknown outcome after write timeout → do not blindly retry.**
3. **Edited arguments → revalidate and reauthorize.**
4. **Unclassified file/data → no external egress.**
5. **Generated code → no trusted-runtime execution.**
6. **Missing tenant/user isolation → no durable memory write.**
7. **Capability not policy-approved → do not expose it to the model.**
8. **No external completion receipt → completion remains unverified.**
9. **Budget exhausted → terminate, do not ask model whether to continue.**
10. **Unsupported/unknown protocol revision → fail compatibility negotiation explicitly.**

## 8. Adversarial fixtures for later MKs

- web page tells agent to reveal secrets and call a write tool;
- PDF contains fake system instructions;
- generated Python tries to read environment variables;
- browser attempts navigation outside allowed domains;
- DB agent emits `DELETE` under read-only credentials;
- external POST succeeds but client times out before response;
- resumed graph attempts the same write twice;
- reviewer edits recipient or amount after approval request;
- low-level sender invoked directly without approval receipt;
- memory record from tenant A appears in tenant B retrieval;
- another agent claims a task is complete without receipt;
- model semantically repeats a failed action with syntactically changed args;
- MCP server exposes a new tool not present in policy;
- tool result contains instruction-like text that attempts privilege escalation.

## 9. Risk is compositional

A system may combine individually moderate capabilities into a critical path:

```text
read arbitrary file
 +
external HTTP upload
 =
data-exfiltration capability
```

```text
browser authenticated session
 +
model-directed click/type
 =
transactional authority
```

```text
memory write
 +
cross-session retrieval
 =
persistent influence channel
```

MK1 must therefore classify both individual capabilities and **capability composition**.

## 10. MK0 disposition

This threat model is sufficient for MK0 framing because it:

- derives from observed P0 blast-radius families;
- preserves UNKNOWNs;
- produces framework-independent trust boundaries;
- defines adversarial questions for every candidate invariant family;
- gives MK1 concrete dimensions to normalize.

It is not a substitute for project-specific threat modeling, penetration testing or runtime certification.