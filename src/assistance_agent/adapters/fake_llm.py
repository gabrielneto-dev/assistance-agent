"""LLM fake: determinístico, sem rede e sem credenciais (SPEC-0001/REQ-005)."""

from collections.abc import Sequence

from ..core.messages import Message

FAKE_PREFIX = "[fake] você disse: "
FAKE_EMPTY_REPLY = "[fake] olá! Como posso ajudar?"


class FakeLLMClient:
    """Repete a última mensagem do usuário.

    Serve para testes e para a CLI enquanto não há provedor real.
    """

    async def complete(self, messages: Sequence[Message]) -> Message:
        last_user = next((m.content for m in reversed(messages) if m.role == "user"), None)
        if last_user is None:
            return Message("assistant", FAKE_EMPTY_REPLY)
        return Message("assistant", FAKE_PREFIX + last_user)
