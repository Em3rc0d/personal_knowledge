# KU-NNN — <short title>

Date: YYYY-MM-DD  
Consumer: <project / decision / product / task>  
Outcome: `HELPED | PARTIAL | STALE | NO_VALUE | INCONCLUSIVE`  
Confidence: `high | medium | low`

## Problem

¿Qué trabajo real estábamos intentando resolver?

## Knowledge used

| Knowledge | Revision / observation boundary | Reuse type |
|---|---|---|
| `path/to/artifact` | commit / date / UNKNOWN | decision / evidence / method / pattern / architecture / template / source-map |

## What was reused

¿Qué decisión, regla, evidencia, patrón o contexto no tuvo que ser reconstruido desde cero?

## Work avoided

Registrar solo lo observable.

```yaml
rediscovery_avoided:
decision_reconstruction_avoided:
research_avoided:
rework_avoided:
time_saved: UNKNOWN
```

Si algo no se midió, usar `UNKNOWN`.

## Friction / stale knowledge

¿Qué estaba incompleto, ambiguo, incorrecto o stale?

Si nada material apareció:

`NONE OBSERVED`

## Knowledge returned

¿Qué evidencia, regla, contradicción o mejora nueva regresó a `personal_knowledge` como resultado de este consumo?

## Evidence

Pointers verificables:

- branch / PR / commit;
- project artifact;
- issue;
- test;
- decision receipt;
- source/evidence path.

## Interpretation

¿Qué soporta realmente este receipt?

¿Qué **no** soporta?

## Disposition

Una o más:

- `KEEP`
- `EXPAND`
- `SIMPLIFY`
- `AUTOMATE_CANDIDATE`
- `MERGE_CANDIDATE`
- `ARCHIVE_CANDIDATE`
- `KILL_CANDIDATE`
- `PRODUCTIZE_CANDIDATE`
- `NO_CHANGE`

Disposition es una señal, no una decisión automática de promoción.
