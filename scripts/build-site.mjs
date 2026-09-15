import { cp, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const dist = resolve(root, 'dist');
if (dirname(dist) !== root || !dist.endsWith('dist')) {
  throw new Error(`Destino de build inesperado: ${dist}`);
}

await rm(dist, { recursive: true, force: true });
await mkdir(dist, { recursive: true });
await cp(join(root, 'site'), dist, { recursive: true });
await mkdir(join(dist, 'documents'), { recursive: true });
await mkdir(join(dist, 'work'), { recursive: true });

for (const name of await readdir(join(root, 'outputs'))) {
  if (name.endsWith('.md')) {
    const text = await readFile(join(root, 'outputs', name), 'utf8');
    await writeFile(join(dist, 'documents', name), text.replace(/\r\n/g, '\n'), 'utf8');
  }
}

for (const name of ['RIGHTS.md', 'LICENSE-DATA.md', 'LICENSE']) {
  const content = await readFile(join(root, name), 'utf8');
  await writeFile(join(dist, 'documents', name), content.replace(/\r\n/g, '\n'), 'utf8');
}

for (const name of [
  'registro_extraccion_congelado_v1.0.csv',
  'evaluacion_desenlaces_v1.0.csv',
  'orden_seleccion_s3_v0.2.csv',
  'analisis_derivado_v1.2.csv',
  'metricas_robustez_v1.2.csv',
  'inventario_fuentes_v1.2.csv',
  'registro_candidatos_excluidos_template_v1.2.csv',
  'influencia_sesiones_v1.3.csv',
  'escenarios_indeterminados_v1.3.csv',
  'triage_evidencia_v1.4.csv',
  'rendimiento_sesiones_s3_v1.4.csv',
  'reconstruccion_marco_no_s3_template_v1.4.csv',
  'estado_enlaces_fuentes_2026-09-15.csv',
  'revision_compromiso_y_operacionalizacion_v1.4.csv',
  'tarjeta_pronostico_prospectivo_template_v1.4.csv',
  'alternativas_enlaces_fuentes_v1.4.csv',
  'seguimiento_enlaces_fuentes_v1.4a.csv',
  'marco_maestro_189_sesiones_v0.9.csv',
  'disponibilidad_blackhat_2005_2013_v0.2.csv',
  'disponibilidad_blackhat_2014_2018_v0.2.csv',
  'disponibilidad_vb_30_v0.5.csv',
]) {
  const source = join(root, 'work', name);
  const target = join(dist, 'work', name);
  if (name === 'evaluacion_desenlaces_v1.0.csv') {
    const text = await readFile(source, 'utf8');
    await writeFile(target, text.replace(/^\uFEFF/, '').replace(/\r\n/g, '\n'), 'utf8');
  } else {
    await cp(source, target);
  }
}

await cp(
  join(root, 'work', 'registro_extraccion_congelado_v1.0.csv'),
  join(dist, 'documents', 'registro_extraccion_congelado_v1.0.csv'),
);
await cp(join(dist, 'work', 'evaluacion_desenlaces_v1.0.csv'), join(dist, 'documents', 'evaluacion_desenlaces_v1.0.csv'));

console.log(`Sitio construido en ${dist}`);
