from __future__ import annotations

from fastapi import APIRouter

from models import CreateSessionRequest, CreateSessionResponse
from routers.deps import CurrentUser, StorageDep
from services.sessions import start_session

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("", response_model=CreateSessionResponse, status_code=201)
async def create_session(
    payload: CreateSessionRequest,
    user: CurrentUser,
    storage: StorageDep,
) -> CreateSessionResponse:
    session = await start_session(
        storage,
        uid=user.uid,
        platform=payload.platform,
        embed_origin=payload.embed_origin,
    )
    return CreateSessionResponse(session_id=session.id)
