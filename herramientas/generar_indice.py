#!/usr/bin/env python3
"""Valida los efectos y regenera efectos/index.json (lo que la app de Corta descarga para mostrar el catálogo).

Uso: python3 herramientas/generar_indice.py   (desde la raíz del catálogo; solo biblioteca estándar)

Un efecto es solo datos. Se rechaza cualquier archivo que no cumpla el formato de herramientas/efecto_formato.py (el mismo archivo
que usa la app para validar lo que descarga), que no esté en la carpeta de su categoría, que pese más de 64 KB o que repita un id.
El índice lleva la huella SHA-256 y el tamaño de cada archivo: la app los compara con lo que descarga antes de guardarlo.
"""
import hashlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
import efecto_formato  # noqa: E402

MAX_BYTES = 64 * 1024


def main():
    base = os.path.join(RAIZ, "efectos")
    indice, fallas, vistos = [], 0, {}
    for categoria in sorted(os.listdir(base)):
        carpeta = os.path.join(base, categoria)
        if not os.path.isdir(carpeta):
            if categoria != "index.json":
                fallas += 1
                print(f"✗ efectos/{categoria}: aquí solo van carpetas de categorías e index.json")
            continue
        if categoria not in efecto_formato.CATEGORIAS:
            fallas += 1
            print(f"✗ efectos/{categoria}/: categoría desconocida (" + ", ".join(efecto_formato.CATEGORIAS) + ")")
            continue
        for nombre in sorted(os.listdir(carpeta)):
            relativa = f"efectos/{categoria}/{nombre}"
            ruta = os.path.join(carpeta, nombre)
            if not nombre.endswith(".json") or not os.path.isfile(ruta) or os.path.islink(ruta):
                fallas += 1
                print(f"✗ {relativa}: solo archivos .json")
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
                errores += efecto_formato.validar_efecto(d, ruta)
                if isinstance(d, dict) and d.get("categoria") != categoria:
                    errores.append(f"está en efectos/{categoria}/ pero su categoria es «{d.get('categoria')}»")
                if isinstance(d, dict) and d.get("id") in vistos:
                    errores.append(f"el id «{d['id']}» ya existe en {vistos[d['id']]}")
            if errores:
                fallas += 1
                print(f"✗ {relativa}: " + "; ".join(errores))
                continue
            vistos[d["id"]] = relativa
            indice.append({**d, "archivo": relativa, "sha256": hashlib.sha256(crudo).hexdigest(), "bytes": len(crudo)})
            print(f"✓ {relativa}")
    with open(os.path.join(base, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"formato": 1, "efectos": indice}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"\n{len(indice)} efectos en el índice" + (f", {fallas} con problemas" if fallas else ""))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
