# Test & Proof

TEST demuestra afirmaciones; PROVE define qué claims quedan realmente soportados.

## Evidence ladder

```text
inspection
  ↓
static validation
  ↓
unit evidence
  ↓
integration evidence
  ↓
end-to-end evidence
  ↓
real external dependency
  ↓
physical / field evidence
```

No siempre se necesita toda la escalera. La fuerza requerida depende del claim, riesgo y consecuencia.

## Required test thinking

Cuando corresponda, incluir:

- positive cases;
- negative cases;
- edge cases;
- counterexamples;
- fail-closed behavior;
- regression evidence;
- reproducible fixtures;
- resilience testing;
- performance proof solo si performance forma parte del claim.

## Proof model

```text
Claim
  ↓
Evidence
  ↓
Source
  ↓
Provenance
  ↓
Verification
```

Estados permitidos/recomendados:

```text
PASS
PASS WITH LIMITATIONS
FAIL
UNKNOWN
BLOCKED
INCONCLUSIVE
```

## Review rule

`looks good`, `probably works`, `CI is green` o `agent says DONE` nunca sustituyen el análisis del boundary real que el claim pretende cerrar.
