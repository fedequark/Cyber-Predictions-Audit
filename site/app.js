const translations = {
  fulfilled: { es: 'Cumplida', en: 'Fulfilled' },
  not_fulfilled: { es: 'Incumplida', en: 'Not fulfilled' },
  indeterminate: { es: 'Indeterminada', en: 'Indeterminate' },
  mixed: { es: 'Mixta', en: 'Mixed' },
};
let language = 'es';
let records = [];
let visible = 12;
let sourceChecks = new Map();
let sourceAlternatives = new Map();
let sourceCandidates = new Map();

function parseCsv(text) {
  const rows = [];
  let row = [], field = '', quoted = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i], next = text[i + 1];
    if (quoted) {
      if (c === '"' && next === '"') { field += '"'; i++; }
      else if (c === '"') quoted = false;
      else field += c;
    } else if (c === '"') quoted = true;
    else if (c === ',') { row.push(field); field = ''; }
    else if (c === '\n') { row.push(field.replace(/\r$/, '')); rows.push(row); row = []; field = ''; }
    else field += c;
  }
  if (field || row.length) { row.push(field); rows.push(row); }
  const headers = rows.shift();
  return rows.filter(r => r.length > 1).map(r => Object.fromEntries(headers.map((header, i) => [header, r[i] ?? ''])));
}

