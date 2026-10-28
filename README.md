# Catálogo de Corta

Efectos, filtros y **plantillas** que [Corta](https://github.com/corta-app/corta) descarga gratis, ordenados por categoría. Sin
servidores: la app lee estos archivos directo desde GitHub y **solo acepta datos JSON** que pasan la misma validación que este repo
(nunca código). *(English below.)*

## Qué hay

| Carpeta | Contenido |
|---|---|
| `efectos/<categoria>/<id>.json` | Un archivo por efecto. Categorías: `filtro`, `color`, `movimiento` y `transicion`. |
| `plantillas/<categoria>/<id>.json` | Un archivo por plantilla. Categorías: `negocios`, `presentacion`, `recuerdos`, `tutorial` y `celebracion`. |
| `efectos/index.json`, `plantillas/index.json` | Los índices que lee la app: cada archivo con su huella SHA-256 y su tamaño (se generan, no se editan a mano). |
| `herramientas/efecto_formato.py`, `herramientas/plantilla_formato.py` | Los formatos y su validación: **los mismos archivos** que usa la app (`corta/bin/`). |
| `herramientas/generar_indice.py` | Valida todo y regenera los índices. |

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

## Plantillas

Una plantilla es un video armado de antemano con **huecos** para tus clips o fotos. En Corta eliges una, eliges tus clips y se
arma sola: cada clip en su hueco, con sus efectos, transiciones y textos. Después lo retocas como cualquier video y lo exportas.

Una plantilla **no trae** video, fotos, música ni código: solo dice cuánto dura cada hueco y usa por su nombre efectos (de este
catálogo o de los que trae Corta) y un estilo de subtítulos de Corta (`caja`, `neon`, `palabra`, `pop`, `suave` o `titular`).

```json
{
 "formato": 1,
 "id": "oferta-del-dia",
 "categoria": "negocios",
 "nombre": {"es": "Oferta del día", "en": "Deal of the day"},
 "autor": "tu-usuario",
 "proporcion": "1:1",
 "huecos": [
  {"dur": 2, "tipo": "cualquiera", "pista": {"es": "El producto", "en": "The product"}, "transicion": "destello"},
  {"dur": 2, "tipo": "cualquiera", "pista": {"es": "Un detalle", "en": "A detail"}, "transicion": "destello"},
  {"dur": 3, "tipo": "cualquiera", "pista": {"es": "El precio", "en": "The price"}, "efectos": ["zoom-dramatico"]}
 ],
 "textos": [{"en_hueco": 0, "texto": {"es": "Oferta del día", "en": "Deal of the day"}, "posicion": 0.18}],
 "subtitulos": {"estilo": "caja", "activos": true},
 "efectos": ["vivido"],
 "musica": {"bpm": 120}
}
```

| Campo | Qué es |
|---|---|
| `proporcion` | `9:16` (Shorts, Reels, TikTok), `1:1`, `4:5` o `16:9`. |
| `huecos` | De 1 a 20, en orden; entre todos, hasta 90 segundos. Cada uno: `dur` (0,5 a 15 s), `tipo` (`video`, `foto` o `cualquiera`: lo que conviene poner), y opcionales `pista` (qué poner, hasta 40 caracteres), `efectos` (hasta 3, solo en ese hueco; no transiciones), `transicion` (cómo pasa al siguiente: un efecto con pasos `transicion`, como `destello`, `transicion-negro` o `parpadeo`) y `zoom` (si cae una foto: `acercar`, que es lo normal, `alejar` o `no`). |
| `textos` | Opcional, hasta 10: `en_hueco` (número del hueco, desde 0), `texto` (hasta 60 caracteres) y `posicion` (altura, de 0,08 arriba a 0,9 abajo). |
| `subtitulos` | Opcional: `estilo` (con él se dibujan los subtítulos y los textos) y `activos`. |
| `efectos` | Opcional: hasta 3 efectos para todo el video (un filtro, `fundido-entrada`, `fundido-salida`…). |
| `musica` | Opcional: solo el ritmo (`bpm`, 60 a 200) para el que pensaste los cortes. Nunca un archivo: cada persona pone su música. |

Si la persona no elige suficientes clips, se repiten (de otra parte del video); si una plantilla usa un efecto del catálogo que la
persona no tiene, Corta le ofrece descargarlo.

1. **Pruébala en Corta:** guarda tu archivo en `~/Corta/.corta/plantillas/<id>.json` y úsala desde «Plantillas».
2. **Compártela:** abre un [issue «Proponer una plantilla»](https://github.com/corta-app/corta-catalogo/issues/new?template=plantilla.yml)
   y descríbela con palabras (hueco por hueco) o pega el JSON: nosotros la armamos. También puedes abrir un pull request con
   `plantillas/<categoria>/<id>.json` después de correr `python3 herramientas/generar_indice.py`.

Más detalle en [CONTRIBUTING.md](CONTRIBUTING.md). Todo aporte lo revisa una persona antes de entrar.

🔒 ¿Una falla de seguridad? Avísanos en privado: [SECURITY.md](SECURITY.md).

---

## English

**Corta's community catalog:** free effects, filters and **templates** that the [Corta](https://github.com/corta-app/corta) video
editor downloads, sorted by category. Each file is **data-only JSON**: the app validates it with the same format files this repo uses,
and builds the preview (CSS) and the export (a whitelist of ffmpeg filters) from its numbers, so nothing here can ever run code.

**Effects** (`efectos/`: `filtro` filters, `color`, `movimiento` motion, `transicion` transitions) are a short list of steps (color,
tint, blur, vignette, zoom, fade, transition) with numbers in known ranges.

**Templates** (`plantillas/`: `negocios` business, `presentacion` intros, `recuerdos` memories, `tutorial`, `celebracion` celebrations)
are pre-made videos with **slots** for your clips or photos: each slot's length (`dur`), what fits best (`tipo`: `video`, `foto` photo
or `cualquiera` any), an optional hint (`pista`), effects for that slot, the transition to the next slot (an effect made of
`transicion` steps), an optional zoom for photos, texts on top of a slot, the caption style, effects for the whole video and the music
tempo the cuts were designed for (`bpm` only: templates never include music, footage or images). In Corta you pick a template, pick your
clips, and the video builds itself; then you edit it like any other video. If a template uses a catalog effect you don't have, Corta
offers to download it.

**Make one without coding:** try it in Corta by saving it to `~/Corta/.corta/efectos/<id>.json` or
`~/Corta/.corta/plantillas/<id>.json`, then share it by opening a ["Propose an effect"](https://github.com/corta-app/corta-catalogo/issues/new?template=efecto.yml)
or ["Propose a template"](https://github.com/corta-app/corta-catalogo/issues/new?template=plantilla.yml) issue (for templates you can
just describe the slots in words), or a pull request after running `python3 herramientas/generar_indice.py`. A maintainer reviews
every contribution. Security issues: please report them privately ([SECURITY.md](SECURITY.md)).
