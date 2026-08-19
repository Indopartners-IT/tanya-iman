<script setup lang="ts">
/** F-5: one conversation, many questions. There is no "new question" button —
 *  the seeker just keeps typing. */
const { t } = useCopy()
const auth = useAuthStore()
const chat = useChatStore()
const router = useRouter()

const scroller = ref<HTMLElement | null>(null)

onMounted(async () => {
  if (!auth.isAuthenticated) {
    await router.replace('/')
    return
  }
  await chat.start()
})

watch(
  () => chat.messages.length,
  async () => {
    await nextTick()
    scroller.value?.scrollTo({ top: scroller.value.scrollHeight, behavior: 'smooth' })
  },
)
</script>

<template>
  <div class="flex h-dvh flex-col bg-slate-50">
    <header
      class="flex items-center justify-between border-b border-slate-200 bg-white px-4 py-3"
    >
      <h1 class="text-base font-semibold text-slate-900">{{ t('ui.app_name') }}</h1>
      <p class="text-xs text-slate-500">{{ t('shared.source_note') }}</p>
    </header>

    <div ref="scroller" class="flex-1 space-y-3 overflow-y-auto px-4 py-4">
      <MessageBubble
        v-for="message in chat.messages"
        :key="message.id"
        :message="message"
        @like="chat.toggleLike"
      />
    </div>

    <Composer :disabled="chat.sending" @submit="chat.ask" />
  </div>
</template>
