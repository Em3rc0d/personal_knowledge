# MK0 — Reproducir los checks localmente

Revisión 2026-10-08. Objetivo: reproducir la **validación declarativa y estructural**, no afirmar certificación operativa ni crear pipelines nuevos.

## Entradas exactas

- Repositorio: `Em3rc0d/personal_knowledge`; rama `knowledge/diagram-engineering-mk0-pilot`.
- Versión de referencia de esta documentación: `3b3dbcdfd8b837c5128e50308142f67c1cf5e477` (los commits posteriores son nuevas revisiones; consultar `STATUS.md`).
- Casos: `mk/MK0/outputs/{echo,ninfa,knowledge}.html`.
- Contratos: `graph_contract.json` y `layout_spec_v2.json`.
- Dependencias básicas: **Python 3.10+**, estándar de Python. No requiere API, backend, paquetes de pago ni servicios en la nube.

## Comandos desde la raíz de un checkout

```bash
git switch knowledge/diagram-engineering-mk0-pilot
python3 diagram-engineering/mk/MK0/verify_pilot.py
python3 diagram-engineering/mk/MK0/test_adversarial.py
```

El primer comando audita estructura SVG, endpoint IDs, tipos, rutas ortogonales, extremos de conectores, cruces con nodos no participantes, alternativa textual, accesibilidad básica, formato, fuente fijada, algunos controles de seguridad y un contraste de referencia. El segundo ensaya 12 mutaciones deliberadas **sobre ECHO**, no 12 por cada diagrama.

Una salida `PASS` confirma solo ese contrato. **No** significa que se hayan ejecutado las suites del upstream, que una fuente sea correcta o que un usuario haya comprendido el diagrama.

## Revisión en navegador, no automatizada por Git

Abrir cada `outputs/*.html` en Chromium (o navegador equivalente) y comprobar por separado:

- Escritorio de referencia: 1440 px. Móvil de referencia: 390 px.
- Que no se recorte texto/etiquetas en rectángulos y enlaces; inspeccionar conectores y leyendas.
- Que el body no crezca horizontalmente; el contenedor **sí** desplaza horizontalmente en móvil y muestra una pista visible.
- En móvil, arrastrar hasta el extremo derecho; con teclado, enfocar la región y recorrerla.
- Abrir el detalle de texto y comprobar todas las relaciones contra la vista SVG.
- Verificar intersecciones, solapamientos y legibilidad real en pantalla/zoom, no solo métricas de DOM.

En un entorno local con Chromium disponible, una captura básica se puede generar, de forma **opcional**, por ejemplo:

```bash
chromium --headless --disable-gpu --no-sandbox --window-size=1440,1100 \
  --screenshot=/tmp/echo-desktop.png \
  "file://$(pwd)/diagram-engineering/mk/MK0/outputs/echo.html"
```

Las dimensiones de una captura básica pueden diferir de un test automatizado de página completa. El script experimental externo usado para las capturas históricas **no está versionado aquí**. Por tanto no se ofrece un comando fingidamente reproducible que regenere dichas métricas en este commit.

## Reproducibilidad y cambios

El repositorio contiene HTML/SVG, el contrato de nodos y un `layout_spec_v2.json` declarativo, **pero NO incluye actualmente un renderizador versionado y portátil que regenere automáticamente el HTML desde el layout**. Tampoco se debe ejecutar el `build.mjs` de un ZIP experimental como fuente autoritativa: tenía rutas absolutas de un entorno temporal y no fue incorporado al PR.

La regla presente es **sincronización explícita y revisión manual**; no existe una compilación `source → HTML` certificada. Si se automatiza, hacerlo en un MK posterior con fixture/golden, diff y source provenance. Evitar GitHub Actions: ejecutar los tests localmente.

**Fallo esperado:** si cualquier test falla, detener promoción; conservar logs, la fuente fijada y el diff, sin reparar automáticamente basándose solo en la imagen.
