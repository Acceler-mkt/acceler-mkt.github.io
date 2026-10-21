"""Copia a assets/portfolio las piezas elegidas (carruseles y estáticos) en tamaño web.

Uso: python tools/portfolio.py
Las piezas y su orden están en ELEGIDAS. Salida: JPG de 720 px de ancho (calidad 80) + portfolio.json para la web.
"""
import json
from pathlib import Path

from PIL import Image

CL = Path.home() / "Documents/Evolve Agency/Clientes"
OUT = Path(__file__).resolve().parent.parent / "assets/portfolio"
ANCHO = 720

CARRUSELES = {
    "miguel": ("Miguel Sierra", "@miguelsierrag", CL / "Miguel Sierra/CARROUSELES OCT 2026",
               ["01 - Paco, Pedro y Miguel", "07 - Vender la empresa con holding", "05 - Subida de sueldo e IRPF",
                "06 - En junio ya es tarde", "10 - Varios negocios en una SL", "03 - Fracasar antes de empezar"]),
    "alex": ("Álex Mestres · GLA Patrimonio", "@alexsmestres", CL / "Alex Mestres/CARROUSELES OCT 2026",
             ["01 - 40.000 parados, 3 preguntas", "03 - Herencia, no firmes", "05 - Inflación del 4,9 %",
              "07 - La bolsa cae un 30 %", "13 - Dos hermanos heredan 60.000", "14 - 289 toneladas de oro"]),
}
# Solo la tanda de abril 2027 del sistema de estáticos (22-10-2026): fotográficos (P) y tipográficos (T)
ESTATICOS = Path(__file__).resolve().parent.parent / "ads/iuver/abr27"


def guardar(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    im = im.resize((ANCHO, round(im.height * ANCHO / im.width)), Image.LANCZOS)
    im.save(dst, "JPEG", quality=80, optimize=True, progressive=True)
    return f"assets/portfolio/{dst.parent.name}/{dst.name}", im.width, im.height


def main():
    datos = {"carruseles": [], "estaticos": []}
    for clave, (cliente, cuenta, base, carpetas) in CARRUSELES.items():
        for i, carpeta in enumerate(carpetas, 1):
            slides = sorted((base / carpeta).glob("slide-*.png")) or sorted((base / carpeta).glob("*.png"))
            rutas = [guardar(s, OUT / clave / f"c{i:02d}-{n:02d}.jpg")[0] for n, s in enumerate(slides, 1)]
            datos["carruseles"].append({"cliente": cliente, "cuenta": cuenta, "titulo": carpeta.split(" - ", 1)[1], "slides": rutas})
    for viejo in (OUT / "iuver").glob("e*.jpg"):
        viejo.unlink()
    for i, src in enumerate(sorted(ESTATICOS.glob("*.png")), 1):
        ruta, w, h = guardar(src, OUT / "iuver" / f"e{i:02d}.jpg")
        datos["estaticos"].append({"cliente": "IUVER Academy", "src": ruta, "w": w, "h": h})
    (OUT / "portfolio.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    # La web lo carga como script para que funcione también abriendo el HTML en local (sin servidor)
    (OUT / "portfolio.js").write_text("window.PORTFOLIO = " + json.dumps(datos, ensure_ascii=False) + ";\n", encoding="utf-8")
    peso = sum(f.stat().st_size for f in OUT.rglob("*.jpg")) / 1e6
    print(f"{len(datos['carruseles'])} carruseles, {len(datos['estaticos'])} estáticos, {peso:.1f} MB")


if __name__ == "__main__":
    main()
