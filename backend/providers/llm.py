from __future__ import annotations

from typing import Any, Protocol

from config import get_settings


class LLMProvider(Protocol):
    name: str

    async def complete_json(
        self, system: str, user: str, *, max_tokens: int = 700, temperature: float = 0.4
    ) -> dict[str, Any]:
        """Return parsed structured output. Raises on transport failure."""
        ...


class FakeLLM:
    """Deterministic stand-in used by tests and `LLM_PROVIDER=fake`.

    Its existence is what lets the engine test suite run with no network, no
    cost, and no flakiness. Phase 5 tests assert against this, then the
    benchmark suite exercises the real provider separately.
    """

    name = "fake"

    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []
        self.next_response: dict[str, Any] | None = None

    async def complete_json(
        self, system: str, user: str, *, max_tokens: int = 700, temperature: float = 0.4
    ) -> dict[str, Any]:
        self.calls.append((system, user))
        if self.next_response is not None:
            return self.next_response
        return {
            "answer": (
                "Terima kasih sudah bertanya. Allah mengenal apa yang sedang Anda "
                "rasakan, dan Isa Al-Masih datang untuk membawa pengharapan bagi "
                "mereka yang mencari kebenaran dengan sungguh-sungguh."
            ),
            "used_passages": [1],
            "quran_reference": None,
            "bible_references": [],
            "confidence": "medium",
        }


_instance: LLMProvider | None = None


def get_llm() -> LLMProvider:
    global _instance
    if _instance is None:
        settings = get_settings()
        if settings.llm_provider == "fake":
            _instance = FakeLLM()
        else:  # pragma: no cover - real providers land in Phase 5
            raise NotImplementedError(
                f"LLM provider '{settings.llm_provider}' is not implemented yet. "
                "Real providers land in Phase 5 (PIP Task 5.4), and only after "
                "Zero Data Retention terms are confirmed in writing (PIP B3)."
            )
    return _instance


def reset_llm(provider: LLMProvider | None = None) -> None:
    global _instance
    _instance = provider
