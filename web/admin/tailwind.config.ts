import type { Config } from 'tailwindcss'

export default {
  content: ['./components/**/*.{vue,ts}', './pages/**/*.vue', './app.vue'],
  theme: { extend: {} },
} satisfies Config
