# Q-006 — Auditoría real de código reutilizable en NINFA

Fecha: 2026-10-07 (Lima). Repositorio: [Em3rc0d/NINFA](https://github.com/Em3rc0d/NINFA), rama `main`.
Provenance: `OBSERVED` para código, esquemas y configs directamente inspeccionados; `OFFICIAL/INTERNAL` para afirmaciones de sus documentos; `INFERRED` para recomendaciones.
Estado: **INSPECTED / BOUNDED / NO VIDEO RENDERER CODE VERIFIED**.

## Verificación técnica y alcance

Se inspeccionaron directamente los archivos de implementación identificados en el historial de commits, los manifes­tos de UAT/Shorts y la documentación de producción. No se pudo recorrer un árbol recursivo completo mediante el conector; por lo tanto, **"no localizado" no implica una prueba de inexistencia absoluta**. El hallazgo sólo permite afirmar que no se verificó una API/CLI versionada de compositor audiovisual en las superficies inspeccionadas.

| Artefacto | Evidencia inspeccionada | Clasificación |
|---|---|---|
| [`tools/chatterbox-local/app/app.py`](https://github.com/Em3rc0d/NINFA/blob/main/tools/chatterbox-local/app/app.py) | UI Gradio, segmentación de texto, `ChatterboxMultilingualTTS`, concatenación WAV, FFmpeg `-vn -ar 24000` para **normalizar audio de referencia** | **TTS comprobable en código, NO ensamblador MP4** |
| [`tools/chatterbox-local/Dockerfile`](https://github.com/Em3rc0d/NINFA/blob/main/tools/chatterbox-local/Dockerfile) | Python 3.11, CUDA wheels PyTorch 2.6, FFmpeg instalado, versión Chatterbox `0.1.7` | ejecución audio local; no video pipeline |
| [`tools/chatterbox-local/docker-compose.yml`](https://github.com/Em3rc0d/NINFA/blob/main/tools/chatterbox-local/docker-compose.yml) | `gpus: all`, mount de voces/inputs/outputs, puerto `7860:7860` | servicio de voz con requisitos GPU y superficie de red |
| [`tools/chatterbox-local/scripts/start.sh`](https://github.com/Em3rc0d/NINFA/blob/main/tools/chatterbox-local/scripts/start.sh) | ejecuta `docker run --gpus all ... nvidia-smi` incondicionalmente **antes** de iniciar | **CPU fallback documentado ≠ startup sin GPU validado** |
| [`.github/workflows/kokoro-short-narration.yml`](https://github.com/Em3rc0d/NINFA/blob/main/.github/workflows/kokoro-short-narration.yml) | instala `kokoro-onnx`, sintetiza una locución fija y sube `narration.wav` + JSON | workflow de audio, NO exportador de MP4 |
| [`experiments/uat-001/scene_manifest.json`](https://github.com/Em3rc0d/NINFA/blob/main/experiments/uat-001/scene_manifest.json) | `1920x1080`, 30fps, 14 escenas descriptivas, sin tiempo absoluto de inicio/fin por escena | contrato editorial de escenas, **no timeline ejecutable unívoco** |
| [`content/shorts/2026-10-02-cross-app-fragmentation/scene_manifest.json`](https://github.com/Em3rc0d/NINFA/blob/main/content/shorts/2026-10-02-cross-app-fragmentation/scene_manifest.json) | `1080x1920`, beats `start/end` en segundos, narración y metadata, duración visual `12.5s`, voz final `12.7s` | mejor input para timebase, pero sin export API y con reconciliación AV pendiente |
| [`docs/MK1_BOOTSTRAP_VIDEO_FACTORY.md`](https://github.com/Em3rc0d/NINFA/blob/main/docs/MK1_BOOTSTRAP_VIDEO_FACTORY.md) | declara UAT exitosa, FFmpeg/1080p/SRT y trabajo de producción realizado | **declaración documental sobre pipeline**, no prueba de código reusable en repo |
| [`docs/MK1_STATUS.md`](https://github.com/Em3rc0d/NINFA/blob/main/docs/MK1_STATUS.md) | declara UAT-001..005 y dos videos completos | evidencia histórica reportada por proyecto; no render interface verificada |

## Riesgos que cambian la integración

### R1 — No hay un video builder listo para importar (verificación actual)

El nombre "NINFA" **no** puede utilizarse como valor de `renderer_id` sin módulo ejecutable/versionado y fixture que demuestre `scene manifest → MP4`. El código disponible y directamente inspeccionado es principalmente **audio/TTS**; manifiestos + README no suplen API de ensamblaje audiovisual.

**Decisión:** `REUSE_MANIFEST_SEMANTICS`, `KEEP_TTS_OPTIONAL`, `NO_CODE_COPY_AS_VIDEO_ENGINE`. Si el código FFmpeg/edición usado realmente para los episodios vive fuera del repo, deberá recuperarse explícitamente antes de considerarse reutilizable.

### R2 — GPU obligatoria en arranque de Chatterbox

`docker-compose.yml` usa `gpus: all` y `scripts/start.sh` lanza un chequeo `--gpus all` incondicionalmente. `DEVICE=cpu` en Python no demuestra que ese procedimiento arranque sin GPU.

**Decisión:** NUNCA hacer TTS parte obligatoria del video POC. Empezar silente. No corregir este script como efecto secundario de la auditoría.

### R3 — Superficie local expuesta en red y datos

Gradio inicia `server_name="0.0.0.0"`, Compose publica `${CHATTERBOX_PORT:-7860}:7860` en interfaces del host. Montajes incluyen referencias de voz y WAV. Sin un contrato adicional de aislamiento/acceso, no acoplar ese servicio a un renderer que ejecuta JS generado.

**Decisión:** si alguna vez se invoca TTS, tratarlo como puerto interno **autorizado y separado** con controles de red/identidad; no montar `/voices` en worker de video.

### R4 — Manifiestos de escenas son insumo semántico, no especificación de composición

UAT-001 usa descripciones de escenas sin marcas temporales; el Short fija beats en segundos; no hay schema compartido verificado para tipografía, safe zones, easing, interpolación, asset hashes, frames o recovery. Estos conceptos no deben rellenarse por inferencia.

**Decisión:** normalizar por `frame_index` y validar secuencias contiguas; conservar segundos del Short como input histórico, no como tiempo fuente de verdad.

### R5 — Derechos y provenance

Se intentó leer `LICENSE`, `LICENSE.md`, `COPYING` en raíz y ninguno existía en esas rutas. **No puede inferirse una licencia de redistribución del código o assets por ser público**. El usuario controla ambos proyectos, pero compartir a terceros, distribuir una derivación o incorporar assets tiene requisitos distintos; revisión antes de release. La marca *Does It Automate?* y referencias de voz no son fixtures genéricos.

### R6 — Costos/recursos

Los benchmarks Chatterbox en `docs/VOICE_CLONE_CHATTERBOX.md` corresponden a **TTS**, no a FFmpeg ni video. La GPU GTX 1650 4GB disponible en esa prueba no implica que Three.js/WebGL funcione bien para 300 frames 1080x1920 simultáneamente.

## API candidate: proven vs unproven

| Capability | Evidence | Candidate reuse |
|---|---|---|
| Datos de escenas y secuencia narrativa | manifests UAT/Short inspeccionados | **YES**, normalizando schema |
| Generación WAV offline | código `app.py` + scripts | **OPTIONAL**, requiere hardening para worker/CPU |
| Scene → RGBA frames/HTML/video | no módulo/CLI verificado | **NO** |
| MP4 encoding loop | README declara uso FFmpeg; no composición versionada verificada | **UNKNOWN / RECOVER** |
| Captions SRT + mux | documentación, no API de export auditada | **UNKNOWN / RECOVER** |
| Render smoke fixtures | UAT descriptions and outputs declared, no automated MP4 regression harness inspected | **UNKNOWN** |
| Browser/UI capture | declarado en docs, sin pipeline reusable verificado | **UNKNOWN** |

## Gate de reutilización

No prometer "NINFA renderer integrated" hasta identificar en el código: entrypoint, inputs tipados, assets, licencia, output, comandos reproducibles, versions, determinismo, tests, failure behavior, resource ceiling y artifact SHA. De lo contrario, reutilizar **patrones y evidencia**, no código inexistente/ilocalizable.

## Próximo paso

Cerrar sólo el contrato para un **primer demo silente, 3 escenas, formas tipográficas originales**, bajo un `VideoRenderPortV0` separado del renderer PNG de prodAgentic. Comparar una implementación local mínima (FFmpeg + frames propios) con HyperFrames **sólo** si aparece necesidad visual que justifique otra dependencia. Ningún código de producto hasta cerrar seguridad, workers, inputs y UAT.
