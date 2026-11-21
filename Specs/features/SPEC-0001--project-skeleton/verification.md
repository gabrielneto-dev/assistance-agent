---
id: SPEC-0001-VER
type: verification
spec: SPEC-0001
title: Verificação — Esqueleto do projeto
status: done
created_at: 2026-11-19
updated_at: 2026-11-19
---

# Verificação — SPEC-0001

Ambiente principal: Windows 11, uv 0.13.9, Python 3.13.18, `.venv` recriado do zero (`rm -rf .venv && uv sync`). Todos os comandos rodados como `uv run python -m ...`. AC-010 verificado também no Linux Mint 22.3 (V-008).

## Resumo

| AC | REQ | Último resultado | Verificação |
|---|---|---|---|
| AC-001 | REQ-001 | PASS | V-001 |
| AC-002 | REQ-002 | PASS | V-002 |
| AC-003 | REQ-003 | PASS | V-003 |
| AC-004 | REQ-004 | PASS | V-004 |
| AC-005 | REQ-005 | PASS | V-005 |
| AC-006 | REQ-006 | PASS | V-005 |
| AC-007 | REQ-007 | PASS | V-006 |
| AC-008 | REQ-007 | PASS | V-006 |
| AC-009 | REQ-008 | PASS | V-007 |
| AC-010 | REQ-009 | PASS | V-008 |
| AC-011 | REQ-010 | PASS | V-009 |
| AC-012 | REQ-011 | PASS | V-010 |
| AC-013 | REQ-012 | PASS | V-011 |

## Registros

### V-001 — Instalação e ajuda da CLI

- Covers: AC-001 (REQ-001)
- Method: `rm -rf .venv && uv sync`; `uv run python -m assistance_agent --help`
- Result: PASS
- Date: 2026-11-19
- Evidence: `uv sync` → 0; `--help` → 0, lista o subcomando `chat`. `uv.lock` versionável na raiz.
- Limitations: o script instalado `assistance-agent.exe` é bloqueado no Windows pelo Defender (ASR da TI). Por isso o AC usa `python -m` (Change Log da spec). O script deve funcionar no Linux Mint, a confirmar na T010.

### V-002 — Regra de dependência entre camadas

- Covers: AC-002 (REQ-002)
- Method: `tests/test_architecture.py` (análise de imports com `ast`, incluindo relativos), mais testes que plantam imports proibidos
- Result: PASS
- Date: 2026-11-19
- Evidence: todos os arquivos de `core/` e `ports/` sem imports de `adapters`/`interfaces`; os 4 imports plantados são detectados.
- Limitations: detecta só imports estáticos (não `importlib` dinâmico).

### V-003 — Validação do TenantId

- Covers: AC-003 (REQ-003)
- Method: `tests/test_tenant.py`
- Result: PASS
- Date: 2026-11-19
- Evidence: rejeita vazio, maiúscula, espaço, `_`, `-` inicial, 65 caracteres, `!` e não-texto; aceita 1 e 64 caracteres; não existe padrão (`TenantId()` → `TypeError`).

### V-004 — Isolamento do histórico por tenant

- Covers: AC-004 (REQ-004)
- Method: `tests/test_fake_adapters.py::test_history_is_isolated_per_tenant`, `tests/test_conversation_service.py::test_two_tenants_same_conversation_are_isolated`
- Result: PASS
- Date: 2026-11-19
- Evidence: os tenants `a` e `b` na mesma conversa `c1` só veem as próprias mensagens; o tenant `c` vê histórico vazio; `load` devolve uma cópia.
- Limitations: isolamento só em memória; persistência real fica para uma spec futura (nível critical).

### V-005 — Adapters fake de LLM e embeddings

- Covers: AC-005 (REQ-005), AC-006 (REQ-006)
- Method: `tests/test_fake_adapters.py`
- Result: PASS
- Date: 2026-11-19
- Evidence: o LLM fake devolve respostas iguais para o mesmo histórico. Os embeddings fake: `x == x` e `x != y`; dimensão 8; norma 1; modelo `fake-embeddings-v1`; query ≠ document. Nenhuma chamada de rede (fixture de V-010 ativa).

### V-006 — CLI `chat`

