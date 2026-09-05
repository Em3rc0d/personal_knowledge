# Quarry — SSH, State and Job Execution

## SSH as a control-plane transport

`OBSERVED / confidence: high`

SSH is a first-class transport, not scattered `ssh` subprocess calls. The API has an `sshManager` responsible for pooled/managed connections, reachability and shared execution behavior.

Remote operations include system checks, package/component setup, edge operations, git workflows, deployment tasks and tunnels.

## Git credential strategies

Observed strategies include:

- ephemeral token;
- remote credential helper;
- SSH key + pinned `known_hosts`;
- ambient credentials already owned by the build host;
- desktop credential relay for private clone flows;
- clone-on-server to avoid orchestrator download/re-upload of large sources.

## Embedded vs shared state

`OBSERVED`

Local/bare modes can use **PGlite** as embedded PostgreSQL-like state. The code contains explicit single-instance locking/recovery handling because PGlite does not provide ordinary cross-process locking semantics.

Always-on/team/cloud modes can use PostgreSQL and Redis.

## Job execution

The API can choose an in-process runner where appropriate and BullMQ/Redis where shared queue semantics are required. In modes that require Redis, it does not silently degrade to a process-local queue.

## Reusable candidate patterns

`INSPIRED`

```text
simple/local       → embedded state + process-local execution
always-on/team     → shared relational state + shared queue
multi-replica      → shared state + mandatory distributed queue
```

This is a complexity ladder, not a universal prescription.

## Failure-boundary lesson

Transport errors must remain transport errors. Misclassifying an SSH/channel failure as "component missing" can trigger incorrect remediation. Error taxonomies must preserve layer ownership.
