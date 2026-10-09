# Evidence receipt — v2, inspección de repositorio + material local

**Fecha de inspección:** 2026-10-08 (America/Lima).
**Repo:** [personal_knowledge PR #33](https://github.com/Em3rc0d/personal_knowledge/pull/33).
**Commit examinado:** `3b3dbcdfd8b837c5128e50308142f67c1cf5e477` de `knowledge/diagram-engineering-mk0-pilot`.
**Clasificación:** `OBSERVED` para contenido publicado y tests locales; `GENERATED` para gráficos. **No** certificado por terceros.

## 1) Lectura exacta del estado publicado

Se consultaron por el conector GitHub los tres `outputs/*.html`, `graph_contract.json` y `layout_spec_v2.json` de esa rama, comparando nodos, aristas, tipos, SHA de fuente, etiquetado accesible básico, alternativa textual, señal móvil y presencia de scripts/enlaces externos.

| Case | HTML Git blob | Pin de fuente | Nodos | Aristas | Chequeos remotos limitados |
|---|---|---|---:|---:|---|
| echo | `71f3ed3a435683ce0b6bf20339bf32073e0a9eee` | `0c8ac4b9ed277737ac98d1db10992acb157940ab` | 11 | 11 | PASS |
| ninfa | `f296f2dfb60a26f6015321d6e53af6ae0243616c` | `c8ee078ee65b8c06e94317edbe4f70f088e87e8e` | 9 | 10 | PASS |
| knowledge | `5bbce397c11aa7fbf37774b02f379bed829fa916` | `1ad55d76726823b0f82d1fea10763b329d048ddf` | 12 | 11 | PASS |

**Importante:** el check remoto fue inspección estática ad hoc de contenido, **no** ejecución remota de Python, Chromium o GitHub Actions. Es reproducible materializando el SHA y usando el verificador versionado; no equivale a run de CI.

## 2) Ejecución local del paquete experimental, distinta del commit

Se reejecutaron en un ZIP local de la iteración v2 el `verify_pilot.py` y `test_adversarial.py`: **3/3 PASS** y **12/12 mutaciones detectadas**. El paquete incluye además metadatos de 6 vistas Chromium (1440 escritorio, 390 móvil), sin errores de página ni etiquetas desbordadas en esos resultados.

**Límite crítico:** los HTML y scripts del ZIP local poseen **blob SHA distintos** a los archivos del PR. Por tanto este paquete **NO** certifica byte a byte el HEAD de GitHub. El repositorio sí recibió un control independiente de estructura contra `graph_contract.json`. No afirmar que las 6 capturas proceden exactamente del commit actual.

La diferencia es relevante para reproducibilidad y debe mantenerse visible hasta regenerar evidencia directamente desde el checkout de ese commit, sin editar o sustituir outputs.

## 3) Riesgos pendientes

- Comparación independiente de semántica original vs versión resumida: **PENDING**.
- Reejecución exacta desde checkout del commit publicado, y captura con SHA/entorno en el recibo: **PENDING**.
- Auditar totalidad de accesibilidad/contraste en navegador: **PENDING** (el verificador cubre un subconjunto).
- Auditoría de scripts/código del upstream: **NOT EXECUTED**.
- Comparación A/B de lectores, tiempo de mantenimiento y tokens facturados: **NOT MEASURED**.
- `layout_spec_v2.json` sin compilador versionado determinista: **OPEN**.
- La rama fue creada desde `main@1ad55d7`; `main` ha avanzado posteriormente. Los SHA de fuentes son **intencionalmente históricos**. No atribuirles frescura actual ni rebasear/promover sin comparar diffs.

## Decisión

**HOLD — evidencia técnica preliminar suficiente para continuar investigación, insuficiente para promoción a canon.** Nada en este recibo reemplaza la autoridad de ECHO, NINFA o del protocolo JEM. Siguiente movimiento: revisión de [trazabilidad](TRACEABILITY.md), [gate A/B](REVIEW-GATE.md) y reproducción desde checkout de Git.
