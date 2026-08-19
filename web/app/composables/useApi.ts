import { createClient, type ApiClient } from '@tanya-iman/shared'
import { useAuthStore } from '~/stores/auth'

let client: ApiClient | null = null

export function useApi(): ApiClient {
  if (!client) {
    const config = useRuntimeConfig()
    const auth = useAuthStore()
    // Resolved per request rather than captured once: Firebase ID tokens
    // expire after an hour and a seeker may well sit on one conversation
    // longer than that.
    client = createClient({
      baseUrl: config.public.apiBase,
      getToken: () => auth.getIdToken(),
    })
  }
  return client
}
