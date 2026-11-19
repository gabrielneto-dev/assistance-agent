"""Histórico de conversas em memória, com chave (tenant, conversa) (SPEC-0001/REQ-004)."""

from ..core.messages import ConversationId, Message
from ..core.tenant import TenantId


class InMemoryHistoryStore:
    def __init__(self) -> None:
        self._data: dict[tuple[TenantId, ConversationId], list[Message]] = {}

    async def load(self, tenant: TenantId, conversation: ConversationId) -> list[Message]:
        # Cópia: quem chama não consegue alterar o histórico armazenado.
        return list(self._data.get((tenant, conversation), ()))

    async def append(
        self, tenant: TenantId, conversation: ConversationId, message: Message
    ) -> None:
        self._data.setdefault((tenant, conversation), []).append(message)
