# Knowledge Foundry

Status: **MK0 — Mine & Frame / active**

Knowledge Foundry es el workspace de `personal_knowledge` para transformar conocimiento trazable y suficientemente maduro en productos educativos verificables: cursos, workshops, playbooks, labs, assessment packs y material para instructores.

No es el dueño del conocimiento técnico de origen. Tampoco es un repositorio de cursos sueltos.

## Boundary

```text
domain canon in personal_knowledge
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
5. qué ejercicio demuestra transferencia;
6. qué assessment diferencia comprensión de repetición;
7. qué licencia/provenance permite publicar el material;
8. qué evidencia de pilotaje soporta que el producto enseña algo útil.

## Compiler model

```text
CANONICAL KNOWLEDGE
      ↓
candidate extraction
      ↓
teachability audit
      ↓
concept dependency graph
      ↓
learning outcomes
      ↓
curriculum / lesson specs
      ↓
labs + assessments
      ↓
source + license manifest
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

Por defecto, un producto educativo consume **canon promovido** desde otros dominios.

Puede inspeccionar quarries o fuentes externas para investigación, pero:

> quarry/source evidence no se convierte directamente en una afirmación de curso.

Debe resolverse provenance, licencia, contradicciones y autoridad del dominio correspondiente.

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
2. estudiar mecanismos reutilizables de empaquetado/evaluación de conocimiento;
3. definir el primer knowledge compiler;
4. definir provenance/licensing boundaries para material comercial;
5. definir el lifecycle de un producto educativo;
6. seleccionar, sin comprometer todavía, un primer candidato de dogfood.

Primer quarry externo: `agent-skills`, usado como fuente de mecanismos sobre skill anatomy, progressive disclosure, routing, evals y pressure testing; no como contenido para copiar.

## Navigation

- `STATUS.md` — estado actual.
- `ROADMAP.md` — secuencia de MK0.
- `REPOSITORY_CONTRACT.md` — autoridad, provenance y promotion rules.
- `KNOWLEDGE_MAP.md` — mapa del workspace.
- `LLM_CONTEXT.md` — routing para lectores agentic.
- `architecture/KNOWLEDGE_COMPILER.md` — arquitectura inicial del compiler.
- `mining-site/` — fuentes inspeccionadas.
- `quarries/` — destilaciones no canónicas.
- `mk/MK0/` — gates, unknowns y ledger del MK activo.
- `products/` — futuros productos compilados; release bloqueado en MK0.
