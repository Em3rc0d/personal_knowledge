# OpenShip — Knowledge Tests

This folder validates **our extracted knowledge**, not the upstream OpenShip implementation itself.

## MK0 review checks

- [ ] Every major factual claim points to an upstream source/artifact.
- [ ] `OBSERVED` and `INFERRED` statements are distinguishable.
- [ ] Version-sensitive behavior names the studied snapshot.
- [ ] No stale Traefik documentation is presented as current runtime truth.
- [ ] No issue report is generalized as a permanent current-version fact without verification.
- [ ] Security claims distinguish design intent from demonstrated enforcement.
- [ ] Reusable patterns state applicability boundaries and failure modes.
- [ ] No large source-code passages are copied unnecessarily.
- [ ] Architecture synthesis identifies state/trust boundaries.
- [ ] MK status does not overclaim certification.

## Future test families

```text
architecture consistency
failure taxonomy
state ownership
secret representation
rollback invariants
agent authorization
privileged-operation gating
documentation drift
release-gate reachability
```
