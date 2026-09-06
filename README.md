# personal_knowledge

Monorepo personal de conocimiento técnico, de producto y diseño.

## Filosofía

Este repositorio convierte fuentes, investigación y experiencia en conocimiento versionado, trazable y reutilizable. No es un almacén de notas sueltas.

Cada dominio evoluciona mediante **MKs (Mark iterations)** y conserva separación explícita entre evidencia, interpretación, diseño, arquitectura, implementación y validación.

El operating model metodológico común está documentado en [`jett-engineering-method/`](./jett-engineering-method/).

## Flujo base

```text
problem / recover
        ↓
mining-site / quarries
        ↓
brainstorming
        ↓
design
        ↓
architecture
        ↓
plan
        ↓
build
        ↓
test
        ↓
prove
        ↓
MK gate / promotion
        ↓
observe / learn
        ↓
next MK / iterate / hold / kill
```

Este flujo expresa madurez epistemológica y de ingeniería; no exige crear burocracia o archivos vacíos cuando una fase no aporta valor.

## Regla de `main`

Todo conocimiento nuevo se trabaja en una branch efímera:

```text
knowledge/<domain>-<mk>-<purpose>
```

`main` es la fuente canónica del monorepo. No se usa como workspace experimental.

> **`main` no es donde pensamos. `main` es donde queda lo que sobrevivió investigación, razonamiento, evidencia, review y validación.**

Flujo de cierre:

```text
branch
  ↓
review
  ↓
tests / evidence
  ↓
MK gate
  ↓
PR ready
  ↓
merge main
  ↓
branch cleanup
```

## Convenciones

- `MK0`: Mine & Frame — captura, minería, scope, vocabulario, provenance, fuentes y primeras hipótesis.
- `MK1`: Normalize & Classify — taxonomía, normalización, deduplicación y resolución de contradicciones.
- `MK2`: Operationalize — reglas, schemas, templates, checklists y artefactos utilizables.
- `MK3`: Integrate — contratos y relaciones entre dominios/sistemas.
- `MK4`: Automate — automatización con boundaries, provenance y comportamiento fail-closed.
- `MK5+`: Certify / Refine — reproducibilidad, fixtures, contraejemplos, resiliencia y refinamiento.
- `mining-site/`: mapa de investigación y provenance.
- `quarries/`: extracciones concretas y evidencia procesada desde fuentes; quarry no equivale a canon.
- No mezclar hechos de fuente con inferencias propias sin etiquetarlos.
- Provenance base: `OFFICIAL`, `OBSERVED`, `INFERRED`, `INSPIRED`, `GENERATED`.
- Todo principio reusable debe terminar expresado como una regla verificable, patrón, antipatrón o criterio de test cuando corresponda.
- Un MK no se cierra por cantidad de archivos; se cierra por acceptance criteria y evidencia.
- `STATUS.md` de cada dominio es su tablero canónico: completed, in progress, blocked, unknown/open questions y next gate.
- Nunca convertir silenciosamente `implemented → production-ready`, `inference → fact` o `agent says DONE → verified completion`.

## Jett Engineering Method — reglas base

- Evidence over narrative.
- No claim without evidence; no evidence without provenance.
- Recovery before construction.
- Brainstorming is not canon.
- Jett reviews; agents execute.
- BUILD is not the beginning.
- BUILD is not the end.
- Evidence strength is proportional to risk.
- Working once is not the same as working reliably.
- UNKNOWN remains UNKNOWN.
- Preserve reversibility and history.
- Security and provenance are architecture.
- Limit work in progress.
- Not every good idea deserves a roadmap.
- Kill decisions are valid engineering decisions.

La especificación completa vive en [`jett-engineering-method/README.md`](./jett-engineering-method/README.md).

## Dominios

- [`jett-engineering-method/`](./jett-engineering-method/) — Operating model interno para llevar problemas desde incertidumbre hasta conocimiento/software demostrado, con gates, claim discipline, evidence y promotion rules.
- [`ux-laws/`](./ux-laws/) — Psicología aplicada a UX convertida en reglas operables para diseño de producto.
- [`web-design/`](./web-design/) — Design intelligence para websites: evidencia visual, gramática visual, `DESIGN.md`, tokens, contratos de componentes, responsive, accesibilidad, motion y verificación visual. RICOUI es una fuente relevante dentro de este dominio, no el dominio mismo.
- [`openship/`](./openship/) — Arquitectura de control plane, deployment, runtimes, edge, SSH, seguridad, CI/CD y MCP extraída del proyecto OpenShip para estudiar patrones reutilizables de plataformas de infraestructura.
- [`research-corpora/whatsapp-links-2025-2026/`](./research-corpora/whatsapp-links-2025-2026/) — Corpus transversal de 89 URLs + 1 imagen estudiado con provenance, estados de acceso, contradicción científica, MK0→MK2 y Acta de Conformidad CA-001; preserva fuentes externas por identidad pero organiza el conocimiento promovido por significado, no por publisher.
