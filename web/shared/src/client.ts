/**
 * API client shared by the seeker app, the embedded widget, and the Android
 * shell. All three speak to the same backend over the same contract, so the
 * transport lives here once.
 */

import type {
  AskRequest,
  AskResponse,
  CreateSessionRequest,
  CreateSessionResponse,
  HealthResponse,
  LikeResponse,
} from './types'

export class ApiError extends Error {
  constructor(
    readonly status: number,
    readonly detail: string,
    /** Present on 429. Seconds until the quota window rolls over. */
    readonly retryAfterSeconds?: number,
  ) {
    super(detail)
    this.name = 'ApiError'
  }

  get isRateLimited(): boolean {
    return this.status === 429
  }

  get isSessionGone(): boolean {
    return this.status === 404 || this.status === 410
  }
}

export interface ClientOptions {
  baseUrl: string
  /** Returns a fresh Firebase ID token. Called per request — tokens expire. */
  getToken: () => Promise<string | null>
  fetchImpl?: typeof fetch
}

export function createClient(options: ClientOptions) {
  const doFetch = options.fetchImpl ?? globalThis.fetch
  const baseUrl = options.baseUrl.replace(/\/$/, '')

  async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
    const token = await options.getToken()
    const headers = new Headers(init.headers)
    headers.set('Content-Type', 'application/json')
    if (token) headers.set('Authorization', `Bearer ${token}`)

    const response = await doFetch(`${baseUrl}${path}`, { ...init, headers })

    if (!response.ok) {
      const body = await response.json().catch(() => ({}))
      const retryAfter = response.headers.get('Retry-After')
      throw new ApiError(
        response.status,
        typeof body?.detail === 'string' ? body.detail : response.statusText,
        retryAfter ? Number(retryAfter) : undefined,
      )
    }

    return (await response.json()) as T
  }

  return {
    health: () => request<HealthResponse>('/health'),

    createSession: (payload: CreateSessionRequest) =>
      request<CreateSessionResponse>('/sessions', {
        method: 'POST',
        body: JSON.stringify(payload),
      }),

    ask: (payload: AskRequest) =>
      request<AskResponse>('/ask', {
        method: 'POST',
        body: JSON.stringify(payload),
      }),

    like: (questionId: string, liked: boolean) =>
      request<LikeResponse>(
        `/questions/${encodeURIComponent(questionId)}/like?liked=${liked}`,
        { method: 'POST' },
      ),
  }
}

export type ApiClient = ReturnType<typeof createClient>
