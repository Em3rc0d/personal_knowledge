# OpenShip — Status

Updated: 2026-09-05

## Current gate

```text
DOMAIN                    openship
CURRENT MK                MK0
STATE                     IN PROGRESS
UPSTREAM SNAPSHOT         v0.7.0 / 6510d3fd...
CONTROL-PLANE MAP         INITIAL PASS COMPLETE
DEPLOYMENT PIPELINE       INITIAL PASS COMPLETE
SECURITY BOUNDARIES       INITIAL PASS COMPLETE
MCP MODEL                 INITIAL PASS COMPLETE
OPERATIONS MODEL          INITIAL PASS COMPLETE
REUSABLE RULES            NOT YET CERTIFIED
AUTOMATED TESTING         NOT YET STARTED
```

## MK progression

| MK | Objective | State |
|---|---|---|
| MK0 | Mine source, architecture, runtime, deployment, security, MCP, CI and known failure modes | IN PROGRESS |
| MK1 | Normalize patterns, contracts, boundaries and contradictions | BLOCKED BY MK0 |
| MK2 | Convert findings into reusable architecture/deployment/security rules | BLOCKED |
| MK3 | Produce portable platform/control-plane architecture templates | BLOCKED |
| MK4 | Formalize safe agent-driven infrastructure operations | BLOCKED |
| MK5 | Build automated checks and certification harnesses | BLOCKED |
| MK6+ | Validate patterns against additional platforms and real systems | BLOCKED |

## MK0 closure gate

- [x] domain contract exists;
- [x] primary upstream/source registry exists;
- [x] upstream snapshot is pinned;
- [x] initial monorepo/control-plane map exists;
- [x] runtime abstraction is mapped;
- [x] deployment sequencing and rollback model are mapped;
- [x] SSH/remote execution role is mapped;
- [x] edge/routing/TLS boundary is mapped;
- [x] MCP/agent interface is mapped;
- [x] security trust-boundary guide is captured;
- [x] CI/release-gate evolution is captured;
- [x] representative recent failure modes are logged;
- [ ] all critical source files are catalogued by responsibility;
- [ ] every major subsystem has explicit input/output/failure contracts;
- [ ] current documentation drift is exhaustively mapped;
- [ ] high-blast-radius operations have a complete threat model;
- [ ] platform claims are cross-checked against current implementation and tests;
- [ ] MK0 review finds no unlabelled observation-vs-inference mixing.

Until these close, **MK1 remains blocked**.
