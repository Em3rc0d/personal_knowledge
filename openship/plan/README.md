# OpenShip — Knowledge Plan

## MK0 remaining work

1. Inventory all critical files by subsystem and owner contract.
2. Map data models for projects, deployments, domains, servers, jobs, auth and secrets.
3. Trace one complete deployment from API request to runtime mutation and route switch.
4. Trace one rollback and one cancellation path.
5. Trace one remote-server deployment including SSH acquisition/recovery.
6. Trace one MCP tool from route metadata to final authorized action.
7. Build a documentation-drift matrix: README/docs vs current code.
8. Build a failure taxonomy from representative issues.
9. Complete threat model for Docker socket, root SSH, edge takeover and secret flows.
10. Review MK0 for provenance mixing.

## MK1 target

Normalize the mined material into explicit contracts:

```text
ControlPlaneContract
RuntimeContract
DeploymentTransactionContract
ResolvedSpecContract
EdgeContract
ExecutorContract
SecretRepresentationContract
AgentToolContract
ReleaseCertificationContract
```

No contract moves to MK2 until its applicability boundaries and counterexamples are documented.
