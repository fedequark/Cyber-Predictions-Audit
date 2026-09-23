#!/usr/bin/env python3
"""Calcula acuerdo pareado y consenso entre salidas de convalidadores IA."""

from __future__ import annotations

import csv
import itertools
import sys
from collections import Counter
from pathlib import Path


CATEGORIES = ("fulfilled", "not_fulfilled", "indeterminate", "mixed")


def read(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    values = {}
    for row in rows:
        value = row.get("independent_judgment", "").strip()
        if value not in CATEGORIES:
            raise SystemExit(f"Valor inválido o vacío en {path}: {row.get('prediction_key')}={value!r}")
        values[row["prediction_key"]] = value
    return values


def agreement(a: dict[str, str], b: dict[str, str]) -> tuple[int, float, float]:
    keys = sorted(set(a) & set(b))
    pairs = [(a[k], b[k]) for k in keys]
    observed = sum(x == y for x, y in pairs) / len(pairs)
    ac, bc = Counter(x for x, _ in pairs), Counter(y for _, y in pairs)
    expected = sum(ac[c] * bc[c] for c in CATEGORIES) / (len(pairs) ** 2)
    kappa = (observed - expected) / (1 - expected) if expected < 1 else 1.0
    return len(pairs), observed, kappa


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("Uso: python scripts/calcular_acuerdo_ias_v1_0.py modelo=archivo.csv [modelo=archivo.csv ...]")
    data = {}
    for item in sys.argv[1:]:
        name, raw_path = item.split("=", 1)
        data[name] = read(Path(raw_path))
    print("modelo_a,modelo_b,n,acuerdo_bruto,kappa")
    for left, right in itertools.combinations(data, 2):
        n, raw, kappa = agreement(data[left], data[right])
        print(f"{left},{right},{n},{raw:.3f},{kappa:.3f}")
    common = sorted(set.intersection(*(set(values) for values in data.values())))
    unanimous = sum(len({data[name][key] for name in data}) == 1 for key in common)
    majority = sum(Counter(data[name][key] for name in data).most_common(1)[0][1] >= 3 for key in common)
    print(f"\nCasos comunes: {len(common)}")
    print(f"Unanimidad 4/4: {unanimous}/{len(common)}")
    print(f"Mayoría >=3/4: {majority}/{len(common)}")


if __name__ == "__main__":
    main()
