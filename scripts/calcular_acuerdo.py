#!/usr/bin/env python3
"""Calcula acuerdo entre los juicios congelados y una segunda codificación."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "work" / "evaluacion_desenlaces_v1.0.csv"
CATEGORIES = ("fulfilled", "not_fulfilled", "indeterminate", "mixed")


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python scripts/calcular_acuerdo.py <hoja_segundo_codificador.csv>")
    second_path = Path(sys.argv[1]).resolve()
    reference = {row["prediction_key"]: row["judgment"] for row in rows(REFERENCE)}
    second = rows(second_path)
    pairs: list[tuple[str, str]] = []
    for row in second:
        value = row.get("independent_judgment", "").strip()
        if not value:
            continue
        if value not in CATEGORIES:
            raise SystemExit(f"Juicio inválido para {row.get('prediction_key')}: {value}")
        key = row["prediction_key"]
        if key not in reference:
            raise SystemExit(f"Clave desconocida: {key}")
        pairs.append((reference[key], value))
    if not pairs:
        raise SystemExit("La hoja no contiene juicios independientes completos.")

    n = len(pairs)
    agreement = sum(a == b for a, b in pairs) / n
    first_counts = Counter(a for a, _ in pairs)
    second_counts = Counter(b for _, b in pairs)
    expected = sum(first_counts[c] * second_counts[c] for c in CATEGORIES) / (n * n)
    kappa = (agreement - expected) / (1 - expected) if expected < 1 else 1.0

    print(f"Casos comparados: {n}")
    print(f"Acuerdo bruto: {agreement:.3f}")
    print(f"Kappa de Cohen: {kappa:.3f}")
    print("\nMatriz de confusión (filas=original, columnas=independiente)")
    print("original," + ",".join(CATEGORIES))
    matrix = Counter(pairs)
    for first in CATEGORIES:
        print(first + "," + ",".join(str(matrix[(first, second)]) for second in CATEGORIES))


if __name__ == "__main__":
    main()
