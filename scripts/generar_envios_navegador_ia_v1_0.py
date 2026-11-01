#!/usr/bin/env python3
"""Concatena cada paquete IA para enviarlo por interfaces web sin file upload."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "work" / "convalidacion_ia_v1.0"


for model in ("claude", "deepseek", "gemini"):
    folder = BASE / model
    parts = [
        ("INSTRUCCIONES", folder / "PROMPT.md"),
        ("DESENLACES_30.CSV", folder / "desenlaces_30.csv"),
        ("BUSQUEDA_INDEPENDIENTE_8.CSV", folder / "busqueda_independiente_8.csv"),
        ("FIDELIDAD_SEMANTICA_30.CSV", folder / "fidelidad_semantica_30.csv"),
    ]
    chunks = [
        "Procesá el paquete ciego siguiente. Devolvé exactamente tres bloques de código CSV completos, en el mismo orden y con los mismos encabezados y filas, titulados con sus nombres de archivo. No omitas columnas ni filas. No añadas texto dentro de los bloques CSV.\n"
    ]
    for title, path in parts:
        chunks.extend((f"\n===== {title} =====\n", path.read_text(encoding="utf-8-sig")))
    (folder / "ENVIO_NAVEGADOR.txt").write_text("".join(chunks), encoding="utf-8", newline="\n")
    print(model, (folder / "ENVIO_NAVEGADOR.txt").stat().st_size)
