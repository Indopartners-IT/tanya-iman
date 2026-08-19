<script setup lang="ts">
/**
 * F-1: the entry screen offers SMS, WhatsApp, and Guest.
 *
 * Guest is listed last but is not hidden or de-emphasised. Someone with
 * questions about faith may have good reasons not to attach their phone number
 * to them, and making that the awkward path costs us the conversation.
 *
 * SMS and WhatsApp are disabled until Phase 3 (PIP Tasks 3.1-3.3).
 */
const { t } = useCopy()
const auth = useAuthStore()
const router = useRouter()

const busy = ref(false)

async function continueAsGuest() {
  busy.value = true
  try {
    await auth.signInAsGuest()
    await router.push('/chat')
  } finally {
    busy.value = false
  }
}
</script>

<template>
  <main class="flex min-h-dvh flex-col items-center justify-center bg-slate-50 px-6">
    <div class="w-full max-w-sm">
      <h1 class="text-center text-2xl font-semibold text-slate-900">
        {{ t('ui.login_title') }}
      </h1>
      <p class="mt-2 text-center text-[15px] leading-relaxed text-slate-600">
        {{ t('ui.login_subtitle') }}
      </p>

      <div class="mt-8 space-y-3">
        <button
          type="button"
          disabled
          class="w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-400"
        >
          {{ t('ui.login_sms') }}
        </button>
        <button
          type="button"
          disabled
          class="w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-400"
        >
          {{ t('ui.login_whatsapp') }}
        </button>
        <button
          type="button"
          :disabled="busy"
          class="w-full rounded-xl bg-emerald-600 px-4 py-3 text-sm font-medium text-white transition hover:bg-emerald-700 disabled:bg-slate-300"
          @click="continueAsGuest"
        >
          {{ t('ui.login_guest') }}
        </button>
      </div>

      <p class="mt-4 text-center text-xs leading-relaxed text-slate-500">
        {{ t('ui.login_guest_note') }}
      </p>
    </div>
  </main>
</template>
