"""Serviço de conversa: registra a mensagem, consulta o LLM e guarda a resposta."""

from ..ports.history import ConversationHistoryStore
from ..ports.llm import LLMClient
from .messages import ConversationId, Message
from .tenant import TenantId


class EmptyMessageError(ValueError):
    """Mensagem do usuário vazia (só espaços)."""


class ConversationService:
    def __init__(self, llm: LLMClient, history: ConversationHistoryStore) -> None:
        self._llm = llm
        self._history = history

    async def send(self, tenant: TenantId, conversation: ConversationId, text: str) -> Message:
        """Processa uma mensagem do usuário dentro do escopo de um tenant."""
        if not text.strip():
            raise EmptyMessageError("a mensagem está vazia")
        await self._history.append(tenant, conversation, Message("user", text))
        reply = await self._llm.complete(await self._history.load(tenant, conversation))
        await self._history.append(tenant, conversation, reply)
        return reply

    async def history(self, tenant: TenantId, conversation: ConversationId) -> list[Message]:
        return await self._history.load(tenant, conversation)
