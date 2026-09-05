import type { NextConfig } from 'next';

// Generate a fully pre-rendered site. The resulting dist/client directory can
// be served directly by Apache; it does not need a Node.js runtime.
const nextConfig: NextConfig = {
  output: 'export',
};

export default nextConfig;
