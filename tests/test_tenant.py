"""SPEC-0001/AC-003: `TenantId` exige identificador válido; não há tenant padrão."""

import pytest

from assistance_agent.core.messages import (
    ConversationId,
    InvalidConversationError,
    InvalidMessageError,
    Message,
)
from assistance_agent.core.tenant import InvalidTenantError, TenantId


@pytest.mark.parametrize(
    "value",
    ["", "Loja", "loja centro", "-loja", "loja_1", "a" * 65, "loja!", " loja", None, 123],
)
def test_invalid_tenant_is_rejected(value: object) -> None:
    with pytest.raises(InvalidTenantError):
        TenantId(value)  # type: ignore[arg-type]


@pytest.mark.parametrize("value", ["a", "demo", "loja-centro-2", "1loja", "a" * 64])
def test_valid_tenant_is_accepted(value: str) -> None:
    assert str(TenantId(value)) == value


def test_tenant_has_no_default() -> None:
    with pytest.raises(TypeError):
        TenantId()  # type: ignore[call-arg]


def test_tenants_compare_by_value() -> None:
    assert TenantId("a") == TenantId("a")
    assert TenantId("a") != TenantId("b")


def test_invalid_conversation_is_rejected() -> None:
    with pytest.raises(InvalidConversationError):
        ConversationId("Conversa 1")


def test_message_rejects_unknown_role() -> None:
    with pytest.raises(InvalidMessageError):
        Message("robot", "oi")  # type: ignore[arg-type]
