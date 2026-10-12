# UAT-001 — Evidencia local de transferencia social-media-skills
Fecha: 2026-10-12 | Clase: OBSERVED (ejecución local) / INFERRED (utilidad), no performance uplift.

## Fuente del experimento
- Repositorio operativo: Em3rc0d/content-seller, mk1/test/uat/uat001/README.md.
- Fuente original inspiradora: content-strategy/mining-site/S-016-social-media-skills-2026-10-12.md.
- Pieza: una infografía TikTok es-PE explicando FOREIGN KEY en SQLite; contenido visual/caption/repro generado en local, con bloqueo de publicación intacto.
- Evidencia factual independiente: https://www.sqlite.org/foreignkeys.html, sección 2, y experimento Python sqlite3 3.46.1 (OFF acepta registro huérfano, ON lo rechaza).

## Resultado demostrado
1. 5/5 tests del adaptador editorial-to-media/v1 pasaron en Python utilizando copias byte-iguales, verificadas por Git blob SHA, de validador/test/fixture de main.
2. Un borrador sin pruebas fue bloqueado. El piloto real permaneció bloqueado por cobertura de novedad parcial y human QA pendiente.
3. Se renderizó un PNG 1080×1920 en local; control geométrico: 16 regiones de texto dentro de TikTok safe bounds x50..910, y260..1420. La revisión móvil humana no se efectuó.
4. El chequeo de novedad inspeccionó seis artefactos de inventario, NO el historial completo/scheduled de TikTok; ausencia parcial de coincidencia no equivale a certificación.
5. El contrato de Shorts DoesItAutomate en NINFA exige en para contenido, narración y subtítulos. No fue ejecutado con es-PE; hacerlo requeriría contrato de canal separado. Un handoff documentado no equivale a un renderer interoperable.

## Falsabilidad / valor
- **YES**: demostró reproducibilidad de un caso y rechazo seguro de estados no autorizados sin API pagada ni Actions.
- **UNKNOWN**: reducción de minutos, tokens, correcciones por post, calidad comparada, conversiones, crecimiento y scheduling. No existe benchmark previo comparable ni revisión humana definitiva.
- **DO NOT PROMOTE** a playbook universal, contrato A3, integración NINFA activa ni regla de éxito de crecimiento. No se declara GO público o autopost.
- **NEXT EVIDENCE**: comparación controlada temporal sobre briefs equivalentes, revisión móvil por owner, historial real contra queue scheduled y un adapter/scene contract específico para español si el formato video realmente lo requiere.

Conserva la distinción KNOWLEDGE PATTERN / STRUCTURAL TEST / REAL MEDIA / HUMAN RELEASE / EXTERNAL OUTCOME. El repositorio de conocimiento no debe sustituir el ledger de operaciones.
