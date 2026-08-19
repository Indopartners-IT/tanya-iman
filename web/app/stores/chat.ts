import { defineStore } from 'pinia'
import { ApiError, type AskResponse, type Citation } from '@tanya-iman/shared'

export interface Message {
  id: string
  role: 'seeker' | 'iman'
  text: string
  citations?: Citation[]
  /** Absent on seeker messages and on system copy. */
  questionId?: string
  likeable?: boolean
  liked?: boolean
  pending?: boolean
}

export const useChatStore = defineStore('chat', () => {
  const messages = ref<Message[]>([])
  const sessionId = ref<string | null>(null)
  const sending = ref(false)
  const error = ref<string | null>(null)

  const { t } = useCopy()

  function push(message: Message) {
    messages.value.push(message)
  }

  async function start() {
    const api = useApi()
    const { platform, embedOrigin } = usePlatform()

    const { session_id } = await api.createSession({
      platform,
      embed_origin: embedOrigin,
    })
    sessionId.value = session_id
    messages.value = []

    push({
      id: 'greeting',
      role: 'iman',
      text: t('shared.greeting'),
    })
  }

  async function ask(text: string) {
    const trimmed = text.trim()
    if (!trimmed || sending.value) return
    if (!sessionId.value) await start()

    error.value = null
    sending.value = true

    push({ id: `local_${Date.now()}`, role: 'seeker', text: trimmed })
    const placeholderId = `pending_${Date.now()}`
    push({ id: placeholderId, role: 'iman', text: '', pending: true })

    try {
      const api = useApi()
      const response: AskResponse = await api.ask({
        session_id: sessionId.value!,
        text: trimmed,
      })
      replacePending(placeholderId, {
        id: response.question_id,
        role: 'iman',
        text: response.answer_text,
        citations: response.citations,
        questionId: response.question_id,
        likeable: response.likeable,
        liked: false,
      })
    } catch (err) {
      handleAskError(err, placeholderId)
    } finally {
      sending.value = false
    }
  }

  function replacePending(placeholderId: string, message: Message) {
    const index = messages.value.findIndex((m) => m.id === placeholderId)
    if (index >= 0) messages.value[index] = message
  }

  function handleAskError(err: unknown, placeholderId: string) {
    // Rate limits and expired sessions are ordinary outcomes, not faults, and
    // are shown as a message in the conversation rather than as an error
    // banner. Getting told "you have asked a lot today, come back in 20
    // minutes" should not feel like the app broke.
    if (err instanceof ApiError && err.isRateLimited) {
      replacePending(placeholderId, {
        id: placeholderId,
        role: 'iman',
        text: err.detail,
      })
      return
    }

    if (err instanceof ApiError && err.isSessionGone) {
      sessionId.value = null
      replacePending(placeholderId, {
        id: placeholderId,
        role: 'iman',
        text: t('ui.session_expired'),
      })
      return
    }

    replacePending(placeholderId, {
      id: placeholderId,
      role: 'iman',
      text: t('shared.error'),
    })
    error.value = t('ui.network_error')
  }

  async function toggleLike(questionId: string) {
    const message = messages.value.find((m) => m.questionId === questionId)
    if (!message || !message.likeable) return

    const next = !message.liked
    message.liked = next // optimistic; a failed like is not worth an error state
    try {
      await useApi().like(questionId, next)
    } catch {
      message.liked = !next
    }
  }

  function reset() {
    messages.value = []
    sessionId.value = null
    error.value = null
  }

  return { messages, sessionId, sending, error, start, ask, toggleLike, reset }
})
