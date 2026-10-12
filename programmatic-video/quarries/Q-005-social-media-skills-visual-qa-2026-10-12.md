# Q-005 — Social skills para QA audiovisual sin nuevas APIs
Fecha: 2026-10-12 | Provenance: INSPIRED / GENERATED | Fuente primaria: CS-SRC-016

## Enlace a la evidencia
https://github.com/charlie947/social-media-skills/tree/8cefb5b6d03757885faa6918bd8bfaef202a83db
Revisados: graphic-designer, gemini-carousel, gemini-infographic, reels-scripting, youtube-thumbnail, analytics-dashboard.
MIT, copyright Charlie Hills 2026. La presente nota abstrae procedimientos; no replica arte o prompts extensos.

## Patrones transferibles
- Representar estados de output diferenciados: script, storyboard, prompt-ready, render-pending, rendered, visually-reviewed, approved-for-export, scheduled, published. Nunca inferir un estado a partir del anterior.
- Renderizar donde sea posible en local con source reproducible (HTML/SVG/FFmpeg), y comprobar píxeles exportados en full size + tamaño real de feed; cada slide debe aprobar por separado.
- Narración y escenas deben contar una transformación real. Un motion dinámico pero falso no es un resultado.
- Un clip tomado de un experimento mayor debe aportar una lección nueva, no sólo cambiar el título/ángulo superficialmente.
- Thumbnail y hook prometen sólo resultados ya confirmados por el experimento, con excepción de hipótesis claramente marcadas.
- Analítica de medios mantiene ventanas, denominadores, origen, cohortes y objetivos separados; no convertir likes/CTR en ventas.

## Límites
- NINFA ya tiene Brand Identity v1, shorts-motion schema para DoesItAutomate en inglés y gates humanos. No sobrescribirlos.
- Locale es-PE y safe zones de TikTok no pueden pasar por las reglas inglesas de Shorts.
- No inferir editabilidad a partir de un bitmap; no proclamar calidad a partir de un prompt.
- Sin claves de proveedores, Apify, Gemini de pago ni CI de render por defecto.
- Derechos y assets externos deben verificarse por pieza; licencia MIT de una skill no licencia contenido de terceros.

## Validación pendiente
Casos adversariales: resultado aún no ejecutado, fuente ausente, caption cortado por UI, video mudo disfrazado de narrado, voz degradada por DSP, miniatura no renderizada, activos/licencias desconocidos, publicación sin receipt. Observaciones de una sola renderización no bastan para declarar un generador universal.
