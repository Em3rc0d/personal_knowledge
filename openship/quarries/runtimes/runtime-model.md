# Quarry — Runtime Model

## Observed implementations

`OBSERVED`

### DockerRuntime

- self-hosted Docker execution;
- Docker daemon may be reached through local socket, SSH/tunnel or TLS depending on configuration;
- container lifecycle and image/build operations;
- can support overlapping releases when resource allocation allows it.

### BareRuntime

- supervised host processes rather than containers;
- uses command execution locally or over SSH;
- fixed host ports often force non-overlap deployment semantics;
- systemd/nohup-style supervision exists in adapters.

### CloudRuntime

- delegates workload operations to cloud API/provider;
- avoids local shell execution in the cloud control-plane mode by default;
- host build capability is explicitly deny-by-default unless opted in.

## Important distinction

`INFERRED / confidence: high`

The system does not equate "deployment target" with "runtime implementation". Target answers *where/how the control plane is operating*; runtime answers *how the workload is executed*.

## Resource semantics

The shared types define explicit production and build resource contracts. OpenShip differentiates cloud defaults from self-hosted defaults to avoid accidentally applying constrained cloud tiers to operator-owned hardware.

## Reusable candidate rule

`INSPIRED`

> Resource defaults are part of target semantics and must not be globally reused across fundamentally different ownership/cost models.

## Portability insight

Standard containers improve workload portability, but operational portability still depends on edge, secrets, persistent volumes, databases, DNS and control-plane state. "Docker portable" is not equivalent to "platform portable".
