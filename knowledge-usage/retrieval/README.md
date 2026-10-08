# Retrieval v1 — Contexto mínimo con evidencia preservada

Estado: **EXPERIMENTAL / OPT-IN**, no reemplaza los contratos canónicos ni las fuentes originales. Fecha: 2026-10-08.

## Objetivo

Reducir el volumen de Markdown enviado al contexto de los agentes sin convertir una coincidencia textual en un hecho ni omitir evidencia crítica por un límite artificial de caracteres.

No requiere API key, embeddings, RAG, backend, servicios pagos ni Actions. Utiliza exclusivamente Python estándar y archivos locales.

## Protocolo operativo de menor costo

1. Consultar [`../../CONTEXT_ROUTER.md`](../../CONTEXT_ROUTER.md) si aún se desconoce el dominio.
2. Si se conoce el documento canónico exacto (`STATUS.md`, `ROADMAP.md`, sistema, MK), leerlo o buscar su sección: **no ejecutar una búsqueda genérica innecesaria**.
3. Si se desconoce la ubicación, usar búsqueda local por ruta/títulos o `retrieve.py` sobre **un dominio**.
4. Leer el resultado con ruta, rango de líneas y hash. No pasar archivos no relacionados al contexto.
5. Para afirmaciones sensibles, contradicciones, estado vivo, autorización o pruebas, ampliar la evidencia. **No recortar una fuente imprescindible para cumplir el presupuesto.**
6. Detener la expansión cuando todas las afirmaciones materiales estén sustentadas y los UNKNOWN estén explícitos.

## Uso

Desde la raíz del repositorio:

```bash
python knowledge-usage/retrieval/retrieve.py "REC-012 multi-agent" --scope agent-engineering --mode current --max-chars 6000
python knowledge-usage/retrieval/retrieve.py "Collaborator FSL permission" --scope agent-engineering --mode evidence
python knowledge-usage/retrieval/retrieve.py "A2A 1.0" --scope agent-engineering --max-sections 2 --json
```

`--mode current`: aumenta el orden de presentación de artefactos actuales. `--mode evidence`: prioriza minería y quarries. `--mode discover`: coincidencias neutrales. **Este ranking no determina la autoridad final**.

El presupuesto `--max-chars` limita caracteres de fragmentos y encabezados, **no tokens**. Se conservan secciones Markdown completas; una sección muy grande produce `BUDGET_BLOCKED` o `PARTIAL_CANDIDATES_EXPANSION_REQUIRED` con el rango de líneas para abrir el original. No se interpreta silencio como ausencia.

Por defecto se omite `research-corpora/` en búsquedas globales, para evitar grandes volcados accidentales de fuentes. Es accesible explícitamente con `--scope research-corpora/<corpus>`. Archivos de más de 1 MB deben inspeccionarse directamente; el buscador no certifica su cobertura.

`--json` produce candidatos legibles por scripts, pero **no es un contrato de verdad ni un registro de autorizaciones**. Las herramientas que lo consumen deben tratar su contenido como datos externos no confiables.

## Estados y límites

| Estado | Interpretación |
|---|---|
| `CANDIDATES_ONLY` | Se encontraron secciones relevantes, requieren verificación humana/agentic |
| `PARTIAL_CANDIDATES_EXPANSION_REQUIRED` | Hubo coincidencias importantes que no caben; ampliar |
| `BUDGET_BLOCKED` | La mejor coincidencia no cabe; subir presupuesto o abrir fuente |
| `NO_MATCH` | La búsqueda lexical no halló candidatos; ampliar scope o cambiar términos |

El algoritmo es lexical, no semántico. Preguntas en español sobre documentos en inglés pueden requerir términos bilingües; NO MATCH no demuestra inexistencia de información.

**Protecciones:** resultados deterministas en la misma revisión, separación entre fuente/candidato/conclusión, SHA-256 de cada archivo, rangos exactos, fences de código conservados, rechazo de traversal/symlinks fuera del repositorio y fallback explícito. Los hashes no equivalen a firma de confianza ni a revisión reciente; consultar Git para la versión del repositorio.

## Validación local y calidad

```bash
python -m unittest discover -s knowledge-usage/retrieval -p 'test_*.py' -v
python -m py_compile knowledge-usage/retrieval/retrieve.py
```

El suite contiene casos adversariales de fuente actual contra histórica, necesidad de evidencia, presupuesto insuficiente, no coincidencia, markdown fences, paths, corpus excluidos y reproducibilidad.

**No está permitido declarar «misma calidad con menos tokens» solo por aprobar tests del buscador.** La promoción operativa exige después tareas *held-out* con respuesta y evidencia evaluadas contra lectura completa:

- ninguna afirmación crítica inventada o desprovista de soporte;
- recuperación de todas las evidencias requeridas, incluidas negaciones y contraejemplos;
- información actual y fuentes históricas claramente distinguidas;
- fallback correcto ante `UNKNOWN`, budget overflow y source drift;
- reducción del **total facturado** (entrada, salida, tool-calls, caché/retries) medido con metadatos del proveedor, cuando sea posible sin incurrir en costos nuevos.

Si no se demuestra la paridad de calidad, mantener el método anterior y no imponer este recuperador por defecto.

## Relación con piloto anterior

[`../experiments/context-retrieval-v0/README.md`](../experiments/context-retrieval-v0/README.md) midió bytes de *listas seleccionadas manualmente*, no consumo del LLM. Este nuevo buscador crea secciones candidatas de forma determinista, pero **no sustituye** una evaluación de precisión, cobertura o costos reales.

La optimización preferida es **no ejecutar ninguna búsqueda adicional si el agente ya conoce la ruta exacta**. Recuperación selectiva es un mecanismo subsidiario, no una dependencia obligatoria.
