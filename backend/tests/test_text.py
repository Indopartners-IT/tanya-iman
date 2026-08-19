"""Word counting.

These cases are duplicated verbatim in web/shared/src/word-count.test.ts. If you
change one file you must change the other, or the admin editor's live counter
starts disagreeing with the validator that actually blocks publication.
"""

from services.text import MAX_WORDS, MIN_WORDS, count_words, within_length_bounds


def test_empty_and_whitespace():
    assert count_words("") == 0
    assert count_words("   \n\t ") == 0


def test_hyphenated_indonesian_words_count_once():
    assert count_words("anak-anak bermain") == 2
    assert count_words("Isa Al-Masih") == 2


def test_punctuation_is_not_a_word():
    assert count_words("Damai — sejahtera • bagimu") == 3
    assert count_words("Ya! Tentu, benar.") == 3


def test_apostrophes_count_once():
    assert count_words("Qur'an") == 1
    assert count_words("Qur\u2019an") == 1


def test_numbers_count():
    assert count_words("Yohanes 3 16") == 3


def test_length_bounds_are_inclusive():
    assert within_length_bounds(" ".join(["kata"] * MIN_WORDS))
    assert within_length_bounds(" ".join(["kata"] * MAX_WORDS))
    assert not within_length_bounds(" ".join(["kata"] * (MIN_WORDS - 1)))
    assert not within_length_bounds(" ".join(["kata"] * (MAX_WORDS + 1)))
