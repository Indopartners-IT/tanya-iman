<script setup lang="ts">
/**
 * Phase 4 shell (PIP section 2). The admin surface is specified in
 * docs/admin-ux-specification.md; this page exists so the app builds,
 * deploys, and has a route to hang the real screens off.
 */
const phases = [
  { id: 'AD-1', label: 'Daftar & detail pertanyaan', task: 'PIP Task 4.2' },
  { id: 'AD-2', label: 'Editor jawaban kurasi', task: 'PIP Task 4.3' },
  { id: 'AD-3', label: 'Topik & frekuensi pertanyaan', task: 'PIP Task 4.4' },
  { id: 'AD-4', label: 'Peninjauan jawaban tanpa dasar', task: 'PIP Task 4.5' },
]
</script>

<template>
  <div>
    <h2 class="text-lg font-semibold text-slate-900">Ringkasan</h2>
    <p class="mt-1 text-sm text-slate-600">
      Kerangka panel admin. Layar berikut dibangun pada Fase 4.
    </p>

    <ul class="mt-6 divide-y divide-slate-200 rounded-lg border border-slate-200 bg-white">
      <li
        v-for="phase in phases"
        :key="phase.id"
        class="flex items-center justify-between px-4 py-3"
      >
        <div>
          <p class="text-sm font-medium text-slate-800">{{ phase.label }}</p>
          <p class="text-xs text-slate-500">{{ phase.id }}</p>
        </div>
        <span class="rounded-full bg-slate-100 px-2.5 py-1 text-xs text-slate-600">
          {{ phase.task }}
        </span>
      </li>
    </ul>
  </div>
</template>
