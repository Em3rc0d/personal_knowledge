# Q-002 — Landscape inicial de renderizado programático

Status: **QUARRY_ONLY**. Revisión de documentación, no benchmark.
Observed: 2026-10-07 America/Lima.
Sources: `SRC-PV-002` a `SRC-PV-005` en [SOURCES](../mining-site/SOURCES.md).

## Problema técnico

HTML, Canvas, SVG y Three.js crean escenas o animaciones. Para declarar `video produced` hace falta **control de tiempo/frame, captura, encoding, audio/mux, validación de output** y evidencia de coste. Una reproducción en navegador no garantiza MP4 reproducible.

## Comparación preliminar

| Candidato | Superficie documentada | Ventaja teórica | Riesgo / límite | Estado |
|---|---|---|---|---|
| HTML/CSS/JS + captura DIY | Web APIs (Canvas captureStream); encoder por integrar | mínima dependencia de framework | tiempo real ≠ frame-seek determinista, audio/mux/browser | CANDIDATE, NO BENCHMARK |
| HyperFrames | HTML + seekable animations + Chrome/FFmpeg + CLI | encaja con conocimientos frontend y autoría agentic | madurez/versiones, sandbox, headless GPU, APIs cambiantes | CANDIDATE, NO BENCHMARK |
| Remotion | composiciones React/JS + CLI render | timeline/frame composition y props parametrizables | runtime React y licencia condicionada al tipo/tamaño de entidad | CANDIDATE, NO BENCHMARK |

## Fuentes primarias inspeccionadas

- [HyperFrames README, HeyGen](https://github.com/heygen-com/hyperframes): proyecto declara composición HTML/CSS/JS, seekable animations, browser capture, FFmpeg y licencia Apache-2.0. `OFFICIAL` sobre documentación; **determinismo real no medido**.
- [Remotion CLI render](https://www.remotiondocs.com/docs/cli/render): especifica `npx remotion render` y parámetros de dimensión, duración, FPS y props. `OFFICIAL`; salida real no probada.
- [Remotion LICENSE.md](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md): licencia dual con elegibilidad para Free y Company License; no asumir que "open source" implica libre reutilización irrestricta para empresa/servicio.
- [MDN canvas captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream): captura en tiempo real mediante `MediaStream`; no resolver por sí solo determinismo, mix de audio ni MP4.
- [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html): documenta filtrado/escala; disponibilidad de H.264, versiones de FFmpeg y duración de proceso deben verificarse en el entorno.

## Hipótesis de selección (INFERRED)

**Primera prueba recomendada:** HyperFrames, condicionada a una revisión rápida de instalación, licencia, seguridad y un render mínimo; si falla por entorno/API, evaluar Remotion y luego un fallback Canvas+FFmpeg aislado.

No es una decisión de plataforma. La elección definitiva requiere medir:

- tiempo de cold start y render por 300 frames;
- CPU máximo, RAM pico, soporte headless / GPU;
- consistencia por frame entre 2 renders de la misma composición;
- legibilidad, calidad de anti-aliasing, tipografía, color y audio;
- dependencias externas, llamadas a red, licencia real según uso;
- retry/failure paths y exportación de un MP4 utilizable.

## Riesgos no funcionales

- Animación basada sólo en `requestAnimationFrame` / reloj real puede romper `seek` arbitrario.
- JS generado externamente no debe ejecutarse con acceso a secretos ni a red abierta.
- No consumir audio/video de terceros sin derechos; no descargar desde posts X automáticamente.
- Dependencias CDN no fijadas rompen un pipeline reproducible/offline.
- FFmpeg no implica costo variable de API, pero sí coste de electricidad, CPU, almacenamiento y mantenimiento.

## Decisión provisional

`ADOPT_FOR_SANDBOX_REVIEW` HyperFrames; `KEEP_AS_ALTERNATIVE` Remotion; `DO_NOT_BUILD_A_RENDERING_PLATFORM` en MK0. Esta decisión expira si falla licencia, seguridad o verificación del ejecutable.
