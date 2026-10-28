# Seguridad del catálogo de Corta

*(English below.)*

Este repo tiene los efectos que la app [Corta](https://github.com/corta-app/corta) descarga. Son **solo datos** (JSON): ningún
archivo de aquí debe poder ejecutar código, leer archivos, colar algo en el comando de ffmpeg ni traer HTML a la app.

Si encuentras algo que se salte esa regla (un efecto que haga algo raro en la app o al exportar, una forma de que un JSON pase la
validación con texto escondido, un problema en `herramientas/` o en el workflow), avísanos **en privado** en
[**Reportar una vulnerabilidad**](https://github.com/corta-app/corta-catalogo/security/advisories/new). No abras un issue público ni
un pull request con el detalle mientras no esté arreglado. Te respondemos dentro de una semana.

Cómo nos cuidamos:
- Todo entra por pull request y lo revisa una persona.
- `herramientas/generar_indice.py` valida con `herramientas/efecto_formato.py` (el mismo archivo que la app): claves y tipos
  conocidos, números dentro de rangos, colores `#RRGGBB` y textos sin HTML. GitHub lo corre en cada pull request con permiso de
  solo lectura, actions fijadas por SHA y sin `pull_request_target`.
- La app solo descarga desde `raw.githubusercontent.com/corta-app/corta-catalogo`, sin seguir redirecciones y con tamaño máximo;
  compara la huella SHA-256 del índice y vuelve a validar cada efecto antes de guardarlo. Al exportar, el código arma los filtros de
  ffmpeg (de una lista blanca) solo con los números del efecto.

---

**English:** this repo holds data-only JSON effects downloaded by the Corta app. If you find a way for catalog content to run code,
inject anything into the ffmpeg command or the app's UI, or an issue in `herramientas/` or the workflow, please report it privately via
[Report a vulnerability](https://github.com/corta-app/corta-catalogo/security/advisories/new) instead of a public issue. We reply
within a week.
