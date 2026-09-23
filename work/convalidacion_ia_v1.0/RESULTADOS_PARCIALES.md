# Resultados de convalidación multi-IA v1.0

> **Actualización del 23 de septiembre de 2026:** el autor completó una revisión focal de 48 casos. Las decisiones y la comprobación de fuentes están en [CONCILIACION_REVISION_AUTOR_2026-09-23.md](CONCILIACION_REVISION_AUTOR_2026-09-23.md). Las tablas de abajo describen exclusivamente la fase previa de las cuatro IAs; la revisión posterior no las convierte en validación humana independiente ni modifica los 120 desenlaces canónicos.

**Fecha de congelación:** 22 de septiembre de 2026  
**Brazos:** Codex, Claude, DeepSeek y Gemini  
**Alcance por modelo:** 30 desenlaces, 8 búsquedas independientes y 30 controles semánticos.

Los cuatro brazos son no humanos. No sustituyen la doble codificación humana
preregistrada y sus errores pueden estar correlacionados.

## Ejecución e integridad

- Codex: contexto aislado; modelo declarado `gpt-5`.
- Claude: navegador; modelo visible `Claude Opus 5.5`, Medium.
- Gemini: navegador en modo visible Flash; la salida declaró `Gemini 1.5-Pro`,
  por lo que la versión queda como metadato no verificado.
- DeepSeek: API oficial; modelo devuelto `deepseek-flash`, temperatura 0 y lotes
  estructurados de cinco filas.
- Los 12 CSV finales tienen exactamente 30/8/30 filas y ninguna fila desalineada.

## Desenlaces con evidencia suministrada

| Modelo | fulfilled | not_fulfilled | indeterminate | mixed |
|---|---:|---:|---:|---:|
| Codex | 12 | 11 | 7 | 0 |
| Claude | 18 | 6 | 5 | 1 |
| DeepSeek | 11 | 4 | 15 | 0 |
| Gemini | 23 | 7 | 0 | 0 |

| Par | Acuerdo | κ |
|---|---:|---:|
| Codex–Claude | 0,633 | 0,434 |
| Codex–DeepSeek | 0,633 | 0,467 |
| Codex–Gemini | 0,567 | 0,287 |
| Claude–DeepSeek | 0,667 | 0,502 |
| Claude–Gemini | 0,733 | 0,459 |
| DeepSeek–Gemini | 0,500 | 0,273 |

- Unanimidad 4/4: 12/30.
- Mayoría de al menos 3/4: 21/30.
- El acuerdo es sólo moderado y sensible al modelo. Los 18 casos no unánimes
  requieren adjudicación; no debe reemplazarse por voto automático.

Como referencia, Codex tuvo acuerdo 0,800 y κ=0,687 frente al registro original.

## Búsqueda independiente

| Modelo | fulfilled | not_fulfilled | indeterminate | mixed |
|---|---:|---:|---:|---:|
| Codex | 3 | 2 | 3 | 0 |
| Claude | 0 | 0 | 8 | 0 |
| DeepSeek | 6 | 1 | 1 | 0 |
| Gemini | 0 | 0 | 8 | 0 |

- Unanimidad 4/4: 1/8; mayoría de al menos 3/4: 3/8.
- Claude y Gemini declararon que no podían inspeccionar fuentes y marcaron los
  ocho casos `indeterminate`.
- DeepSeek no tuvo navegación en la API; sus seis `fulfilled` no cuentan como
  búsquedas independientes verificadas, aunque se le ordenó declarar esa limitación.
- Sólo Codex produjo una comprobación diagnóstica utilizable. Este componente
  multi-IA **no queda validado**.

## Fidelidad semántica

| Modelo | yes | no | uncertain |
|---|---:|---:|---:|
| Codex | 20 | 6 | 4 |
| Claude | 14 | 0 | 16 |
| DeepSeek | 22 | 0 | 8 |
| Gemini | 29 | 1 | 0 |

La dispersión (14–29 `yes`) es material. Todo caso con algún `no` o `uncertain`
debe ir a revisión humana focal, sin reconciliación automática por mayoría.

## Hashes SHA-256

| Modelo | desenlaces | búsqueda | fidelidad |
|---|---|---|---|
| Codex | `927D2C4A3D8F2BFD6E9B957B69A15EA53529006DDE3B28FA2249B89DAE43D491` | `D01DF37085BA01F2F87E83EFFDC5CB94BF86E431552FDB8DE0D1D6EF4A9585EC` | `CDF82E6E26EF432B4FDED3CCDB7AA549D4FD42D668FFAD3FE11AAED96E296E4E` |
| Claude | `F30F86B3F5FB3EBE52E3769A3FC3213C50EDCAEA4F94B1039BD0D1103471E016` | `D18215D97FF477CDA3AC3A480A268060B3CFD9904A56A1A849BA3C36F5F7D107` | `9623E8A6736EF5216C70FF6F5CC268957BA2A4616782B95A62718A853EB4B954` |
| DeepSeek | `DD45D02D170AB8F29C22918C8FEF2BAEC72AE516B6250D9BB1D53BF84581E25F` | `DCFA55C8EC1E4CE7B4851A11441FEAB2E45D87D1CFDB72305963FA7C685C5B66` | `DDFBBB96CBF089DD912226E7A43774805AB9197525AE9E0943C1A7B1F64C487C` |
| Gemini | `8AE9AF86D08CFD85F03F54BEABB5123EFCC079FB280E3A1B3039C57508262647` | `CADDBE062C363E37BA1022D29E2060007AE4BDB6701661BB43B3B289A71C9AA3` | `ABAE1A793CC1F9AA02F059C9202CB48BD64A59D93F847A9920E3192E0951E4EA` |

## Decisión operativa

La convalidación multi-IA sirve para priorizar revisión, no para cerrar el
sesgo de codificador. Revisar primero los 18 desenlaces sin unanimidad y todos
los casos semánticos con algún `no` o `uncertain`, mediante adjudicación humana
breve, ciega y documentada. El veredicto general permanece **Weak Reject** hasta
resolver los bloqueantes humanos y de trazabilidad ya identificados.
