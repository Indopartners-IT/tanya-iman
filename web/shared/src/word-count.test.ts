import { describe, expect, it } from 'vitest'
import { MAX_WORDS, MIN_WORDS, countWords, withinLengthBounds } from './word-count'

// These cases are duplicated in backend/tests/test_text.py. Change one, change
// both — the two counters must never disagree.
describe('countWords', () => {
  it('returns zero for empty and whitespace', () => {
    expect(countWords('')).toBe(0)
    expect(countWords('   \n\t ')).toBe(0)
  })

  it('counts hyphenated Indonesian words once', () => {
    expect(countWords('anak-anak bermain')).toBe(2)
    expect(countWords('Isa Al-Masih')).toBe(2)
  })

  it('does not count standalone punctuation', () => {
    expect(countWords('Damai — sejahtera • bagimu')).toBe(3)
    expect(countWords('Ya! Tentu, benar.')).toBe(3)
  })

  it('counts apostrophised forms once', () => {
    expect(countWords("Qur'an")).toBe(1)
    expect(countWords('Qur\u2019an')).toBe(1)
  })

  it('counts numbers', () => {
    expect(countWords('Yohanes 3 16')).toBe(3)
  })
})

describe('withinLengthBounds', () => {
  const words = (n: number) => Array(n).fill('kata').join(' ')

  it('is inclusive at both ends', () => {
    expect(withinLengthBounds(words(MIN_WORDS))).toBe(true)
    expect(withinLengthBounds(words(MAX_WORDS))).toBe(true)
    expect(withinLengthBounds(words(MIN_WORDS - 1))).toBe(false)
    expect(withinLengthBounds(words(MAX_WORDS + 1))).toBe(false)
  })
})
