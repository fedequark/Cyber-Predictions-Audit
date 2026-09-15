"""One-time, metadata-only URL availability snapshot; never downloads source bodies."""

from __future__ import annotations

import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATE = datetime.now(timezone.utc).date().isoformat()
INPUT = ROOT / "work" / "inventario_fuentes_v1.2.csv"
CSV_OUTPUT = ROOT / "work" / f"estado_enlaces_fuentes_{DATE}.csv"
REPORT = ROOT / "outputs" / f"revision_disponibilidad_fuentes_{DATE}.md"
if CSV_OUTPUT.exists() or REPORT.exists():
    raise SystemExit(f"La foto {DATE} ya existe; no se sobrescribe una observación publicada.")


def probe(row: dict[str, str]) -> dict[str, str | int]:
    url = row["url"]
    method = "HEAD"
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        request = Request(url, method=method, headers={"User-Agent": "CyberPredictionsAudit/1.4 (research link check; metadata only)"})
        with urlopen(request, timeout=12) as response:
            code, final = response.status, response.url
    except HTTPError as error:
        code, final = error.code, error.url
        if code == 405:
            method = "GET_HEADERS_ONLY"
            try:
                request = Request(url, method="GET", headers={"User-Agent": "CyberPredictionsAudit/1.4 (research link check; metadata only)"})
                with urlopen(request, timeout=12) as response:
                    code, final = response.status, response.url
            except HTTPError as retry_error:
                code, final = retry_error.code, retry_error.url
            except (URLError, TimeoutError, OSError) as retry_error:
                return {"source_role": row["source_role"], "url": url, "checked_at_utc": stamp,
                        "method": method, "http_status": "", "availability": "network_error",
                        "final_url": "", "error_type": type(retry_error).__name__}
    except (URLError, TimeoutError, OSError) as error:
        return {"source_role": row["source_role"], "url": url, "checked_at_utc": stamp,
                "method": method, "http_status": "", "availability": "network_error",
                "final_url": "", "error_type": type(error).__name__}

    if 200 <= code < 400:
        category = "http_success"
    elif code in (401, 403, 429):
        category = "blocked_or_rate_limited"
    elif code in (404, 410):
        category = "http_not_found"
    else:
        category = "http_error"
    return {"source_role": row["source_role"], "url": url, "checked_at_utc": stamp,
            "method": method, "http_status": code, "availability": category,
            "final_url": final, "error_type": ""}


with INPUT.open(encoding="utf-8", newline="") as handle:
    inventory = list(csv.DictReader(handle))
assert len(inventory) == 218
results = []
with ThreadPoolExecutor(max_workers=6) as pool:
    futures = {pool.submit(probe, row): row["url"] for row in inventory}
    for future in as_completed(futures):
        results.append(future.result())
results.sort(key=lambda row: (row["source_role"], row["url"]))

fields = ["source_role", "url", "checked_at_utc", "method", "http_status", "availability", "final_url", "error_type"]
with CSV_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(results)

counts = Counter(row["availability"] for row in results)
lines = [
    f"# Revisión de disponibilidad de enlaces ({DATE})", "",
    "**Alcance:** 218 combinaciones rol–URL del inventario v1.2. Se consultaron únicamente encabezados HTTP. No se descargó ni archivó el contenido y no se verificó que cada URL siga respaldando la proposición.",
    "", "| Resultado de la consulta | Entradas |", "|---|---:|",
]
for category in ("http_success", "blocked_or_rate_limited", "http_not_found", "http_error", "network_error"):
    lines.append(f"| {category} | {counts[category]} |")
lines += [
    "", "Una respuesta 200 sólo indica acceso HTTP en este momento, no preservación ni validez de evidencia. Un 403, 429 o fallo de red tampoco prueba desaparición: puede ser una política anti-bots o un error transitorio. Los casos no accesibles requieren revisión manual y una fuente archivada o alternativa legal.",
    "", f"Detalle: `work/estado_enlaces_fuentes_{DATE}.csv`.", "",
]
REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
print(f"Verificados {len(results)} localizadores; resumen: {dict(counts)}")
