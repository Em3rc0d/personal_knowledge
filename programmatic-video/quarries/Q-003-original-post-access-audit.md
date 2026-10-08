# Q-003 — Muestreo estratificado de originales y límites de acceso

Estado: **QUARRY_ONLY / PARTIAL ACCESS / ORIGINAL NOT VERIFIED**.
Fecha de observación: 2026-10-07 America/Lima.
Fuente catalogada: `SRC-PV-001` fijada al SHA `756290289742535eb0ac3817548f152e9759cc70`.

## Pregunta

¿Podemos confirmar que el texto catalogado es el prompt compartido por el autor, completo y relacionado con el material audiovisual que se atribuye a Opus 5.5?

## Diseño de la muestra

La unidad de muestreo es el **registro** y no el prompt único. Se eligieron ocho registros de `data/videos.json`: una entrada `prompt_partial=false` y una `prompt_partial=true` por categoría, mediante orden lexicográfico de `slug` para reducir selección por impacto visual. El muestreo no es aleatorio ni prueba representatividad de los 513.

| Categoría | `prompt_partial` | Registro | Post original | Inspección directa |
|---|---|---|---|---|
| motion | false | `0xevinho-436195` | https://x.com/0xEvinho/status/2103212966703436195 | BLOCKED: fetch deshabilitado |
| motion | true | `0xrapzz-433554` | https://x.com/0xRapzz/status/2106062139920433554 | BLOCKED: fetch deshabilitado |
| explainer | false | `0xnfrith-068999` | https://x.com/0xnfrith/status/2103358957050068999 | BLOCKED: fetch deshabilitado |
| explainer | true | `konstantinsaifo-501736` | https://x.com/konstantinsaifo/status/2104094723887501736 | BLOCKED: HTTP 403 |
| interactive | false | `0xchuckstock-879327` | https://x.com/0xChuckstock/status/2103804606794879327 | BLOCKED: fetch deshabilitado |
| interactive | true | `0xpai-eth-635565` | https://x.com/0xpai_eth/status/2103870009877635565 | BLOCKED: fetch deshabilitado |
| 3d | false | `alexalbert-274839` | https://x.com/alexalbert__/status/2102466523164274839 | BLOCKED: HTTP 403 |
| 3d | true | `0xsolty-735200` | https://x.com/0xSolty/status/2102888414219735200 | BLOCKED: fetch deshabilitado |

**Resultado observado:** 0/8 publicaciones originales inspeccionadas; 8/8 con identidad/URL visible en el catálogo; el contenido mostrado en este dominio proviene de fuente secundaria. `BLOCKED` es estado de acceso, **no** señal de que los posts no existan.

## Corroboración secundaria limitada

- Página Skillry de `0xchuckstock-879327`: https://skillry.dev/ai-videos/opus-5-5/0xchuckstock-879327 ; muestra el mismo texto breve de juego 3D, etiquetas Three.js/GLSL/Playable y referencias «Original» y «Remake». Esto **verifica consistencia entre superficies del mismo catálogo**, no contenido original de X.
- Página Skillry de `0xsolty-735200`: https://skillry.dev/ai-videos/opus-5-5/0xsolty-735200 ; señala explícitamente «The author shared part of the prompt» y reproduce una descripción de planeta programático, no un prompt operativo completo.

**No existe aquí inspección del video fuente, del workspace del autor, del historial de iteraciones ni de assets.** El código de reproducción tampoco fue ejecutado. Las fuentes secundarias comparten procedencia editorial y no cuentan como confirmación independiente.

## Clasificación epistemológica

| Claim | Clase | Estado |
|---|---|---|
| El JSON contiene las URLs y cadenas incluidas | OBSERVED | VERIFIED para el archivo fijado |
| El catálogo etiqueta 4 categorías y parciales | OBSERVED | VERIFIED para el archivo fijado |
| Skillry presenta enlaces «Original» y «Remake» | OBSERVED (secondary) | VERIFIED para páginas inspeccionadas |
| El creador usó exactamente ese prompt | EXTERNAL ATTRIBUTION | UNVERIFIED |
| El texto marcado `false` es íntegro | ASSUMPTION | UNVERIFIED |
| Resultado generado exclusivamente con Opus 5.5 | EXTERNAL ATTRIBUTION | UNVERIFIED |
| Cada caso es reproducible | HYPOTHESIS | UNTESTED |

## Decisión

`NO_PROMOTION` de evidencia de autoría ni de equivalencia visual. Preservar el catálogo como **source-discovery** mientras no haya inspección directa o evidencia aportada por creador. El bloqueo de X no se resolverá recurriendo a copias no autorizadas ni tratando previews como posts originales.

## Follow-up admitido

- Revisión humana de URL en navegador/sesión autorizada y recibo mínimo con fecha, extracto autorizado, autor, contexto, captura y discrepancias.
- Si los originales siguen inaccesibles, pasar a experimentos con brief, assets y código originales, sin presentar el dataset como benchmark de Opus 5.5.
