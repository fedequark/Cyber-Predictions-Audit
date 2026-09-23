#!/usr/bin/env python3
"""Traduce los textos visibles de la revisión sin tocar los CSV originales."""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

import requests

from generar_revision_humana_ia_v1_0 import BASE, build_tasks


CACHE = BASE / "TRADUCCIONES_ES.json"
URL = "https://api.deepseek.com/chat/completions"
FIELDS = ("verbatim", "context", "restatement", "indicator", "success", "contradiction", "missing_rule")
VOTE_FIELDS = ("rationale", "caveat")


def key_for(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def source_strings() -> dict[str, str]:
    values = {}
    for task in build_tasks():
        for field in FIELDS:
            value = task[field]
            if value:
                values[key_for(value)] = value
        for vote in task["votes"].values():
            for field in VOTE_FIELDS:
                value = vote[field]
                if value:
                    values[key_for(value)] = value
    return values


def translate(api_key: str, batch: list[tuple[str, str]]) -> tuple[dict[str, str], str]:
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": (
                "Sos un traductor técnico para una auditoría académica de predicciones de ciberseguridad. "
                "Traducí cada texto al español claro y fiel. Conservá exactamente nombres propios, "
                "URLs, cifras, fechas, porcentajes, operadores de umbral, negaciones, modalidad "
                "(posibilidad frente a certeza), alcance, plazo y distinción entre ausencia de prueba y prueba de ausencia. "
                "Traducí también las citas en alemán o inglés. No añadas hechos ni corrijas el contenido. "
                "Las frases incompletas y puntos suspensivos deben seguir siendo incompletos. "
                "Devolvé sólo JSON válido con una clave 'translations', un objeto cuyos identificadores "
                "sean los recibidos y cuyos valores sean traducciones en español."
            )},
            {"role": "user", "content": json.dumps({
                "translations": [{"id": identifier, "original": value} for identifier, value in batch]
            }, ensure_ascii=False)},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "max_tokens": 12000,
    }
    for attempt in range(5):
        response = requests.post(
            URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=300,
        )
        if response.status_code == 200:
            body = response.json()
            content = body["choices"][0]["message"]["content"]
            if body["choices"][0]["finish_reason"] != "stop" or not content:
                raise RuntimeError("Respuesta de traducción incompleta")
            translations = json.loads(content)["translations"]
            expected = {identifier for identifier, _ in batch}
            if set(translations) != expected or any(not isinstance(v, str) or not v.strip() for v in translations.values()):
                raise RuntimeError("Respuesta con identificadores ausentes o traducciones vacías")
            return translations, body.get("model", "deepseek-chat")
        if response.status_code not in {429, 500, 502, 503, 504}:
            raise RuntimeError(f"Error HTTP {response.status_code}: {response.text[:300]}")
        time.sleep(2 ** attempt)
    raise RuntimeError("La API no respondió después de cinco intentos")


def main() -> None:
    api_key = os.environ["DEEPSEEK_API_KEY"]
    sources = source_strings()
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {
        "format": "cyber-predictions-review-translation-v1",
        "language": "es",
        "model": "",
        "items": {},
    }
    missing = [(identifier, value) for identifier, value in sources.items() if identifier not in cache["items"]]
    print(f"Textos: {len(sources)}; pendientes: {len(missing)}", flush=True)
    for offset in range(0, len(missing), 12):
        batch = missing[offset:offset + 12]
        translated, model = translate(api_key, batch)
        cache["model"] = model
        for identifier, original in batch:
            cache["items"][identifier] = {"original": original, "es": translated[identifier]}
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Traducidos: {min(offset + 12, len(missing))}/{len(missing)}", flush=True)


if __name__ == "__main__":
    main()
