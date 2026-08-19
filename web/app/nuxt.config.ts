// One codebase, three delivery targets (F-24): the hosted web app, the
// WordPress widget, and the Capacitor Android shell. SPA mode is what makes
// that possible — `nuxt generate` with ssr:false produces static assets that
// Capacitor can bundle and that an iframe can load, and there is no server to
// run in the Android case.
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  ssr: false,

  modules: ['@pinia/nuxt'],

  // Tailwind is wired through Nuxt's own PostCSS rather than
  // @nuxtjs/tailwindcss. That module writes a postcss.mjs which gets loaded
  // outside ESM context and fails the build; see AGENTS.md.
  css: ['~/assets/css/tailwind.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  devtools: { enabled: true },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
      firebaseApiKey: process.env.NUXT_PUBLIC_FIREBASE_API_KEY || '',
      firebaseAuthDomain: process.env.NUXT_PUBLIC_FIREBASE_AUTH_DOMAIN || '',
      firebaseProjectId: process.env.NUXT_PUBLIC_FIREBASE_PROJECT_ID || '',
      firebaseAppId: process.env.NUXT_PUBLIC_FIREBASE_APP_ID || '',
    },
  },

  app: {
    // Relative base so the same build works from a subdirectory, from an
    // iframe, and from Capacitor's file:// origin.
    baseURL: './',
    head: {
      htmlAttrs: { lang: 'id' },
      title: 'Tanya Iman',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'Ruang untuk bertanya tentang iman, keraguan, dan pergumulan hidup.',
        },
      ],
    },
  },

  nitro: {
    prerender: { crawlLinks: false, routes: ['/'] },
  },
})
