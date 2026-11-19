---
id: CTX-NTE-20261119-python-tooling-pitfalls
type: note
title: Armadilhas do ferramental Python (uv, ruff, pre-commit, terminal) encontradas no esqueleto
branch: infrastructure
tags: [tooling]
status: active
confidence: verified
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: []
related: [CTX-FCT-20261119-windows-asr-blocks-venv-exes, CTX-DEC-20261119-layered-package-and-quality-tooling, CTX-NTE-20261119-validate-script-pitfalls]
depends_on: []
---

# Armadilhas do ferramental Python

Encontradas e verificadas na implementação da `SPEC-0001` (2026-11-19, uv 0.13.9, ruff 0.17.6, pre-commit 4.7.0, Python 3.13.18).

- **O ruff 0.17 formata Markdown.** Sem configuração, `ruff format` também entra em `.md` (blocos de código) e alcançaria `Context/` e `Specs/`. O `pyproject.toml` tem `[tool.ruff] include = ["*.py", "*.pyi"]`; não remova.
- **`pre-commit run --all-files` só vê arquivos rastreados pelo git.** Antes do primeiro commit do código, os hooks dão "no files to check". Para verificar antes de commitar, use `uv run python -m pre_commit run --files <arquivos>`.
- **Acentos no Git Bash.** Com a saída redirecionada (pipe) no Git Bash, o Python no Windows escreve em cp1252 e os acentos aparecem trocados. No PowerShell (console UTF-8) e no Linux saem certos. É uma questão de exibição, não do código.
- **PATH depois de instalar o uv via winget.** Terminais abertos antes da instalação não enxergam o `uv`. Abra um terminal novo ou use `%LOCALAPPDATA%\Microsoft\WinGet\Links\uv.exe`.
- **`uv python install` falhou uma vez** ("Missing expected target directory for Python minor version link") ao criar o link `cpython-3.13-...`. A segunda execução passou sem nenhuma mudança: basta repetir.
- **O mypy (strict) cobre só `src/`** (decisão da `SPEC-0001`). Os testes não são checados por tipo; a conformidade dos adapters com as portas é verificada em `config.py`, que fica em `src/`.
- **Bloqueio de rede nos testes** (`tests/conftest.py`). Ele precisa liberar o loopback, porque o asyncio no Windows usa um par de sockets locais, e também bloquear `getaddrinfo`, senão a resolução de DNS vaza para a rede.
