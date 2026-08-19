import pytest

pytestmark = pytest.mark.asyncio


async def test_health_reports_engine_and_corpus(client):
    response = await client.get("/health")
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "ok"
    # Phase 2 runs the stub with an empty corpus. Both facts must be visible.
    assert body["engine"] == "stub"
    assert body["corpus_chunk_count"] == 0


async def test_ask_requires_a_token(client, session_id):
    response = await client.post("/ask", json={"session_id": session_id, "text": "halo"})
    assert response.status_code == 401


async def test_ask_returns_an_answer_with_citations(client, auth_headers, session_id):
    response = await client.post(
        "/ask",
        json={"session_id": session_id, "text": "Siapakah Isa Al-Masih?"},
        headers=auth_headers,
    )
    body = response.json()

    assert response.status_code == 200
    assert body["answer_source"] == "generated"
    assert body["citations"]
    assert body["likeable"] is True


async def test_ask_rejects_empty_text(client, auth_headers, session_id):
    response = await client.post(
        "/ask", json={"session_id": session_id, "text": "   "}, headers=auth_headers
    )
    assert response.status_code == 400


async def test_ask_rejects_another_users_session(client, session_id):
    """The session belongs to u_test. u_other must not be able to post into it."""
    response = await client.post(
        "/ask",
        json={"session_id": session_id, "text": "halo"},
        headers={"Authorization": "Bearer dev:u_other:guest"},
    )
    assert response.status_code == 404


async def test_multi_turn_conversation_reuses_one_session(
    client, auth_headers, session_id, storage
):
    """F-6: a seeker asks follow-ups in the same conversation."""
    for text in ["Siapakah Isa?", "Mengapa Dia disalibkan?", "Apa artinya bagi saya?"]:
        response = await client.post(
            "/ask",
            json={"session_id": session_id, "text": text},
            headers=auth_headers,
        )
        assert response.status_code == 200

    session = await storage.get_session(session_id)
    assert session.message_count == 3


async def test_crisis_input_bypasses_the_engine(client, auth_headers, session_id):
    response = await client.post(
        "/ask",
        json={"session_id": session_id, "text": "saya ingin bunuh diri"},
        headers=auth_headers,
    )
    body = response.json()

    assert body["answer_source"] == "crisis"
    assert body["citations"] == []
    # F-33: a crisis response must not be likeable.
    assert body["likeable"] is False


async def test_crisis_response_is_still_returned_past_the_rate_limit(
    client, auth_headers, session_id, storage
):
    """F-30. This is the test that keeps the guard ordering honest."""
    from datetime import datetime

    from config import get_settings
    from services.guards import hour_bucket

    # Burn the quota in the window the limiter will actually read.
    bucket = hour_bucket(datetime.now())
    for _ in range(get_settings().rate_limit_per_hour + 5):
        await storage.increment_rate_window("u_test", bucket)

    response = await client.post(
        "/ask",
        json={"session_id": session_id, "text": "saya ingin bunuh diri"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["answer_source"] == "crisis"


async def test_rate_limit_returns_429_with_retry_after(client, auth_headers, session_id):
    from config import get_settings

    limit = get_settings().rate_limit_per_hour
    for _ in range(limit):
        await client.post(
            "/ask",
            json={"session_id": session_id, "text": "halo"},
            headers=auth_headers,
        )

    response = await client.post(
        "/ask", json={"session_id": session_id, "text": "halo"}, headers=auth_headers
    )
    assert response.status_code == 429
    assert "Retry-After" in response.headers


async def test_like_is_idempotent(client, auth_headers, session_id):
    ask = await client.post(
        "/ask", json={"session_id": session_id, "text": "halo"}, headers=auth_headers
    )
    question_id = ask.json()["question_id"]

    first = await client.post(f"/questions/{question_id}/like", headers=auth_headers)
    second = await client.post(f"/questions/{question_id}/like", headers=auth_headers)

    assert first.json()["like_count"] == 1
    assert second.json()["like_count"] == 1


async def test_crisis_answer_cannot_be_liked(client, auth_headers, session_id):
    ask = await client.post(
        "/ask",
        json={"session_id": session_id, "text": "saya ingin bunuh diri"},
        headers=auth_headers,
    )
    question_id = ask.json()["question_id"]

    response = await client.post(f"/questions/{question_id}/like", headers=auth_headers)
    assert response.status_code == 409
