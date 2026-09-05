# OpenShip — Brainstorming

This folder holds hypotheses and design questions that are **not canonical architecture decisions**.

## Current questions

1. Can the OpenShip adapter model be generalized into a portable control-plane reference architecture?
2. Can root SSH / Docker-socket authority be replaced by a restricted host agent with capability-based RPC?
3. What should the canonical `ResolvedDeploymentSpec` contain so build, runtime, rollback and edge all consume the same immutable representation?
4. Can routing/TLS/workload readiness be modeled as independent but composable state machines?
5. How should agent tools expose destructive operations: approval, dry-run, plan receipt, capability token, or multi-stage commit?
6. What failure taxonomy prevents transport, configuration, infrastructure and workload errors from being conflated?
7. Which parts of the local→team→distributed complexity ladder are reusable in our own systems?
8. Can documentation drift be prevented by deriving architecture tables from executable registries/contracts?

All answers remain `INFERRED/INSPIRED` until promoted through design/architecture and tests.
