#!/usr/bin/env python3
"""Valida los efectos y las plantillas y regenera efectos/index.json y plantillas/index.json (lo que la app de Corta descarga).

Uso: python3 herramientas/generar_indice.py   (desde la raíz del catálogo; solo biblioteca estándar)

Todo es solo datos. Se rechaza cualquier archivo que no cumpla su formato (herramientas/efecto_formato.py y
herramientas/plantilla_formato.py: los mismos archivos que usa la app para validar lo que descarga), que no esté en la carpeta de su
categoría, que pese más de 64 KB o que repita un id. Una plantilla además solo puede usar efectos que existan (los de este catálogo o
los que trae la app) y un estilo de subtítulos que traiga la app; una transición entre clips tiene que ser un efecto de pasos
«transicion».
El índice lleva la huella SHA-256 y el tamaño de cada archivo: la app los compara con lo que descarga antes de guardarlo.
"""
import hashlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
import efecto_formato  # noqa: E402
import plantilla_formato  # noqa: E402

MAX_BYTES = 64 * 1024
fallas = 0


def falla(texto):
    global fallas
    fallas += 1
    print("✗ " + texto)


def revisar(carpeta_base, categorias, validar, extra=None):
    """Lee <carpeta_base>/<categoria>/<id>.json, valida cada uno y devuelve la lista para el índice."""
    base = os.path.join(RAIZ, carpeta_base)
    indice, vistos = [], {}
    for categoria in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        carpeta = os.path.join(base, categoria)
        if not os.path.isdir(carpeta):
            if categoria != "index.json":
                falla(f"{carpeta_base}/{categoria}: aquí solo van carpetas de categorías e index.json")
            continue
        if categoria not in categorias:
            falla(f"{carpeta_base}/{categoria}/: categoría desconocida (" + ", ".join(categorias) + ")")
            continue
        for nombre in sorted(os.listdir(carpeta)):
            relativa = f"{carpeta_base}/{categoria}/{nombre}"
            ruta = os.path.join(carpeta, nombre)
            if not nombre.endswith(".json") or not os.path.isfile(ruta) or os.path.islink(ruta):
                falla(f"{relativa}: solo archivos .json")
                continue
            with open(ruta, "rb") as f:
                crudo = f.read()
            errores = []
            if len(crudo) > MAX_BYTES:
                errores.append("pesa más de 64 KB")
            try:
                d = json.loads(crudo.decode("utf-8"))
            except (UnicodeDecodeError, ValueError) as e:
                d, errores = None, errores + [f"no es JSON válido en UTF-8 ({e})"]
            if d is not None:
                errores += validar(d, ruta)
                if isinstance(d, dict) and d.get("categoria") != categoria:
                    errores.append(f"está en {carpeta_base}/{categoria}/ pero su categoria es «{d.get('categoria')}»")
                if isinstance(d, dict) and d.get("id") in vistos:
                    errores.append(f"el id «{d['id']}» ya existe en {vistos[d['id']]}")
                if not errores and extra:
                    errores += extra(d)
            if errores:
                falla(f"{relativa}: " + "; ".join(errores))
                continue
            vistos[d["id"]] = relativa
            indice.append({**d, "archivo": relativa, "sha256": hashlib.sha256(crudo).hexdigest(), "bytes": len(crudo)})
            print(f"✓ {relativa}")
    return indice


def escribir(ruta, clave, lista):
    with open(os.path.join(RAIZ, ruta), "w", encoding="utf-8") as f:
        json.dump({"formato": 1, clave: lista}, f, ensure_ascii=False, indent=1)
        f.write("\n")


def main():
    efectos = revisar("efectos", efecto_formato.CATEGORIAS, efecto_formato.validar_efecto)
    escribir("efectos/index.json", "efectos", efectos)
    # Lo que una plantilla puede usar: los efectos de aquí y los que trae la app (si un id está en los dos, manda el de la app).
    conocidos = {e["id"]: (e["categoria"], tuple(p["tipo"] for p in e["pasos"])) for e in efectos}
    conocidos.update(plantilla_formato.EFECTOS_INCLUIDOS)
    plantillas = revisar("plantillas", plantilla_formato.CATEGORIAS, plantilla_formato.validar_plantilla,
                         lambda d: plantilla_formato.referencias(d, conocidos, plantilla_formato.ESTILOS_INCLUIDOS))
    escribir("plantillas/index.json", "plantillas", plantillas)
    print(f"\n{len(efectos)} efectos y {len(plantillas)} plantillas en los índices" + (f", {fallas} con problemas" if fallas else ""))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