function keyOf(row) { return `${Number(row.selection_order)}-${row.session_id}-${row.candidate_order}`; }
function escapeHtml(value = '') {
  return String(value).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
function link(url, label) {
  return /^https?:\/\//i.test(url || '') ? `<a href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${label}</a>` : '';
}
function checkFor(role, url) { return sourceChecks.get(`${role}|${url}`); }
function checkLabel(role, url) {
  if (!url) return language === 'es' ? 'Sin URL registrada' : 'No URL recorded';
  const check = checkFor(role, url);
  if (!check) return language === 'es' ? 'No figura en la consulta v1.4' : 'Not included in the v1.4 check';
  const date = check.checked_at_utc.slice(0, 10);
  if (check.availability === 'http_success') return `HTTP ${escapeHtml(check.http_status)} · ${date}`;
  if (check.availability === 'http_not_found') return `HTTP ${escapeHtml(check.http_status)} · ${date} · ${language === 'es' ? 'revisar' : 'review'}`;
  if (check.availability === 'blocked_or_rate_limited') return `HTTP ${escapeHtml(check.http_status)} · ${date} · ${language === 'es' ? 'consulta bloqueada' : 'check blocked'}`;
  return `${escapeHtml(check.availability)} · ${date} · ${language === 'es' ? 'verificar manualmente' : 'verify manually'}`;
}
function challengeLink(key) {
  const params = new URLSearchParams({
    title: `Evidence challenge: ${key}`,
    body: `Prediction key: ${key}\n\nSource URL and exact locator:\n\nFrozen threshold affected:\n\nProposed correction and reason:\n\nPlease do not paste third-party content without permission.`,
  });
  return `https://github.com/fedequark/Cyber-Predictions-Audit/issues/new?${params}`;
}
function evidenceLine(label, url, role) {
  const availability = checkLabel(role, url);
  const alternative = sourceAlternatives.get(`${role}|${url}`);
  const alternativeLink = alternative
    ? `<span class="source-alternative">${link(alternative.alternate_url, language === 'es' ? 'Alternativa oficial del orden S3 (HTTP 200)' : 'Official S3-order alternative (HTTP 200)')}</span>`
    : '';
  const candidate = sourceCandidates.get(`${role}|${url}`);
  const candidateLabel = candidate?.candidate_relation === 'same_release_publisher_archive'
    ? (language === 'es' ? 'Archivo oficial del mismo comunicado (HTTP 200)' : 'Official archive of the same release (HTTP 200)')
    : (language === 'es' ? 'Guía oficial relacionada, no idéntica (HTTP 200)' : 'Related official guidance, not identical (HTTP 200)');
  const candidateLink = candidate && !alternative
    ? `<span class="source-alternative">${link(candidate.publisher_candidate_url, candidateLabel)}</span>`
    : '';
  return `<div><strong>${label}:</strong> ${link(url, language === 'es' ? 'Abrir fuente original' : 'Open original source') || `<span>${language === 'es' ? 'no registrada' : 'not recorded'}</span>`}<span class="source-check">${availability}</span>${alternativeLink}${candidateLink}</div>`;
}
function renderCard(row) {
  const isSpanish = language === 'es';
  const rights = isSpanish ? 'La cita pertenece al ponente y queda fuera de la licencia CC BY 4.0 del research.' : 'The quote belongs to the speaker and is excluded from the research CC BY 4.0 license.';
  const semantics = row.prediction_class_frozen === 'B'
    ? (isSpanish ? 'Clase B: umbral operacionalizado; revisión semántica v1.4 no realizada.' : 'Class B: operationalized threshold; v1.4 semantic review not performed.')
    : (isSpanish ? 'Clase A: directamente puntuable según el registro congelado.' : 'Class A: directly scoreable in the frozen register.');
  const alias = row.session_id === 'CCC-2013-034'
    ? `<p class="case-alert">${isSpanish ? 'Inconsistencia de ID: el orden S3 llama a esta sesión CCC-2013-043; coinciden orden y URL oficial.' : 'ID inconsistency: the S3 order names this session CCC-2013-043; order and official URL match.'}</p>`
    : '';
  return `<article class="case" id="case-${escapeHtml(row.prediction_key)}">
    <div class="case-head"><div><span class="meta">${escapeHtml(row.prediction_key)} · ${escapeHtml(row.speaker)}</span><h3>${escapeHtml(row.atomic_restatement)}</h3></div><span class="badge ${escapeHtml(row.judgment)}">${translations[row.judgment]?.[language] || escapeHtml(row.judgment)}</span></div>
    <p class="meta">${escapeHtml(row.prediction_type)} · ${escapeHtml(row.deadline)} · ${escapeHtml(row.evidence_strength)} · ${escapeHtml(row.priority || 'P4')}</p>
    <details><summary>${isSpanish ? 'Abrir ficha de evidencia y regla de decisión' : 'Open evidence and decision-rule record'}</summary>
      <div class="case-grid"><div><h4>${isSpanish ? 'Afirmación original' : 'Original claim'}</h4>
        <blockquote>${escapeHtml(row.verbatim_text)}</blockquote><p class="meta">${rights} <a href="/rights.html">${isSpanish ? 'Derechos' : 'Rights'}</a></p>
        <p><strong>${isSpanish ? 'Localizador' : 'Locator'}:</strong> ${escapeHtml(row.source_timestamp_or_page || '—')}</p>
        <p><strong>${isSpanish ? 'Reformulación congelada' : 'Frozen restatement'}:</strong> ${escapeHtml(row.atomic_restatement)}</p>
        <p><strong>${isSpanish ? 'Indicador' : 'Indicator'}:</strong> ${escapeHtml(row.indicator_frozen)}</p>
        <p><strong>${isSpanish ? 'Éxito' : 'Success'}:</strong> ${escapeHtml(row.threshold_success_frozen)}</p>
        <p><strong>${isSpanish ? 'Contradicción' : 'Contradiction'}:</strong> ${escapeHtml(row.threshold_contradiction_frozen)}</p>
        <p class="meta">${semantics}</p>${alias}</div>
      <div><h4>${isSpanish ? 'Desenlace y trazabilidad' : 'Outcome and traceability'}</h4>
        <p><strong>${isSpanish ? 'Periodo probatorio' : 'Evidence period'}:</strong> ${escapeHtml(row.evidence_date_or_period || '—')}</p>
        <p><strong>${isSpanish ? 'Fuentes admisibles' : 'Admissible sources'}:</strong> ${escapeHtml(row.admissible_outcome_source_type)}</p>
        <p><strong>${isSpanish ? 'Aplicación del umbral' : 'Threshold application'}:</strong> ${escapeHtml(row.threshold_application)}</p>
        <p><strong>${isSpanish ? 'Conflicto o ausencia' : 'Conflict or absence'}:</strong> ${escapeHtml(row.conflict_or_missing_application)}</p>
        <p><strong>${isSpanish ? 'Síntesis de evidencia' : 'Evidence summary'}:</strong> ${escapeHtml(row.evidence_summary)}</p>
        <div class="source-list">${evidenceLine(isSpanish ? 'Fuente de predicción' : 'Prediction source', row.source_url, 'prediction_source')}
          ${evidenceLine(isSpanish ? 'Desenlace primario' : 'Primary outcome', row.primary_evidence_url, 'primary_outcome_evidence')}
          ${evidenceLine(isSpanish ? 'Desenlace secundario' : 'Secondary outcome', row.secondary_evidence_url, 'secondary_outcome_evidence')}</div>
        <p class="meta">${isSpanish ? 'El estado HTTP es una comprobación de encabezados; no prueba validez ni preservación del contenido.' : 'HTTP status is a headers-only check; it does not prove validity or preservation.'}</p>
        <p><strong>${isSpanish ? 'Revisión pendiente' : 'Pending review'}:</strong> ${escapeHtml(row.review_action || '—')} (${escapeHtml(row.review_status || 'not_started')})</p>
        ${row.review_note_url?.startsWith('/documents/') ? `<p><a href="${escapeHtml(row.review_note_url)}">${isSpanish ? 'Leer búsqueda focal inicial' : 'Read initial focused search'}</a></p>` : ''}
        ${['39-CCC-2006-011-06', '31-VB-2016-P01-10', '34-CCC-2013-034-14'].includes(row.prediction_key)
          ? `<p><a href="/documents/seguimiento_documental_v1.4a.md">${isSpanish ? 'Leer seguimiento documental v1.4a' : 'Read documentary follow-up v1.4a'}</a></p>` : ''}
        ${link(challengeLink(row.prediction_key), isSpanish ? 'Impugnar esta evidencia en GitHub' : 'Challenge this evidence on GitHub')}
      </div></div>
    </details></article>`;
}
function render() {
  const q = document.querySelector('#search').value.toLowerCase();
  const judgment = document.querySelector('#judgment').value;
  const strength = document.querySelector('#strength').value;
  const priority = document.querySelector('#priority').value;
  const filtered = records.filter(row => (!judgment || row.judgment === judgment) && (!strength || row.evidence_strength === strength) && (!priority || row.priority === priority) && (!q || row.search.includes(q)));
  document.querySelector('#status').textContent = language === 'es'
    ? `${filtered.length} ${filtered.length === 1 ? 'predicción encontrada' : 'predicciones encontradas'}`
    : `${filtered.length} ${filtered.length === 1 ? 'prediction found' : 'predictions found'}`;
  document.querySelector('#cards').innerHTML = filtered.slice(0, visible).map(renderCard).join('');
  document.querySelector('#more').hidden = visible >= filtered.length;
}
function setLanguage(lang) {
  language = lang;
  document.documentElement.lang = lang;
  document.querySelectorAll('[data-es][data-en]').forEach(element => { element.textContent = element.dataset[lang]; });
  document.querySelectorAll('[data-lang]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.lang === lang)));
  document.querySelector('.big-number').innerHTML = lang === 'es' ? '60,7<span>%</span>' : '60.7<span>%</span>';
  document.title = lang === 'es' ? 'Cyber Predictions Audit — Auditoría retrospectiva' : 'Cyber Predictions Audit — Retrospective audit';
  render();
}
async function loadCsv(path) {
  const response = await fetch(path);
  if (!response.ok) throw Error(`${path}: HTTP ${response.status}`);
  return parseCsv(await response.text());
}
async function load() {
  try {
    const [extraction, outcomes, triage, operationalization, checks, alternatives, queue] = await Promise.all([
      loadCsv('/work/registro_extraccion_congelado_v1.0.csv'),
      loadCsv('/work/evaluacion_desenlaces_v1.0.csv'),
      loadCsv('/work/triage_evidencia_v1.4.csv'),
      loadCsv('/work/revision_compromiso_y_operacionalizacion_v1.4.csv'),
      loadCsv('/work/estado_enlaces_fuentes_2026-09-15.csv'),
      loadCsv('/work/alternativas_enlaces_fuentes_v1.4.csv'),
      loadCsv('/work/seguimiento_enlaces_fuentes_v1.4a.csv'),
    ]);
    if (extraction.length !== 120 || outcomes.length !== 120 || triage.length !== 120 || operationalization.length !== 120) throw Error('Corpus incompleto');
    sourceChecks = new Map(checks.map(row => [`${row.source_role}|${row.url}`, row]));
    sourceAlternatives = new Map(alternatives.map(row => [`${row.source_role}|${row.original_url}`, row]));
    sourceCandidates = new Map(queue.filter(row => row.publisher_candidate_url).map(row => [`${row.source_role}|${row.original_url}`, row]));
    const byExtraction = new Map(extraction.map(row => [keyOf(row), row]));
    const byTriage = new Map(triage.map(row => [row.prediction_key, row]));
    const byOperation = new Map(operationalization.map(row => [row.prediction_key, row]));
    records = outcomes.map(row => {
      const key = row.prediction_key;
      if (!byExtraction.has(key) || !byTriage.has(key) || !byOperation.has(key)) throw Error(`Falta clave ${key}`);
      const merged = { ...byExtraction.get(key), ...row, ...byTriage.get(key), ...byOperation.get(key) };
      merged.search = Object.values(merged).join(' ').toLowerCase();
      return merged;
    });
    render();
  } catch (error) {
    document.querySelector('#status').textContent = language === 'es' ? 'No se pudieron cargar los CSV. Usa las descargas de documentos.' : 'The CSV files could not be loaded. Use the document downloads.';
  }
}

document.querySelectorAll('[data-lang]').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.lang)));
['search', 'judgment', 'strength', 'priority'].forEach(id => document.querySelector(`#${id}`).addEventListener('input', () => { visible = 12; render(); }));
document.querySelector('#more').addEventListener('click', () => { visible += 12; render(); });
load();
