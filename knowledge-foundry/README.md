# Knowledge Foundry

Status: **MK0 — Mine & Frame / active**

Knowledge Foundry es el workspace de `personal_knowledge` para transformar conocimiento trazable y suficientemente maduro en productos educativos verificables: cursos, workshops, playbooks, labs, assessment packs y material para instructores.

No es el dueño del conocimiento técnico de origen. Tampoco es un repositorio de cursos sueltos.

## Boundary

```text
domain canon in personal_knowledge
        ↓
bounded eligibility
        ↓
Knowledge Foundry
        ↓
educational compilation
        ↓
course / workshop / lab / playbook
```

Ownership:

- los dominios existentes de `personal_knowledge` siguen siendo autoridad sobre su conocimiento técnico;
- `em3rc0d-foundry/` sigue siendo la foundry general de productos y reusable product capital;
- `knowledge-foundry/` es autoridad únicamente sobre el proceso de convertir conocimiento en productos educativos;
- un producto educativo nunca reemplaza al canon del que fue compilado.

## Core thesis

El conocimiento no se monetiza de forma durable copiando notas o fuentes. Se convierte en un activo educativo cuando podemos demostrar:

1. qué sabe el alumno al entrar;
2. qué debe poder hacer al salir;
3. de qué conocimiento y evidencia depende cada claim;
4. qué secuencia reduce prerequisitos y carga cognitiva;
5. qué estrategia instruccional está justificada para ese outcome/audiencia;
6. qué ejercicio demuestra transferencia;
7. qué assessment soporta qué interpretación;
8. qué accessibility/inclusion boundary aplica;
9. qué rights/provenance permite publicar el material;
10. qué evidencia de pilotaje soporta que el producto enseña algo útil;
11. qué cambio del conocimiento fuente invalidaría o exigiría actualizar el producto.

## Compiler model

```text
ELIGIBLE KNOWLEDGE SLICE
      ↓
candidate extraction
      ↓
learner + prerequisite contract
      ↓
concept dependency graph
      ↓
learning outcomes
      ↓
instructional-strategy selection
      ↓
lessons + labs
      ↓
assessment + accessibility
      ↓
source/rights + dependency manifest
      ↓
pilot
      ↓
pedagogical evidence
      ↓
commercial test
      ↓
promotion / release
      ↓
observe / revise / retire
```

### Important distinction

Knowledge Foundry conserva separadas:

- **Technical truth** — qué es correcto según el dominio fuente.
- **Pedagogical truth** — qué secuencia/ejercicio ayuda realmente a aprender.
- **Evidence truth** — qué podemos demostrar con fuentes, fixtures, assessments y resultados.
- **Commercial truth** — qué audiencia está dispuesta a pagar o invertir tiempo en aprender.

Una no implica automáticamente las otras.

## Inputs

Por defecto, un producto educativo consume **bounded knowledge slices** que pasan `architecture/DOMAIN_INPUT_CONTRACT.md`.

Puede inspeccionar quarries o fuentes externas para investigación, pero:

> quarry/source evidence no se convierte directamente en una afirmación de curso.

Debe resolverse authority, maturity, provenance, freshness, rights, contradicciones y dependency revision del slice correspondiente.

## Evidence expansion — 2026-10-07

El audit del repositorio añadió evidence packages específicos para:

- learning science: retrieval practice, worked examples, spacing y formative assessment;
- assessment validity/reliability/fairness;
- accessibility con WCAG 2.2 e inclusive learning con UDL 3.0;
- rights/licensing/provenance con GitHub, Creative Commons, SPDX y W3C PROV;
- learner-pilot data boundary para el contexto peruano.

Estas fuentes son inputs MK0. **No se convierten en una receta educativa universal sin dogfood.**

## Outputs

Knowledge Foundry podrá producir, cuando el MK lo permita:

- courses;
- workshops;
- labs;
- playbooks;
- assessment packs;
- instructor guides;
- reference sheets;
- cohort exercises;
- article/lesson projections;
- reusable educational components.

Los outputs viven bajo `products/` y tienen lifecycle propio. Un draft no es un producto certificado.

## Current MK0 mission

MK0 no intenta vender ni publicar un curso todavía.

Su misión es:

1. fijar los boundaries del workspace;
2. definir qué conocimiento puede entrar al compiler;
3. estudiar mecanismos reutilizables de aprendizaje/evaluación;
4. definir el primer knowledge compiler;
5. definir rights/provenance/licensing boundaries para material comercial;
6. definir accessibility, assessment y pilot-data boundaries;
7. definir el lifecycle de un producto educativo;
8. seleccionar, sin comprometer todavía, un primer candidato de dogfood.

## Navigation

- `STATUS.md` — estado actual.
- `ROADMAP.md` — secuencia de MK0.
- `REPOSITORY_CONTRACT.md` — autoridad, provenance y promotion rules.
- `KNOWLEDGE_MAP.md` — mapa del workspace.
- `LLM_CONTEXT.md` — routing para lectores agentic.
- `architecture/KNOWLEDGE_COMPILER.md` — arquitectura inicial del compiler.
- `architecture/DOMAIN_INPUT_CONTRACT.md` — decide qué slices de conocimiento pueden compilarse.
- `architecture/ASSESSMENT_EVIDENCE_MODEL.md` — limita qué podemos inferir de assessments.
- `architecture/ACCESSIBILITY_AND_INCLUSION.md` — separa conformance e inclusive learning.
- `architecture/RIGHTS_AND_LICENSING.md` — rights/commercial reuse boundary.
- `architecture/KNOWLEDGE_DEPENDENCY_MANIFEST.md` — revisions, derivation and staleness.
- `architecture/PILOT_DATA_BOUNDARY.md` — learner-data fail-closed boundary.
- `mining-site/` — fuentes inspeccionadas.
- `quarries/` — destilaciones no canónicas.
- `mk/MK0/` — gates, unknowns y ledger del MK activo.
- `products/` — futuros productos compilados; release bloqueado en MK0.
