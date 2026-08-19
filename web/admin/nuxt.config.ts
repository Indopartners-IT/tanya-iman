// The admin portal is a separate app from the seeker app on purpose. They share
// the wire types in web/shared and nothing else: different auth, different
// audience, different deploy cadence, and an admin-only bundle that can never
// be served to a seeker by accident.
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  ssr: false,

  modules: ['@pinia/nuxt'],

  // Same PostCSS wiring as web/app — see the note there and in AGENTS.md.
  css: ['~/assets/css/tailwind.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
    },
  },

  app: {
    head: {
      htmlAttrs: { lang: 'id' },
      title: 'Tanya Iman — Admin',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'robots', content: 'noindex, nofollow' },
      ],
    },
  },
})
