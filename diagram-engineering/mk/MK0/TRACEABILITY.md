# MK0 — Matriz de trazabilidad semántica

**Estado:** hipótesis visual sustentada por documentos, todavía **no certificada** mediante revisión independiente. Fuente de autoridad = documento externo al diagrama fijado por SHA. La relación visual es una interpretación `GENERATED`; la extracción de relaciones está basada en contenido `OBSERVED`.

| Caso / afirmación | Autoridad fijada | Evidencia dentro del piloto | Omisiones / límite |
|---|---|---|---|
| ECHO: audio supervisado y segmentado antes de inferencia | [Architecture](https://github.com/Em3rc0d/ECHO/blob/0c8ac4b9ed277737ac98d1db10992acb157940ab/MK1/arch/ARCHITECTURE.md), [Dataflow](https://github.com/Em3rc0d/ECHO/blob/0c8ac4b9ed277737ac98d1db10992acb157940ab/MK1/arch/DATAFLOW.md) | `source→supervisor→decode→buffer→window→scheduler`, e1–e5 | No muestra source-generation identity, fallback ni health |
| ECHO: vuelta de `RAW_INFERENCE` | Mismas fuentes | `scheduler→model→scheduler`, e6–e7, `return` | Scores no equivale a evento confirmado |
| ECHO: temporalidad y salidas distintas | Mismas fuentes | `scheduler→engine→confirmed→mqtt/store`, e8–e11 | Retries, QoS, entrega idempotente y resultados persistidos simplificados |
| NINFA: revisión factual previa a manifest | [Operating model](https://github.com/Em3rc0d/NINFA/blob/c8ee078ee65b8c06e94317edbe4f70f088e87e8e/docs/OPERATING_MODEL.md) | `research→factcheck→manifest`, n1–n2 | No dibuja experiment/build ni topic scoring |
| NINFA: voz/evidencia independientes, render local | [Operating model](https://github.com/Em3rc0d/NINFA/blob/c8ee078ee65b8c06e94317edbe4f70f088e87e8e/docs/OPERATING_MODEL.md), [bootstrap](https://github.com/Em3rc0d/NINFA/blob/c8ee078ee65b8c06e94317edbe4f70f088e87e8e/docs/MK1_BOOTSTRAP_VIDEO_FACTORY.md) | `manifest→voice/evidence→render`, n3–n6 | No implica identidad entre inputs, ni proceso de adquisición automático |
| NINFA: aprobación antes de publicar y feedback | Mismas fuentes | `render→approval→publish→analytics→research`, n7–n10 | QA/packaging/distribución derivada no están representados; no se afirma publicación automática |
| Knowledge: pointer ≠ evidencia | [Root README](https://github.com/Em3rc0d/personal_knowledge/blob/1ad55d76726823b0f82d1fea10763b329d048ddf/README.md), [JEM](https://github.com/Em3rc0d/personal_knowledge/blob/1ad55d76726823b0f82d1fea10763b329d048ddf/jett-engineering-method/README.md) | `pointer→verify→blocked | mining`, k1–k3 | HOLD es una posible salida; no toda fuente llega a quarry |
| Knowledge: revisión y gate previo a main | Mismas fuentes | `quarry→synthesis→prove→gate→canon | gate_hold`, k4–k8, k11 | Fases intermedias agrupadas; no es un diagrama exhaustivo del lifecycle |
| Knowledge: receipt condicional | [Knowledge usage](https://github.com/Em3rc0d/personal_knowledge/blob/1ad55d76726823b0f82d1fea10763b329d048ddf/knowledge-usage/README.md) | `canon→reuse→receipt` con `conditional`, k9–k10 | Un receipt no certifica un MK ni demuestra ahorro económico |

**Aclaraciones de lectura:**
- Un ID de arista prueba que está presente en `graph_contract.json`, no que la relación sea un hecho validado por expertos.
- Los diagramas no verifican el estado operacional de ECHO o NINFA; sus documentación de origen sigue prevaleciendo.
- El MK del proyecto no se da por cerrado por tener 3 archivos bonitos.
- `layout_spec_v2.json` controla posiciones/rutas declaradas, pero todavía **no existe una compilación determinista desde ese JSON versionada en el repositorio**. Los HTML se mantienen manualmente; los cambios deben reconciliar contrato, layout y output, revisarse y ejecutar tests.

## Reglas de actualización

1. Identificar el documento de autoridad y su **SHA exacto**; si cambió, registrar el delta antes de editar.
2. Revisar invariantes y omisiones; evitar inferir nuevos pasos por diseño visual.
3. Modificar coherentemente `graph_contract.json`, `layout_spec_v2.json`, `outputs/<case>.html` y, si cambia la semántica, el `fixtures/<case>.mmd` correspondiente.
4. Ejecutar verificación local + pruebas negativas; inspeccionar escritorio/móvil y transcripción textual.
5. Escribir un nuevo recibo/versionado (no sobrescribir resultados históricos) y actualizar `STATUS.md`; revisión independiente antes de promoción.

Provenance: `OBSERVED` en documentos fuente; `GENERATED` en SVG y texto alternativo; `INFERRED` para abstracciones entre componentes.
