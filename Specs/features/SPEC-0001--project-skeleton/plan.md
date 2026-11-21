---
id: SPEC-0001-PLAN
type: plan
spec: SPEC-0001
title: Plano técnico — Esqueleto do projeto
status: done
created_at: 2026-11-19
updated_at: 2026-11-19
context_refs:
  - CTX-DEC-20261119-python-uv-stack
  - CTX-DEC-20261119-layered-package-and-quality-tooling
  - CTX-DEC-20261119-local-cross-platform-runtime
  - CTX-DEC-20261119-multi-tenant-saas-product
---

# Plano técnico — SPEC-0001

## Current Architecture

Inspecionado em 2026-11-19:

- Não há código-fonte. O repositório contém só `AGENTS.md`, `CLAUDE.md`, `.gitattributes` (`*.sh` em LF), `Context/` e `Specs/`.
- O uv não está instalado no Windows. O Python do sistema é 3.12.10, abaixo do mínimo; o uv baixa o 3.13 sozinho.
- Ainda não há `.gitignore`.

## Approach

1. Instalar o uv (pré-requisito; ação do usuário).
2. `uv init --package` → ajustar o `pyproject.toml` (nome, `requires-python = ">=3.13"`, script `assistance-agent`) e criar as camadas.
3. Domínio e portas primeiro, guiados pelos testes. Depois os adapters fake, a configuração e por último a CLI.
4. Ferramentas de qualidade e o pre-commit com hooks locais.
5. Verificar no Windows e depois no Linux Mint.

## Affected Components and Files

| Componente/arquivo | Mudança | REQ |
|---|---|---|
| `pyproject.toml`, `uv.lock`, `.python-version` | novos: metadados, dependências de dev, configuração de ruff/mypy/pytest | REQ-001, REQ-010 |
| `src/assistance_agent/__init__.py` | novo | REQ-002 |
| `src/assistance_agent/core/tenant.py` | `TenantId` (value object validado) e `InvalidTenantError` | REQ-003 |
| `src/assistance_agent/core/messages.py` | `Message` (role, content), `ConversationId` (separado do serviço para evitar import circular core↔ports) | REQ-004, REQ-005 |
| `src/assistance_agent/core/conversation.py` | `ConversationService` | REQ-004, REQ-005 |
| `src/assistance_agent/ports/llm.py` | `LLMClient` (Protocol): `async complete(messages) -> Message` | REQ-005 |
| `src/assistance_agent/ports/embeddings.py` | `EmbeddingsClient` (Protocol): `async embed(texts, input_type) -> EmbeddingResult(model, vectors)` | REQ-006 |
| `src/assistance_agent/ports/history.py` | `ConversationHistoryStore` (Protocol): `load(tenant, conversation)`, `append(tenant, conversation, message)` | REQ-004 |
| `src/assistance_agent/adapters/fake_llm.py` | `FakeLLMClient` determinístico | REQ-005 |
| `src/assistance_agent/adapters/fake_embeddings.py` | `FakeEmbeddingsClient`: vetor derivado de hash SHA-256, dimensão fixa e normalizado | REQ-006 |
| `src/assistance_agent/adapters/memory_history.py` | `InMemoryHistoryStore`: dicionário com chave `(TenantId, ConversationId)` | REQ-004 |
| `src/assistance_agent/config.py` | lê `ASSISTANCE_AGENT_LLM_PROVIDER` e monta os adapters (composition root) | REQ-008 |
| `src/assistance_agent/interfaces/cli.py` | `argparse`; subcomando `chat`; `asyncio.run` | REQ-007 |
| `tests/` | testes unitários, de arquitetura, da CLI (subprocess ou `main(argv)`) e bloqueio de rede | REQ-002..REQ-011 |
| `.gitignore`, `.gitattributes`, `.env.example`, `.pre-commit-config.yaml` | novos / alterado | REQ-008, REQ-010, REQ-012 |
| `AGENTS.md` (Convenções) | comandos de qualidade | REQ-010 |

## Data Model and Flows

Fluxo de uma mensagem:

