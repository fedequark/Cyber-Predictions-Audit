import {
  ArrowDownRight,
  ArrowUpRight,
  CircleHelp,
  ExternalLink,
  Eye,
  FileText,
  ShieldCheck,
  X,
} from 'lucide-react';

const navItems = [
  ['Hallazgo', '#hallazgo'],
  ['Qué se midió', '#metodo'],
  ['Resultados', '#resultados'],
];

const resultRows = [
  { label: 'Cumplidas', count: 54, percent: '45,0%', color: 'var(--lime)' },
  { label: 'Incumplidas', count: 35, percent: '29,2%', color: 'var(--coral)' },
  { label: 'Indeterminadas', count: 31, percent: '25,8%', color: 'var(--mist)' },
];

const examples = [
  { verdict: 'Aparición', title: 'Gusanos móviles fuera del laboratorio', text: 'La predicción para 2006 exigía propagación autónoma en dispositivos reales. El umbral se cumplió.', key: '45-CCC-2005-006-02' },
  { verdict: 'Mecanismo', title: 'La huella no se mudó mayoritariamente a la nube', text: 'El tema apareció, pero el mecanismo previsto para los teléfonos de 2014 no alcanzó el umbral.', key: '34-CCC-2013-034-10' },
  { verdict: 'Prevalencia y fecha', title: 'eCall no fue mayoritario en 2016', text: 'La adopción posterior no rescata el plazo ni la cuota concreta fijados por la predicción.', key: '92-CCC-2014-045-01' },
];

