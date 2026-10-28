# Cómo aportar al catálogo

Aquí viven los efectos, filtros y plantillas que Corta descarga. Son **solo datos** (JSON): no hace falta programar. *(English below.)*

## Un efecto nuevo
- **Lo más fácil:** pruébalo en Corta (guárdalo en `~/Corta/.corta/efectos/<id>.json`) y propónlo con el formulario
  [«Proponer un efecto»](https://github.com/corta-app/corta-catalogo/issues/new?template=efecto.yml), pegando el JSON. Lo revisamos,
  lo sumamos con tu usuario como autor y te avisamos.
- **Por pull request:** agrega `efectos/<categoria>/<id>.json`, corre `python3 herramientas/generar_indice.py` (valida y regenera
  `efectos/index.json`) y sube los dos archivos.
- **Reglas:** el nombre y la descripción dicen lo que hace (en español y, si puedes, en inglés); el `id` no repite otro; nada
  personal, nada de marcas ni de empresas reales; y que se vea bien en un video de verdad (cuéntanos con cuál lo probaste, sin subirlo).

## Una plantilla nueva
- **Lo más fácil:** descríbela con palabras, hueco por hueco, en el formulario
  [«Proponer una plantilla»](https://github.com/corta-app/corta-catalogo/issues/new?template=plantilla.yml) (o pega el JSON si ya lo
  probaste en `~/Corta/.corta/plantillas/<id>.json`). Nosotros armamos el JSON y te ponemos como autor.
- **Por pull request:** agrega `plantillas/<categoria>/<id>.json`, corre `python3 herramientas/generar_indice.py` (valida el formato y
  que cada efecto y estilo que usa exista) y sube el archivo con `plantillas/index.json`.
- **Reglas:** igual que los efectos, y además: sin música, videos ni imágenes (cada persona pone los suyos; `musica` solo dice el
  ritmo), pistas que digan qué poner en cada hueco y textos cortos que sirvan para cualquiera.

## Cambiar el formato
`herramientas/efecto_formato.py` y `herramientas/plantilla_formato.py` son **los mismos archivos** que `bin/` de la app. Un tipo de paso o un rango nuevo
necesita primero el cambio en la app (vista previa y exportación con ffmpeg, con sus pruebas) y una versión publicada; después se
copia aquí. Así un efecto del catálogo nunca le llega a una app que no lo entiende.

## Cómo revisamos
Todo entra por pull request y lo junta alguien que mantiene el proyecto. Revisamos que el JSON pase la validación (GitHub la corre
en cada pull request, sin secretos y con permiso de solo lectura), que no traiga nada personal ni copiado y que se vea bien.
Si algo falta te lo pedimos con un comentario.

**Fallas de seguridad:** nunca en un issue público; avísanos en privado como explica [SECURITY.md](SECURITY.md).

---

**English:** effects and templates are data-only JSON. Templates can be proposed in plain words, slot by slot, with the
"Propose a template" issue form; they never include music, footage or images. Effects are data-only JSON too. Try yours in Corta (`~/Corta/.corta/efectos/<id>.json`), then propose it with the
"Propose an effect" issue form (paste the JSON) or open a pull request with `efectos/<category>/<id>.json` after running
`python3 herramientas/generar_indice.py`. Name and describe what it does, keep the id unique and nothing personal or branded.
`herramientas/efecto_formato.py` and `herramientas/plantilla_formato.py` are the same files as the app's `bin/`: format changes land in the app first.
A maintainer reviews every pull request. Security issues: report them privately, see [SECURITY.md](SECURITY.md).
