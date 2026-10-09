# MK0 — Revisión independiente y contrato A/B

**State: NOT EXECUTED**. Guía para cerrar el piloto sin sesgo de confirmación. Los tests actuales no sustituyen una revisión semántica por alguien que contraste los documentos.

## Revisión de fidelidad por caso

| Caso | Tres preguntas de control al lector | Fallos que invalidan la prueba |
|---|---|---|
| ECHO | ¿Adónde vuelve `RAW_INFERENCE`? ¿Qué confirma un evento? ¿Cuáles son las dos salidas? | Respuesta que omite scheduler, confunde score y evento, o equipara MQTT y store |
| NINFA | ¿Narración y evidencia son independientes? ¿Se puede publicar sin aprobación? ¿Dónde se usa analytics? | Entrada serial falsa, aprobación omitida, feedback inexistente |
| personal_knowledge | ¿Una URL se promueve automáticamente? ¿Qué sucede ante HOLD/KILL? ¿Cuándo corresponde registrar un receipt? | Fuente no verificada promovida, puerta sin alternativa, receipt obligatorio |

### Registro mínimo por cada ítem

```text
case:
source_ref + source_sha:
question:
reader_variant: ORIGINAL | DIAGRAM
answer:
correct_against_source: YES | NO | AMBIGUOUS
source_evidence:
time_to_answer_seconds: OBSERVED | UNKNOWN
reader_confidence_1_to_5: OBSERVED | UNKNOWN
reviewer_notes:
```

La evaluación debe presentar **el mismo conjunto de preguntas** para origen y diagrama, con orden alternado o asignación aleatoria de formatos entre lectores; no explicar antes lo que se quiere demostrar. Revisar afirmaciones contra las fuentes fijadas; los reviewers no deben usar Mermaid generado como baseline independiente.

**Gate de comprensión:** 3 casos × 3 preguntas; no regresión de exactitud respecto al documento original y ninguna invención material. Cuando haya solo un lector, reportar resultado exploratorio y limitación de muestra. No declarar mejora en tiempo/claridad sin medida observada.

## Cambio controlado (no ejecutado)

Elegir una modificación **real y versionada** de uno de los documentos fuente, cuantificar si altera invariantes, actualizar copia del contrato y visual, evaluar tiempo humano de implementación/revisión y errores. Nunca reescribir un recibo histórico para simular la revisión.

## Decisión

- **GO selectivo:** invariantes revisados sin errores materiales + render/contraste/accesibilidad razonables + A/B sin regresión + costo aceptable + cambio reproducible.
- **PIVOT:** buena utilidad explicativa, pero exceso de trabajo de mantenimiento o semántica demasiado comprimida; conservar solo figuras manuales verificadas.
- **KILL:** fallos no remediables, pérdida semántica o costo superior a lectura estructurada.
- **HOLD:** falta cualquier evidencia indispensable. Es el estado **actual**.

La incorporación documental del PR #33 a `main` fue autorizada expresamente por el usuario y no cierra este contrato. No promover diagramas a fuentes arquitectónicas de autoridad ni declarar MK0 `COMPLETE` hasta cumplir los criterios anteriores.
