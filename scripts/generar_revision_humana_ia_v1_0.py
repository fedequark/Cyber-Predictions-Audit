#!/usr/bin/env python3
"""Genera una página local, autocontenida, para revisar la convalidación IA."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "work" / "convalidacion_ia_v1.0"
OUT = BASE / "REVISION_HUMANA.html"
MODELS = ("codex", "claude", "deepseek", "gemini")
FILES = {
    "desenlace": "desenlaces_30.csv",
    "semantica": "fidelidad_semantica_30.csv",
    "busqueda": "busqueda_independiente_8.csv",
}
TRANSLATIONS = BASE / "TRADUCCIONES_ES.json"
TRANSLATED_FIELDS = ("verbatim", "context", "restatement", "indicator", "success", "contradiction", "missing_rule")


def read(model: str, kind: str) -> dict[str, dict[str, str]]:
    with (BASE / model / FILES[kind]).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {row["prediction_key"]: row for row in rows}


def record(kind: str, key: str, rows: dict[str, dict[str, dict[str, str]]], phase: str, rank: int) -> dict:
    reference = rows["codex"][kind][key]
    field = "semantic_fidelity" if kind == "semantica" else "independent_judgment"
    return {
        "id": f"{kind}:{key}",
        "kind": kind,
        "phase": phase,
        "rank": rank,
        "key": key,
        "speaker": reference["speaker"],
        "verbatim": reference["verbatim_text"],
        "context": reference["context_text"],
        "restatement": reference["atomic_restatement"],
        "source_url": reference["source_url"],
        "timestamp": reference["source_timestamp_or_page"],
        "deadline": reference["deadline"],
        "indicator": reference["indicator_frozen"],
        "success": reference["threshold_success_frozen"],
        "contradiction": reference["threshold_contradiction_frozen"],
        "missing_rule": reference.get("missing_conflict_rule", ""),
        "provided_urls": list(dict.fromkeys(
            url for url in (
                reference.get("provided_primary_evidence_url", ""),
                reference.get("provided_secondary_evidence_url", ""),
            ) if url
        )),
        "votes": {model: {
            "judgment": rows[model][kind][key][field],
            "rationale": rows[model][kind][key].get("rationale", "") or rows[model][kind][key].get("evidence_summary", ""),
            "source": rows[model][kind][key].get("primary_evidence_url", ""),
            "caveat": rows[model][kind][key].get("search_log", ""),
        } for model in MODELS},
    }


def build_tasks() -> list[dict]:
    rows = {model: {kind: read(model, kind) for kind in FILES} for model in MODELS}
    tasks = []
    outcomes = rows["codex"]["desenlace"]
    for key in outcomes:
        counts = Counter(rows[model]["desenlace"][key]["independent_judgment"] for model in MODELS)
        if len(counts) > 1:
            rank = 0 if sorted(counts.values(), reverse=True) == [2, 2] else 1 if max(counts.values()) == 2 else 2
            tasks.append(record("desenlace", key, rows, "rapida" if rank == 0 else "prioritaria", rank))
    for key in rows["codex"]["semantica"]:
        votes = {rows[model]["semantica"][key]["semantic_fidelity"] for model in MODELS}
        if "no" in votes:
            tasks.append(record("semantica", key, rows, "rapida", 3))
        elif "uncertain" in votes:
            tasks.append(record("semantica", key, rows, "ampliacion", 4))
    for key in rows["codex"]["busqueda"]:
        tasks.append(record("busqueda", key, rows, "ampliacion", 5))
    return sorted(tasks, key=lambda task: (task["rank"], int(rows["codex"][task["kind"]][task["key"]]["selection_order"]), task["key"]))


def localize_tasks(tasks: list[dict]) -> None:
    cache = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))["items"]

    def polish(original: str, spanish: str) -> str:
        if "authoritative" in original.lower():
            spanish = re.sub(r"\bautorizad[oa]s?\b", "de referencia", spanish, flags=re.IGNORECASE)
            spanish = spanish.replace("de forma de referencia", "por una fuente de referencia")
        spanish = spanish.replace("que califican", "que cumplen los criterios")
        spanish = spanish.replace("que califica", "que cumple los criterios")
        spanish = spanish.replace("falla calificante", "falla que cumple los criterios")
        spanish = spanish.replace("ataques convencionales de mercancía", "ataques comunes")
        spanish = spanish.replace("malware convencional de mercancía", "malware común")
        spanish = spanish.replace("ataques de mercancía", "ataques comunes")
        spanish = spanish.replace("compromiso técnico", "intrusión técnica")
        spanish = spanish.replace("compromiso previo de la capa de aplicación", "intrusión previa en la capa de aplicación")
        return spanish

    def translated(value: str) -> str:
        if not value:
            return ""
        identifier = hashlib.sha256(value.encode("utf-8")).hexdigest()
        item = cache.get(identifier)
        if not item or item["original"] != value or not item["es"].strip():
            raise ValueError(f"Falta traducción verificada para {identifier}")
        return polish(value, item["es"])

    for task in tasks:
        task["original"] = {field: task[field] for field in TRANSLATED_FIELDS}
        for field in TRANSLATED_FIELDS:
            task[field] = translated(task[field])
        for vote in task["votes"].values():
            vote["original"] = {field: vote[field] for field in ("rationale", "caveat")}
            for field in ("rationale", "caveat"):
                vote[field] = translated(vote[field])


HTML = r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Revisión humana de predicciones</title>
<style>
:root {font-family: system-ui, Segoe UI, sans-serif; color:#172235; background:#f5f7fb}
* {box-sizing:border-box} body {margin:0} button,select,textarea,input {font:inherit}
header {background:#172235;color:white;padding:18px 24px} h1 {font-size:1.45rem;margin:0 0 6px} header p {margin:0;color:#d5ddeb}
.wrap {max-width:1240px;margin:auto;padding:22px;display:grid;grid-template-columns:250px minmax(0,1fr);gap:22px}
aside,main {min-width:0} .panel {background:white;border:1px solid #dce3ee;border-radius:12px;padding:18px;margin-bottom:16px;box-shadow:0 1px 3px #1722350b}
.side {position:sticky;top:16px}.muted {color:#5b687a}.small {font-size:.86rem}.tabs {display:grid;gap:7px;margin:15px 0}
button {cursor:pointer;border:1px solid #bfcbdc;border-radius:8px;padding:8px 11px;background:white;color:#172235}
button:hover {background:#edf3fb} button:focus-visible,select:focus-visible,textarea:focus-visible,input:focus-visible {outline:3px solid #68a7f8}
.tab.active,.primary {background:#1957a6;color:white;border-color:#1957a6}.primary:hover {background:#154883}.tab {text-align:left}
.row {display:flex;gap:9px;flex-wrap:wrap;align-items:center}.space {justify-content:space-between}.progress {height:10px;background:#e8edf5;border-radius:9px;overflow:hidden;margin:7px 0 11px}.progress div {height:100%;background:#20845b}
.list {max-height:50vh;overflow:auto;display:grid;gap:5px}.item {width:100%;text-align:left;padding:9px;border-radius:8px;font-size:.88rem}.item.active {border-color:#1957a6;background:#edf4fd}.done {color:#14714c}
h2 {margin:0 0 9px;font-size:1.28rem} h3 {font-size:1rem;margin:20px 0 6px}.quote {border-left:3px solid #7999c2;padding:8px 12px;background:#f8faff;white-space:pre-wrap}
.value {white-space:pre-wrap;line-height:1.45;margin:4px 0 13px}.field {margin:14px 0}.field label {font-weight:650;display:block;margin-bottom:5px}
select,textarea,input[type=url] {width:100%;padding:9px;border:1px solid #bfcbdc;border-radius:7px;background:white} textarea {min-height:84px;resize:vertical}
a {color:#174f98;word-break:break-all}.bad {color:#a53422}.notice {background:#fff7df;border:1px solid #ead69a;border-radius:8px;padding:10px 12px;margin:12px 0}
.vote {border-top:1px solid #e4e8ef;padding:11px 0}.vote:first-child {border-top:0}.vote strong {display:inline-block;min-width:95px}
.badge {border-radius:30px;background:#e8edf5;padding:4px 9px;font-size:.82rem}.hidden {display:none}.actions {display:flex;gap:9px;flex-wrap:wrap;margin:15px 0}
@media(max-width:820px){.wrap{grid-template-columns:1fr;padding:12px}.side{position:static}.list{max-height:180px}}
</style>
</head>
<body>
<header><h1>Revisión humana de predicciones</h1><p>Empezá con 10 casos críticos. Tu decisión se registra antes de mostrar las IAs.</p></header>
<div class="wrap">
<aside><div class="panel side"><strong>Tu avance</strong><div id="progressText" class="small muted"></div><div class="progress"><div id="progressBar"></div></div>
<div class="tabs"><button class="tab active" data-phase="rapida">Ronda corta · 10</button><button class="tab" data-phase="prioritaria">Completar desacuerdos · 14</button><button class="tab" data-phase="ampliacion">Ampliación · 24</button></div>
<p class="small muted">La ronda corta contiene 4 empates de desenlace y 6 reformulaciones objetadas. La ampliación contiene 16 casos semánticos inciertos y 8 búsquedas.</p>
<div class="row"><button id="export">Exportar revisión</button><button id="importButton">Importar respaldo</button><input id="importFile" class="hidden" type="file" accept="application/json,.json"></div>
<p id="storageNote" class="small muted"></p><div id="taskList" class="list"></div></div></aside>
<main><div class="panel"><div class="row space"><span id="position" class="badge"></span><span id="status" class="small"></span></div><h2 id="heading"></h2><p id="intro" class="muted"></p>
<h3>Lo que se dijo, traducido al español</h3><div id="quote" class="quote"></div><p class="small"><a id="sourceLink" target="_blank" rel="noopener noreferrer">Abrir fuente original</a> <span id="timestamp"></span></p>
<h3>Contexto y reformulación</h3><p id="context" class="value"></p><p id="restatement" class="value"></p>
<div id="ruleBlock"><h3>Regla congelada</h3><p><strong>Plazo:</strong> <span id="deadline"></span></p><p><strong>Indicador:</strong> <span id="indicator"></span></p><p><strong>Se cumple si:</strong> <span id="success"></span></p><p><strong>Se contradice si:</strong> <span id="contradiction"></span></p><p id="missingWrap"><strong>Regla de conflicto:</strong> <span id="missing"></span></p></div>
<details><summary>Ver textos originales para comprobar la traducción</summary><div id="originalTexts" class="small"></div></details>
<div id="links"></div><div class="notice small">Elegí una decisión y el motivo que mejor la describe. Escribí sólo si necesitás agregar un dato concreto. Tu primera decisión se conserva aunque luego cambies la conclusión.</div>
<div id="initialForm"><div class="field"><label for="initial">Tu primera decisión</label><select id="initial"></select></div><div class="field"><label for="reasonChoice">¿Qué observaste?</label><select id="reasonChoice"></select></div><div class="field"><label for="reason">Aclaración opcional</label><textarea id="reason" placeholder="Por ejemplo: la fecha, el número o la frase que cambia el sentido."></textarea></div><div class="field"><label for="evidenceChoice">Fuente que consultaste, si corresponde</label><select id="evidenceChoice"></select><p class="small muted">Elegí una fuente de la lista sólo si la abriste y comprobaste.</p><input id="evidence" type="url" placeholder="O pegá otra URL: https://..."></div><div class="actions"><button id="freeze" class="primary">Guardar primera decisión y ver IAs</button></div><p id="formError" class="bad small"></p></div>
<div id="after" class="hidden"><h3>Tu decisión inicial</h3><p id="frozen" class="value"></p><button id="showVotes">Mostrar dictámenes de las IAs</button><div id="votes" class="hidden"></div>
<h3>Decisión final</h3><div class="field"><label for="final">Veredicto tras comparar</label><select id="final"></select></div><div class="field hidden" id="changeReasonWrap"><label for="changeReason">Si cambiaste de decisión, ¿por qué?</label><select id="changeReason"></select></div><div class="field"><label for="note">Aclaración final opcional</label><textarea id="note" placeholder="Anotá sólo algo que las opciones no expliquen."></textarea></div><div class="actions"><button id="complete" class="primary">Cerrar este caso</button><button id="next">Siguiente pendiente</button></div><p id="finalError" class="bad small"></p></div>
</div></main></div>
<script id="task-data" type="application/json">__DATA__</script>
<script>
const tasks=JSON.parse(document.getElementById('task-data').textContent);
const storageKey='cyber-predictions-human-review-v1';
let answers={}; let phase='rapida'; let current=tasks[0].id; let votesVisible=false;
try {answers=JSON.parse(localStorage.getItem(storageKey)||'{}');} catch {document.getElementById('storageNote').textContent='El guardado automático no está disponible. Exportá el archivo al terminar cada sesión.';}
const $=id=>document.getElementById(id);
const set=(id,value)=>{$(id).textContent=value||''};
function save(){try {localStorage.setItem(storageKey,JSON.stringify(answers));} catch {$('storageNote').textContent='No se pudo guardar automáticamente. Usá Exportar revisión.';}}
function options(kind){return kind==='semantica'?[['','Elegí una opción'],['yes','Sí, fiel'],['no','No, cambia el sentido'],['uncertain','No puedo determinarlo']]:[['','Elegí una opción'],['fulfilled','Se cumplió'],['not_fulfilled','No se cumplió'],['indeterminate','Indeterminado'],['mixed','Evidencia mixta']];}
function judgmentLabel(kind,value){return options(kind).find(([v])=>v===value)?.[1]||value;}
function fillOptions(el,kind,value){el.replaceChildren();for(const [v,label] of options(kind)){const opt=document.createElement('option');opt.value=v;opt.textContent=label;el.append(opt);}el.value=value||'';}
function reasonOptions(kind,decision){
if(kind==='semantica')return ({
yes:[['meaning','La reformulación conserva el sentido, el alcance y el plazo de la cita.']],
no:[['threshold','La reformulación agrega una cifra o un umbral que la cita no dice.'],['strength','La reformulación convierte una posibilidad en certeza o cambia su fuerza.'],['scope','La reformulación cambia la población, el lugar o el mecanismo.'],['time','La reformulación cambia el plazo.'],['prediction','La cita no formula una predicción verificable.'],['other','Hay otro cambio de sentido.']],
uncertain:[['ambiguous','La cita admite más de una interpretación.'],['context','Falta contexto para juzgar la reformulación.'],['translation','Necesito comprobar el idioma original.']]
})[decision]||[];
return ({
fulfilled:[['threshold_met','La fuente consultada documenta el hecho dentro del plazo y cumple el umbral.']],
not_fulfilled:[['threshold_short','La fuente consultada muestra que el hecho no alcanza el umbral.'],['too_late','El hecho documentado ocurrió después del plazo.'],['wrong_scope','La evidencia corresponde a otra población, lugar o mecanismo.']],
indeterminate:[['unavailable','No pude acceder a una fuente suficiente.'],['missing_measure','La fuente no permite medir el umbral exigido.'],['missing_date','No pude comprobar la fecha del hecho.'],['conflict','Las fuentes se contradicen y no puedo resolverlo.']],
mixed:[['mixed_sources','Hay fuentes favorables y contrarias de calidad comparable.'],['mixed_scope','La evidencia cumple una parte de la afirmación, pero no otra.']]
})[decision]||[];}
const changeOptions=[['','Elegí un motivo'],['new_source','Una fuente nueva cambió mi lectura.'],['rule','Releí el umbral o el plazo.'],['meaning','Releí la cita o su contexto.'],['ai_objection','Una objeción de las IAs me llevó a revisar la evidencia.'],['other','Otro motivo.']];
function fillChoices(el,choices,value){el.replaceChildren();for(const [v,label] of choices){const opt=document.createElement('option');opt.value=v;opt.textContent=label;el.append(opt);}el.value=value||'';}
function fillReasons(task,value){fillChoices($('reasonChoice'),[['','Elegí lo que observaste'],...reasonOptions(task.kind,$('initial').value)],value);}
function fillEvidence(task,evidence){const entries=[['','Sin fuente seleccionada'],...task.provided_urls.map((url,i)=>[url,'Fuente suministrada '+(i+1)+' · '+new URL(url).hostname]),['__other__','Otra URL']];fillChoices($('evidenceChoice'),entries,evidence?(task.provided_urls.includes(evidence)?evidence:'__other__'):'');}
function updateChangeReason(){const answer=answers[current]||{};$('changeReasonWrap').classList.toggle('hidden',!answer.initial||$('final').value===answer.initial);}
function label(task){return (task.kind==='desenlace'?'Desenlace':task.kind==='semantica'?'Sentido':'Búsqueda')+' · '+task.key;}
function phaseTasks(){return tasks.filter(t=>t.phase===phase);}
function updateNav(){const group=phaseTasks(), closed=group.filter(t=>answers[t.id]?.closed).length;$('progressText').textContent=`${closed} de ${group.length} casos cerrados`;$('progressBar').style.width=`${100*closed/group.length}%`;const list=$('taskList');list.replaceChildren();for(const task of group){const button=document.createElement('button');button.className='item'+(task.id===current?' active':'');button.textContent=(answers[task.id]?.closed?'✓ ':answers[task.id]?.initial?'◒ ':'○ ')+label(task);button.onclick=()=>{current=task.id;votesVisible=false;render();};list.append(button);}}
function appendLink(container,url,text){try {const parsed=new URL(url);if(!['http:','https:'].includes(parsed.protocol))return;const a=document.createElement('a');a.href=parsed.href;a.target='_blank';a.rel='noopener noreferrer';a.textContent=text||url;container.append(a);}catch{}}
function showVotes(task){const box=$('votes');box.replaceChildren();for(const [model,vote] of Object.entries(task.votes)){const div=document.createElement('div');div.className='vote';const strong=document.createElement('strong');strong.textContent=model[0].toUpperCase()+model.slice(1);const badge=document.createElement('span');badge.className='badge';badge.textContent=judgmentLabel(task.kind,vote.judgment);div.append(strong,badge);const p=document.createElement('p');p.className='small value';p.textContent=vote.rationale||'Sin justificación adicional';div.append(p);if(vote.source)appendLink(div,vote.source,'Fuente citada por la IA');if(vote.caveat){const c=document.createElement('p');c.className='small muted';c.textContent=vote.caveat;div.append(c);}const details=document.createElement('details');const summary=document.createElement('summary');summary.textContent='Ver justificación original de esta IA';details.append(summary);for(const field of ['rationale','caveat'])if(vote.original[field]){const original=document.createElement('p');original.className='small value';original.textContent=vote.original[field];details.append(original);}div.append(details);box.append(div);}box.classList.remove('hidden');$('showVotes').classList.add('hidden');votesVisible=true;}
function render(){const task=tasks.find(t=>t.id===current);if(!task)return;const answer=answers[task.id]||{};updateNav();const group=phaseTasks();set('position',`${group.findIndex(t=>t.id===task.id)+1} de ${group.length} · ${task.kind==='semantica'?'fidelidad semántica':task.kind==='busqueda'?'búsqueda':'desenlace'}`);set('status',answer.closed?'Cerrado':answer.initial?'Primera decisión guardada':'Pendiente');set('heading',label(task));set('intro',task.kind==='semantica'?'Decidí si la reformulación conserva el sentido de la cita, incluido alcance, plazo y fuerza modal.':task.kind==='busqueda'?'Investigá desde cero y registrá evidencia favorable y contraria. Las IAs sin navegación no cuentan como búsqueda verificada.':'Aplicá la regla congelada al hecho documentado antes de ver los dictámenes.');set('quote',task.verbatim);set('context',task.context);set('restatement',task.restatement);set('timestamp',task.timestamp?` · ${task.timestamp}`:'');set('deadline',task.deadline);set('indicator',task.indicator);set('success',task.success);set('contradiction',task.contradiction);set('missing',task.missing_rule);$('missingWrap').classList.toggle('hidden',!task.missing_rule);$('sourceLink').href=task.source_url;
const links=$('links');links.replaceChildren();if(task.provided_urls.length&&task.kind!=='busqueda'){const h=document.createElement('h3');h.textContent='Fuentes suministradas';links.append(h);for(const url of task.provided_urls){const p=document.createElement('p');appendLink(p,url,url);links.append(p);}}
const originals=$('originalTexts');originals.replaceChildren();for(const [field,title] of [['verbatim','Cita literal'],['context','Contexto'],['restatement','Afirmación'],['indicator','Indicador'],['success','Umbral de cumplimiento'],['contradiction','Umbral de contradicción'],['missing_rule','Regla de conflicto']])if(task.original[field]){const p=document.createElement('p');p.className='value';const bold=document.createElement('strong');bold.textContent=title+': ';p.append(bold,document.createTextNode(task.original[field]));originals.append(p);}
fillOptions($('initial'),task.kind,answer.initial);fillReasons(task,answer.reason_code);fillOptions($('final'),task.kind,answer.final||answer.initial);fillChoices($('changeReason'),changeOptions,answer.change_reason);updateChangeReason();$('reason').value=answer.reason_detail||'';$('evidence').value=answer.evidence||'';fillEvidence(task,answer.evidence);$('note').value=answer.note_detail??answer.note??'';set('frozen',answer.initial?`${judgmentLabel(task.kind,answer.initial)} · ${answer.reason}${answer.evidence?' · '+answer.evidence:''}`:'');$('initialForm').classList.toggle('hidden',!!answer.initial);$('after').classList.toggle('hidden',!answer.initial);$('votes').classList.add('hidden');$('showVotes').classList.remove('hidden');votesVisible=false;set('formError','');set('finalError','');}
function next(){const group=phaseTasks();const idx=group.findIndex(t=>t.id===current);const ordered=[...group.slice(idx+1),...group.slice(0,idx+1)];const target=ordered.find(t=>!answers[t.id]?.closed);if(target){current=target.id;render();}else alert('Terminaste esta pasada. Exportá la revisión para conservarla.');}
$('initial').onchange=()=>fillReasons(tasks.find(t=>t.id===current),'');
$('evidenceChoice').onchange=()=>{const chosen=$('evidenceChoice').value;if(chosen&&chosen!=='__other__')$('evidence').value=chosen;else if(!chosen)$('evidence').value='';else $('evidence').focus();};
$('final').onchange=updateChangeReason;
$('freeze').onclick=()=>{const task=tasks.find(t=>t.id===current);const initial=$('initial').value,reasonCode=$('reasonChoice').value,reasonDetail=$('reason').value.trim(),evidence=$('evidence').value.trim();const selected=reasonOptions(task.kind,initial).find(([code])=>code===reasonCode);if(!initial||!selected){set('formError','Elegí una decisión y un motivo. No hace falta redactar.');return;}if(evidence){try{const u=new URL(evidence);if(!['http:','https:'].includes(u.protocol))throw Error();}catch{set('formError','La fuente debe ser una URL web válida.');return;}}if(task.kind!=='semantica'&&['fulfilled','not_fulfilled'].includes(initial)&&!evidence){set('formError','Para decidir un desenlace, elegí una fuente que consultaste o pegá otra URL. Si aún no podés comprobarlo, elegí indeterminado.');return;}const reason=selected[1]+(reasonDetail?' '+reasonDetail:'');answers[current]={initial,reason_code:reasonCode,reason_detail:reasonDetail,reason,evidence,initial_at:new Date().toISOString(),final:initial,note:'',closed:false};save();render();};
$('showVotes').onclick=()=>showVotes(tasks.find(t=>t.id===current));
$('complete').onclick=()=>{const answer=answers[current],final=$('final').value,changeReason=$('changeReason').value,noteDetail=$('note').value.trim(),changed=final!==answer.initial;if(!final||(changed&&!changeReason&&!noteDetail)){set('finalError','Si cambiaste tu decisión, elegí un motivo o escribí una aclaración.');return;}const choice=changeOptions.find(([value])=>value===changeReason);const note=(changed&&choice?choice[1]+' ':'')+noteDetail;Object.assign(answer,{final,change_reason:changed?changeReason:'',note_detail:noteDetail,note:note.trim(),closed:true,closed_at:new Date().toISOString(),votes_viewed:votesVisible});save();next();};
$('next').onclick=next;
for(const tab of document.querySelectorAll('.tab'))tab.onclick=()=>{phase=tab.dataset.phase;for(const b of document.querySelectorAll('.tab'))b.classList.toggle('active',b===tab);current=phaseTasks().find(t=>!answers[t.id]?.closed)?.id||phaseTasks()[0].id;render();};
$('export').onclick=()=>{const payload={format:'cyber-predictions-human-review-v1',exported_at:new Date().toISOString(),answers};const blob=new Blob([JSON.stringify(payload,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='revision_humana_'+new Date().toISOString().slice(0,10)+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);};
$('importButton').onclick=()=>$('importFile').click();
$('importFile').onchange=async event=>{const file=event.target.files[0];if(!file)return;try{const payload=JSON.parse(await file.text());if(payload.format!=='cyber-predictions-human-review-v1'||!payload.answers||typeof payload.answers!=='object')throw Error('Formato incompatible');answers=payload.answers;save();render();}catch(error){alert('No se pudo importar: '+error.message);}event.target.value='';};
render();
</script>
</body></html>'''


def main() -> None:
    tasks = build_tasks()
    localize_tasks(tasks)
    payload = json.dumps(tasks, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    OUT.write_text(HTML.replace("__DATA__", payload), encoding="utf-8")
    counts = Counter(task["phase"] for task in tasks)
    print(f"{OUT}: {counts['rapida']} de ronda corta, {counts['prioritaria']} desacuerdos restantes, {counts['ampliacion']} de ampliación")


if __name__ == "__main__":
    main()
