"""SPEC-0001/AC-007, AC-008, AC-009: CLI `chat`."""

import io
import subprocess
import sys

import pytest

from assistance_agent.adapters.fake_llm import FAKE_PREFIX
from assistance_agent.config import LLM_PROVIDER_VAR
from assistance_agent.interfaces.cli import ASSISTANT_PREFIX, main


def test_help_lists_chat(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--help"], env={}) == 0
    assert "chat" in capsys.readouterr().out


def test_single_message(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["chat", "--tenant", "demo", "--message", "oi"], env={})
    out = capsys.readouterr().out
    assert code == 0
    assert out.strip() == FAKE_PREFIX + "oi"


def test_interactive_session_until_exit_command(
    capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(sys, "stdin", io.StringIO("oi\n\n/sair\nnão deve ser lido\n"))
    code = main(["chat", "--tenant", "demo"], env={})
    out = capsys.readouterr().out
    assert code == 0
    assert out.count(ASSISTANT_PREFIX) == 1
    assert ASSISTANT_PREFIX + FAKE_PREFIX + "oi" in out
    assert "não deve ser lido" not in out


def test_interactive_session_ends_on_eof(
    capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(sys, "stdin", io.StringIO("oi\n"))
    assert main(["chat", "--tenant", "demo"], env={}) == 0
    captured = capsys.readouterr()
    assert ASSISTANT_PREFIX + FAKE_PREFIX + "oi" in captured.out
    assert "Traceback" not in captured.err


@pytest.mark.parametrize(
    "argv",
    [
        ["chat", "--tenant", "Inválido!", "--message", "oi"],
        ["chat", "--message", "oi"],
        ["chat", "--tenant", "demo", "--conversation", "Conversa X", "--message", "oi"],
        [],
    ],
)
def test_invalid_arguments_exit_2(argv: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    assert main(argv, env={}) == 2
    captured = capsys.readouterr()
    assert captured.err.strip() != ""
    assert captured.out == ""


def test_empty_single_message_exit_2(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["chat", "--tenant", "demo", "--message", "  "], env={}) == 2
    assert "vazia" in capsys.readouterr().err


def test_unknown_provider_lists_accepted_values(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["chat", "--tenant", "demo", "--message", "oi"], env={LLM_PROVIDER_VAR: "x"})
    captured = capsys.readouterr()
    assert code != 0
    assert "fake" in captured.err
    assert captured.out == ""


def test_python_dash_m_entry_point() -> None:
    """Executa o pacote de verdade, como o usuário faria (`python -m assistance_agent`)."""
    result = subprocess.run(
        [sys.executable, "-m", "assistance_agent", "chat", "--tenant", "demo", "--message", "oi"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={"PYTHONIOENCODING": "utf-8", "SYSTEMROOT": _systemroot()},
        timeout=60,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == FAKE_PREFIX + "oi"


def _systemroot() -> str:
    import os

    return os.environ.get("SYSTEMROOT", "")
