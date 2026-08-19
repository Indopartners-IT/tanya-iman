import type { Platform } from '@tanya-iman/shared'

/**
 * F-24: every question records where it was asked from, so the admin panel can
 * tell whether widget traffic behaves differently from app traffic. Detected
 * once at runtime rather than baked in at build time, because the widget and
 * the web app are the same bundle.
 */
export function usePlatform(): { platform: Platform; embedOrigin: string | null } {
  if (import.meta.server) return { platform: 'web', embedOrigin: null }

  const isCapacitor =
    'Capacitor' in window || window.location.protocol === 'capacitor:'
  if (isCapacitor) return { platform: 'android', embedOrigin: null }

  const isEmbedded = window.self !== window.top
  if (isEmbedded) {
    // document.referrer is the only cross-origin-safe read of the host page.
    let origin: string | null = null
    try {
      origin = document.referrer ? new URL(document.referrer).origin : null
    } catch {
      origin = null
    }
    return { platform: 'widget', embedOrigin: origin }
  }

  return { platform: 'web', embedOrigin: null }
}
