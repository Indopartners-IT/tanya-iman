"""Deterministic guards that run before the answer engine.

These are ordinary Python and never LLM calls, so they cost nothing and cannot
be prompt-injected. Ordering is specified in AI Spec section 3.2 and asserted by
tests/test_pipeline_order.py — it is not a matter of style.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from config import get_settings
from config.loader import crisis_config, response
from storage.base import Storage


class InputTooLongError(ValueError):
    pass


class InputEmptyError(ValueError):
    pass


@dataclass(frozen=True)
class RateLimitResult:
    allowed: bool
    count: int
    limit: int
    retry_after_seconds: int


@dataclass(frozen=True)
class CrisisResult:
    triggered: bool
    response_text: str = ""


def check_input_bounds(text: str) -> str:
    """Reject empty and over-long input before anything else runs."""
    cleaned = (text or "").strip()
    if not cleaned:
        raise InputEmptyError(response("input_empty"))
    if len(cleaned) > get_settings().max_question_chars:
        raise InputTooLongError(response("input_too_long"))
    return cleaned


def hour_bucket(now: datetime) -> str:
    return now.strftime("%Y%m%d%H")


async def check_rate_limit(
    storage: Storage, uid: str, now: datetime | None = None
) -> RateLimitResult:
    """F-16: 30 messages per rolling hour per user.

    The increment is atomic in every backend, so two concurrent requests at the
    boundary cannot both pass.
    """
    settings = get_settings()
    now = now or datetime.now()
    count = await storage.increment_rate_window(uid, hour_bucket(now))
    limit = settings.rate_limit_per_hour

    seconds_into_hour = now.minute * 60 + now.second
    retry_after = max(0, 3600 - seconds_into_hour)

    return RateLimitResult(
        allowed=count <= limit,
        count=count,
        limit=limit,
        retry_after_seconds=retry_after,
    )


def rate_limit_message(result: RateLimitResult) -> str:
    minutes = max(1, -(-result.retry_after_seconds // 60))  # ceil
    return response("rate_limit", minutes=minutes)


def check_crisis(text: str) -> CrisisResult:
    """F-30: crisis routing runs FIRST, ahead of the rate limiter.

    Someone in crisis who has exhausted their message quota still gets the
    helpline. Reversing that ordering is a safety regression.

    The keyword pass below is deliberately over-inclusive. A false positive
    shows someone a helpline they did not need; a false negative is a P0.
    The semantic check that supplements it lands in Phase 5 (PIP Task 5.1).
    """
    config = crisis_config()
    lowered = (text or "").casefold()
    keywords = config.get("triggers", {}).get("keywords", [])

    if not any(kw.casefold() in lowered for kw in keywords):
        return CrisisResult(triggered=False)

    return CrisisResult(triggered=True, response_text=render_crisis_response())


def render_crisis_response() -> str:
    config = crisis_config()
    lines = [
        f"{h['name']} — {h['number']}" + (f" ({h['hours']})" if h.get("hours") else "")
        for h in config.get("helplines", [])
    ]
    return str(config.get("response", "")).replace("{helplines}", "\n".join(lines))


def assert_crisis_script_approved() -> None:
    """Startup gate.

    The application refuses to boot in staging or production while the crisis
    script is unapproved. Shipping a placeholder helpline number is a P0 safety
    defect, and this is the check that makes that impossible rather than
    merely discouraged. Do not flip `approved` to work around a failing boot.
    """
    settings = get_settings()
    if settings.is_development:
        return

    config = crisis_config()
    if not config.get("approved"):
        raise RuntimeError(
            "REFUSING TO START: backend/config/crisis_scripts.id.yml is not approved. "
            "Every helpline number in it is a placeholder. See PIP B1 "
            "and the crisis script header. This gate exists because shipping a wrong "
            "crisis number is a P0 safety defect."
        )
    if not config.get("verified_on"):
        raise RuntimeError(
            "REFUSING TO START: crisis script is marked approved but has no "
            "`verified_on` date. Helpline numbers must be called and confirmed "
            "reachable, with the date of that check recorded."
        )
