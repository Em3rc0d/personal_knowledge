# RICOUI Quarry — Artifact Pipeline

## Officially observed/documented RICOUI model

```text
website or DESIGN.md input
        ↓
DESIGN.md source
        ↓
source / reading / structured / preview views
        ↓
generated outputs
        ├── DTCG tokens.json
        ├── CSS variables
        ├── Tailwind theme.css
        └── ZIP / delivery artifacts
```

RICOUI documentation states that generated files are not separate sources of truth.

## AI modification boundary

RICOUI documents a useful safety property:

```text
AI proposal
   ↓
complete diff
   ↓
human review
   ↓
explicit apply
```

The AI does not silently overwrite canonical source.

### Extracted principle

**Classification:** `INSPIRED`

Generated design changes should be reviewable against the canonical semantic source. Automation may propose or regenerate derived artifacts, but source-changing operations should have clear ownership and auditability.

## Our expanded pipeline

RICOUI's artifact flow is a seed, not our final model. `web-design` expands it to:

```text
requirements
  ↓
UX constraints
  ↓
visual evidence
  ↓
semantic design contract
  ↓
normalized tokens + component contracts
  ↓
responsive / a11y / motion rules
  ↓
frontend implementation
  ↓
visual + behavioral validation
  ↓
versioned design release
```

This expanded pipeline is `GENERATED / INSPIRED`, not an official RICOUI architecture claim.
