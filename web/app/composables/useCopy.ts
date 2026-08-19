import id from '~/locales/id.json'

type Copy = typeof id

/**
 * Indonesian is the only locale (PRD section 12, out of scope: multi-language).
 * A full i18n module would be dead weight, so this is a flat lookup with
 * `{placeholder}` interpolation and nothing else.
 */
export function useCopy() {
  function t(path: string, vars?: Record<string, string | number>): string {
    const value = path
      .split('.')
      .reduce<unknown>((acc, key) => (acc as Record<string, unknown>)?.[key], id)

    if (typeof value !== 'string') {
      // Loud in development, harmless in production: a missing key renders as
      // its own path rather than as an empty gap in the conversation.
      if (import.meta.dev) console.warn(`[copy] missing key: ${path}`)
      return path
    }

    if (!vars) return value
    return value.replace(/\{(\w+)\}/g, (match, key) =>
      key in vars ? String(vars[key]) : match,
    )
  }

  return { t, copy: id as Copy }
}
