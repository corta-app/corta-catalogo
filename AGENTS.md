# Catálogo de Corta

Repo **público** con los efectos y las plantillas que la app Corta descarga a pedido. Solo datos JSON, validados por la app al descargarlos.
El proyecto principal (y su `AGENTS.md`, la guía para personas y para cualquier IA) está en el repo `corta`. `CLAUDE.md` y
`GEMINI.md` solo importan este archivo.

- `efectos/<categoria>/<id>.json` (categorías: las de `efecto_formato.CATEGORIAS`) + `efectos/index.json` (generado: cada efecto con
  `archivo`, `sha256` y `bytes`; la app compara la huella antes de guardar).
- `plantillas/<categoria>/<id>.json` (categorías: `plantilla_formato.CATEGORIAS`) + `plantillas/index.json` (generado, igual que el
  de efectos). Una plantilla solo usa efectos que existan (de aquí o `plantilla_formato.EFECTOS_INCLUIDOS`, los que trae la app) y
  estilos de `ESTILOS_INCLUIDOS`; nunca música, video ni imágenes (`musica` es solo `bpm`).
- `herramientas/efecto_formato.py` y `herramientas/plantilla_formato.py` son **idénticos** a los de `corta/bin/` (la app lo prueba si este repo está al lado). Un
  cambio de formato entra primero en la app (vista previa + ffmpeg + pruebas) y se publica; después se copia aquí.
- `herramientas/generar_indice.py`: valida y regenera el índice. Córrelo antes de cada commit; el workflow `revisar.yml` revisa que
  esté al día.
- Propuestas por issue (`efecto.yml`, `plantilla.yml`; una plantilla puede venir descrita con palabras: armar el JSON): validar el JSON con `generar_indice.py`, poner `autor` (usuario de GitHub), revisarlo a mano
  (nada personal ni de marcas, nombre que diga lo que hace) y abrir el pull request.

Reglas: nada personal del usuario ni de su trabajo (es público); nunca código, CSS, HTML ni texto de filtros de ffmpeg en los JSON.
Commits en español, autor con correo `@users.noreply.github.com`. Revisar aportes: skill `revisar-aportes-open-source`; nunca se
junta sin aprobación de quien mantiene.
