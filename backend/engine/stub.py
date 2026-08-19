"""Stub engine — Phase 2 only.

It returns a fixed, editorially safe Indonesian answer with a fixed citation so
that the full request path (auth, session, guards, persistence, UI rendering,
likes, admin capture) can be built and tested end to end before any model or
corpus exists. This is what lets Phase 3 and Phase 4 proceed in parallel with
Phase 5 (PIP section 2).

It must never reach staging with `ANSWER_ENGINE=stub`; the health endpoint
reports the active engine so that mistake is visible rather than silent.
"""

from __future__ import annotations

from config import get_settings, response
from engine.base import EngineRequest
from models import Citation, EngineResult
from models.enums import AnswerSource

STUB_ANSWER = (
    "Terima kasih sudah membawa pertanyaan ini. Banyak orang bergumul dengan hal "
    "yang sama, dan mencari jawaban adalah langkah yang baik. Allah tidak jauh "
    "dari mereka yang mencari-Nya dengan hati yang tulus, dan Isa Al-Masih "
    "berkata bahwa siapa yang mencari akan mendapat, dan siapa yang mengetuk "
    "akan dibukakan pintu. Anda dipersilakan membaca artikel di bawah ini untuk "
    "penjelasan yang lebih lengkap, dan Anda boleh bertanya lagi kapan saja "
    "tentang apa pun yang masih mengganjal di hati Anda."
)

STUB_CITATION = Citation(
    title="Siapakah Isa Al-Masih?",
    url="https://isadanislam.org/",
    site="isadanislam.org",
)


class StubEngine:
    name = "stub"

    async def answer(self, request: EngineRequest) -> EngineResult:
        settings = get_settings()

        # One real behaviour is worth keeping even in the stub: an empty corpus
        # must never produce an invented answer. Phase 5 replaces the condition
        # with a retrieval-score check; the response copy stays the same.
        if not request.question_text.strip():
            return EngineResult(
                answer_source=AnswerSource.no_grounding,
                answer_text=response("no_grounding"),
                prompt_version=settings.prompt_version,
            )

        return EngineResult(
            answer_source=AnswerSource.generated,
            answer_text=STUB_ANSWER,
            citations=[STUB_CITATION],
            topic_slug="lainnya",
            model="stub",
            prompt_version=settings.prompt_version,
        )
