# S-016 — Social Media Skills (Charlie Hills)
Captura: 2026-10-12
Source ID: CS-SRC-016
Clases: OBSERVED (estructura, instrucciones, código de tests), INSPIRED (patrones derivados)

## Identidad de fuente
- Original: https://github.com/charlie947/social-media-skills
- Fork: https://github.com/Em3rc0d/social-media-skills
- Git commit/tree main observado: 8cefb5b6d03757885faa6918bd8bfaef202a83db
- Versión documentada 1.1.0 (VERSIONS.md, 2026-09-15)
- 17 skills; .claude-plugin/marketplace.json, README, CONTRIBUTING, validate-skills.sh, tests/test-codex-portability.py.
- Licencia MIT; copyright (c) 2026 Charlie Hills; conservar notice correspondiente para reutilizaciones.
- El fork y upstream coincidían en el mismo commit durante la consulta; no reclamar mejoras propias en el fork.

## Qué se verificó
1. 17 archivos SKILL.md y referencias puntuales: identidad, contenido LinkedIn, hooks, matriz, investigación, scraping opcional, visuales, Reels, thumbnails, scoring y dashboards.
2. Tests de portabilidad estructural y copia no destructiva; test opcional para descubrimiento local Codex. No equivale a QA audiovisual ni a proveedor realmente activado.
3. Rutas visuales HTML/CSS exportables frente a prompts Gemini. Un prompt no representa píxeles inspeccionados.
4. Falta de sistema operativo de publicación completo, deduplicación de historial global y contrato JSON interoperable entre skills.
5. Reels-scripting menciona @google/generative-ai y actores Apify: dependencia específica que debe revalidarse antes de integrar. No activar credenciales, scraping de comentarios o API de pago por la presencia del procedimiento.

## Confianza y límites
- ALTA: estructura y texto de los 17 archivos consultados.
- MEDIA: transferibilidad de sus reglas a distintos perfiles (inferencia arquitectónica, no test de resultados).
- NO PROBADO: mejora causal del engagement, aumento de ventas, calidad de generación, compatibilidad live y publicación programada.
- El material público es una biblioteca de instrucciones. No incluir claves, configuraciones privadas ni nombres/métricas del autor como defaults del usuario.

## Extracción normativa
Patrones aptos para evaluación:
- onboarding con muestras auténticas, perfil de voz versionado, prohibición de first-person invented;
- investigación fechada con cobertura explícita;
- ideación pilar × formato como fuente de candidatos, no obligación de publicar;
- copy/hook ligado a público, evidencia y objetivo, no clickbait libre;
- briefs de piezas/diapositivas y revisión de render real;
- scoring separado entre juicio editorial e historial real, no pronóstico;
- contrato de estado DRAFT/PROMPT_READY/RENDER_UNREVIEWED/HUMAN_REVIEWED;
- gating humano y receipts externos para cualquier acción sobre plataformas.

Transferencia a los repositorios operativos:
- Content Seller: mk1/integration/SOCIAL_SKILLS_TRANSFER_2026-10-12.md (contrato adapter no autoritativo + preflight estructural).
- NINFA: docs/contracts/SOCIAL_SKILLS_MEDIA_ADAPTER_2026-10-12.md (consumo de brief, ejecución media y QA; sin changes al runtime).
- Knowledge: content-strategy/quarries/Q-006-social-media-skills-transfer-2026-10-12.md, programmatic-video/quarries/Q-005-social-media-skills-visual-qa-2026-10-12.md.

## Anti-corrupción
La transferencia sólo añade reglas cuando faltan. No sustituye los ledgers existentes, los contratos de publicación específicos, la certificación de A3 o los gates de NINFA. Una herramienta externa no adquiere autoridad por estar documentada.
