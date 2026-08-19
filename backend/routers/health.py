from __future__ import annotations

from fastapi import APIRouter

from config import get_settings
from engine import get_engine
from models import HealthResponse
from routers.deps import StorageDep

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health(storage: StorageDep) -> HealthResponse:
    """Liveness plus the two facts that catch the worst deploy mistakes:
    which engine is live, and whether the corpus is actually there."""
    settings = get_settings()
    return HealthResponse(
        status="ok",
        env=str(settings.env),
        prompt_version=settings.prompt_version,
        corpus_chunk_count=await storage.count_article_chunks(),
        engine=get_engine().name,
    )
