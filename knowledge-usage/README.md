# Knowledge Usage

`knowledge-usage/` es la capa mínima de observación para comprobar si `personal_knowledge` realmente compone.

No es un dominio de conocimiento. No tiene MK propio, arquitectura propia ni un pipeline nuevo.

## Pregunta que responde

> **¿El conocimiento que acumulamos vuelve a ser usado y reduce trabajo futuro?**

La métrica importante no es cuántos Markdown existen. Es si ocurre repetidamente:

```text
problem / project
      ↓
existing knowledge found
      ↓
decision / research / pattern reused
      ↓
less reconstruction or rework
      ↓
new evidence returns to personal_knowledge
```

## Qué es un Knowledge Usage Receipt

Un receipt registra un caso material de consumo. Puede ser positivo o negativo.

Ejemplos válidos:

- una decisión anterior evitó volver a debatir una arquitectura;
- una source map evitó rehacer investigación;
- un patrón existente aceleró un proyecto;
- conocimiento existente estaba stale y causó fricción;
- un artefacto no aportó suficiente valor;
- un proyecto reveló que una abstracción merece simplificarse o eliminarse.

## Cuándo crear uno

Crear receipt solo cuando ocurra al menos una de estas condiciones:

1. conocimiento previo cambió materialmente una decisión u output;
2. evitó una reconstrucción/reinvestigación perceptible;
3. una pieza stale/incompleta generó trabajo adicional;
4. el consumo produjo nuevo conocimiento que regresó al repo;
5. descubrimos que mantener un artefacto cuesta más que volver a derivarlo.

No crear receipt por cada lectura, búsqueda o consulta trivial.

## Estructura

```text
knowledge-usage/
├── README.md
├── LEDGER.md
├── TEMPLATE.md
└── YYYY/
    └── KU-NNN-<slug>.md
```

`LEDGER.md` es el índice humano. Los receipts contienen evidencia cualitativa y, solo cuando exista, cuantitativa.

## Estados de resultado

- `HELPED` — reutilización claramente útil.
- `PARTIAL` — ayudó, pero también hubo reconstrucción/gaps.
- `STALE` — conocimiento previo estaba desactualizado y requirió reparación.
- `NO_VALUE` — no justificó su mantenimiento/uso en este caso.
- `INCONCLUSIVE` — no hay evidencia suficiente para decidir.

Un estado negativo es evidencia útil.

## Regla de medición

Nunca inventar ahorro. Si no se midió, usar `UNKNOWN`.

Preferir:

```yaml
time_saved: UNKNOWN
research_avoided: "no se volvió a diseñar el provenance vocabulary"
```

antes que inventar una cifra de horas.

## Qué podremos observar con suficientes receipts

Sin crear todavía dashboards ni scores, el ledger podrá revelar:

- qué knowledge domains son realmente consumidos;
- qué artefactos se reutilizan repetidamente;
- qué conocimiento se vuelve stale con frecuencia;
- dónde seguimos reconstruyendo decisiones;
- qué piezas merecen automatización;
- qué piezas deberían simplificarse, fusionarse, archivarse o eliminarse;
- qué conocimiento tiene evidencia suficiente para convertirse en reusable capital, playbook, workflow o producto educativo.

## Experimento de recuperación selectiva y coste de contexto

El [piloto Context Retrieval v0](./experiments/context-retrieval-v0/README.md) compara cuatro tareas reales utilizando rutas amplias y rutas mínimas de documentación, con fuentes fijadas por SHA y un verificador offline. El [recibo estático](./experiments/context-retrieval-v0/static-receipt-2026-10-08.json) mide **reducción de bytes de entrada** (no tokens facturados). Las rutas fueron seleccionadas manualmente; la calidad de respuestas, el coste de routing, los tokens reales y el ahorro temporal siguen `UNKNOWN` / `NOT_EVALUATED`.

Este piloto no añade automatización continua, vector DB, servicios de inferencia ni un MK nuevo. Solo habilita una medición localizada y reversible; cualquier optimización general requiere gates de calidad y evidencia adicional.

## No automation yet

No se crea schema, CI, database, graph runtime ni dashboard para esta capa en su primera versión.

Automation se justifica solo cuando receipts reales demuestren un patrón repetido que la disciplina manual ya no maneja bien.

## Relación con otras capas

```text
knowledge domains
      ↓
knowledge consumed by real work
      ↓
knowledge-usage receipt
      ↓
evidence of reuse / friction / staleness
      ↓
KEEP / EXPAND / SIMPLIFY / AUTOMATE / MERGE / ARCHIVE / KILL / PRODUCTIZE
```

Un receipt **no promueve canon**, no cierra un MK y no prueba por sí solo causalidad.

Es evidencia operacional de consumo.
