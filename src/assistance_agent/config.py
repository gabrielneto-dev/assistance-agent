"""Composition root: lê a configuração do ambiente e liga as portas aos adapters.

Variáveis (só nomes; valores em `.env`, que não é versionado — ver `.env.example`):
- `ASSISTANCE_AGENT_LLM_PROVIDER`: adapter de LLM. Padrão: `fake`.
"""

import os
from collections.abc import Callable, Mapping
from dataclasses import dataclass

from .adapters.fake_embeddings import FakeEmbeddingsClient
from .adapters.fake_llm import FakeLLMClient
from .adapters.memory_history import InMemoryHistoryStore
from .core.conversation import ConversationService
from .ports.embeddings import EmbeddingsClient
from .ports.history import ConversationHistoryStore
from .ports.llm import LLMClient

LLM_PROVIDER_VAR = "ASSISTANCE_AGENT_LLM_PROVIDER"
DEFAULT_LLM_PROVIDER = "fake"

LLM_PROVIDERS: dict[str, Callable[[], LLMClient]] = {"fake": FakeLLMClient}


class ConfigError(ValueError):
    """Configuração inválida."""


@dataclass(frozen=True, slots=True)
class Settings:
    llm_provider: str

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "Settings":
        source = os.environ if env is None else env
        provider = source.get(LLM_PROVIDER_VAR, "").strip().lower() or DEFAULT_LLM_PROVIDER
        if provider not in LLM_PROVIDERS:
            accepted = ", ".join(sorted(LLM_PROVIDERS))
            raise ConfigError(
                f"{LLM_PROVIDER_VAR}={provider!r} não é suportado. Valores aceitos: {accepted}."
            )
        return cls(llm_provider=provider)


@dataclass(frozen=True, slots=True)
class Container:
    llm: LLMClient
    embeddings: EmbeddingsClient
    history: ConversationHistoryStore
    conversations: ConversationService


def build_container(settings: Settings) -> Container:
    llm = LLM_PROVIDERS[settings.llm_provider]()
    history: ConversationHistoryStore = InMemoryHistoryStore()
    return Container(
        llm=llm,
        embeddings=FakeEmbeddingsClient(),
        history=history,
        conversations=ConversationService(llm, history),
    )
