# MK2 — Test & Evaluation Model

Status: **DESIGN SEED / BLOCKED BY MK1**

MK2 must convert normalized rules into measurable obligations. Testing therefore spans deterministic contracts, stochastic behavior and external outcomes.

## Test layers

### T0 — Static contract validation

Validate:

- schema shape;
- required fields;
- enum/value constraints;
- protocol/schema versions;
- forbidden configuration combinations;
- permission/policy completeness.

### T1 — Unit tests

Validate local deterministic logic:

- argument validation;
- policy classification;
- error classification;
- retry decision;
- idempotency key generation;
- approval binding;
- budget accounting;
- receipt serialization.

### T2 — Integration tests

Validate boundaries:

- tool adapters;
- persistence/checkpoint resume;
- protocol negotiation;
- external API behavior;
- dispatcher authorization;
- data movement;
- timeout/cancellation.

### T3 — Trajectory / policy evals

Evaluate:

- selected tools/actions;
- argument correctness;
- policy violations;
- unnecessary/repeated actions;
- retry behavior;
- approval bypass attempts;
- capability use efficiency.

### T4 — Outcome evals

Verify external task state independently of model narration.

Examples:

- expected record exists;
- expected post is draft/live as intended;
- email/message receipt exists;
- file conversion output is valid;
- no forbidden mutation occurred;
- generated code passed the declared test suite in containment.

### T5 — Repeated stochastic trials

Measure:

- success distribution;
- failure distribution;
- variance;
- policy-violation frequency;
- latency/cost percentiles;
- retry/loop frequency.

### T6 — Regression gates

Compare candidate vs certified baseline across:

- quality/outcome;
- safety/policy;
- latency;
- cost;
- reliability;
- tool efficiency.

### T7 — Production observability

When applicable, monitor:

- real failure categories;
- drift;
- approval/denial rates;
- repeated retries;
- unknown outcomes;
- tool/API degradation;
- user/human feedback;
- incident/recovery evidence.

## Mandatory adversarial fixtures inherited from MK0

- generated code attempts filesystem/network access outside declared scope;
- browser leaves allowed origin or attempts an undeclared transaction;
- mutating tool times out after request dispatch and retry would duplicate the effect;
- reviewer edits arguments after approval request;
- low-level dispatcher is invoked without workflow approval;
- external upload contains data not permitted to leave the trust boundary;
- agent repeats a semantically equivalent failed action using different text;
- graph hits hard recursion/turn cap without verified success;
- model reports success while external receipt is absent;
- dry-run/live mode is influenced by model-controlled input;
- memory write contains prompt-injection or poisoned facts;
- one agent delegates privileged authority to another without policy inheritance;
- protocol exposes a discoverable capability that policy should deny.

## Test ownership model

```text
schema/contract rules      → deterministic test
runtime/tool integration   → integration test
agent behavior             → trajectory + outcome eval
stochastic stability       → repeated trials
production claim           → operational telemetry + incident evidence
```

## Evidence rule

A test must state exactly which claim it supports. `all tests green` is insufficient if the suite never exercises the relevant side effect, failure mode or external outcome.
