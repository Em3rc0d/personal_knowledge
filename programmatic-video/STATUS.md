# Programmatic Video — Status

Updated: 2026-10-07 (America/Lima)
Review: [MK0 closure](mk/MK0/CLOSURE.md) — **PASS WITH LIMITATIONS** for bounded discovery ONLY.

## Estado canónico

| Superficie | Estado |
|---|---|
| MK0 Mine & Frame | CLOSED WITH LIMITATIONS: seed catalog = discovery, not verified benchmark |
| MK1 Normalize & Classify | IN PROGRESS / FIRST 8 FIXTURES MAPPED |
| MK2 Operationalize | BLOCKED BY MK1 |
| MK3 Integrate | BLOCKED |
| MK4 Automate | BLOCKED |
| MK5+ Certify | BLOCKED |
| Fuente seed | SHA pinneado, JSON inspeccionado, atribución de originales UNVERIFIED |
| Originales X | 8 intentados / 0 inspeccionados, BLOCKED |
| Runtime renderer | CANDIDATES ONLY; HyperFrames y Remotion, sin instalación |
| Sandbox ejecutable | Limited trusted-data execution tested; OS no-egress/secret isolation NOT CERTIFIED |
| Prototipo / MP4 | PV-POC-001 deterministic silent baseline; PV-POC-003 GH Actions neural WAV+MP4 success; original animation remux H264/AAC PASS; prodAgentic integration NOT DONE |
| Auditoría de integración NINFA/prodAgentic | Q-005 + Q-006 CAPTURED / video renderer not verified, TTS source inspected |
| Video handoff proposal | MK1 candidate + ADR-001 / product build NOT AUTHORIZED; [Q-007](quarries/Q-007-pv-poc-001-local-proof.md) is evidence of narrow local export only |
| Coste y calidad audiovisual | PV-POC-002 eSpeak robotic rejected for target quality; PV-POC-003 Piper CI audio/video PASS (no paid TTS API), human naturalness NOT EVALUATED; see [Q-008](quarries/Q-008-piper-spanish-voice-poc.md) |
| Content Seller / Ninfa | UNCHANGED; integration BLOCKED |

## MK0 — GATES

- [x] Responsabilidad y exclusiones de dominio.
- [x] Identidad y commit de fuente fijados.
- [x] Auditoría del dataset, sesgos, duplicados y límites.
- [x] Intento de corroboración estratificada: fuente original **BLOCKED**, sin elevar claims de autoría.
- [x] Excluir medios/prompts de terceros de reproducción hasta verificar derechos.
- [x] Security threat model y condiciones fail-closed definidas.
- [x] Fuentes primarias de render, licensing y frame/seek semántica documentadas.
- [x] Contratos de experimento definidos ANTES de crear código.
- [x] Review claims→evidence; cierre formal con límites explícitos.

El cierre MK0 **no** resuelve el bloqueo de X ni valida atributos del video original: esos claims quedan fuera del conocimiento promovido.

## Handoff a MK1 (IN PROGRESS, cierre pendiente)

- [x] Definir taxonomía/contrato inicial de provenance (ver `mk/MK1/TAXONOMY.md`).
- [x] Distinguir ID de registro, clustering textual y familia semántica; dedup semántica real aún pendiente.
- [x] Definir campos de técnica y derechos, defaults `UNKNOWN`; 8 fixtures trazados (ver `mk/MK1/NORMALIZATION-RECEIPT.md`).
- [ ] Evaluar 24+ registros y casos negativos, sin importar prompts completos.
- [ ] Validar reglas del contrato en los 513 registros y revisión independiente.
- [ ] Completar revisión MK1 antes de contratos operativos MK2.

## Preflight de producto e integración (permanece BLOCKED; sandbox synthetic POC separately passed output only)

- [ ] Resolver stack/versiones, CPU/GPU/RAM/OS del equipo ejecutor.
- [ ] Confirmar sandbox OS-level, no egress/no secrets, timeout/restricciones verificadas.
- [ ] Validar licencias de dependencias, fonts y assets concretos.
- [ ] Validar seek por frame y export con pruebas negativas.
- [ ] Registrar costo y benchmark en equipo real.

**No coding/rendering until the engineering graph for the chosen experiment is closed.**
