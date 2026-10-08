# Programmatic Video — Roadmap

## MK0 — Mine & Frame (cerrado con límites; ver [CLOSURE](mk/MK0/CLOSURE.md))

1. **Intake:** congelar URL/SHA/fecha del catálogo, confirmar identidad upstream y límites del contenido republicado.
2. **Quarry:** caracterizar duplicados, prompts parciales, categorías, tecnologías, sesgo de selección y dependencias externas.
3. **Fuentes independientes:** consultar documentación primaria de al menos dos alternativas de render, con licencias diferenciadas.
4. **Riesgos:** resolver código no confiable, derechos de terceros, costes locales, secretos y APIs externas.
5. **Contrato de prueba:** especificar 3 microexperimentos sintéticos, sin copiar assets ni publicar contenido.
6. **Review:** evaluar si los claims presentes tienen soporte, documentar huecos y cerrar MK0 **sólo** con evidence gate.

Output de cierre: `mk/MK0/CLOSURE.md` — `PASS WITH LIMITATIONS`: sólo alcance discovery, sin verificación de posts originales ni runtime.

## MK1 — Normalize & Classify (habilitado; aún sin ejecutar)

Taxonomía mínima: `technique`, `composition_type`, `source_provenance`, `prompt_coverage`, `rights_state`, `external_dependency`, `render_backend`, `determinism_scope`, `quality_issue`, `verification_status`. Dedupe por prompt normalizado y similitud semántica con trazabilidad de variantes.

## MK2 — Operationalize (bloqueado)

Definir contrato `brief -> scene spec -> timeline -> renderer -> MP4 -> ffprobe/frame review -> evidence manifest`; reproducibilidad, sandbox, schemas, fallos y reglas transferibles. Sólo construir el slice mínimo si MK0/MK1 demuestran valor.

## MK3 — Integrate (bloqueado)

Interfaz con Content Operations: guion aprobado, cuenta/branding, vertical-safe regions, anti-repetition, export/approval handoff. Publicación y scheduling fuera de alcance.

## MK4 — Automate (bloqueado)

Orquestación local con batch queues, retries acotados, observabilidad y cost guardrails; nada de tokens o APIs de pago por defecto.

## MK5+ — Certify / Refine (bloqueado)

Fixtures golden-frame, comparaciones de escenas, ejecución en dos entornos, revisión humana, licencias, regresión y evidencia de uso externo.

## Criterio de kill / hold

Si ninguno de los tres casos puede renderearse en local con calidad adecuada, sin servicios pagados obligatorios y coste operativo razonable, la decisión válida es `HOLD` o `KILL`. La cantidad de prompts de origen no cambia el resultado.
