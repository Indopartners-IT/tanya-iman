"""Storage interface.

Only modules in this package may import a database SDK. Everything above the
storage layer talks to this protocol, which is what makes the test suite run
without an emulator and keeps a future backend swap to one directory.
"""

from __future__ import annotations

from datetime import datetime
from typing import Protocol

from models import Question, Session, User
from models.enums import AuthMethod, Platform


class Storage(Protocol):
    # --- users ---------------------------------------------------------------
    async def get_user(self, uid: str) -> User | None: ...

    async def create_user(self, uid: str, auth_method: AuthMethod) -> User: ...

    async def touch_user(self, uid: str, at: datetime) -> None: ...

    # --- sessions ------------------------------------------------------------
    async def create_session(
        self,
        uid: str,
        platform: Platform,
        embed_origin: str | None,
        now: datetime,
        ttl_hours: int,
    ) -> Session: ...

    async def get_session(self, session_id: str) -> Session | None: ...

    async def record_turn(self, session_id: str, now: datetime, ttl_hours: int) -> None: ...

    # --- questions -----------------------------------------------------------
    async def save_question(self, question: Question) -> None: ...

    async def get_question(self, question_id: str) -> Question | None: ...

    async def recent_questions(self, session_id: str, limit: int) -> list[Question]: ...

    # --- likes ---------------------------------------------------------------
    async def set_like(self, uid: str, question_id: str, liked: bool) -> int:
        """Idempotent by construction — the like key is ``{uid}_{question_id}``.

        Returns the resulting like count for the question.
        """
        ...

    async def is_liked(self, uid: str, question_id: str) -> bool: ...

    # --- rate limiting -------------------------------------------------------
    async def increment_rate_window(self, uid: str, bucket: str) -> int:
        """Atomically increment and return the count for this uid/hour bucket."""
        ...

    # --- corpus --------------------------------------------------------------
    async def count_article_chunks(self) -> int: ...
