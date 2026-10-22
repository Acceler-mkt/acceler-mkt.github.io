"""Copia a assets/portfolio las piezas de la web en tamaño web: 2 portadas de carrusel y 3 estáticos.

Uso: python tools/portfolio.py
Las piezas están en PIEZAS. Salida: JPG de 720 px de ancho (calidad 82).
"""
from pathlib import Path

from PIL import Image

CL = Path.home() / "Documents/Evolve Agency/Clientes"
RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "assets/portfolio"
ANCHO = 720


def portada(carpeta: Path) -> Path:
    return (sorted(carpeta.glob("slide-*.png")) or sorted(carpeta.glob("*.png")))[0]


# nombre de salida → original (22-10-2026: la landing se queda con una pieza de cada tipo)
PIEZAS = {
    "ms-carrusel.jpg": portada(CL / "Miguel Sierra/CARROUSELES OCT 2026/01 - Paco, Pedro y Miguel"),
    "gla-carrusel.jpg": portada(CL / "Alex Mestres/CARROUSELES OCT 2026/01 - 40.000 parados, 3 preguntas"),
    "est-1.jpg": RAIZ / "tools/fuentes/est-1-dna.webp",
    "est-2.jpg": RAIZ / "tools/fuentes/est-2-iuver-pinchar.webp",
    "est-3.jpg": RAIZ / "tools/fuentes/est-3-iuver-paciente.webp",
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for nombre, src in PIEZAS.items():
        im = Image.open(src).convert("RGB")
        im = im.resize((ANCHO, round(im.height * ANCHO / im.width)), Image.LANCZOS)
        im.save(OUT / nombre, "JPEG", quality=82, optimize=True, progressive=True)
    print(f"{len(PIEZAS)} piezas en {OUT}")


if __name__ == "__main__":
    main()
