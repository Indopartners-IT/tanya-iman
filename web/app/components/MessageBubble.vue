<script setup lang="ts">
import type { Message } from '~/stores/chat'

const props = defineProps<{ message: Message }>()
const emit = defineEmits<{ like: [questionId: string] }>()

const { t } = useCopy()
const isSeeker = computed(() => props.message.role === 'seeker')

function onLike() {
  if (props.message.questionId) emit('like', props.message.questionId)
}
</script>

<template>
  <div :class="['flex w-full', isSeeker ? 'justify-end' : 'justify-start']">
    <div
      :class="[
        'max-w-[85%] rounded-2xl px-4 py-3 text-[15px] leading-relaxed',
        isSeeker
          ? 'bg-emerald-600 text-white rounded-br-md'
          : 'bg-white text-slate-800 shadow-sm ring-1 ring-slate-200 rounded-bl-md',
      ]"
    >
      <p v-if="message.pending" class="flex gap-1 py-1" aria-live="polite">
        <span class="sr-only">{{ t('ui.composer_thinking') }}</span>
        <span
          v-for="i in 3"
          :key="i"
          class="h-2 w-2 animate-bounce rounded-full bg-slate-400"
          :style="{ animationDelay: `${(i - 1) * 0.15}s` }"
        />
      </p>

      <p v-else class="whitespace-pre-wrap">{{ message.text }}</p>

      <!-- F-12: reference articles are part of the answer, not decoration.
           They are how a seeker verifies what they just read. -->
      <div v-if="message.citations?.length" class="mt-3 border-t border-slate-100 pt-3">
        <p class="mb-1.5 text-xs font-medium text-slate-500">
          {{ t('ui.answer_sources') }}
        </p>
        <ul class="space-y-1">
          <li v-for="citation in message.citations" :key="citation.url">
            <a
              :href="citation.url"
              target="_blank"
              rel="noopener noreferrer"
              class="text-sm text-emerald-700 underline decoration-emerald-200 underline-offset-2 hover:decoration-emerald-500"
            >
              {{ citation.title }}
            </a>
          </li>
        </ul>
      </div>

      <button
        v-if="message.likeable && message.questionId"
        type="button"
        class="mt-3 text-xs text-slate-500 transition hover:text-emerald-700"
        :aria-pressed="message.liked"
        @click="onLike"
      >
        {{ message.liked ? t('ui.answer_liked') : t('ui.answer_like') }}
      </button>
    </div>
  </div>
</template>
