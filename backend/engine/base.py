from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from config import get_settings
from models import EngineResult, Question


@dataclass(frozen=True)
class EngineRequest:
    question_text: str
    uid: str
    session_id: str
    context: list[Question] = field(default_factory=list)


class AnswerEngine(Protocol):
    name: str

    async def answer(self, request: EngineRequest) -> EngineResult: ...


_instance: AnswerEngine | None = None


def get_engine() -> AnswerEngine:
    global _instance
    if _instance is None:
        settings = get_settings()
        if settings.answer_engine == "rag":  # pragma: no cover - Phase 5
            from engine.rag import RAGEngine

            _instance = RAGEngine()
        else:
            from engine.stub import StubEngine

            _instance = StubEngine()
    return _instance


def reset_engine(engine: AnswerEngine | None = None) -> None:
    global _instance
    _instance = engine
