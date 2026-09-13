#!/usr/bin/env python3
"""Genera la capa analítica post hoc v1.2 sin modificar los CSV congelados."""

from __future__ import annotations

import csv
import hashlib
import math
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
EXTRACTION = ROOT / "work" / "registro_extraccion_congelado_v1.0.csv"
EVALUATION = ROOT / "work" / "evaluacion_desenlaces_v1.0.csv"
SELECTION = ROOT / "work" / "orden_seleccion_s3_v0.2.csv"
DERIVED = ROOT / "work" / "analisis_derivado_v1.2.csv"
METRICS = ROOT / "work" / "metricas_robustez_v1.2.csv"
SOURCES = ROOT / "work" / "inventario_fuentes_v1.2.csv"
REPORT = ROOT / "outputs" / "analisis_robustez_y_representatividad_v1.2.md"

SN_TITLES = re.compile(r"^Security Nightmares(?:\s|$)", re.IGNORECASE)
NUMBER_DETAIL = re.compile(
    r"(?:\d|%|percent|per cent|majority|minority|half|third|quarter|"
    r"double|triple|million|billion|most|least|more than|less than)",
    re.IGNORECASE,
)
HIGH_DIFFICULTY = {
    "count", "trend", "prevalence", "proportion", "share", "record",
    "direction_and_mechanism", "conjunctive_occurrence", "compound_state",
    "persistence_and_adoption", "policy_consequence",
}
MEDIUM_DIFFICULTY = {
    "direction", "adoption", "design_feature", "nonoccurrence",
    "non_occurrence", "persistence", "occurrence_and_breadth",
    "salience_and_occurrence", "textual_similarity",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def prediction_key(row: dict[str, str]) -> str:
    return f"{int(row['selection_order'])}-{row['session_id']}-{row['candidate_order']}"


def wilson(k: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    p = k / n
    den = 1 + z * z / n
    center = (p + z * z / (2 * n)) / den
    radius = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return center - radius, center + radius


def binomial_two_sided(k: int, n: int, p: float = 0.5) -> float:
    observed = math.comb(n, k) * p**k * (1 - p) ** (n - k)
    probs = [math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(n + 1)]
    return min(1.0, sum(value for value in probs if value <= observed + 1e-15))


def inv_logit(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, -35, 35)
    return 1 / (1 + np.exp(-x))


def clustered_logit(
    x: np.ndarray, y: np.ndarray, clusters: list[str]
) -> tuple[np.ndarray, np.ndarray]:
    beta = np.zeros(x.shape[1])
    for _ in range(100):
        p = inv_logit(x @ beta)
        w = np.clip(p * (1 - p), 1e-8, None)
        hessian = x.T @ (w[:, None] * x)
        step = np.linalg.pinv(hessian) @ (x.T @ (y - p))
        beta += step
        if float(np.max(np.abs(step))) < 1e-9:
            break
    p = inv_logit(x @ beta)
    bread = np.linalg.pinv(x.T @ ((p * (1 - p))[:, None] * x))
    scores: dict[str, np.ndarray] = defaultdict(lambda: np.zeros(x.shape[1]))
    for row, residual, cluster in zip(x, y - p, clusters):
        scores[cluster] += row * residual
    meat = sum((s[:, None] @ s[None, :]) for s in scores.values())
    g = len(scores)
    n, q = x.shape
    correction = (g / (g - 1)) * ((n - 1) / (n - q)) if g > 1 and n > q else 1
    covariance = correction * bread @ meat @ bread
    return beta, np.sqrt(np.clip(np.diag(covariance), 0, None))


def pct(value: float) -> str:
    return f"{100 * value:.1f}".replace(".", ",") + "%"


def num(value: float, digits: int = 2) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def main() -> None:
    extraction = read_csv(EXTRACTION)
    evaluation = read_csv(EVALUATION)
    selection = read_csv(SELECTION)
    if (len(extraction), len(evaluation), len(selection)) != (120, 120, 138):
        raise SystemExit("Los tamaños de los registros canónicos no coinciden con 120/120/138.")

    frame = {row["frame_id"]: row for row in selection}
    frame["CCC-2013-034"] = frame["CCC-2013-043"]
    outcomes = {row["prediction_key"]: row for row in evaluation}
    records: list[dict[str, object]] = []
    for source in extraction:
        key = prediction_key(source)
        outcome = outcomes[key]
        session = frame[source["session_id"]]
        try:
            start = date.fromisoformat(source["horizon_start"])
            deadline = date.fromisoformat(source["deadline"])
            horizon_days: int | str = (deadline - start).days
        except ValueError:
            horizon_days = ""
        original = source["verbatim_text"]
        components = {
            "directamente_puntuable": source["prediction_class"] == "A",
            "detalle_numerico_original": bool(NUMBER_DETAIL.search(original)),
            "horizonte_explicito": bool(source["horizon_literal"].strip()),
            "poblacion_y_geografia": bool(source["population"].strip() and source["geography"].strip()),
        }
        specificity = sum(components.values())
        ptype = source["prediction_type"]
        difficulty = "alta" if ptype in HIGH_DIFFICULTY else "media" if ptype in MEDIUM_DIFFICULTY else "baja"
        records.append({
            "prediction_key": key,
            "session_id_original": source["session_id"],
            "session_id_normalized": session["frame_id"],
            "venue": session["venue"],
            "session_title": session["title"],
            "session_year": int(session["year"]),
            "security_nightmares": int(bool(SN_TITLES.match(session["title"]))),
            "judgment": outcome["judgment"],
            "resolvable": int(outcome["judgment"] != "indeterminate"),
            "fulfilled_binary": 1 if outcome["judgment"] == "fulfilled" else 0 if outcome["judgment"] == "not_fulfilled" else "",
            "prediction_class": source["prediction_class"],
            "prediction_type": ptype,
            "evidence_strength": outcome["evidence_strength"],
            "horizon_days": horizon_days,
            "specificity_proxy_score": specificity,
            "specificity_proxy_band": "alta" if specificity >= 4 else "media" if specificity == 3 else "baja",
            "specificity_proxy_components": ";".join(name for name, yes in components.items() if yes),
            "difficulty_proxy": difficulty,
            "source_url": source["source_url"],
            "source_locator": source["source_timestamp_or_page"],
            "primary_evidence_url": outcome["primary_evidence_url"],
            "secondary_evidence_url": outcome["secondary_evidence_url"],
        })

    fields = list(records[0].keys())
    write_csv(DERIVED, records, fields)

    judgments = Counter(str(row["judgment"]) for row in records)
    k, failed, missing = judgments["fulfilled"], judgments["not_fulfilled"], judgments["indeterminate"]
    n = k + failed
    low, high = wilson(k, n)
    session_counts = Counter(str(row["session_id_normalized"]) for row in records)
    shares = [count / len(records) for count in session_counts.values()]
    hhi = sum(share * share for share in shares)
    effective_sessions = 1 / hhi
    sn = [row for row in records if row["security_nightmares"]]
    other = [row for row in records if not row["security_nightmares"]]

    rng = np.random.default_rng(20260913)
    sessions = sorted(session_counts)
    by_session = {s: [r for r in records if r["session_id_normalized"] == s and r["resolvable"]] for s in sessions}
    bootstrap = []
    for _ in range(20_000):
        sample = [row for s in rng.choice(sessions, len(sessions), replace=True) for row in by_session[s]]
        if sample:
            bootstrap.append(sum(int(row["fulfilled_binary"]) for row in sample) / len(sample))
    boot_low, boot_high = np.quantile(bootstrap, [0.025, 0.975])

    resolvable = [row for row in records if row["resolvable"]]
    year = np.array([float(row["session_year"]) for row in resolvable])
    specificity = np.array([float(row["specificity_proxy_score"]) for row in resolvable])
    difficulty = np.array([{"baja": 0, "media": 1, "alta": 2}[str(row["difficulty_proxy"])] for row in resolvable], dtype=float)
    standardize = lambda a: (a - a.mean()) / a.std(ddof=0) if a.std(ddof=0) else a * 0
    x = np.column_stack([
        np.ones(len(resolvable)),
        np.array([float(row["security_nightmares"]) for row in resolvable]),
        standardize(year), standardize(specificity), standardize(difficulty),
    ])
    y = np.array([float(row["fulfilled_binary"]) for row in resolvable])
    beta, se = clustered_logit(x, y, [str(row["session_id_normalized"]) for row in resolvable])
    terms = ["Intercepto", "Security Nightmares", "Año (1 DE)", "Especificidad proxy (1 DE)", "Dificultad proxy (1 DE)"]
    model_rows = []
    for term, coefficient, error in zip(terms, beta, se):
        model_rows.append({
            "term": term,
            "odds_ratio": math.exp(coefficient),
            "ci_low": math.exp(coefficient - 1.96 * error),
            "ci_high": math.exp(coefficient + 1.96 * error),
            "coefficient": coefficient,
            "cluster_robust_se": error,
        })

    metric_rows: list[dict[str, object]] = [
        {"metric": "fulfilled", "value": k, "denominator": 120, "analysis_status": "confirmatory"},
        {"metric": "not_fulfilled", "value": failed, "denominator": 120, "analysis_status": "confirmatory"},
        {"metric": "indeterminate", "value": missing, "denominator": 120, "analysis_status": "confirmatory"},
        {"metric": "resolved_fulfilled_rate", "value": k / n, "denominator": n, "analysis_status": "confirmatory"},
        {"metric": "wilson_95_low", "value": low, "denominator": n, "analysis_status": "confirmatory"},
        {"metric": "wilson_95_high", "value": high, "denominator": n, "analysis_status": "confirmatory"},
        {"metric": "all_indeterminate_fail", "value": k / 120, "denominator": 120, "analysis_status": "confirmatory_sensitivity"},
        {"metric": "all_indeterminate_success", "value": (k + missing) / 120, "denominator": 120, "analysis_status": "confirmatory_sensitivity"},
        {"metric": "cluster_bootstrap_95_low", "value": boot_low, "denominator": len(sessions), "analysis_status": "exploratory"},
        {"metric": "cluster_bootstrap_95_high", "value": boot_high, "denominator": len(sessions), "analysis_status": "exploratory"},
        {"metric": "session_hhi", "value": hhi, "denominator": len(sessions), "analysis_status": "exploratory"},
        {"metric": "effective_session_count", "value": effective_sessions, "denominator": len(sessions), "analysis_status": "exploratory"},
        {"metric": "binomial_p_vs_50pct", "value": binomial_two_sided(k, n), "denominator": n, "analysis_status": "exploratory_reference_only"},
    ]
    for row in model_rows:
        metric_rows.extend([
            {"metric": f"logit_or::{row['term']}", "value": row["odds_ratio"], "denominator": n, "analysis_status": "exploratory"},
            {"metric": f"logit_ci_low::{row['term']}", "value": row["ci_low"], "denominator": n, "analysis_status": "exploratory"},
            {"metric": f"logit_ci_high::{row['term']}", "value": row["ci_high"], "denominator": n, "analysis_status": "exploratory"},
        ])
    write_csv(METRICS, metric_rows, ["metric", "value", "denominator", "analysis_status"])

    source_inventory: dict[tuple[str, str], dict[str, object]] = {}
    source_lookup = {prediction_key(row): row for row in extraction}
    for row in records:
        key = str(row["prediction_key"])
        original = source_lookup[key]
        outcome = outcomes[key]
        candidates = [
            ("prediction_source", str(row["source_url"]), original["verbatim_text"] + "\n" + original["context_text"]),
            ("primary_outcome_evidence", str(row["primary_evidence_url"]), outcome["evidence_summary"] + "\n" + outcome["threshold_application"]),
            ("secondary_outcome_evidence", str(row["secondary_evidence_url"]), outcome["evidence_summary"] + "\n" + outcome["threshold_application"]),
        ]
        for role, url, capsule in candidates:
            if not url:
                continue
            inventory_key = (role, url)
            item = source_inventory.setdefault(inventory_key, {
                "source_role": role,
                "url": url,
                "prediction_keys": [],
                "source_locators": [],
                "_capsules": [],
                "preservation_level": "locator_and_text_capsule",
                "archived_copy_url": "",
                "archive_status": "pending_external_archive",
            })
            item["prediction_keys"].append(key)
            item["_capsules"].append(capsule)
            if role == "prediction_source" and row["source_locator"]:
                item["source_locators"].append(str(row["source_locator"]))
    inventory_rows = []
    for item in source_inventory.values():
        capsules = sorted(set(item.pop("_capsules")))
        item["prediction_keys"] = ";".join(sorted(set(item["prediction_keys"])))
        item["source_locators"] = ";".join(sorted(set(item["source_locators"])))
        item["preserved_capsule_count"] = len(capsules)
        item["preserved_text_capsule_sha256"] = hashlib.sha256(
            "\n\n--- CAPSULE ---\n\n".join(capsules).encode("utf-8")
        ).hexdigest().upper()
        inventory_rows.append(item)
    inventory_rows.sort(key=lambda row: (str(row["source_role"]), str(row["url"])))
    write_csv(SOURCES, inventory_rows, list(inventory_rows[0].keys()))

    def group_rate(rows: list[dict[str, object]]) -> tuple[int, int, int, float]:
        counts = Counter(str(row["judgment"]) for row in rows)
        resolved = counts["fulfilled"] + counts["not_fulfilled"]
        return counts["fulfilled"], counts["not_fulfilled"], counts["indeterminate"], counts["fulfilled"] / resolved

    sn_stats, other_stats = group_rate(sn), group_rate(other)
    specificity_table = []
    for band in ("baja", "media", "alta"):
        rows = [row for row in records if row["specificity_proxy_band"] == band]
        if rows:
            specificity_table.append((band, len(rows), *group_rate(rows)))
    difficulty_table = []
    for band in ("baja", "media", "alta"):
        rows = [row for row in records if row["difficulty_proxy"] == band]
        if rows:
            difficulty_table.append((band, len(rows), *group_rate(rows)))

    model_md = "\n".join(
        f"| {row['term']} | {num(row['odds_ratio'])} | {num(row['ci_low'])}–{num(row['ci_high'])} |"
        for row in model_rows[1:]
    )
    specificity_md = "\n".join(
        f"| {band.capitalize()} | {total} | {ok} | {fail} | {ind} | {pct(rate)} |"
        for band, total, ok, fail, ind, rate in specificity_table
    )
    difficulty_md = "\n".join(
        f"| {band.capitalize()} | {total} | {ok} | {fail} | {ind} | {pct(rate)} |"
        for band, total, ok, fail, ind, rate in difficulty_table
    )
    source_types = Counter(row["source_role"] for row in inventory_rows)
    report = f"""# Análisis de robustez y representatividad v1.2

**Fecha:** 13 de septiembre de 2026  
**Estado:** capa derivada post hoc. No modifica los registros congelados v1.0.

## 1. Incertidumbre y datos indeterminados

El estimando registrado se mantiene en **{k}/{n} = {pct(k/n)}** entre casos resolubles, con IC Wilson descriptivo de 95% **{pct(low)}–{pct(high)}**. Los {missing} casos indeterminados abren una banda extrema de **{pct(k/120)}–{pct((k+missing)/120)}**. Bastaría que 7 de los 31 indeterminados fueran cumplidos para que el resultado sobre los 120 casos superase 50%; por eso la indeterminación es parte central del resultado.

El remuestreo exploratorio por sesión (20.000 muestras, semilla `20260913`) produce un intervalo percentil de **{pct(float(boot_low))}–{pct(float(boot_high))}**. No es un intervalo poblacional: cuantifica fragilidad ante la composición de las 36 sesiones observadas.

## 2. Referencias base

No existe una línea base sustantiva reconstruible: las predicciones no traen probabilidades, alternativas mutuamente excluyentes ni una clase de referencia preregistrada. Se publican tres referencias para evitar confundirlas con *skill*:

| Referencia | Valor | Qué demuestra |
|---|---:|---|
| Moneda justa sobre los 89 resolubles | 50,0% | Referencia matemática; prueba binomial bilateral post hoc, p={num(binomial_two_sided(k,n), 3)} |
| Sorteo que reproduce la prevalencia observada | {pct((k/n)**2 + (failed/n)**2)} | Exactitud esperada de etiquetas aleatorias con la misma mezcla; no es un pronóstico histórico |
| “Siempre cumplida” sobre resolubles | {pct(k/n)} | Iguala el titular por construcción y muestra que la tasa sola no mide discriminación |

La conclusión correcta sigue siendo descriptiva. Una réplica prospectiva deberá registrar probabilidades y un baseline antes de observar desenlaces.

## 3. Representatividad y concentración

Las 120 predicciones provienen de 36 sesiones. El HHI por sesión es **{num(hhi, 3)}**, equivalente a sólo **{num(effective_sessions, 1)} sesiones de igual peso**. La familia *Security Nightmares* aporta {len(sn)}/120 ({pct(len(sn)/120)}).

| Estrato | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
| Security Nightmares | {len(sn)} | {sn_stats[0]} | {sn_stats[1]} | {sn_stats[2]} | {pct(sn_stats[3])} |
| Resto | {len(other)} | {other_stats[0]} | {other_stats[1]} | {other_stats[2]} | {pct(other_stats[3])} |

Esto no representa “todas las keynotes”: el marco fue documental, tres venues no son la industria completa y una serie domina la muestra.

## 4. Especificidad y dificultad: proxies auditables

Para no recodificar retrospectivamente el texto como si hubiera sido preregistrado, v1.2 publica proxies mecánicos. La especificidad suma cuatro señales: clase A directamente puntuable, detalle numérico en el original, horizonte explícito y población+geografía declaradas. La dificultad usa una tabla fija por `prediction_type`: ocurrencia/saliencia/capacidad como baja; dirección/adopción/no-ocurrencia como media; conteo/tendencia/prevalencia/proporción/mecanismo compuesto como alta. Son análisis exploratorios, no mediciones validadas.

| Especificidad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
{specificity_md}

| Dificultad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
{difficulty_md}

## 5. Modelo explicativo exploratorio

Se ajustó una regresión logística sobre los 89 casos resolubles, con errores sándwich agrupados por sesión. Los predictores fueron pertenencia a *Security Nightmares*, año, especificidad proxy y dificultad proxy; los tres últimos continuos se estandarizaron. Con 33 sesiones resolubles, el modelo es deliberadamente pequeño.

| Predictor | Odds ratio | IC 95% agrupado |
|---|---:|---:|
{model_md}

Los coeficientes describen asociación condicional en este corpus. No identifican causalidad ni habilidad de ponentes; el proxy de especificidad incorpora clase A/B y el de dificultad fue definido después de conocer el corpus.

## 6. Flujo de selección reconstruible

| Etapa | n | Estado de evidencia |
|---|---:|---|
| Sesiones en el marco cerrado | 189 | Documentado en protocolo/manuscrito |
| Sesiones con disponibilidad S3 | 138 | Registro fila por fila |
| Sesiones sin S3 | 51 | Diferencia documentada; no hay registro de exclusión individual en este paquete |
| Sesiones S3 revisadas | 138 | Orden de selección publicado |
| Sesiones que aportaron predicciones | 36 | Derivable del corpus |
| Predicciones incluidas | 120 | Registro congelado |
| Candidatos textuales excluidos | n.d. | No se preservó un registro; no puede reconstruirse honestamente |

El archivo `work/registro_candidatos_excluidos_template_v1.2.csv` fija el esquema para una réplica, pero no rellena retrospectivamente candidatos inexistentes.

## 7. Preservación de evidencia

El inventario contiene {len(inventory_rows)} localizadores únicos: {source_types['prediction_source']} fuentes de predicción, {source_types['primary_outcome_evidence']} fuentes primarias de desenlace y {source_types['secondary_outcome_evidence']} secundarias. Cada entrada enlaza las claves afectadas y un SHA-256 de la cápsula textual ya preservada en los CSV. Esto protege identificación y texto auditado, no los bytes originales del recurso remoto. El archivado WARC/PDF/captura sigue pendiente de una operación externa y se marca explícitamente como tal.

## 8. Separación confirmatoria/exploratoria

| Componente | Estado |
|---|---|
| 54/35/31; 54/89; Wilson; extremos 45,0–70,8 | Confirmatorio según protocolo operativo |
| Sensibilidad sólo clase A | Prevista, potencia insuficiente |
| Análisis por sesión, concentración, proxies, referencias base y regresión | Exploratorio/post hoc |
| Doble codificación | Prevista y pendiente; fuera de v1.2 por decisión del autor |

## Artefactos reproducibles

- `work/analisis_derivado_v1.2.csv`: una fila por predicción con variables derivadas.
- `work/metricas_robustez_v1.2.csv`: estimaciones y estado analítico.
- `work/inventario_fuentes_v1.2.csv`: inventario de localizadores y cápsulas preservadas.
- `scripts/analizar_robustez_v1_2.py`: generación determinista de esta capa.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")
    print(f"Generados: {DERIVED.name}, {METRICS.name}, {SOURCES.name}, {REPORT.name}")


if __name__ == "__main__":
    main()
