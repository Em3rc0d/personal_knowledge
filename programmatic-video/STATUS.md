# Programmatic Video — Status

Updated: 2026-10-07 (America/Lima)

## Estado actual

| Superficie | Estado |
|---|---|
| Dominio | MK0 — IN PROGRESS |
| Fuente seed | INSPECTED / BOUNDED; fijada por SHA |
| Auditoría estructural dataset | CAPTURED en quarry |
| Documentación inicial de renderers | CAPTURED / documentación, NO runtime |
| Clasificación de prompts completos vs parciales | OBSERVED / pendiente verificar cobertura real |
| Derechos de videos, audio, imágenes y marcas | UNKNOWN para obras individuales |
| Motor de render elegido | NO DECIDIDO |
| Prototipo MP4 | NOT BUILT |
| Reproducibilidad real | UNTESTED |
| Coste local de CPU/GPU/tiempo | UNMEASURED |
| Integración Content Seller / Ninfa | BLOCKED |

## Gates de cierre MK0

- [x] Definir responsabilidad de dominio y exclusiones.
- [x] Identificar y fijar fuente seed al commit.
- [x] Auditar estructura, distribución y límites de calidad del dataset.
- [x] Registrar fuentes primarias de renderizadores y diferencias de licencia.
- [x] Separar hipótesis de observaciones y marketing.
- [x] Especificar tres pruebas y sus métricas **antes** de implementarlas.
- [ ] Validar una muestra estratificada de prompts contra publicaciones originales y registrar evidencia de acceso/post/contexto.
- [ ] Verificar derechos de los recursos concretos que entrarían en los 3 experimentos, o sustituirlos por assets originales.
- [ ] Revisar riesgos de ejecución de HTML/JS generado por agentes en sandbox local, dependencias y acceso a red.
- [ ] Definir baseline de máquina, memoria y stack para medir coste/performance.
- [ ] Completar segunda fuente independiente de principios técnicos (no otra simple galería).
- [ ] Ejecutar review de trazabilidad claims -> fuente -> limitaciones y producir acta de cierre MK0.

**MK0 permanece abierto** hasta superar los gates. Un documento de experimento no constituye evidencia de render o exportación.

## Gates posteriores

| MK | Objetivo | Estado |
|---|---|---|
| MK1 | Normalizar técnica/formato/dependencia/derechos/evidencia/fracaso | BLOCKED BY MK0 |
| MK2 | Diseñar contratos de composición, render, pruebas y reusable patterns | BLOCKED |
| MK3 | Definir interfaces con Content Operations, sin publicar | BLOCKED |
| MK4 | Automatizar con aislamiento, permisos, validación y límites de costo | BLOCKED |
| MK5+ | Certificar reproducibilidad, calidad y regresión real | BLOCKED |

## Próximo paso

Hacer auditoría manual pequeña y diversa (no seleccionar sólo virales), completar intake de licencias/seguridad y resolver un stack candidato **sin crear plataforma**. Dejar cada bloqueo en `UNKNOWN` hasta que exista evidencia.
