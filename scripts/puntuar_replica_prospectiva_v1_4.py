"""Validate and score genuinely prospective binary forecasts; empty template yields no score."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "work" / "tarjeta_pronostico_prospectivo_template_v1.4.csv"


def instant(value: str, field: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{field}: fecha ISO-8601 inválida") from error
    if parsed.tzinfo is None:
        raise ValueError(f"{field}: falta zona horaria")
    return parsed.astimezone(timezone.utc)


def probability(value: str, field: str) -> float:
    try:
        number = float(value)
    except ValueError as error:
        raise ValueError(f"{field}: falta probabilidad numérica") from error
    if not 0 <= number <= 1:
        raise ValueError(f"{field}: probabilidad fuera de [0,1]")
    return number


def score(rows: list[dict[str, str]]) -> dict[str, float | int | None]:
    ids = [row["forecast_id"] for row in rows]
    if not all(ids) or len(set(ids)) != len(ids):
        raise ValueError("IDs vacíos o duplicados")
    resolved = []
    paired = []
    for row in rows:
        key = row["forecast_id"]
        for field in ("source_url", "source_locator", "event_binary_frozen", "population", "success_threshold_frozen", "admissible_resolution_source_frozen"):
            if not row[field].strip():
                raise ValueError(f"{key}: falta {field}")
        issued = instant(row["issued_at_utc"], f"{key}.issued_at_utc")
        locked = instant(row["locked_at_utc"], f"{key}.locked_at_utc")
        deadline = instant(row["deadline_utc"], f"{key}.deadline_utc")
        if not issued <= locked < deadline:
            raise ValueError(f"{key}: cierre debe ocurrir después de emisión y antes de plazo")
        p = probability(row["probability_original"], f"{key}.probability_original")
        baseline_text = row["baseline_probability"].strip()
        base = probability(baseline_text, f"{key}.baseline_probability") if baseline_text else None
        if base is not None and (not row["baseline_name"] or not row["baseline_source_url"]):
            raise ValueError(f"{key}: baseline sin nombre o fuente")
        y_text = row["outcome_binary"].strip()
        if not y_text:
            if row["resolved_at_utc"] or row["resolution_evidence_url"]:
                raise ValueError(f"{key}: desenlace parcial")
            continue
        if y_text not in ("0", "1") or not row["resolution_evidence_url"]:
            raise ValueError(f"{key}: resultado debe ser 0/1 y tener URL probatoria")
        resolution = instant(row["resolved_at_utc"], f"{key}.resolved_at_utc")
        if resolution < deadline or resolution < locked:
            raise ValueError(f"{key}: resultado registrado antes de la fecha límite")
        y = int(y_text)
        resolved.append((p - y) ** 2)
        if base is not None:
            paired.append(((p - y) ** 2, (base - y) ** 2))
    mean = sum(resolved) / len(resolved) if resolved else None
    paired_forecast = sum(a for a, _ in paired) / len(paired) if paired else None
    paired_baseline = sum(b for _, b in paired) / len(paired) if paired else None
    skill = 1 - paired_forecast / paired_baseline if paired_baseline and paired_forecast is not None else None
    return {"cards": len(rows), "resolved": len(resolved), "unresolved": len(rows) - len(resolved),
            "brier_mean": mean, "paired_count": len(paired), "paired_forecast_brier": paired_forecast,
            "paired_baseline_brier": paired_baseline, "paired_skill_score": skill}


def self_test() -> None:
    with DEFAULT.open(encoding="utf-8", newline="") as handle:
        fields = csv.DictReader(handle).fieldnames or []
    base = {key: "" for key in fields}
    base.update({
        "forecast_id": "synthetic-test-only", "source_url": "https://example.org/source", "source_locator": "page 1",
        "event_binary_frozen": "event", "population": "population", "success_threshold_frozen": "threshold",
        "admissible_resolution_source_frozen": "official record", "issued_at_utc": "2026-01-01T00:00:00Z",
        "locked_at_utc": "2026-01-02T00:00:00Z", "deadline_utc": "2026-06-01T00:00:00Z",
        "probability_original": "0.8", "baseline_probability": "0.5", "baseline_name": "reference",
        "baseline_source_url": "https://example.org/baseline", "outcome_binary": "1",
        "resolved_at_utc": "2026-06-02T00:00:00Z", "resolution_evidence_url": "https://example.org/result",
    })
    result = score([base])
    assert result["brier_mean"] is not None and abs(result["brier_mean"] - 0.04) < 1e-12
    assert result["paired_skill_score"] is not None and abs(result["paired_skill_score"] - 0.84) < 1e-12
    for field, invalid in (("locked_at_utc", "2026-06-03T00:00:00Z"), ("outcome_binary", "maybe"), ("baseline_probability", "1.5")):
        bad = dict(base, **{field: invalid})
        try:
            score([bad])
        except ValueError:
            pass
        else:
            raise AssertionError(f"No se rechazó {field}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("Pruebas sintéticas del puntuador: correctas; ningún pronóstico real creado.")
        return
    with args.input.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result = score(rows)
    if not rows:
        print("Plantilla vacía: cero pronósticos reales; no hay puntuación publicable.")
        return
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
