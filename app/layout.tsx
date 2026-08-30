import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: '¿Acertaron los escenarios del futuro cyber?',
  description: 'Auditoría retrospectiva de 120 predicciones explícitas en conferencias de ciberseguridad, 2005–2018.',
  openGraph: {
    title: '¿Acertaron los escenarios del futuro cyber?',
    description: '120 predicciones · 2005–2018',
    images: ['/og.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: '¿Acertaron los escenarios del futuro cyber?',
    description: '120 predicciones · 2005–2018',
    images: ['/og.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
