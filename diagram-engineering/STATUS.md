# Diagram Engineering — estado de MK0

**Actualizado:** 2026-10-08 · **origen:** `knowledge/diagram-engineering-mk0-pilot` · **integración documental:** [PR #33](https://github.com/Em3rc0d/personal_knowledge/pull/33)

**Decisión:** **HOLD / REVIEW REQUIRED** para adoptar Diagram Engineering como estándar o cerrar MK0. El usuario autorizó explícitamente **merge documental a `main`**, conservando el carácter experimental y su evidencia limitada.

| Dimensión | Estado y evidencia válida |
|---|---|
| Fuentes/provenance | Source SHAs fijados; ver [registro](mining-site/SOURCES.md) |
| Artefactos | Tres HTML/SVG + Mermaid generados; 11/9/12 nodos |
| Integridad del grafo en GitHub | PASS estático ad hoc 3/3 en snapshot `3b3dbcdf`; ver [recibo](mk/MK0/EVIDENCE-RECEIPT-2026-10-08.md) |
| Python local (paquete v2) | 3/3 y 12/12 mutaciones rechazadas; **ZIP no idéntico al commit** |
| Chromium escritorio/móvil (paquete v2) | 6 vistas sin errores informados; **no recapturadas desde el HEAD** |
| Verificador upstream | NOT EXECUTED |
| Compilador JSON → HTML versionado | NOT IMPLEMENTED; outputs mantenidos explícitamente |
| Semántica revisada por tercero | PENDING |
| A/B comprensión | NOT EXECUTED |
| Tiempo, mantenimiento y tokens facturados | UNKNOWN |
| Change rehearsal / drift review | NOT EXECUTED |
| Gate de MK0 | HOLD / NO-GO para certificación y adopción automática; merge documental autorizado |

## Para reanudar con contexto mínimo

[README](README.md) → [matriz semántica](mk/MK0/TRACEABILITY.md) → [reproducción](mk/MK0/REPRODUCE.md) → [evidence receipt](mk/MK0/EVIDENCE-RECEIPT-2026-10-08.md) → [gate de revisión](mk/MK0/REVIEW-GATE.md).

**No se han modificado los proyectos ECHO, NINFA ni el fork de Diagram Design.** La documentación puede conservarse en `main` a solicitud del usuario, pero los SVG siguen siendo muestras no autoritativas. Cualquier cambio funcional futuro requiere nuevas evidencias y gate.
