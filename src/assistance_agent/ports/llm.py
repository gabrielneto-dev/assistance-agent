"""Porta do modelo de linguagem (o provedor ainda não foi escolhido)."""

from collections.abc import Sequence
from typing import Protocol

from ..core.messages import Message


class LLMClient(Protocol):
    """Gera a próxima mensagem do assistente a partir do histórico."""

    async def complete(self, messages: Sequence[Message]) -> Message: ...
