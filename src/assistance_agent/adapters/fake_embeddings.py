"""Embeddings fake: vetores determinísticos derivados de SHA-256 (SPEC-0001/REQ-006)."""

import hashlib
import math
from collections.abc import Sequence

from ..ports.embeddings import EmbeddingResult, InputType

FAKE_EMBEDDINGS_MODEL = "fake-embeddings-v1"
FAKE_EMBEDDINGS_DIMENSION = 8


def _vector(text: str, input_type: InputType) -> tuple[float, ...]:
    digest = hashlib.sha256(f"{input_type}:{text}".encode()).digest()
    raw = [(byte - 127.5) / 127.5 for byte in digest[:FAKE_EMBEDDINGS_DIMENSION]]
    norm = math.sqrt(sum(x * x for x in raw)) or 1.0
    return tuple(x / norm for x in raw)


class FakeEmbeddingsClient:
    """Texto igual → vetor igual; vetores normalizados (comprimento 1)."""

    async def embed(self, texts: Sequence[str], input_type: InputType) -> EmbeddingResult:
        return EmbeddingResult(
            model=FAKE_EMBEDDINGS_MODEL,
            vectors=tuple(_vector(text, input_type) for text in texts),
        )
