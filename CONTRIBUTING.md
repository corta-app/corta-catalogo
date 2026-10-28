# Cómo aportar al catálogo

Aquí viven los efectos y filtros que Corta descarga. Son **solo datos** (JSON): no hace falta programar. *(English below.)*

## Un efecto nuevo
- **Lo más fácil:** pruébalo en Corta (guárdalo en `~/Corta/.corta/efectos/<id>.json`) y propónlo con el formulario
  [«Proponer un efecto»](https://github.com/corta-app/corta-catalogo/issues/new?template=efecto.yml), pegando el JSON. Lo revisamos,
  lo sumamos con tu usuario como autor y te avisamos.
- **Por pull request:** agrega `efectos/<categoria>/<id>.json`, corre `python3 herramientas/generar_indice.py` (valida y regenera
  `efectos/index.json`) y sube los dos archivos.
- **Reglas:** el nombre y la descripción dicen lo que hace (en español y, si puedes, en inglés); el `id` no repite otro; nada
  personal, nada de marcas ni de empresas reales; y que se vea bien en un video de verdad (cuéntanos con cuál lo probaste, sin subirlo).

## Cambiar el formato
`herramientas/efecto_formato.py` es **el mismo archivo** que `bin/efecto_formato.py` de la app. Un tipo de paso o un rango nuevo
necesita primero el cambio en la app (vista previa y exportación con ffmpeg, con sus pruebas) y una versión publicada; después se
copia aquí. Así un efecto del catálogo nunca le llega a una app que no lo entiende.

## Cómo revisamos
Todo entra por pull request y lo junta alguien que mantiene el proyecto. Revisamos que el JSON pase la validación (GitHub la corre
en cada pull request, sin secretos y con permiso de solo lectura), que no traiga nada personal ni copiado y que se vea bien.
Si algo falta te lo pedimos con un comentario.

**Fallas de seguridad:** nunca en un issue público; avísanos en privado como explica [SECURITY.md](SECURITY.md).

---

**English:** effects are data-only JSON. Try yours in Corta (`~/Corta/.corta/efectos/<id>.json`), then propose it with the
"Propose an effect" issue form (paste the JSON) or open a pull request with `efectos/<category>/<id>.json` after running
`python3 herramientas/generar_indice.py`. Name and describe what it does, keep the id unique and nothing personal or branded.
`herramientas/efecto_formato.py` is the same file as the app's `bin/efecto_formato.py`: format changes land in the app first.
A maintainer reviews every pull request. Security issues: report them privately, see [SECURITY.md](SECURITY.md).
