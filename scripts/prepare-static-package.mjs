import { access, cp, mkdir, rm } from 'node:fs/promises';
import { resolve } from 'node:path';

const projectRoot = process.cwd();
const packageRoot = resolve(projectRoot, 'dist', 'client');
const documentsRoot = resolve(packageRoot, 'documents');
const researchRoot = resolve(projectRoot, '..');

const documents = [
  [
    resolve(researchRoot, 'outputs', 'paper_auditoria_predicciones_cyber_v1.1.md'),
    'paper_auditoria_predicciones_cyber_v1.1.md',
  ],
  [
    resolve(researchRoot, 'outputs', 'anexo_metodologico_y_trazabilidad_v1.1.md'),
    'anexo_metodologico_y_trazabilidad_v1.1.md',
  ],
  [
    resolve(researchRoot, 'work', 'registro_extraccion_congelado_v1.0.csv'),
    'registro_extraccion_congelado_v1.0.csv',
  ],
];

await access(resolve(packageRoot, 'index.html'));
await rm(documentsRoot, { recursive: true, force: true });
await mkdir(documentsRoot, { recursive: true });

for (const [source, fileName] of documents) {
  await cp(source, resolve(documentsRoot, fileName));
}

console.log('Copied research documents into dist/client/documents.');
