# Quarry — MCP / Agent Interface

## Observed model

`OBSERVED / confidence: high`

OpenShip exposes MCP as an additional operator interface over the existing API/control-plane, not as a separate infrastructure execution stack.

Conceptually:

```text
AI agent / MCP client
        ↓
MCP tool registry
        ↓
principal/tool filtering
        ↓
dispatch through API operation
        ↓
authorization + org/target checks
        ↓
control-plane adapters
        ↓
infrastructure
```

Routes opt in through MCP metadata. Tool visibility is filtered for the principal, and dispatch still relies on backend authorization rather than treating tool discovery as permission.

Tests cover cases where local-only capabilities must not be exposed in environments where those operations do not exist.

## Why this matters

`INFERRED`

The agent is constrained to the same domain operations and permission system as human/API clients. This is safer and more maintainable than handing an agent generic Docker/SSH/root tools and attempting to control behavior only through prompting.

## Reusable candidate pattern

`INSPIRED`

**Policy-backed tool projection**:

1. Define safe domain operation in API.
2. Attach explicit permission/capability metadata.
3. Project only selected operations into agent tools.
4. Filter tools for principal/environment.
5. Re-authorize every invocation server-side.
6. Audit the call independently of the model's narrative.

## Anti-pattern

```text
agent
  ↓
raw shell / docker socket / unrestricted SSH
```

Prompt instructions are not a security boundary.
