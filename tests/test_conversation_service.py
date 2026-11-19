"""SPEC-0001/AC-004 (serviço) e AC-009 (configuração, nível unitário)."""

import pytest

from assistance_agent.adapters.fake_llm import FakeLLMClient
from assistance_agent.adapters.memory_history import InMemoryHistoryStore
from assistance_agent.config import (
    LLM_PROVIDER_VAR,
    ConfigError,
    Settings,
    build_container,
)
from assistance_agent.core.conversation import ConversationService, EmptyMessageError
from assistance_agent.core.messages import ConversationId, Message
from assistance_agent.core.tenant import TenantId


@pytest.fixture
def service() -> ConversationService:
    return ConversationService(FakeLLMClient(), InMemoryHistoryStore())


async def test_send_records_user_message_and_reply(service: ConversationService) -> None:
    tenant, conv = TenantId("demo"), ConversationId("c1")
    reply = await service.send(tenant, conv, "oi")
    assert reply.role == "assistant"
    assert await service.history(tenant, conv) == [Message("user", "oi"), reply]


async def test_two_tenants_same_conversation_are_isolated(service: ConversationService) -> None:
    conv = ConversationId("c1")
    await service.send(TenantId("a"), conv, "segredo da loja a")
    await service.send(TenantId("b"), conv, "mensagem da loja b")

    history_a = await service.history(TenantId("a"), conv)
    history_b = await service.history(TenantId("b"), conv)
    assert all("loja b" not in m.content for m in history_a)
    assert all("loja a" not in m.content for m in history_b)
    assert len(history_a) == len(history_b) == 2


async def test_empty_message_is_rejected_without_calling_llm(
    service: ConversationService,
) -> None:
    tenant, conv = TenantId("demo"), ConversationId("c1")
    with pytest.raises(EmptyMessageError):
        await service.send(tenant, conv, "   ")
    assert await service.history(tenant, conv) == []


def test_default_provider_is_fake() -> None:
    assert Settings.from_env({}).llm_provider == "fake"
    assert Settings.from_env({LLM_PROVIDER_VAR: ""}).llm_provider == "fake"


def test_unknown_provider_lists_accepted_values() -> None:
    with pytest.raises(ConfigError, match="fake"):
        Settings.from_env({LLM_PROVIDER_VAR: "inexistente"})


def test_container_uses_fake_llm_by_default() -> None:
    container = build_container(Settings.from_env({}))
    assert isinstance(container.llm, FakeLLMClient)
