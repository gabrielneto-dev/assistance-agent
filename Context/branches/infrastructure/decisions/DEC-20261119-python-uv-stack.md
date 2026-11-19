---
id: CTX-DEC-20261119-python-uv-stack
type: decision
title: Projeto em Python com uv como gerenciador de pacotes e ambiente
branch: infrastructure
tags: [stack, tooling]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-QUE-20261119-tech-stack, CTX-DEC-20261119-local-cross-platform-runtime, CTX-DEC-20261119-layered-package-and-quality-tooling]
depends_on: []
supersedes: null
superseded_by: null
revisit_at: null
---

# Python com uv

## Decisão

- Linguagem: **Python**.
- Gerenciador de pacotes, versão do Python e ambiente virtual: **uv** (`pyproject.toml` + `uv.lock` versionados).

## Opções consideradas

- TypeScript (Node) — preterido pelo usuário.
- Poetry, pip + venv — preteridos em favor de uv.

## Motivo

Escolha do usuário. Python tem ecossistema forte para agentes/RAG; uv é rápido, tem lockfile e gerencia a versão do Python de forma idêntica em Windows e Linux (`CTX-DEC-20261119-local-cross-platform-runtime`).

## Consequências

- Dependências via `uv add`, execução via `uv run`, sincronização via `uv sync` (regra em `AGENTS.md`).
- `.gitignore` de Python/uv pode ser criado.

## Em aberto

Framework da API, banco de dados e armazenamento vetorial → `CTX-QUE-20261119-tech-stack`.