- Covers: AC-007, AC-008 (REQ-007)
- Method: `tests/test_cli.py` (inclui um subprocess real de `python -m assistance_agent`), mais execução manual
- Result: PASS
- Date: 2026-11-19
- Evidence:
  - `chat --tenant demo --message "oi"` → `[fake] você disse: oi`, código 0.
  - Interativo `oi` / frase / `/sair` → 2 respostas, código 0; EOF encerra sem traceback.
  - `--tenant "Inválido!"`, `--tenant` ausente e conversa inválida → stderr e código 2.
  - Mensagem vazia → código 2.
- Limitations: no Git Bash, com a saída redirecionada, os acentos aparecem em cp1252; no PowerShell (console UTF-8) aparecem certos.

### V-007 — Seleção do provedor de LLM

- Covers: AC-009 (REQ-008)
- Method: `tests/test_conversation_service.py`, `tests/test_cli.py::test_unknown_provider_lists_accepted_values`, mais execução manual com `ASSISTANCE_AGENT_LLM_PROVIDER=inexistente`
- Result: PASS
- Date: 2026-11-19
- Evidence: sem a variável (ou vazia) → `fake`. Valor desconhecido → "Valores aceitos: fake", código 1. `.env.example` lista só o nome da variável.

### V-008 — Portabilidade Windows / Linux Mint

- Covers: AC-010 (REQ-009)
- Method: `uv sync`, `uv run python -m pytest` e o comando do AC-007 em cada máquina
- Result: PASS
- Date: 2026-11-19
- Evidence:
  - **Windows 11: PASS** (V-001, V-006, V-009).
  - **Linux Mint 22.3: PASS** — uv 0.11.7, CPython 3.13.13, `rm -rf .venv && uv sync` → 0. `uv run python -m pytest` → 59 passed, 0. `ruff check` → 0; `ruff format --check` → 24 arquivos, 0; `mypy` strict → 0 issues em 17 arquivos. `pre_commit run --all-files` → os três hooks Passed.
  - CLI no Linux: `uv run python -m assistance_agent chat --tenant demo --message "oi"` → `[fake] você disse: oi`, 0. O script instalado também funciona: `uv run assistance-agent --help` → 0; modo interativo `olá` + `/sair` → 0; tenant inválido → 2; provedor desconhecido → 1. Acentos corretos no terminal.
  - `git check-attr eol` → `lf` para `*.py` e `uv.lock`; `.env` e `.venv` ignorados.
- Limitations: no Linux, a execução foi na worktree do commit `15bf92e` (mesmo conteúdo do repositório), não num `git clone` novo do GitHub; o `.venv` foi recriado do zero.

### V-009 — Portões de qualidade e pre-commit

- Covers: AC-011 (REQ-010)
- Method: `uv run python -m pytest` / `ruff check` / `ruff format --check` / `mypy`; `uv run python -m pre_commit run --files <todos os .py e pyproject.toml>`
- Result: PASS
- Date: 2026-11-19
- Evidence: 59 passed; ruff 0; 24 arquivos formatados; mypy strict 0 issues em 17 arquivos; os hooks ruff check, ruff format e mypy → Passed. Hook instalado em `.git/hooks/pre-commit`.
- Limitations: `pre_commit run --all-files` só considera arquivos rastreados pelo git, e nenhum `.py` está commitado ainda; por isso foi usado `--files` com a lista explícita, que equivale a todos os arquivos do projeto.

### V-010 — Sem rede e sem credenciais

- Covers: AC-012 (REQ-011)
- Method: fixture autouse em `tests/conftest.py` (bloqueia `connect`/`connect_ex` fora do loopback e o DNS); `tests/test_network_guard.py`; suíte rodada com as variáveis de nome parecido com credencial removidas do ambiente (`env -u`)
- Result: PASS
- Date: 2026-11-19
- Evidence: conexões externas por nome e por IP levantam `NetworkAccessError`; o loop asyncio funciona; 59 passed sem nenhuma variável `*api_key*|*token*|*secret*`.

### V-011 — Arquivos ignorados e fim de linha

- Covers: AC-013 (REQ-012)
- Method: `git check-ignore .env .venv`; `git check-attr eol -- src/assistance_agent/__init__.py uv.lock`
- Result: PASS
- Date: 2026-11-19
- Evidence: `.env` e `.venv` ignorados; `.env.example` não é ignorado; `eol: lf` para `*.py` e `uv.lock`.

## Limitações e riscos remanescentes

- Isolamento por tenant só lógico/em memória; autenticação e persistência ficam para specs futuras de nível critical.
- No Windows de desenvolvimento, use sempre `python -m` (ASR do Defender).
