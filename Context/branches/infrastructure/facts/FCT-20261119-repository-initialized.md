---
id: CTX-FCT-20261119-repository-initialized
type: fact
title: Repositório criado vazio e inicializado com git em 2026-11-19
branch: infrastructure
tags: [git, project-setup]
status: active
confidence: verified
created_at: 2026-11-19
updated_at: 2026-11-21
source_ids: [CTX-SRC-20261119-user-bootstrap-answers]
related: [CTX-QUE-20261119-tech-stack, CTX-NTE-20261119-validate-script-pitfalls]
depends_on: []
valid_from: 2026-11-19
valid_until: null
revisit_at: null
---

# Repositório criado vazio e inicializado com git em 2026-11-19

## Fato

Em 2026-11-19 a pasta do projeto estava completamente vazia (nenhum código, documentação ou instrução de agente pré-existente). Na mesma data:

- `git init` foi executado (a pedido do usuário); **nenhum commit** foi feito;
- foi instalado o sistema de contexto: `AGENTS.md`, `CLAUDE.md`, `Context/`.

Não existe `.gitignore` nem remoto git configurado.

**Atualização (2026-11-19):** os primeiros commits já foram feitos em `main`, a pedido do usuário: bootstrap de contexto, depois `.gitattributes` forçando LF em `*.sh` (necessário para o Bash executar `Context/_meta/validate.sh` com `core.autocrlf=true`). Na sequência, foi instalado o SDD em `Specs/`. Continua sem remoto e sem `.gitignore`.

Identidade git (`user.name`/`user.email`) configurada **só neste repositório** (`git config --local`), por escolha do usuário; não alterar a configuração global.

## Implicações

- Não havia documentação a migrar; todo o conhecimento inicial veio das respostas do usuário.
- `.gitignore` criado na `SPEC-0001` (Python/uv, `.env`).

## Evidência

Inspeção da pasta e saída do `git init` durante o bootstrap (`CTX-CP-20261119-0928-context-bootstrap`).

**Atualização (2026-11-19, tarde):** existe código: o esqueleto da `SPEC-0001` (`src/assistance_agent/`, `tests/`, `pyproject.toml`, `uv.lock`, `.pre-commit-config.yaml`, `.gitignore`, `.env.example`, `.python-version`). O hook do pre-commit está instalado em `.git/hooks/pre-commit`. Commitado em `e35a0ae` (2026-11-19), junto com o contexto da sessão. Os hooks do pre-commit passaram nesse commit.

**Atualização (2026-11-19, remoto):** remoto `origin` = `https://github.com/gabrielneto-dev/assistance-agent.git`. A `main` foi enviada a pedido do usuário e acompanha `origin/main`. Push só sob pedido explícito.

**Atualização (2026-11-21, Linux Mint):** o repositório também está clonado no Linux Mint, com `main` = `origin/main` = `15bf92e`. O fechamento da `SPEC-0001` foi feito numa worktree do Claude Code (branch `claude/continuar-desenvolvimento-d63219`, em `.claude/worktrees/`) e **ainda não foi commitado**. Nesse clone o hook do pre-commit **não está instalado** (`.git/hooks` só tem exemplos): é preciso rodar `uv run python -m pre_commit install` uma vez por clone, senão os commits feitos no Linux não passam pelo ruff e pelo mypy.
