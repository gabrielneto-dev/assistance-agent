"""SPEC-0001/AC-012: a suíte não consegue acessar a rede externa."""

import socket

import pytest

from conftest import NetworkAccessError


def test_external_connection_is_blocked() -> None:
    with pytest.raises(NetworkAccessError):
        socket.create_connection(("example.com", 443), timeout=1)


def test_external_connection_by_ip_is_blocked() -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        with pytest.raises(NetworkAccessError):
            sock.connect(("93.184.216.34", 80))
    finally:
        sock.close()


async def test_asyncio_event_loop_still_works() -> None:
    # O loop de eventos usa sockets de loopback internamente; não pode ser bloqueado.
    import asyncio

    await asyncio.sleep(0)
