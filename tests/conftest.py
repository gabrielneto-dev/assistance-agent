"""Configuração comum dos testes.

Toda conexão de rede para fora da máquina é bloqueada (SPEC-0001/REQ-011). Conexões de
loopback continuam permitidas porque o asyncio usa um par de sockets locais no Windows.
"""

import socket
from collections.abc import Callable
from typing import Any

import pytest

LOOPBACK_HOSTS = {"127.0.0.1", "::1", "localhost"}


class NetworkAccessError(RuntimeError):
    """Um teste tentou acessar a rede externa."""


def _is_loopback(address: Any) -> bool:
    return isinstance(address, tuple) and len(address) >= 1 and address[0] in LOOPBACK_HOSTS


def _guard(original: Callable[..., Any]) -> Callable[..., Any]:
    def guarded(sock: socket.socket, address: Any, *args: Any, **kwargs: Any) -> Any:
        if _is_loopback(address):
            return original(sock, address, *args, **kwargs)
        raise NetworkAccessError(f"acesso à rede bloqueado nos testes: {address!r}")

    return guarded


def _guard_getaddrinfo(original: Callable[..., Any]) -> Callable[..., Any]:
    def guarded(host: Any, *args: Any, **kwargs: Any) -> Any:
        if host is None or host in LOOPBACK_HOSTS:
            return original(host, *args, **kwargs)
        raise NetworkAccessError(f"resolução de DNS bloqueada nos testes: {host!r}")

    return guarded


@pytest.fixture(autouse=True)
def _block_network(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(socket.socket, "connect", _guard(socket.socket.connect))
    monkeypatch.setattr(socket.socket, "connect_ex", _guard(socket.socket.connect_ex))
    monkeypatch.setattr(socket, "getaddrinfo", _guard_getaddrinfo(socket.getaddrinfo))
