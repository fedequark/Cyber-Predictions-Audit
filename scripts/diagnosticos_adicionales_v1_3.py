#!/usr/bin/env python3
"""Diagnósticos descriptivos v1.3; nunca altera los juicios congelados."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "work" / "analisis_derivado_v1.2.csv"
FRAME = ROOT / "work" / "orden_seleccion_s3_v0.2.csv"
INFLUENCE = ROOT / "work" / "influencia_sesiones_v1.3.csv"
SCENARIOS = ROOT / "work" / "escenarios_indeterminados_v1.3.csv"
REPORT = ROOT / "outputs" / "diagnosticos_adicionales_v1.3.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def pct(value: float) -> str:
    return f"{100 * value:.1f}%".replace(".", ",")


def counts(rows: list[dict[str, str]]) -> Counter[str]:
    return Counter(row["judgment"] for row in rows)


def main() -> None:
    rows = read_csv(DERIVED)
    frame = read_csv(FRAME)
    if len(rows) != 120 or len(frame) != 138:
        raise SystemExit("El corpus derivado o el marco no tiene el tamaño esperado.")
    keys = [row["prediction_key"] for row in rows]
    if len(set(keys)) != 120:
        raise SystemExit("Las claves de predicción no son únicas.")

    global_counts = counts(rows)
    if global_counts != Counter({"fulfilled": 54, "not_fulfilled": 35, "indeterminate": 31}):
        raise SystemExit("Los juicios no concuerdan con los registros congelados.")
    base = 54 / 89

    sessions: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        sessions[row["session_id_normalized"]].append(row)
    influence: list[dict[str, object]] = []
    for session_id in sorted(sessions):
        own = sessions[session_id]
        c = counts(own)
        remaining_fulfilled = 54 - c["fulfilled"]
        remaining_failed = 35 - c["not_fulfilled"]
        rate = remaining_fulfilled / (remaining_fulfilled + remaining_failed)
        influence.append({
            "session_id": session_id,
            "venue": own[0]["venue"],
            "session_title": own[0]["session_title"],
            "n_predictions": len(own),
            "n_fulfilled": c["fulfilled"],
            "n_not_fulfilled": c["not_fulfilled"],
            "n_indeterminate": c["indeterminate"],
            "n_remaining_resolvable": remaining_fulfilled + remaining_failed,
            "rate_without_session": f"{rate:.12g}",
            "change_percentage_points": f"{100 * (rate - base):.12g}",
        })
    write_csv(INFLUENCE, influence, list(influence[0]))
    lowest = min(influence, key=lambda row: float(row["rate_without_session"]))
    highest = max(influence, key=lambda row: float(row["rate_without_session"]))

    scenarios: list[dict[str, object]] = []
    for resolved_as_success in (0, 7, 16, 24, 31):
        scenarios.append({
            "indeterminate_resolved_as_success": resolved_as_success,
            "indeterminate_resolved_as_failure": 31 - resolved_as_success,
            "fulfilled_total": 54 + resolved_as_success,
            "corpus_total": 120,
            "rate_all_120": f"{(54 + resolved_as_success) / 120:.12g}",
            "analysis_status": "exploratory_counterfactual_not_recoding",
        })
    write_csv(SCENARIOS, scenarios, list(scenarios[0]))

    def group_stats(label: str, subset: list[dict[str, str]]) -> str:
        c = counts(subset)
        return f"| {label} | {len(subset)} | {c['fulfilled']} | {c['not_fulfilled']} | {c['indeterminate']} | {pct(c['indeterminate']/len(subset))} |"

    difficulty = "\n".join(
        group_stats(band.capitalize(), [row for row in rows if row["difficulty_proxy"] == band])
        for band in ("baja", "media", "alta")
    )
    sn = "\n".join(
        group_stats(label, [row for row in rows if row["security_nightmares"] == code])
        for label, code in (("Security Nightmares", "1"), ("Resto", "0"))
    )
    period_groups = (("2005–2009", 2005, 2009), ("2010–2014", 2010, 2014), ("2015–2018", 2015, 2018))
    periods = "\n".join(
        group_stats(label, [row for row in rows if start <= int(row["session_year"]) <= end])
        for label, start, end in period_groups
    )

    frame_by_venue = Counter(row["venue"] for row in frame)
    contributors_by_venue = Counter()
    for own in sessions.values():
        contributors_by_venue[own[0]["venue"]] += 1
    venue = "\n".join(
        f"| {label} | {frame_by_venue[label]} | {contributors_by_venue[label]} | {sum(row['venue']==label for row in rows)} |"
        for label in ("Black Hat USA", "CCC", "Virus Bulletin")
    )

    no_evidence = [row for row in rows if not row["primary_evidence_url"] and not row["secondary_evidence_url"]]
    weak_failed = [row for row in rows if row["judgment"] == "not_fulfilled" and row["evidence_strength"] == "weak"]
    if len(no_evidence) != 18 or len(weak_failed) != 1:
        raise SystemExit("Los diagnósticos de evidencia cambiaron inesperadamente.")
    weak_key = weak_failed[0]["prediction_key"]
    weak_reclassified = 54 / 88
    scenario_lines = "\n".join(
        f"| {row['indeterminate_resolved_as_success']} | {row['indeterminate_resolved_as_failure']} | {pct(float(row['rate_all_120']))} |"
        for row in scenarios
    )

    report = f"""# Diagnósticos adicionales v1.3