export default function Home() {
  return (
    <main>
      <header className="site-header">
        <a className="brand" href="#inicio" aria-label="Inicio de la auditoría"><span className="brand-mark" aria-hidden="true">/</span><span>Futuro cyber<br />auditado</span></a>
        <nav className="top-nav" aria-label="Navegación principal">{navItems.map(([label, href]) => <a href={href} key={href}>{label}</a>)}</nav>
        <a className="header-link" href="#fuentes">Ver trazabilidad <ArrowDownRight size={16} /></a>
      </header>

      <section id="inicio" className="hero section-shell">
        <div className="eyebrow"><span /> Auditoría retrospectiva · 2005–2018</div>
        <div className="hero-grid">
          <div>
            <p className="hero-kicker">¿Qué queda cuando el futuro ya ocurrió?</p>
            <h1>Las conferencias cyber <em>vieron</em> venir los temas. No siempre supieron medirlos.</h1>
            <p className="hero-copy">Convertimos 120 predicciones explícitas en pruebas con fecha, umbral y evidencia. El resultado no es un ranking de gurús: es una auditoría de lo que el discurso prospectivo puede —y no puede— prometer.</p>
            <div className="hero-actions"><a className="button-primary" href="#hallazgo">Ver el hallazgo <ArrowDownRight size={18} /></a><a className="button-text" href="#metodo">Cómo se hizo <ArrowDownRight size={17} /></a></div>
          </div>
          <div className="hero-side" aria-label="Datos de alcance del estudio">
            <div className="hero-stat"><strong>120</strong><span>predicciones<br />con horizonte vencido</span></div>
            <div className="hero-stat"><strong>36</strong><span>sesiones de tres<br />conferencias</span></div>
            <div className="hero-stat"><strong>138</strong><span>sesiones S3<br />revisadas</span></div>
          </div>
        </div>
        <p className="hero-footnote">Black Hat USA · Chaos Communication Congress · Virus Bulletin</p>
      </section>

      <section id="hallazgo" className="verdict-section"><div className="section-shell verdict-grid">
        <div className="section-label"><span>01</span> El hallazgo</div>
        <div className="verdict-content"><p className="overline">Entre las predicciones resolubles</p><div className="big-result"><span>60,7</span><b>%</b></div><h2>superó el umbral fijado antes de mirar el desenlace.</h2><p className="verdict-copy">Son 54 cumplidas de 89 resolubles. Las otras 31 no se convirtieron automáticamente en fallos: no había evidencia suficiente para aplicar el umbral sin forzar una conclusión.</p><a className="inline-link" href="#resultados">Ver la distribución completa <ArrowDownRight size={17} /></a></div>
        <aside className="honesty-card"><CircleHelp size={22} /><p>Este número <strong>no</strong> estima la precisión de todas las keynotes ni prueba “habilidad predictiva”.</p><span>Es un descriptor de este corpus, condicionado a que cada caso pudiera resolverse.</span></aside>
      </div></section>

      <section id="metodo" className="section-shell method-section">
        <div className="section-label"><span>02</span> Qué se midió</div>
        <div className="method-lead"><h2>Una predicción no es una frase memorable. Es una afirmación que admite estar equivocada.</h2><p>Antes de buscar resultados, cada fila congeló la cita literal, la reformulación atómica, la fecha límite, el indicador, los umbrales y los tipos de fuente admisibles.</p></div>
        <div className="method-steps"><article><span>01</span><h3>Extraer</h3><p>Se revisaron las sesiones completas, siguiendo un orden previamente fijado.</p></article><article><span>02</span><h3>Congelar</h3><p>El corpus quedó bloqueado antes de habilitar la búsqueda de desenlaces.</p></article><article><span>03</span><h3>Contrastar</h3><p>Fuentes oficiales, técnicas y contemporáneas se aplicaron contra cada umbral.</p></article><article><span>04</span><h3>Conservar la duda</h3><p>Si la evidencia no resolvía el caso, quedó como indeterminado.</p></article></div>
        <div className="method-callout"><ShieldCheck size={20} /><p>El registro de extracción y la evaluación de desenlaces se conservaron como archivos separados, con hashes SHA-256 verificables.</p></div>
      </section>

      <section id="resultados" className="results-section"><div className="section-shell">
        <div className="section-label light"><span>03</span> Resultado completo</div>
        <div className="results-head"><h2>El resultado es una distribución, no un único titular.</h2><p>Las indeterminadas importan: hacen visible el coste de predecir con métricas vagas o fuentes históricas incompletas.</p></div>
        <div className="result-layout"><div className="result-chart" role="img" aria-label="54 cumplidas, 35 incumplidas y 31 indeterminadas"><div className="stacked-bar"><span className="bar-fulfilled" style={{ width: '45%' }} /><span className="bar-not" style={{ width: '29.2%' }} /><span className="bar-indeterminate" style={{ width: '25.8%' }} /></div><div className="result-rows">{resultRows.map((item) => <div className="result-row" key={item.label}><span className="legend-dot" style={{ background: item.color }} /><span>{item.label}</span><strong>{item.count}</strong><small>{item.percent}</small></div>)}</div></div><div className="sensitivity-card"><p className="overline">Sensibilidad a la incertidumbre</p><div><span>45,0%</span><p>si todas las indeterminadas fueran fallos</p></div><div className="sensitivity-main"><span>60,7%</span><p>análisis principal: se excluyen del denominador</p></div><div><span>70,8%</span><p>si todas las indeterminadas fueran aciertos</p></div></div></div>
        <p className="results-note">El intervalo Wilson descriptivo del análisis principal es 50,3–70,2%. Al considerar la agrupación por sesión en una comprobación exploratoria, el intervalo aproximado se amplía a 47,7–73,7%.</p>
      </div></section>

      <section id="lectura" className="section-shell reading-section">
        <div className="section-label"><span>04</span> La lectura útil</div>
        <div className="reading-grid"><div><p className="overline">No es lo mismo acertar que algo ocurrirá…</p><h2>…que acertar <em>cómo</em>, <em>cuánto</em> o <em>cuándo</em>.</h2></div><div className="dimension-list"><div><span className="dimension-number">01</span><h3>Aparición de un tema</h3><p>¿Ocurrió al menos un caso? Es la dimensión que el corpus resuelve con más frecuencia.</p></div><div><span className="dimension-number">02</span><h3>Mecanismo concreto</h3><p>¿Llegó por la arquitectura técnica que se anticipó?</p></div><div><span className="dimension-number">03</span><h3>Magnitud y prevalencia</h3><p>¿Alcanzó la cuota, el volumen o la difusión prometida?</p></div><div><span className="dimension-number">04</span><h3>Fecha</h3><p>¿Ocurrió dentro del plazo, en vez de suceder años después?</p></div></div></div>
        <div className="examples-grid">{examples.map((example) => <article className="example-card" key={example.key}><p>{example.verdict}</p><h3>{example.title}</h3><span>{example.text}</span><code>{example.key}</code></article>)}</div>
      </section>

      <section className="concentration-section"><div className="section-shell concentration-grid"><div className="section-label light"><span>05</span> Un resultado concentrado</div><div><h2>Una sola serie aporta<br /><strong>73 de 120</strong> predicciones.</h2><p><em>Security Nightmares</em> obtuvo 66,0% de acierto entre resolubles; el resto del corpus, 53,8%. La diferencia no demuestra que unos ponentes fueran mejores: también puede reflejar el formato, el tipo de tema y las tasas base.</p></div><div className="concentration-graphic" aria-hidden="true"><span className="concentration-major" /><span className="concentration-minor" /><p>60,8%<br /><small>Security Nightmares</small></p></div></div></section>

      <section id="limites" className="section-shell limits-section"><div className="section-label"><span>06</span> Límites que cambian la lectura</div><div className="limits-grid"><h2>El resultado es útil<br />precisamente porque<br />no se disfraza de certeza.</h2><ul><li><X size={18} /> Muestra no probabilística y dependiente de disponibilidad documental.</li><li><X size={18} /> 115 de 120 predicciones son clase B: requirieron operacionalización.</li><li><X size={18} /> Un solo codificador; la doble codificación prevista no se realizó.</li><li><X size={18} /> Preregistro interno, no depositado externamente.</li><li><X size={18} /> Sin línea base ni probabilidades: no hay <em>skill score</em>.</li><li><X size={18} /> Probar una ausencia histórica suele ser más difícil que probar un evento.</li></ul></div></section>

      <section id="fuentes" className="source-section"><div className="section-shell source-grid"><div><p className="overline">Datos y trazabilidad</p><h2>Todo resultado debe poder volver a su fila.</h2><p>La investigación conserva el texto, el umbral y la evidencia de cada predicción. El mejor uso de esta landing es como puerta de entrada a ese registro, no como sustituto suyo.</p></div><div className="source-links"><a href="../outputs/paper_auditoria_predicciones_cyber_v1.1.md"><FileText size={20} /><span><b>Leer el paper</b><small>Metodología, resultados y límites completos</small></span><ArrowUpRight size={18} /></a><a href="../outputs/anexo_metodologico_y_trazabilidad_v1.1.md"><Eye size={20} /><span><b>Explorar el anexo</b><small>Tablas derivadas y claves de casos</small></span><ArrowUpRight size={18} /></a><a href="../work/registro_extraccion_congelado_v1.0.csv"><ExternalLink size={20} /><span><b>Consultar el corpus congelado</b><small>120 predicciones outcome-blind</small></span><ArrowUpRight size={18} /></a></div></div></section>
      <footer><span>¿Acertaron los escenarios del futuro cyber?</span><span>Auditoría retrospectiva · versión 1.1 · agosto de 2026</span></footer>
    </main>
  );
}