```text
CLI (--tenant, --conversation, texto)
  → TenantId(...) valida
  → ConversationService.send(tenant, conversation, text)
      → history.append(tenant, conv, user msg)
      → llm.complete(history.load(tenant, conv))
      → history.append(tenant, conv, assistant msg)
  → imprime a resposta
```

O `core` depende só de `ports` (Protocols). A ligação com os adapters é feita em `config.py`, fora do `core`.

## Interfaces / API Contracts

- `Message`: `role: Literal["user", "assistant", "system"]`, `content: str` (dataclass imutável).
- `EmbeddingResult`: `model: str`, `vectors: list[list[float]]`.
- O fake de embeddings usa o identificador de modelo `fake-embeddings-v1` e dimensão 8.

## Security and Privacy

- Não há segredos. `.env` vai para o `.gitignore`; `.env.example` tem só os nomes das variáveis.
- O isolamento por tenant é garantido pela chave composta do store e testado (AC-004). Sem autenticação nesta spec.

## Performance and Compatibility

- Python ≥ 3.13, sem dependências de runtime além da biblioteca padrão. Dependências de dev: pytest, pytest-asyncio, ruff, mypy, pre-commit.
- Portabilidade: `pathlib`, nenhum script de shell, `.gitattributes` com `*.py text eol=lf`.

## Migrations and Rollback

Não há estado nem dados. Rollback = reverter os commits da spec.

## Test Strategy

| AC | Verificação |
|---|---|
| AC-001 | `uv sync` e `uv run assistance-agent --help` (manual e registrado) |
| AC-002 | `tests/test_architecture.py`: varre os arquivos de `core/` e `ports/` com `ast` em busca de imports proibidos |
| AC-003 | `tests/core/test_tenant.py`, parametrizado |
| AC-004 | `tests/adapters/test_memory_history.py` e um teste do serviço com dois tenants |
| AC-005, AC-006 | testes dos fakes |
| AC-007, AC-008, AC-009 | `tests/interfaces/test_cli.py` chamando `main(argv)` com stdin/stdout capturados e env com `monkeypatch`, mais uma execução real via `uv run` registrada |
| AC-010 | executar no Windows (agente) e no Linux Mint (usuário) e registrar ambos |
| AC-011 | os quatro comandos de qualidade e `uv run pre-commit run --all-files` |
| AC-012 | fixture `autouse` em `tests/conftest.py` que faz `socket.socket.connect` levantar erro, e execução sem variáveis de credencial |
| AC-013 | `git check-ignore` e `git check-attr` |

## Decisions

- **Duráveis** (registradas em `Context/`): `CTX-DEC-20261119-layered-package-and-quality-tooling` (layout, Python 3.13, ferramentas).
- **Locais**:
  - ports assíncronas (A2);
  - `argparse` na CLI (A3);
  - `typing.Protocol` para as portas;
  - pytest-asyncio para os testes assíncronos;
  - mypy `strict = true` em `src/`;
  - pre-commit com hooks `repo: local` (`uv run python -m ruff ...`, `uv run python -m mypy`), sem baixar hooks;
  - todo comando de ferramenta usa `uv run python -m <módulo>`, porque os lançadores `.exe` do `.venv` são bloqueados pelo Defender (ASR) no Windows de desenvolvimento;
  - `src/assistance_agent/__main__.py` para permitir `python -m assistance_agent`.

## Trade-offs

- Ports assíncronas complicam um pouco a CLI (`asyncio.run`), mas evitam reescrever tudo quando vierem a API e os SDKs assíncronos dos provedores.
- `argparse` tem menos ergonomia que Typer, mas não acrescenta dependência.

## Risks and Dependencies

- Pré-requisito: instalar o uv. Isso exige baixar e executar o instalador oficial; fica a cargo do usuário (T001).
- Windows (ASR do Defender, gerenciado pela TI) bloqueia `.venv/Scripts/*.exe`; usar sempre `python -m`. Não alterar a política.
- O AC-010 depende do Linux Mint, que o agente não acessa: o resultado fica NOT_RUN até o usuário rodar lá.
