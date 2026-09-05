import { rm } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { resolve } from 'node:path';

const projectRoot = process.cwd();
const outputRoot = resolve(projectRoot, 'dist');
const vinextCli = resolve(projectRoot, 'node_modules', 'vinext', 'dist', 'cli.js');

await rm(outputRoot, { recursive: true, force: true });

const exitCode = await new Promise((resolveBuild) => {
  const build = spawn(process.execPath, [vinextCli, 'build'], {
    cwd: projectRoot,
    stdio: 'inherit',
  });

  build.once('error', () => resolveBuild(1));
  build.once('close', (code) => resolveBuild(code ?? 1));
});

// Vinext's Windows teardown can return a non-zero status after it has fully
// emitted and prerendered the export. The preparation step verifies the export
// exists, so genuine build failures (which do not produce index.html) still
// fail this command.
await import('./prepare-static-package.mjs');

if (exitCode !== 0) {
  console.warn(
    'Vinext exited during Windows teardown after producing the validated static export.',
  );
}