**Fecha:** 15 de septiembre de 2026. **Estado:** exploratorio/post hoc.
Esta capa no sustituye la evaluación congelada ni resuelve por decreto los 31 casos indeterminados.

## 1. Influencia de cada sesión

Se eliminaron, una por una, las 36 sesiones aportantes y se recalculó la proporción entre los casos resolubles restantes. El 60,7% original queda entre **{pct(float(lowest['rate_without_session']))}** (sin `{lowest['session_id']}`) y **{pct(float(highest['rate_without_session']))}** (sin `{highest['session_id']}`). La tabla completa preserva las 36 contribuciones y el cambio en puntos porcentuales.

Esto mide dependencia de sesiones concretas dentro del corpus, no incertidumbre de muestreo poblacional. Eliminar una sesión con pocos casos casi no mueve el resultado; una sesión con varios casos resolubles puede moverlo más.

## 2. Heterogeneidad descriptiva de la indeterminación

| Dificultad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % indeterminado |
|---|---:|---:|---:|---:|---:|
{difficulty}

| Familia | n | Cumplidas | Incumplidas | Indeterminadas | % indeterminado |
|---|---:|---:|---:|---:|---:|
{sn}

| Periodo de sesión | n | Cumplidas | Incumplidas | Indeterminadas | % indeterminado |
|---|---:|---:|---:|---:|---:|
{periods}

Los estratos muestran heterogeneidad descriptiva de la indeterminación según atributos observados. No prueban un mecanismo de ausencia de datos ni justifican imputar a los indeterminados con la tasa de los resolubles. Las categorías de dificultad son proxies post hoc y tampoco prueban causalidad.

## 3. Identificación parcial explícita

Si `u` de las 31 indeterminadas finalmente resultara cumplida, la tasa sobre el corpus sería `(54+u)/120`. Los siguientes son escenarios contrafactuales, no nuevos juicios:

| Indeterminadas como cumplidas | Como incumplidas | % de 120 |
|---:|---:|---:|
{scenario_lines}

Siete cumplidas serían suficientes para superar 50% sobre los 120 casos. El corpus no permite estimar cuántas son realmente cumplidas sin nuevas fuentes.

## 4. Sensibilidad de evidencia débil

Dieciocho filas no tienen URL probatoria primaria ni secundaria: 17 indeterminadas y una incumplida. El único incumplimiento con fuerza `weak` es `{weak_key}`. Si **sólo para probar fragilidad** se lo tratara como indeterminado, el balance resoluble sería 54/88 = **{pct(weak_reclassified)}**, frente a 54/89 = **{pct(base)}**. El juicio canónico no se modifica.

No se calcula una tasa “sólo evidencia fuerte” como estimador principal: la fuerza de evidencia se asignó después de observar el desenlace y puede seleccionar casos fáciles de probar, tanto positivos como negativos.

## 5. Composición del marco y rendimiento documental

| Venue | Sesiones S3 | Sesiones que aportaron predicciones | Predicciones incluidas |
|---|---:|---:|---:|
{venue}

Una sesión que no aportó predicciones no es equivalente a una predicción fallida. La disponibilidad documental y la densidad de proposiciones cambian mucho entre venues; estas cifras no permiten una comparación de calidad predictiva entre conferencias.

## Reproducibilidad

- `work/influencia_sesiones_v1.3.csv`: eliminación de cada sesión, fila por fila.
- `work/escenarios_indeterminados_v1.3.csv`: identificación parcial de escenarios.
- `scripts/diagnosticos_adicionales_v1_3.py`: generación determinista.
- Juicios y citas originales: registros v1.0, sin cambios.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")
    print(f"Generados: {INFLUENCE.name}, {SCENARIOS.name}, {REPORT.name}")


if __name__ == "__main__":
    main()
