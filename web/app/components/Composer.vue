<script setup lang="ts">
const props = defineProps<{ disabled?: boolean }>()
const emit = defineEmits<{ submit: [text: string] }>()

const { t } = useCopy()
const MAX_CHARS = 1000 // mirrors MAX_QUESTION_CHARS in backend settings

const text = ref('')
const textarea = ref<HTMLTextAreaElement | null>(null)

const remaining = computed(() => MAX_CHARS - text.value.length)
const tooLong = computed(() => remaining.value < 0)
const canSend = computed(
  () => !props.disabled && text.value.trim().length > 0 && !tooLong.value,
)

function submit() {
  if (!canSend.value) return
  emit('submit', text.value)
  text.value = ''
  resize()
}

function onKeydown(event: KeyboardEvent) {
  // Enter sends, Shift+Enter breaks the line. On touch keyboards Enter is a
  // newline, so the send button is the primary control there.
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault()
    submit()
  }
}

function resize() {
  const el = textarea.value
  if (!el) return
  el.style.height = 'auto'
  el.style.height = `${Math.min(el.scrollHeight, 160)}px`
}
</script>

<template>
  <form
    class="flex items-end gap-2 border-t border-slate-200 bg-white p-3"
    @submit.prevent="submit"
  >
    <div class="flex-1">
      <textarea
        ref="textarea"
        v-model="text"
        rows="1"
        :placeholder="t('ui.composer_placeholder')"
        :aria-label="t('ui.composer_placeholder')"
        class="w-full resize-none rounded-xl border border-slate-300 px-3 py-2.5 text-[15px] leading-relaxed outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100"
        @input="resize"
        @keydown="onKeydown"
      />
      <p
        v-if="remaining < 100"
        :class="['mt-1 text-right text-xs', tooLong ? 'text-red-600' : 'text-slate-400']"
      >
        {{ t('ui.composer_counter', { count: text.length }) }}
      </p>
    </div>

    <button
      type="submit"
      :disabled="!canSend"
      class="mb-0.5 shrink-0 rounded-xl bg-emerald-600 px-4 py-2.5 text-sm font-medium text-white transition disabled:cursor-not-allowed disabled:bg-slate-300"
    >
      {{ t('ui.composer_send') }}
    </button>
  </form>
</template>
