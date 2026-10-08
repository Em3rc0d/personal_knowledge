# Q-001 — Auditoría de catálogo Opus 5.5

Status: **QUARRY_ONLY**, not domain canon.
Source: `SRC-PV-001` — https://github.com/Em3rc0d/awesome-opus5-5-videos/tree/756290289742535eb0ac3817548f152e9759cc70
Dataset: `data/videos.json` at pinned commit.
Observed: 2026-10-07 America/Lima (latest commit recorded as 2026-10-08 UTC).

## Método

Se inspeccionó el JSON completo y se calculó una auditoría descriptiva de registros y prompts. La normalización de deduplicación fue básica: pasar a minúsculas, colapsar espacios y eliminar puntuación final `.` y `!`. Esto **no** equivale a deduplicación semántica. No se ejecutó el contenido ni se autenticó el historial de publicaciones X.

## Evidencia estructural OBSERVED

| Métrica | Resultado |
|---|---:|
| Registros | 513 |
| Autores textualmente distintos (`author`) | 476 |
| `prompt_partial: true` | 234 |
| `prompt_partial: false` | 279 |
| Prompts vacíos | 0 |
| Prompt texts distintos tras normalización ligera | 454 |
| Registros de más por repetición textual | 59 |
| Grupos textuales con multiplicidad >1 | 12 |
| Máximo tamaño de un grupo idéntico | 41 |

**Interpretación:** 45.6% está expresamente marcado como parcial; `false` solo significa "no marcado parcial por el catálogo", no "verificado completo". El mismo prompt genérico de showreel aparece en 41 registros y no prueba igualdad de ejecución.

## Categorías OBSERVED

| Categoría en JSON | Registros |
|---|---:|
| `motion` | 317 |
| `interactive` | 70 |
| `explainer` | 67 |
| `3d` | 59 |

Estas categorías suman 513; no representan una evaluación independiente del contenido.

## Tecnologías etiquetadas OBSERVED

Top tags en `tech_tags`: `canvas=351`, `svg=219`, `threejs=147`, `shader=104`, `gsap=100`, `css=68`, `audio=36`, `particles=26`, `playable=22`, `pixel=16`. Tags son multivalor y reflejan la etiqueta del catálogo sobre las recreaciones, **no un inventario auditado del software del autor original**.

## Formato de cada registro

Campos observados: `slug`, `author`, `author_url`, `post_url`, `category`, `tech_tags`, `prompt`, `prompt_partial`, `poster_url`, `skillry_url`, `added`.

El README muestra 100 ejemplos destacados y enlaces a un comparador Skillry. `added` presenta lotes de `2026-09-26`, `2026-09-28`, `2026-09-29`, `2026-10-08` (fecha UTC del lote). Son fechas del dataset, no evidencia de creación real de cada obra.

## Tres registros examinados individualmente

1. `prompts/himanshutwtxs-882858.md`: instrucción de showreel breve y genérica; insuficiente para reconstruir de forma independiente estilo, render, control temporal y assets.
2. `prompts/anabology-491441.md`: instrucción extensa dependiente de un MP4 original, audio, workspace `/asic`, tooling de imagen/video, ElevenLabs y API keys del creador; transferibilidad sin contexto **no demostrada**.
3. `prompts/0xchuckstock-879327.md`: consigna de juego multijugador de naves. No describe por sí sola el código, infraestructura, assets o criterios de validación.

Enlaces directos: [ejemplo showreel](https://github.com/Em3rc0d/awesome-opus5-5-videos/blob/756290289742535eb0ac3817548f152e9759cc70/prompts/himanshutwtxs-882858.md), [ejemplo con dependencias](https://github.com/Em3rc0d/awesome-opus5-5-videos/blob/756290289742535eb0ac3817548f152e9759cc70/prompts/anabology-491441.md), [juego](https://github.com/Em3rc0d/awesome-opus5-5-videos/blob/756290289742535eb0ac3817548f152e9759cc70/prompts/0xchuckstock-879327.md).

## Inferencias y riesgo de sesgo (INFERRED)

- La colección permite detectar técnicas candidatas pero no medir una tasa de éxito de Opus 5.5 sin muestras fallidas y condiciones de generación.
- La selección "viral" favorece demos llamativas; una colección curada no establece calidad promedio.
- Duplicar exactamente un prompt no garantiza duplicar video: faltan variables de entorno, versiones y decisiones iterativas del agente.
- No se evaluó calidad en móvil, uso de CPU/GPU, derechos o iteraciones por intento.

## Reglas de extracción candidatas (GENERATED / NO PROMOVIDAS)

1. Preferir pruebas con brief y assets propios para reducir confusión de licencias.
2. Definir la animación por tiempo absoluto o frame (seekability) cuando se requiera salida frame-by-frame repetible.
3. Separar `prompt → escena ejecutable → encoder → artefacto → verificación`.
4. Exigir fuente exacta y estado de completitud antes de atribuir resultado a un prompt.
5. Diseñar benchmark de calidad con casos negativos, no sólo videos virales.

## Evidencia faltante

- Confirmación de 12+ ejemplos distribuidos por categorías, completos/parciales y dependencia externa, comparados con el post original.
- Evidencia de generación exacta, número de iteraciones, gastos, versiones y reproducibilidad.
- Verificación de derechos por obra individual.

No se recomienda copiar al repositorio los archivos multimedia alojados por terceros.
