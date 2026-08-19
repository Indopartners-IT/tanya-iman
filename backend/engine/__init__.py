"""Answer engines.

The router calls ``get_engine().answer(...)`` and nothing else. Phase 2 ships
the stub; Phase 5 replaces it with the RAG pipeline described in
docs/ai-answer-engine-specification.md. Because both satisfy ``EngineResult``, the swap
is a one-line change in the factory and no change at all in ``routers/``.
"""

from engine.base import AnswerEngine, EngineRequest, get_engine, reset_engine

__all__ = ["AnswerEngine", "EngineRequest", "get_engine", "reset_engine"]
