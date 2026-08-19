<template>
  <div class="min-h-dvh bg-slate-100">
    <header class="border-b border-slate-200 bg-white px-6 py-3">
      <div class="mx-auto flex max-w-6xl items-center justify-between">
        <h1 class="text-sm font-semibold text-slate-900">Tanya Iman — Admin</h1>
        <nav class="flex gap-4 text-sm text-slate-600">
          <NuxtLink to="/" class="hover:text-emerald-700">Ringkasan</NuxtLink>
          <NuxtLink to="/questions" class="hover:text-emerald-700">Pertanyaan</NuxtLink>
          <NuxtLink to="/topics" class="hover:text-emerald-700">Topik</NuxtLink>
        </nav>
      </div>
    </header>

    <main class="mx-auto max-w-6xl px-6 py-8">
      <NuxtPage />
    </main>
  </div>
</template>
