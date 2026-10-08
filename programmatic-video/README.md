# Programmatic Video — dominio de conocimiento

Status: **MK0 — CLOSED WITH LIMITATIONS; MK1 IN PROGRESS** (2026-10-07, America/Lima).

## Hipótesis

Las técnicas de *creative coding* pueden convertirse en conocimiento reusable para producir piezas audiovisuales verificables sin dependencia obligatoria de APIs de video por créditos. **Es una hipótesis, no una capacidad demostrada.**

## Problema

El catálogo `awesome-opus5-5-videos` muestra piezas llamativas, pero disponer de un prompt o de una vista previa no demuestra que el resultado sea reproducible, rentable ni jurídicamente reutilizable. La finalidad de este dominio es aislar las técnicas transferibles y sus pruebas, no almacenar prompts virales.

## Ownership y límites

**Este dominio sí estudia:** composición temporal y espacial, tipografía animada, SVG, Canvas, WebGL/Three.js, GSAP, audio, renderización local, reproducibilidad visual, rendimiento, licencias de assets y evaluación de calidad.

**Este dominio no posee:** estrategia editorial, calendario, publicación, analítica de cuentas, identidad oficial de marcas, automatización de TikTok, producto SaaS ni código operativo de Content Seller/Ninfa.

Interfaces con otros dominios:

- `content-strategy/`: aporta brief, audience, rol, novedad/no-repeat, requisitos de canal y medición; aquí se estudia la ejecución audiovisual.
- `web-design/`: aporta tokens/branding/gramática visual; un video puede consumir un design system, no reescribirlo.
- `agent-engineering/`: aporta harness, permisos, herramientas, loops de verificación y side-effect boundaries.
- `knowledge-foundry/`: puede consumir conocimiento maduro, nunca prompts sin licencia como material vendible.
- `em3rc0d-foundry/`: evalúa si la reutilización posterior crea valor real.

## Pipeline epistemológico

```text
external source -> source intake -> mining-site -> quarries
  -> MK0 framing + gates -> MK1 taxonomy -> MK2 operating rules
  -> MK3 integration contracts -> MK4 automation -> MK5+ certification
```

Las iteraciones MK describen **madurez del conocimiento**, no sprints ni funcionalidades. Un experimento aislado no asciende automáticamente de MK0 a MK2.

## Primera fuente y postura

- Seed: [Em3rc0d/awesome-opus5-5-videos](https://github.com/Em3rc0d/awesome-opus5-5-videos) fijado al commit `756290289742535eb0ac3817548f152e9759cc70`.
- El dataset y los prompts son **material de descubrimiento**, no evidencia de que cada video usó exactamente ese prompt ni de que una recreación equivalga al original.
- No se copian los 513 prompts, imágenes ni videos al dominio. Cada asset externo requiere una comprobación de derechos independiente; licencia MIT del repositorio no concede automáticamente derechos sobre obras de terceros.
- Cualquier extracción debe conservar enlace, commit/versión, fecha, clase de procedencia, límite de inspección y estado de verificación.

## Lectura recomendada

- [Estado y gates](STATUS.md)
- [Ruta de trabajo](ROADMAP.md)
- [MK0 y acta de cierre](mk/MK0/README.md)
- [MK1 taxonomía y fixtures](mk/MK1/README.md)
- [Fuentes](mining-site/SOURCES.md)
- [Auditoría del catálogo](quarries/Q-001-opus55-catalog-audit.md)
- [Investigación de renderers](quarries/Q-002-renderer-landscape.md)
- [Muestra de posts bloqueados](quarries/Q-003-original-post-access-audit.md)
- [Riesgos de seguridad y derechos](quarries/Q-004-security-rights-threat-model.md)
- [Auditoría Content Ops + NINFA + prodAgentic](quarries/Q-005-content-ops-ninfa-integration-audit.md)
- [Contrato experimental](mk/MK0/EXPERIMENT-CONTRACT.md)

## Invariantes

1. `prompt exists != prompt is complete != video is independently reproduced`.
2. `framework advertises deterministic != our pipeline is proven deterministic`.
3. `free license for some users != zero infra cost != unrestricted redistribution`.
4. `render succeeds once != production-ready`.
5. `source catalog != production architecture`.
6. Cualquier regla promovida debe ser verificable y preservar provenance `OFFICIAL | OBSERVED | INFERRED | INSPIRED | GENERATED`.
