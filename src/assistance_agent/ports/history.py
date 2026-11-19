"""Porta do histórico de conversas, sempre com escopo de tenant (SPEC-0001/REQ-004)."""

from typing import Protocol

from ..core.messages import ConversationId, Message
from ..core.tenant import TenantId


class ConversationHistoryStore(Protocol):
    async def load(self, tenant: TenantId, conversation: ConversationId) -> list[Message]: ...

    async def append(
        self, tenant: TenantId, conversation: ConversationId, message: Message
    ) -> None: ...
