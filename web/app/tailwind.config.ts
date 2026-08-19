import type { Config } from 'tailwindcss'

export default {
  content: [
    './components/**/*.{vue,ts}',
    './composables/**/*.ts',
    './pages/**/*.vue',
    './stores/**/*.ts',
    './app.vue',
  ],
  theme: {
    extend: {
      fontSize: {
        // Conversational Indonesian at default browser size is cramped. The
        // chat surface reads at 15px/1.7 throughout.
        base: ['15px', '1.7'],
      },
    },
  },
} satisfies Config
