"""Porta de embeddings (base de conhecimento / RAG)."""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal, Protocol

InputType = Literal["query", "document"]


@dataclass(frozen=True, slots=True)
class EmbeddingResult:
    """Vetores gerados e o modelo que os gerou (necessário para reindexar ao trocar de modelo)."""

    model: str
    vectors: tuple[tuple[float, ...], ...]


class EmbeddingsClient(Protocol):
    async def embed(self, texts: Sequence[str], input_type: InputType) -> EmbeddingResult: ...
