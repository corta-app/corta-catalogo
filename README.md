# Catálogo de Corta

Efectos y filtros que [Corta](https://github.com/corta-app/corta) descarga gratis, ordenados por categoría. Sin servidores: la app lee
estos archivos directo desde GitHub y **solo acepta datos JSON** que pasan la misma validación que este repo (nunca código).
*(English below.)*

## Qué hay

| Carpeta | Contenido |
|---|---|
| `efectos/<categoria>/<id>.json` | Un archivo por efecto. Categorías: `filtro`, `color`, `movimiento` y `transicion`. |
| `efectos/index.json` | El índice que lee la app: cada efecto con su huella SHA-256 y su tamaño (se genera, no se edita a mano). |
| `herramientas/efecto_formato.py` | El formato y su validación: **el mismo archivo** que usa la app (`corta/bin/efecto_formato.py`). |
| `herramientas/generar_indice.py` | Valida todos los efectos y regenera el índice. |

## Crear un efecto (sin programar)

Un efecto es una lista corta de **pasos** con números. Por ejemplo, «Cálido»:

```json
{
 "formato": 1,
 "id": "calido",
 "categoria": "color",
 "nombre": {"es": "Cálido", "en": "Warm"},
 "descripcion": {"es": "Tonos dorados, como al atardecer.", "en": "Golden tones, like a sunset."},
 "autor": "tu-usuario",
 "etiquetas": ["atardecer", "sunset"],
 "pasos": [{"tipo": "color", "saturacion": 1.15, "sepia": 0.12}, {"tipo": "tinte", "color": "#FF8A2A", "fuerza": 0.1}]
}
```

| Paso (`tipo`) | Campos (rangos) |
|---|---|
| `color` | `brillo` 0,5–1,5 · `contraste` 0,5–2 · `saturacion` 0–2 · `tono` −180–180 · `sepia` 0–1 · `grises` 0–1 |
| `tinte` | `color` `#RRGGBB` · `fuerza` 0,02–0,5 |
| `desenfoque` | `radio` 0,5–20 |
| `vineta` | `fuerza` 0,1–1 |
| `zoom` | `desde`, `hasta` 1–1,6 · `curva` `lineal`, `suave` o `golpe` |
| `fundido` | `entrada`, `salida` 0–3 (segundos) · `color` `negro` o `blanco` |
| `transicion` | `duracion` 0,1–1,5 (segundos) · `color` `negro` o `blanco` |

1. **Pruébalo en Corta:** guarda tu archivo en `~/Corta/.corta/efectos/<id>.json` y ábrelo en la pestaña Efectos con un video tuyo.
2. **Compártelo:** abre un [issue «Proponer un efecto»](https://github.com/corta-app/corta-catalogo/issues/new?template=efecto.yml) y
   pega el JSON (lo sumamos por ti), o abre un pull request con `efectos/<categoria>/<id>.json` después de correr
   `python3 herramientas/generar_indice.py`.

Más detalle en [CONTRIBUTING.md](CONTRIBUTING.md). Todo aporte lo revisa una persona antes de entrar.

🔒 ¿Una falla de seguridad? Avísanos en privado: [SECURITY.md](SECURITY.md).

---

## English

**Corta's community catalog:** free effects and filters that the [Corta](https://github.com/corta-app/corta) video editor downloads,
sorted by category (`filtro` filters, `color`, `movimiento` motion, `transicion` transitions). Each effect is a **data-only JSON** file:
a short list of steps (color, tint, blur, vignette, zoom, fade, transition) with numbers in known ranges. The app builds the preview
(CSS filters) and the export (a whitelist of ffmpeg filters) from those numbers, so no effect can ever run code.

**Make one without coding:** copy an effect, change its `id`, names and numbers, try it in Corta by saving it to
`~/Corta/.corta/efectos/<id>.json`, then share it by opening a ["Propose an effect" issue](https://github.com/corta-app/corta-catalogo/issues/new?template=efecto.yml)
with the JSON, or a pull request after running `python3 herramientas/generar_indice.py`. A maintainer reviews every contribution.
Security issues: please report them privately ([SECURITY.md](SECURITY.md)).
