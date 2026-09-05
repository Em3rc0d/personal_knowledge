# OpenShip — Architecture Synthesis

`GENERATED from OBSERVED evidence; not yet certified as a universal reference architecture.`

## Layer model

```text
┌─────────────────────────────────────────────┐
│ Operator surfaces                           │
│ Desktop · Web · CLI · REST · MCP            │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│ API / Control Plane                         │
│ auth · org scope · orchestration · state    │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│ Pure/shared domain rules                    │
│ core · resolved specs · policies            │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│ Infrastructure adapters                     │
│ runtime · routing · SSL · system · executor │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│ Execution transports                        │
│ Docker · local shell · SSH · cloud API      │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│ Managed workloads/infrastructure            │
└─────────────────────────────────────────────┘
```

## Central architectural seams

1. `Platform` factory — target composition.
2. `RuntimeAdapter` — workload lifecycle.
3. shared deploy pipeline — sequencing/recovery.
4. `CommandExecutor` / SSH manager — host mutation transport.
5. routing/SSL provider — edge state.
6. database/job-runner choice — control-plane durability/concurrency.
7. secure API route metadata — permission boundary.
8. MCP tool projection — agent surface.

## State boundaries to track

```text
source state
resolved build configuration
build artifact
runtime deployment state
route state
certificate state
persistent data/volumes
auth/secret state
control-plane job state
```

MK1 must identify which component is source-of-truth for each and where duplicate representations exist.

## High-level risk graph

```text
control-plane compromise
      ↓
privileged executor / Docker authority
      ↓
host compromise
      ↓
workload + data compromise
```

The architecture therefore demands stronger security review than a normal CRUD application.
