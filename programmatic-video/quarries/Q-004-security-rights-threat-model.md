# Q-004 — Threat model y derechos para render HTML/JS

Estado: **GENERATED / REVIEW REQUIRED**, aún no probado.
Fecha: 2026-10-07 America/Lima.
Fuentes primarias: https://playwright.dev/docs/api/class-browsercontext ; https://playwright.dev/docs/network ; https://github.com/heygen-com/hyperframes/blob/main/SECURITY.md ; https://github.com/heygen-com/hyperframes/blob/main/LICENSE ; https://github.com/remotion-dev/remotion/blob/main/LICENSE.md .

## Trust boundary

Una escena HTML/JS generada por agente es **código no confiable** aunque parezca una animación inofensiva. Puede abrir conexiones, leer datos accesibles al proceso, invocar runtime side effects indirectos o agotar memoria/CPU. Un browser headless **no sustituye** aislamiento del sistema operativo. La seguridad se evalúa en dos niveles: permisos del proceso/contendor y restricción de navegador; ninguno debe presentarse como garantía universal.

```text
untrusted brief/source/prompt
  -> static inspect + licensed asset intake
  -> isolated non-privileged render worker (no secrets)
  -> browser context with offline/block external network
  -> restricted FFmpeg encoder
  -> artifacts allowlist (MP4, thumbnails, evidence)
  -> ffprobe + human review
```

## Contrato de aislamiento (precondición de cualquier render)

| Vector | Medida exigida | Evidencia que falta |
|---|---|---|
| Exfiltración HTTP/fetch/WebSocket | network namespace sin egress por defecto; bloquear Service Workers; interceptar solicitudes del navegador para diagnóstico | configuración real + prueba de conexión fallida |
| Lectura de `.env`, tokens, home, SSH | proceso sin secretos, `HOME` temporal vacío, FS de entrada read-only y workdir aislado | mount map + env redacted |
| Host break-out / comandos del sistema | sin root, sin Docker socket, sin host mounts sensibles, sin privilegios extras | perfil contenedor + negative test |
| Recurso agotado | timeouts, `memory`, `cpus`, `pids`, límite de salida y cleanup | logs de límites durante carga adversa |
| Dependencies / supply chain | versiones/lockfile pinneados; evitar CDN durante runtime; inspección de paquetes | manifest y hashes |
| Browser/device | Chromium/headless version pinneada; no apertura de puertos públicos; gestión de WebGL/llvmpipe | `doctor` + smoke test |
| Encoding | FFmpeg versión/flags documentados; input/local files allowlist, no URL network fetch | argv sanitized + ffprobe output |
| Fonts and audio | font con licencia y hash; audio generado/propio o uso explícitamente permitido | assets manifest |
| Artifacts | writer restringido a directorio de output; no subida ni publicación automática | lista de archivos y checksum |
| Fail-closed | asset no encontrado, llamada externa o codec ausente -> error, no éxito ficticio | 1+ prueba negativa |

## Punto crítico: Playwright route no basta

La documentación de Playwright explica que `browserContext.route()` puede interceptar requests, pero **no** necesariamente las solicitudes interceptadas por Service Workers; recomienda `serviceWorkers: 'block'` para esas pruebas. La defensa primaria contra exfiltración es **restricción de red a nivel del proceso/contenedor**, no sólo JS/interception. Ver: https://playwright.dev/docs/api/class-browsercontext#browser-context-route

Un contenedor con `--network none` es candidato para la prueba offline, pero **su disponibilidad/seguridad/compatibilidad real queda UNTESTED**; no agregarlo en producción sin revisar capacidad de fonts/browser/FFmpeg.

## Derecho de uso (target de experimentos)

Los tres experimentos usarán **contenido sintético original**: tipografía/licencias verificadas, formas SVG propias, primitivas geométricas y audio omitido por defecto. No se copiarán clips originales, voz, pistas musicales, personajes, logotipos ni vídeos de Skillry/X. No se incorporarán prompts de terceros como código ejecutable.

| Origen | Uso inicial | Estado |
|---|---|---|
| Shapes, escenas, guiones originales | permitido en pruebas internas; registrar authorship/revisión | `DESIGNED`, todavía no construido |
| Fonts instaladas en host | prohibido asumir permiso de redistribución | `UNKNOWN` |
| Música / efectos de terceros | excluidos en los tres tests | `OUT_OF_SCOPE` |
| Previews, remakes, videos de X | enlaces de referencia únicamente | `NOT_LICENSED_FOR_REUSE` |
| HyperFrames source | Apache-2.0 visible en el repositorio; respetar notices/dependencies | `DOCUMENTED`, review de release pendiente |
| Remotion source | Free/Company License con condiciones de elegibilidad | `DOCUMENTED`, revisión concreta pendiente |

## Revisión comercial

Tener un render «sin API por créditos» no elimina costo de hardware, energía, almacenamiento o mantenimiento. Los renders locales bajo estudio no prueban que operar una Video Factory sea rentable. Aún no existen benchmark, instalación ni MP4, por lo que los requisitos de aislamiento figuran como **planned**, nunca `PASS`.

## Criterio de pase de seguridad

`PASS` sólo después de evidencia observable: proceso sin secretos, sin egress externo, limits efectivos, zero unsafe mounts, dependencias pinneadas, negativa de conexión demostrada, salida/errores verificables y revisión de derechos de assets. Antes de eso: **OPEN / BLOCKED**.
