# MK0 Closure — Programmatic Video

Date: **2026-10-07 America/Lima**.
Gate outcome: **PASS WITH LIMITATIONS**, exclusivamente para el alcance *Mine & Frame / source-discovery*. Esta acta no valida el catálogo como benchmark, no aprueba ejecución, no elige renderer final y no declara «Video Factory» lista.

## Problema y scope cerrado

Pregunta MK0: ¿podemos crear un mapa de investigación trazable y falsable de producción audiovisual basada en código, sin confundir galerías virales con ingeniería probada?

**Sí, para el alcance restringido a descubrimiento de técnicas y contratos de evaluación**. La prueba de producción real queda explícitamente fuera de MK0.

## Evidencia de revisión

| Claim / gate | Evidencia | Resultado |
|---|---|---|
| Scope y ownership definidos | `README.md` | PASS |
| Fuente seed identificada por commit | `mining-site/SOURCES.md`, `SRC-PV-001`, SHA `756290289742535eb0ac3817548f152e9759cc70` | PASS |
| Auditoría estructural del catálogo | `quarries/Q-001-opus55-catalog-audit.md`: 513 entradas, 234 marcadas parciales, 454 textos distintos tras dedupe ligera | PASS / DATASET ONLY |
| Autenticidad de posts y atribución a modelo | `quarries/Q-003-original-post-access-audit.md`: 8 originales intentados, 0 inspeccionados por bloqueo X | **NOT VERIFIED / EXCLUDED FROM CANON** |
| Independencia de fuente comercial | Skillry sólo corroboró parcialmente *su propio* catálogo; no se usa como validación independiente de un post | PASS / LIMITATION PRESERVED |
| Fuentes de render y diferenciación de licencia | `SRC-PV-002..005` + Q-002: docs HyperFrames, Remotion, MDN, FFmpeg | PASS / DOCUMENTATION ONLY |
| Necesidad de timeline consultable por frame | HyperFrames README (tracks/seek), Remotion fundamentals/flickering (useCurrentFrame), sin pruebas runtime | PASS / CONCEPT, RUNTIME UNKNOWN |
| Seguridad, derechos y coste | `quarries/Q-004-security-rights-threat-model.md`; pruebas proponen assets sintéticos originales, sin música | PASS / PLAN ONLY |
| 3 experimentos diseñados y falsables | `mk/MK0/EXPERIMENT-CONTRACT.md` | PASS / NOT EXECUTED |
| Sin mezclar `source → canon` | Review manual de quarries, leyendas OBSERVED/INFERRED/GENERATED, statements negados | PASS WITH LIMITATIONS |

## Decisiones de cierre

- `ADOPT`: conceptos de video como función de frame, catálogo como candidato de técnicas, local render como hipótesis, documentación primaria para backend preselection.
- `REJECT`: claim de «513 videos reproducibles», atribución demostrada a Opus 5.5, prompts completos por `prompt_partial=false`, ausencia de costo operativo, derechos implícitos sobre videos de terceros.
- `HOLD`: selección definitiva HyperFrames/Remotion; reproducibilidad visual, GPU/headless, calidad, permisos, integración con Content Seller/Ninfa.
- `NO ACTION`: no se modifica software de producción ni se ejecutan snippets de autores. Ningún MP4 ha sido generado.

## Tratamiento explícito de límites

1. **Post originals = BLOCKED**: al no poder inspeccionar X, **se retiran del conjunto de claims promovibles** los detalles de autoría, proceso exacto, assets y relación prompt→video. No se interpreta como verificación negativa ni se infiere contenido. Podrán recuperarse en una cantera posterior si hay acceso autorizado.
2. **Derechos por obra = UNKNOWN**: los 3 futuros experimentos serán de creación original (formas, datos inventados, sin audio/licencias ajenas) para evitar basarse en esos derechos. Antes de renderizar, se verificará cualquier font/plugin/asset concreto.
3. **Máquina de usuario = NOT INSPECTED**: el baseline de OS/CPU/GPU/RAM no puede inferirse de este repositorio; será capturado en el `preflight` del entorno real, no falsificado en MK0.
4. **Seguridad = DOCUMENTED / NOT ENFORCED**: el threat model especifica aislamiento de procesos, red bloqueada, secrets, limits, pruebas negativas. Sólo un test real del sandbox habilitará ejecución de HTML/JS de origen no confiable.
5. **Seekability = DOCUMENTED / NOT PROVEN**: el comportamiento de runtime deberá probarse en dos renders con versiones pinneadas; no promovemos claims de marketing.

## Decisión de madurez

```text
MK0   PASS WITH LIMITATIONS (bounded discovery)
MK1   ELIGIBLE TO BEGIN (normalize taxonomy + controls)
MK2+  BLOCKED BY MK1
BUILD  BLOCKED: preflight/sandbox/rights/stack not proven
MP4    NOT GENERATED
```

Esto cumple el principio de *fail closed*: los gaps que impiden claims fuertes siguen impidiéndolos. El cierre se limita a una **unidad de conocimiento acotada**, no a una aprobación técnica o comercial de la hipótesis del producto.

## Handoff obligatorio para MK1

- Taxonomía de `category`, `tech_tags`, `prompt_coverage`, `dependency`, `rights_state`, `animation_clock`, `render_backend`, `evidence_class`, `quality_issue` y `test_outcome`.
- Clasificación de fuentes secundarias, tests sintéticos y posibles originales inspeccionados sin mezclar niveles.
- Dedupe textual y semántica evitando ocultar variaciones entre prompts iguales.
- Decisión del stack `CANDIDATE` basada en preflight técnico; no instalar por reputación.
- `MK2` no puede comenzar antes del gate de normalización; `BUILD` no puede comenzar mientras falten permisos, sandbox, licencias, baseline y acceptance criteria de runtime.

## Review

Reviewed evidence surfaces: root README, SOURCE-INTAKE-CONTRACT, SRC-PV-001..005, Q-001..004, contrato de experimentos y fuentes primarias vinculadas. No hubo ejecución de video, auditoría de seguridad dinámica ni revisión presencial de originales.

**Resultado: cierre documental acotado, no certificación audiovisual.**
