import pytest

from config import get_settings
from services import guards


def test_empty_input_rejected():
    with pytest.raises(guards.InputEmptyError):
        guards.check_input_bounds("   ")


def test_over_long_input_rejected():
    limit = get_settings().max_question_chars
    with pytest.raises(guards.InputTooLongError):
        guards.check_input_bounds("a" * (limit + 1))


def test_input_is_trimmed():
    assert guards.check_input_bounds("  halo  ") == "halo"


@pytest.mark.asyncio
async def test_rate_limit_allows_up_to_the_cap_then_blocks(storage):
    limit = get_settings().rate_limit_per_hour

    for _ in range(limit):
        assert (await guards.check_rate_limit(storage, "u1")).allowed

    blocked = await guards.check_rate_limit(storage, "u1")
    assert not blocked.allowed
    assert blocked.count == limit + 1


@pytest.mark.asyncio
async def test_rate_limit_is_per_user(storage):
    limit = get_settings().rate_limit_per_hour
    for _ in range(limit + 1):
        await guards.check_rate_limit(storage, "u1")

    assert (await guards.check_rate_limit(storage, "u2")).allowed


def test_crisis_keyword_triggers_and_renders_helplines():
    result = guards.check_crisis("saya ingin bunuh diri")
    assert result.triggered
    assert result.response_text
    # The rendered response must not still contain the template slot.
    assert "{helplines}" not in result.response_text


def test_ordinary_question_does_not_trigger_crisis():
    assert not guards.check_crisis("Siapakah Isa Al-Masih?").triggered
