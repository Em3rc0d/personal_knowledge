# Q-007 — PlacaClara: creatividad premium ≠ conversión certificada
Fecha: 2026-10-12 | Case: Em3rc0d/plate | Fuente: [contrato editorial](https://github.com/Em3rc0d/plate/blob/main/docs/social/SOCIAL_EDITORIAL_CONTRACT.md), [piloto / PR #8](https://github.com/Em3rc0d/plate/pull/8).
Clases: OBSERVED (artefactos y reacción del dueño); OFFICIAL (verdad de código producto), INFERRED (criterios de diseño); GENERATED (matriz propuesta).

## Contexto
Se pidió conservar la calidad de posters históricos premium de Content Seller, Logan/automotriz y PlacaClara, manteniendo CTA adaptado al embudo de cada cuenta. Una prueba Content Seller previa resultó técnicamente correcta pero visualmente inferior. El contrato PlacaClara fue formalizado después en `plate/docs/social/` y permite un solo objetivo principal DISCOVERY/EDUCATION/TRUST/COVERAGE_INTENT/PURCHASE_INTENT con CTA/KPI congruentes.

## Episodio observado
Piloto `PC-20261012-COVERAGE-DATE-001`: «Te mostraron un dato. ¿De qué fecha es?», buyer de usado, fuente/fecha/cobertura, CTA revisar cobertura en placaclara.com. El propietario pidió evitar uncanny valley; aceptó la dirección artística de una versión posterior («Me gusta mucho!»). La aceptación es cualitativa del look, NO señal de CTR/venta o confirmación de bytes publicables.
Original: 941×1672, SHA-256 `01e919fa77f437db7b6c01c2b48077495c370db89a70d16505e739360516ea73`.
Copia normalizada por escala: 1080×1920, SHA-256 `7daa15667eef5238cd208248011a5243b8b83d31ce1849f44499265a61fcf64f`.
Un escalado no resuelve el logo en zona superior ni CTA inferior en los márgenes preventivos TikTok. Ambos binarios son REFERENCIA, no release certificado. Package, manifiesto y gate audit viven en `plate/docs/social/pilots/PC-20261012-COVERAGE-DATE-001/` (rama PR #8 hasta merge). El ZIP del chat entrega la imagen, no es un recurso permanente del repositorio.

## Lecciones reutilizables
- Un formato premium necesita personaje/escena con significado, tensión real y un solo trabajo visual, pero una imagen atractiva no demuestra impacto en conversiones.
- El uso de imagen generada NO sustituye QA sobre manos/caras/gestos, plausibilidad contextual, claims, texto y logo. Personas ilustradas no son clientes.
- Contrato por marca: PlacaClara optimiza la transición a cobertura/precio informado; Content Seller tiene aprendizaje/comunidad/inbound; NINFA es un medio/productor, no editorial business owner. No propagar CTA comerciales entre marcas por analogía.
- Tres fronteras: (a) dirección creativa elegida, (b) QA del arte exacto con hash, marca, copyright/safe zones y veracidad, (c) recibo de publicación/plataforma y outcome medido. No colapsarlas.
- Tener una UI 9:16 y export 1080×1920 no prueba que esté safe for TikTok; se necesita simulación de overlay + inspección plataforma real.
- No reclamar precio/cobertura live a partir de un default en el código, ni cambiar NOT_FOUND por vehículo limpio. Atribución per-post a ventas sigue UNKNOWN.
- Novedad semántica recorre publicados/programados/aprobados/planificados; ausencia de acceso ≠ corpus vacío.
- Sin medir baseline de preparación y outcome, el piloto no valida ahorro de tiempo ni crecimiento causal.

## Estado y criterio de cierre
**DOCUMENTED**: contrato editorial de `plate`, piloto/versiones visuales, aceptación de dirección y gates declarados.
**BLOCKED**: publicación/programación por datos comerciales efectivos, historial completo, QA de logos/zona segura y signoff del PNG final.
**UNPROVEN**: conversión atribuida, incremento de seguidores, disminución de edición manual o automatización de NINFA.
No iniciar otra fase ni duplicar este paquete en personal_knowledge; aquí solo se conserva conocimiento y enlaces. Mantener artefactos operativos en el repositorio propietario.
