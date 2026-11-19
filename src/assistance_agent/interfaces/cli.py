"""CLI `assistance-agent` (SPEC-0001/REQ-007).

Uso portável: `uv run python -m assistance_agent chat --tenant <id> [--message "<texto>"]`.
"""

import argparse
import asyncio
import sys
from collections.abc import Mapping, Sequence

from ..config import ConfigError, Settings, build_container
from ..core.conversation import ConversationService
from ..core.messages import (
    DEFAULT_CONVERSATION,
    ConversationId,
    InvalidConversationError,
)
from ..core.tenant import InvalidTenantError, TenantId

EXIT_COMMAND = "/sair"
USER_PROMPT = "você> "
ASSISTANT_PREFIX = "assistente> "


def _tenant(value: str) -> TenantId:
    try:
        return TenantId(value)
    except InvalidTenantError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def _conversation(value: str) -> ConversationId:
    try:
        return ConversationId(value)
    except InvalidConversationError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="assistance-agent",
        description="Atendente de IA para assistências técnicas (esqueleto, LLM fake).",
    )
    commands = parser.add_subparsers(dest="command", metavar="<comando>")
    commands.required = True

    chat = commands.add_parser("chat", help="conversar com o assistente no terminal")
    chat.add_argument("--tenant", required=True, type=_tenant, help="identificador da loja")
    chat.add_argument(
        "--conversation",
        type=_conversation,
        default=DEFAULT_CONVERSATION,
        help="identificador da conversa (padrão: default)",
    )
    chat.add_argument("--message", help="envia uma única mensagem, imprime a resposta e encerra")
    return parser


async def _send_once(
    service: ConversationService, tenant: TenantId, conversation: ConversationId, text: str
) -> int:
    if not text.strip():
        print("erro: a mensagem está vazia", file=sys.stderr)
        return 2
    reply = await service.send(tenant, conversation, text)
    print(reply.content)
    return 0


async def _interactive(
    service: ConversationService, tenant: TenantId, conversation: ConversationId
) -> int:
    print(f"Conversa com o tenant '{tenant}'. Digite {EXIT_COMMAND} para sair.")
    while True:
        print(USER_PROMPT, end="", flush=True)
        line = await asyncio.to_thread(sys.stdin.readline)
        if line == "":  # EOF (Ctrl+D / Ctrl+Z)
            print()
            return 0
        text = line.strip()
        if text == EXIT_COMMAND:
            return 0
        if not text:
            continue
        reply = await service.send(tenant, conversation, text)
        print(ASSISTANT_PREFIX + reply.content, flush=True)


def main(argv: Sequence[str] | None = None, env: Mapping[str, str] | None = None) -> int:
    try:
        args = build_parser().parse_args(argv)
    except SystemExit as exc:  # argparse: --help (0) ou argumentos inválidos (2)
        return exc.code if isinstance(exc.code, int) else 2

    try:
        settings = Settings.from_env(env)
    except ConfigError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 1

    service = build_container(settings).conversations
    if args.message is not None:
        return asyncio.run(_send_once(service, args.tenant, args.conversation, args.message))
    try:
        return asyncio.run(_interactive(service, args.tenant, args.conversation))
    except KeyboardInterrupt:
        print()
        return 130
