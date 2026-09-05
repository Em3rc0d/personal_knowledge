# OpenShip — Design Extraction

No reusable design rule is certified yet. Current candidate principles are extracted from observed behavior and must pass MK1/MK2 normalization.

## Candidate principles

### One system, many operator surfaces

`INSPIRED`

Desktop, dashboard, CLI and agents should manipulate the same domain model instead of implementing separate behavior stacks.

### Progressive operational complexity

`INSPIRED`

Use the simplest state/execution substrate compatible with the operational contract, then require shared infrastructure only when concurrency/team/multi-replica semantics demand it.

### Healthy workload ≠ healthy public endpoint

`INSPIRED`

Expose these states independently so the user can distinguish application failure from DNS/TLS/routing remediation.

### User decisions as typed events

The deploy pipeline contains structured prompt payloads for conflicts such as edge takeover/port decisions. Candidate generalized pattern: infrastructure workflows should pause on explicit, machine-readable decisions rather than free-form interactive shell prompts.

### Agent UX mirrors human capabilities, not raw infrastructure

Project safe domain operations into agent tools and preserve backend authorization.
