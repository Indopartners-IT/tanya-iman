from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from models.enums import AnswerSource, AuthMethod, Platform, ValidatorCode

# --- Stored entities ---------------------------------------------------------


class User(BaseModel):
    uid: str
    auth_method: AuthMethod
    phone_e164_enc: str | None = None
    phone_hash: str | None = None
    created_at: datetime
    last_active_at: datetime
    superseded_by: str | None = None
    question_count: int = 0


class Session(BaseModel):
    id: str
    uid: str
    platform: Platform = Platform.web
    embed_origin: str | None = None
    started_at: datetime
    last_message_at: datetime
    expires_at: datetime
    message_count: int = 0


class Citation(BaseModel):
    title: str
    url: str
    site: str
    article_id: str | None = None


class Question(BaseModel):
    id: str
    session_id: str
    uid: str
    question_text: str
    answer_text: str | None = None
    answer_source: AnswerSource
    topic_slug: str | None = None
    cluster_id: str | None = None
    citations: list[Citation] = Field(default_factory=list)
    retrieved_chunk_ids: list[str] = Field(default_factory=list)
    like_count: int = 0
    is_refused: bool = False
    is_crisis: bool = False
    has_grounding: bool = False
    validator_failures: list[ValidatorCode] = Field(default_factory=list)
    model: str | None = None
    prompt_version: str | None = None
    latency_ms: int = 0
    created_at: datetime


# --- Engine contract ---------------------------------------------------------


class EngineResult(BaseModel):
    """What any answer engine returns. The stub and the real pipeline both
    satisfy this, so Phase 5 swaps the engine without touching the router."""

    answer_source: AnswerSource
    answer_text: str
    citations: list[Citation] = Field(default_factory=list)
    topic_slug: str | None = None
    retrieved_chunk_ids: list[str] = Field(default_factory=list)
    validator_failures: list[ValidatorCode] = Field(default_factory=list)
    model: str | None = None
    prompt_version: str | None = None


# --- API surface -------------------------------------------------------------


class CreateSessionRequest(BaseModel):
    platform: Platform = Platform.web
    embed_origin: str | None = None


class CreateSessionResponse(BaseModel):
    session_id: str


class AskRequest(BaseModel):
    session_id: str
    text: str


class AskResponse(BaseModel):
    question_id: str
    answer_source: AnswerSource
    answer_text: str
    citations: list[Citation] = Field(default_factory=list)
    topic_slug: str | None = None
    likeable: bool
    latency_ms: int


class LikeResponse(BaseModel):
    question_id: str
    liked: bool
    like_count: int


class HealthResponse(BaseModel):
    status: str
    env: str
    prompt_version: str
    corpus_chunk_count: int
    # Surfaced so that "staging is still running the stub" is visible in a
    # smoke check rather than discovered by a seeker.
    engine: str
