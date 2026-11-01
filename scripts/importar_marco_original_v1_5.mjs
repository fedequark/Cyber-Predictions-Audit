import { copyFile, readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const sourceDir = process.argv[2];
if (!sourceDir) throw new Error('Uso: node scripts/importar_marco_original_v1_5.mjs <carpeta work original>');

const sources = new Map([
  ['marco_maestro_189_sesiones_v0.9.csv', 'A9C608FA24B54FFEE534500EBA46FEA1F9B4FB0C331B80C02EE6359762B68EDB'],
  ['disponibilidad_blackhat_2005_2013_v0.2.csv', '4D9B7B560CA715FFFA3DFBD4BC2401DBC83C725ECAB5B9B57A5264B845BAE1CB'],
  ['disponibilidad_blackhat_2014_2018_v0.2.csv', '0A92DE1C5E3AD9FDC8C5803DF3419E052DF0E412A4C61F691BC1389C0A0FC8CB'],
  ['disponibilidad_vb_30_v0.5.csv', '38BE2A60CA85E1196CA9C8F79AF9A6E869CAD7E81596E8302B1BE7083BDEAE5B'],
]);

for (const [name, expected] of sources) {
  const source = join(resolve(sourceDir), name);
  const target = join(root, 'work', name);
  const bytes = await readFile(source);
  const hash = createHash('sha256').update(bytes).digest('hex').toUpperCase();
  if (hash !== expected) throw new Error(`${name}: SHA-256 distinto; no se importa`);
  try {
    const existing = await readFile(target);
    if (!existing.equals(bytes)) throw new Error(`${name}: destino distinto; no se sobrescribe`);
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
    await copyFile(source, target);
  }
  console.log(`${name}: ${hash}`);
}
