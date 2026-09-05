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
  title: 'Cyber Predictions Audit',
  description: 'A retrospective audit of 120 explicit predictions from cybersecurity conferences, 2005–2018.',
  openGraph: {
    title: 'Cyber Predictions Audit',
    description: '120 predictions · 2005–2018',
    images: ['/og.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Cyber Predictions Audit',
    description: '120 predictions · 2005–2018',
    images: ['/og.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
