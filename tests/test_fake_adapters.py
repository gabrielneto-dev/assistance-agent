"""SPEC-0001/AC-004, AC-005, AC-006: adapters fake e histórico isolado por tenant."""

import math

from assistance_agent.adapters.fake_embeddings import (
    FAKE_EMBEDDINGS_DIMENSION,
    FAKE_EMBEDDINGS_MODEL,
    FakeEmbeddingsClient,
)
from assistance_agent.adapters.fake_llm import FakeLLMClient
from assistance_agent.adapters.memory_history import InMemoryHistoryStore
from assistance_agent.core.messages import ConversationId, Message
from assistance_agent.core.tenant import TenantId
from assistance_agent.ports.embeddings import EmbeddingsClient
from assistance_agent.ports.history import ConversationHistoryStore
from assistance_agent.ports.llm import LLMClient

# Conformidade estrutural com as portas (checada pelo mypy).
_llm: LLMClient = FakeLLMClient()
_emb: EmbeddingsClient = FakeEmbeddingsClient()
_hist: ConversationHistoryStore = InMemoryHistoryStore()


async def test_fake_llm_is_deterministic() -> None:
    llm = FakeLLMClient()
    history = [Message("user", "oi")]
    first = await llm.complete(history)
    second = await llm.complete(history)
    assert first == second
    assert first.role == "assistant"
    assert "oi" in first.content


async def test_fake_llm_answers_last_user_message() -> None:
    llm = FakeLLMClient()
    history = [Message("user", "primeira"), Message("assistant", "x"), Message("user", "segunda")]
    reply = await llm.complete(history)
    assert reply.content.endswith("segunda")


async def test_fake_embeddings_are_deterministic_and_normalized() -> None:
    result = await FakeEmbeddingsClient().embed(["x", "x", "y"], "document")
    x1, x2, y = result.vectors
    assert result.model == FAKE_EMBEDDINGS_MODEL
    assert x1 == x2
    assert x1 != y
    assert {len(v) for v in result.vectors} == {FAKE_EMBEDDINGS_DIMENSION}
    for vector in result.vectors:
        assert math.isclose(math.fsum(c * c for c in vector), 1.0)


async def test_fake_embeddings_distinguish_query_and_document() -> None:
    client = FakeEmbeddingsClient()
    doc = await client.embed(["x"], "document")
    query = await client.embed(["x"], "query")
    assert doc.vectors != query.vectors


async def test_history_is_isolated_per_tenant() -> None:
    store = InMemoryHistoryStore()
    conv = ConversationId("c1")
    a, b = TenantId("a"), TenantId("b")
    await store.append(a, conv, Message("user", "mensagem de a"))
    await store.append(b, conv, Message("user", "mensagem de b"))

    assert await store.load(a, conv) == [Message("user", "mensagem de a")]
    assert await store.load(b, conv) == [Message("user", "mensagem de b")]
    assert await store.load(TenantId("c"), conv) == []


async def test_history_load_returns_a_copy() -> None:
    store = InMemoryHistoryStore()
    tenant, conv = TenantId("a"), ConversationId("c1")
    await store.append(tenant, conv, Message("user", "oi"))
    loaded = await store.load(tenant, conv)
    loaded.append(Message("user", "intruso"))
    assert await store.load(tenant, conv) == [Message("user", "oi")]
