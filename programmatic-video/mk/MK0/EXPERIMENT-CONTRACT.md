# MK0 — Contrato de experimentos propuestos

Status: **DESIGNED / NOT EXECUTED**. Artefacto `GENERATED`.
Date: 2026-10-07 (America/Lima).

## Hipótesis falsable

Podemos producir 3 videos verticales distintos mediante código (no text-to-video), localmente y sin servicios de generación de video pagados obligatorios, conservando control por frame, calidad suficiente en móvil, derechos claros y costes medibles.

**Lo que NO se demuestra en MK0:** que el runtime está instalado, que exporta MP4, que el resultado es atractivo, que cuesta US$0 operarlo, ni que integrar con Content Operations es rentable.

## Gate de preparación obligatorio

- [ ] MK0 source/license/security gates revisados y cerrados.
- [ ] Definir máquina observada: OS, CPU, GPU, RAM, browser, Node, FFmpeg y versiones.
- [ ] Confirmar red deshabilitada o explícitamente allowlisted durante render; cero secretos expuestos.
- [ ] Assets/fonts/audio: originales, generados localmente o licencia específica trazada.
- [ ] Elegir/registrar backend y su licencia **para el uso previsto**.
- [ ] Definir dónde se guardarán los artefactos y recibos (fuera de este repo de conocimiento).
- [ ] Aprobación para ejecutar scripts de terceros/generados, si aplica.

## Tres casos controlados

### PV-EXP-01 — Tipografía cinética / Motion

- Brief original: `concepto → promesa → prueba → CTA`; no usar copy ya publicado en las cuentas.
- Target: vertical `1080x1920`, `30fps`, `10s` (300 frames).
- Composición: máximo 4 escenas, tipografía animada, transiciones de alto contraste y área segura superior/inferior derivada de la plantilla de canal; sin material ajeno.
- Probar: seek a frames `0, 75, 150, 225, 299`, cortes y legibilidad.

### PV-EXP-02 — Explainer / Diagrama animado

- Brief original: explicar una arquitectura genérica de 3 pasos con una sola idea central.
- Target: `1080x1920`, `30fps`, `10s`.
- Composición: shapes/vector, datos sintéticos, labels y transición entre estados.
- Probar: claridad secuencial, orden visual, ausencia de dependencia de APIs, precisión de labels.

### PV-EXP-03 — Escena 3D / Cámara

- Brief original: objeto geométrico simple, cámara y luces animadas; sin marcas ni modelos externos.
- Target: `1080x1920`, `30fps`, `10s`.
- Composición: primitivas Three.js/WebGL o alternativa justificada, variación de cámara controlada por tiempo absoluto.
- Probar: compatibilidad headless/software GPU, fugas de recursos, caída de frames, consistencia de iluminación y fallback ante fallo de WebGL.

## Evidencia por experimento

| Campo | Requerido |
|---|---|
| `experiment_id`, `revision`, `timestamp` | Identidad estable |
| `scene_source_sha`, `assets_manifest` | Reproducibilidad y derechos |
| `renderer_version`, `browser_version`, `ffmpeg_version` | Entorno |
| `os`, `cpu`, `gpu`, `ram_total` | Baseline del equipo |
| `resolution`, `fps`, `expected_frames` | Target |
| `duration_probe`, `frame_count_probe`, `codec_probe` | Validación con ffprobe |
| `render_1_elapsed_s`, `render_2_elapsed_s`, `peak_ram` | Coste temporal y recursos |
| `external_requests`, `paid_api_calls` | Dependencia y coste |
| `frame_diff_or_hashes`, `reviewer_notes` | Consistencia/quality |
| `rights_status`, `decision`, `limitations` | Claim boundary |

## Acceptance criteria

1. **Export:** un MP4 decodificable y verificado por `ffprobe`; codec, resolución, duración y conteo de frames coinciden con contrato (duración ±1 frame).
2. **Aislamiento:** no se filtraron secretos, no hubo red externa no autorizada ni llamadas a servicios por créditos.
3. **Repetición:** dos renders completos sobre el mismo input; comparar frames clave decodificados con métricas/report visual. **No exigir hash binario idéntico de archivos** si el contenedor incorpora metadata variable; explicar toda discrepancia.
4. **Legibilidad/seguridad:** revisión humana en formato de teléfono; no recortes críticos de texto, no exceder safe-area definida y revisión de flashes/contraste.
5. **Coste:** reportar tiempo, CPU/RAM, tamaño final y recursos; no afirmar coste cero absoluto sólo porque no hubo API.
6. **Derechos:** evidencias de licencia de todos los assets usados.
7. **Independencia:** cada caso debe correr desde un comando documentado y datos de entrada versionados en un entorno limpio razonable, sin depender de X, Skillry ni cuentas del creador.
8. **Negativos:** registrar al menos un caso de fallo controlado (asset ausente, WebGL no disponible, fallo de encoder u otro) con error visible, sin falso éxito.

**Regla de decisión:** `PASS` sólo si cumple 1–8 para su caso. `PASS WITH LIMITATIONS` para fallas no críticas y explícitas; `FAIL` si impide el claim; `BLOCKED` si permisos/licencia/entorno impiden ejecutar. Un único PASS no implica que la Video Factory está lista.

## Forma mínima del pipeline esperado

```text
approved synthetic brief
   -> scene spec + local assets
   -> seekable composition
   -> local renderer + encoder
   -> MP4
   -> ffprobe + selected frame review + risk checks
   -> evidence receipt + PASS/FAIL/HOLD
```

Ni el scheduler de TikTok ni Ninfa ni Content Seller se modifican para correr estos experimentos. Cuando exista evidencia, primero se propone un contrato de entrada/salida a esos sistemas, separado de la decisión editorial.
