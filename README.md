# personal_knowledge

Monorepo personal de conocimiento técnico, de producto y diseño.

## Filosofía

Este repositorio convierte fuentes, investigación y experiencia en conocimiento versionado, trazable y reutilizable. No es un almacén de notas sueltas.

Cada dominio evoluciona mediante **MKs (Mark iterations)** y conserva separación explícita entre evidencia, interpretación, diseño, arquitectura, implementación y validación.

## Flujo base

```text
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
next MK / certification
```

## Convenciones

- `MK0`: captura, minería, scope, vocabulario, fuentes y primeras hipótesis.
- `MK1+`: iteraciones progresivas que cierran decisiones y aumentan operacionalización/verificación.
- `mining-site/`: mapa de investigación y provenance.
- `quarries/`: extracciones concretas y evidencia procesada desde fuentes.
- No mezclar hechos de fuente con inferencias propias sin etiquetarlos.
- Todo principio reusable debe terminar expresado como una regla verificable, patrón, antipatrón o criterio de test.

## Dominios

- [`ux-laws/`](./ux-laws/) — Psicología aplicada a UX convertida en reglas operables para diseño de producto.
