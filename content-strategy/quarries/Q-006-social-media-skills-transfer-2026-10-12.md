# Q-006 — Skills editoriales como patrones, no dependencia
Fecha: 2026-10-12 | Fuente: CS-SRC-016 | Estado: DESTILADO / NO CERTIFICADO COMO MEJORA EMPÍRICA

## Pregunta
¿Qué ideas de social-media-skills elevan la producción de Content Seller y NINFA sin fragmentar la arquitectura, aumentar tokens/costo recurrente o debilitar veracidad/novelty?

## Clasificación completa (17)
| Skill | Extracción | Destino / decisión |
|---|---|---|
| voice-builder | voice samples reales + ausencia provisional | Content Seller profile/voice, ADOPTAR PATRÓN |
| newsletter-voice | variación por medio | REFERENCIA, sólo si newsletter justifica |
| profile-optimizer | propuesta de perfil con hechos confirmados | REFERENCIA LinkedIn |
| post-writer | voice + research + approve | ADAPTAR a brief existente |
| graphic-designer | HTML editable vs prompt, inspect PNG | ADOPTAR patrón a visual QA |
| post-scorer | historial vs evaluación editorial | ADAPTAR; no usar 1-10 como predicción |
| reels-scripting | ingeniería inversa del mecanismo, guion original | ADAPTAR NINFA; NO copiar scraping/SDK |
| youtube-thumbnail | promesa verificable + lectura mobile | ADAPTAR NINFA y no inventar resultados |
| pinned-comment | humor visual y voz | REFERENCIA, no default |
| hook-generator | seis ángulos candidatos sin cifras inventadas | ADAPTAR a nuestro hook gate |
| post-formatter | PAS/AIDA/BAB/STAR/SLAY | REFERENCIA; no rigidez global |
| content-matrix | pilar × ocho formatos | ADOPTAR sólo como brainstorming, novelty antes de producción |
| niche-research | 7 días, origen fechado, cobertura | ADOPTAR con fuentes multifuente y alcance |
| gemini-infographic | brief de estructura y revisión | REFERENCIA, sin Gemini obligatorio |
| gemini-carousel | una idea por slide, aprobación de brief | ADOPTAR patrón, cada slide inspeccionado |
| quote-post | frase original + imagen | REFERENCIA, no sustituye prueba real |
| analytics-dashboard | export, denominadores, ventanas | ADAPTAR a snapshots y outcomes existentes |

## Hallazgos
- **OBSERVED**: prompts y checklists detallados, pero no orquestación transaccional ni scheduling probado.
- **INFERRED**: reutilizar reglas concisas como políticas vinculadas a un contrato JSON reduce relectura y conflicto entre agentes; ahorro de tokens NO MEDIDO.
- **GENERATED**: adapter editorial-to-media/v1 opcional, no nueva fuente de verdad.
- **REJECTED**: copiar las 17 skills completas, imponer inglés británico en es-PE, cargar arquetipos ajenos como autobiografía, 4×N publicaciones por cuota, aumentar dependencia de Apify/Gemini.
- **RISK**: Apify puede devolver datos fuera del alcance deseado; prohibir scraping de comentarios por configuración efectiva, no sólo por instrucciones.
- **RISK**: evaluar desempeño con reacciones + 3×comentarios confunde exposición/objetivo; separar orgánico, paid, cohortes, ventanas y eventos comerciales.
- **RISK**: crear teaser o thumbnail basado en un resultado aún no observado fabrica prueba.

## Encaje en el sistema existente
Content Seller sigue decidiendo QUÉ/QUIÉN/POR QUÉ y tiene autoridad sobre topic bank, fuentes, historial y novelty. NINFA produce multimedia con su propia marca/audio/QA. prodAgentic conserva coordinación, aprobación, publicación y reconciliación. personal_knowledge conserva patrones y procedencia, no datos operativos que dupliquen sus ledgers.

## Gates verificables sugeridos
1. G-ID: profile_id y locale coinciden con el canal seleccionado; cambios de cuenta no contaminan assets.
2. G-NOV: tema, angle, hook, lesson, example, structure, visual_pattern, CTA comprobados frente a corpus e inventario programado.
3. G-EVID: claims verificados y vacíos declarados, ninguna experiencia ficticia.
4. G-VIS: safe zones + legibilidad móvil + copia exacta en PNG/MP4 realmente revisado.
5. G-RELEASE: aprobación humana y receipts externos independientes; ninguna puntuación editorial autoriza publicar.
6. G-LEARN: posterior medición con muestras comparables; una victoria aislada no promueve una regla.

## Experimento y evidencia faltante
Comparar 3–5 briefs reales con el método previo y la transferencia; medir correcciones humanas, colisiones semánticas, tasa de fixtures rechazadas, defectos visuales y costo/tiempo; no inventar uplift. Sin este experimento no proclamar que el nuevo adapter aumenta conversión ni autonomía.

## Criterio de cierre
Extracción conceptual **registrada**; integración operativa completa **no demostrada**; A3/prodAgentic no recertificados. Reabrir sólo si un caso real muestra un gap no cubierto, con nueva evidencia y baseline.
