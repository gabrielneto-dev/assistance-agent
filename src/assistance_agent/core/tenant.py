"""Identificação do tenant (loja de assistência técnica).

Todo acesso a dados exige um `TenantId` explícito; não existe tenant padrão (SPEC-0001/REQ-003).
"""

import re
from dataclasses import dataclass

# 1 a 64 caracteres em [a-z0-9-], começando por letra ou dígito (SPEC-0001, hipótese A1).
_IDENTIFIER = re.compile(r"[a-z0-9][a-z0-9-]{0,63}")


class InvalidIdentifierError(ValueError):
    """Identificador fora do formato permitido."""


class InvalidTenantError(InvalidIdentifierError):
    """`TenantId` vazio ou fora do formato permitido."""


def validate_identifier(value: object, error: type[InvalidIdentifierError], kind: str) -> str:
    if not isinstance(value, str) or not _IDENTIFIER.fullmatch(value):
        raise error(
            f"{kind} inválido: {value!r}. Use 1 a 64 caracteres em a-z, 0-9 e '-', "
            "começando por letra ou dígito."
        )
    return value


@dataclass(frozen=True, slots=True)
class TenantId:
    value: str

    def __post_init__(self) -> None:
        validate_identifier(self.value, InvalidTenantError, "tenant")

    def __str__(self) -> str:
        return self.value
