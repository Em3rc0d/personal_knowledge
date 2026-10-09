# MK0 pilot contract — Diagram Engineering

## Design / scope
Three cases: **ECHO** (data flow), **NINFA** (production process), **personal_knowledge** (evidence dependency path). Only source documents at SRC-ECHO, SRC-NINFA, SRC-PK revisions can authorize diagram claims.

Output settings: HTML source + inline SVG; slide-16x9 / 1280×720; no motion; mixed audience; simplified overview with explicit deviations from density target; offline system fonts; shared neutral editorial tokens. Generated Mermaid files are companion representations, not a converter benchmark.

## Invariants
- ECHO: source supervision → normalization → bounded audio → windows/scheduling → ModelRunner → EventEngine → confirmed event → separate MQTT/persistence.
- NINFA: structured scene manifest, evidence/voice inputs, local render/SRT, human QA **before** delivery. No automatic release claim.
- personal_knowledge: source ≠ evidence; resolved source precedes quarry; MK gate before main; later reuse may yield a receipt.

## Fail-closed gate
1. **Structural**: one accessible named SVG with description, IDs unique, all connectors refer to visible nodes; no script/remote dependencies; readable scroll container.
2. **Semantic**: independent reviewer checks each invariant and all omissions against the pinned original. Material omitted path or fictitious behavior => FAIL.
3. **Visual**: screenshot of browser render (desktop/mobile) for collision, clipping, legibility and color contrast. Passing code check alone => UNKNOWN.
4. **A/B**: compare original source text/ASCII and rendered overview with the same three source-specific questions. No decline in answer accuracy; record speed, confidence and review time. Reviewer must not be primed to prefer visuals.
5. **Cost**: measure author/review elapsed time, prompt+tool payload tokens if provider instrumentation exists, incremental edit burden. Do not infer billed tokens from byte size.
6. **Change rehearsal**: replay one actual source revision into visual; review extra work and provenance update.

GO only for selective use if all three semantic, visual and comprehension gates pass and cost is acceptable; otherwise PIVOT to hand-curated figures or KILL automatic use. This is a pilot, no downstream project mutation, no default adoption. Human promotion required.

## Contrato de evidencia v2 — corrección de límites

No confundir `graph_contract.json` con autoridad científica, de producto o de ingeniería del sistema original. Verificación de relaciones **dentro del propio gráfico** y revisión de relaciones **respecto a la fuente** son gates distintos. Un test autoconsistente puede seguir siendo semánticamente incorrecto.

El paquete de evidencia local v2 difiere del commit remoto en bytes; para elevarlo a evidencia reproducible del repositorio es obligatorio ejecutar los comandos de [REPRODUCE.md](REPRODUCE.md) sobre checkout exacto y capturar versión, commit, salida, navegador, dimensiones y comparación de archivos.

Los tests adversariales actuales abarcan 12 mutaciones en el caso ECHO, no 12 por caso ni una prueba de seguridad exhaustiva. Los controles de contraste están acotados a tokens y superficies conocidas; no hay prueba de WCAG integral.

Antes del GO: revisar la [matriz de trazabilidad](TRACEABILITY.md), completar la evaluación del lector [REVIEW-GATE.md](REVIEW-GATE.md), registrar un rehearsal con revisión de fuente y evaluar mantenimiento sin prometer ahorro. No ejecutar CI, API pagada ni nuevas automatizaciones por defecto.
