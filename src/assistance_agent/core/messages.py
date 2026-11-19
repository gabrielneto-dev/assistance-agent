"""Mensagens e identificação de conversas."""

from dataclasses import dataclass
from typing import Literal

from .tenant import InvalidIdentifierError, validate_identifier

Role = Literal["user", "assistant", "system"]
ROLES: frozenset[str] = frozenset({"user", "assistant", "system"})


class InvalidConversationError(InvalidIdentifierError):
    """`ConversationId` vazio ou fora do formato permitido."""


class InvalidMessageError(ValueError):
    """Mensagem com papel desconhecido ou conteúdo que não é texto."""


@dataclass(frozen=True, slots=True)
class ConversationId:
    value: str

    def __post_init__(self) -> None:
        validate_identifier(self.value, InvalidConversationError, "conversa")

    def __str__(self) -> str:
        return self.value


DEFAULT_CONVERSATION = ConversationId("default")


@dataclass(frozen=True, slots=True)
class Message:
    role: Role
    content: str

    def __post_init__(self) -> None:
        if self.role not in ROLES:
            raise InvalidMessageError(f"papel desconhecido: {self.role!r}")
        if not isinstance(self.content, str):
            raise InvalidMessageError("o conteúdo da mensagem precisa ser texto")
