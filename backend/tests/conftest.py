from __future__ import annotations

import os

os.environ.setdefault("ENV", "development")
os.environ.setdefault("STORAGE_BACKEND", "memory")
os.environ.setdefault("ANSWER_ENGINE", "stub")
os.environ.setdefault("LLM_PROVIDER", "fake")
os.environ.setdefault("OTP_PROVIDER", "fake")

import pytest  # noqa: E402
from httpx import ASGITransport, AsyncClient  # noqa: E402

from engine import reset_engine  # noqa: E402
from providers.llm import reset_llm  # noqa: E402
from providers.otp import reset_otp  # noqa: E402
from storage import MemoryStorage, reset_storage  # noqa: E402


@pytest.fixture
def storage() -> MemoryStorage:
    store = MemoryStorage()
    reset_storage(store)
    yield store
    reset_storage(None)
    reset_engine(None)
    reset_llm(None)
    reset_otp(None)


@pytest.fixture
async def client(storage: MemoryStorage) -> AsyncClient:
    from main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def auth_headers() -> dict[str, str]:
    return {"Authorization": "Bearer dev:u_test:guest"}


@pytest.fixture
async def session_id(client: AsyncClient, auth_headers: dict[str, str]) -> str:
    response = await client.post("/sessions", json={"platform": "web"}, headers=auth_headers)
    return response.json()["session_id"]
