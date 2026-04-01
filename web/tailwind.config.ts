import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        teal: {
          brand: '#21D4B0',
          dark: '#22C0A0',
        },
        gray: {
          bg: '#F5F4F6',
          card: '#EEEEF4',
          text: '#444445',
          muted: '#A1A1AE',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
export default config
