---
id: SPEC-0001-TASKS
type: tasks
spec: SPEC-0001
title: Tarefas — Esqueleto do projeto
status: ready
created_at: 2026-11-19
updated_at: 2026-11-19
---

# Tarefas — SPEC-0001

- [x] SPEC-0001-T001 — Instalar o uv no Windows 11 (e no Linux Mint) — ação do usuário
  Status: completed
  Requirements: REQ-001, REQ-009
  Depends on: none
  Done when: `uv --version` funciona no terminal usado pelo agente
  Evidence: 2026-11-19 — instalado via winget; `%LOCALAPPDATA%/Microsoft/WinGet/Links/uv.exe --version` → `uv 0.13.9`. O PATH do shell do agente aberto antes da instalação não o enxerga: use o caminho completo ou um terminal novo. Linux Mint: coberto pela T010.

- [x] SPEC-0001-T002 — Inicializar o projeto uv (pyproject, Python 3.13, script `assistance-agent`, lock), `.gitignore`, `.gitattributes` com `*.py` em LF e `.env.example`
  Status: completed
  Requirements: REQ-001, REQ-008, REQ-012
  Depends on: SPEC-0001-T001
  Done when: `uv sync` termina com 0; `git check-ignore .env .venv` e `git check-attr eol` dão o esperado (AC-013)
  Evidence: 2026-11-19 — `uv init --package` + `pyproject.toml` (Python >=3.13, só o nome do autor, sem e-mail); `uv sync` → código 0, Python 3.13.18 (a primeira tentativa falhou ao criar o link de versão menor do uv; a segunda passou sem mudanças). `uv.lock` gerado. `git check-ignore .env .venv` → os dois ignorados; `.env.example` não é ignorado; `git check-attr eol -- src/assistance_agent/__init__.py` → `eol: lf`. Descoberta: o Defender (regra ASR gerenciada pela TI) bloqueia `.venv/Scripts/assistance-agent.exe` ("Acesso negado"); a spec passou a usar `uv run python -m ...` (Change Log).

- [x] SPEC-0001-T003 — Configurar ruff, mypy (strict), pytest + pytest-asyncio e o pre-commit com hooks locais
  Status: completed
  Requirements: REQ-010
  Depends on: SPEC-0001-T002
  Done when: os quatro comandos de qualidade rodam (com o pacote vazio) e `uv run python -m pre_commit run --all-files` passa
  Evidence: 2026-11-19 — `[tool.ruff]` (py313, E/F/W/I/UP/B/SIM/RUF), `[tool.mypy]` (strict, `src`), `[tool.pytest.ini_options]` (asyncio auto, escopo `function`); `.pre-commit-config.yaml` com hooks `repo: local` via `uv run python -m`. `ruff check` 0, `ruff format --check` 0, `mypy` 0; `pytest` 5 (nenhum teste ainda, esperado). `pre_commit install` OK; `pre_commit run --all-files` → 0, mas "no files to check" porque nada está rastreado no git ainda — a execução real dos hooks fica para a T009 (`--files`).

- [x] SPEC-0001-T004 — Criar as camadas e o teste de arquitetura (imports proibidos em core/ports), mais a fixture de bloqueio de rede
  Status: completed
  Requirements: REQ-002, REQ-011
  Depends on: SPEC-0001-T003
  Done when: `tests/test_architecture.py` passa e falha ao plantar um import proibido; a fixture de rede está ativa em todos os testes
  Evidence: 2026-11-19 — Camadas `core/ports/adapters/interfaces` criadas. `tests/test_architecture.py` analisa os imports de `core/` e `ports/` com `ast` (inclusive imports relativos) e tem testes que plantam imports proibidos e confirmam que são detectados. `tests/conftest.py` tem uma fixture autouse que bloqueia `connect`/`connect_ex` fora do loopback e o DNS (`getaddrinfo`); `tests/test_network_guard.py` comprova o bloqueio e que o loop asyncio continua funcionando. `uv run python -m pytest` → 11 passed; ruff e mypy → 0. Ajuste: `[tool.ruff] include = ["*.py","*.pyi"]`, porque o ruff 0.17 também formataria blocos de código em Markdown de Context/ e Specs/ (nenhum .md foi alterado).

- [x] SPEC-0001-T005 — Domínio: `TenantId`, `Message`, `ConversationId` e portas (LLM, embeddings, histórico)
  Status: completed
  Requirements: REQ-003, REQ-005, REQ-006, REQ-004
  Depends on: SPEC-0001-T004
  Done when: os testes do AC-003 passam; mypy strict sem erros
  Evidence: 2026-11-19 — `core/tenant.py` (`TenantId`, `InvalidTenantError`, `validate_identifier`), `core/messages.py` (`Message`, `Role`, `ConversationId`, `DEFAULT_CONVERSATION`), `ports/llm.py`, `ports/embeddings.py` (`EmbeddingResult` com `model`), `ports/history.py`. Desvio do plano: `Message`/`ConversationId` ficaram em `core/messages.py`, para evitar um import circular core↔ports (o plano foi ajustado). `tests/test_tenant.py`: inválidos (vazio, maiúscula, espaço, `_`, `-` inicial, 65 caracteres, não-str) rejeitados; válidos (1 e 64 caracteres) aceitos; não há default. `pytest` → 35 passed; ruff, format e mypy strict → 0.

- [x] SPEC-0001-T006 — Adapters fake (LLM, embeddings) e histórico em memória
  Status: completed
  Requirements: REQ-004, REQ-005, REQ-006
  Depends on: SPEC-0001-T005
  Done when: os testes do AC-004, AC-005 e AC-006 passam
  Evidence: 2026-11-19 — `adapters/fake_llm.py` (ecoa a última mensagem do usuário), `adapters/fake_embeddings.py` (SHA-256 → vetor normalizado de dimensão 8, modelo `fake-embeddings-v1`, query ≠ document), `adapters/memory_history.py` (chave `(TenantId, ConversationId)`; `load` devolve cópia). `tests/test_fake_adapters.py`: determinismo do LLM (AC-005), embeddings iguais/diferentes/normalizados com modelo informado (AC-006), isolamento a/b/c na mesma conversa `c1` (AC-004). `pytest` → 41 passed; ruff, format e mypy → 0.

- [x] SPEC-0001-T007 — `ConversationService` e composition root (`config.py`) com `ASSISTANCE_AGENT_LLM_PROVIDER`
  Status: completed
  Requirements: REQ-004, REQ-005, REQ-008
  Depends on: SPEC-0001-T006
  Done when: o teste do serviço com dois tenants passa; o provedor desconhecido gera erro que lista `fake` (AC-009, nível unitário)
  Evidence: 2026-11-19 — `core/conversation.py` (`ConversationService.send/history`; rejeita mensagem vazia sem chamar o LLM) e `config.py` (`Settings.from_env`, `ASSISTANCE_AGENT_LLM_PROVIDER` com padrão `fake`, `ConfigError` listando os valores aceitos; `build_container` tipado pelas portas, então o mypy confere a conformidade dos adapters). `tests/test_conversation_service.py`: dois tenants na mesma conversa isolados; provedor desconhecido → erro citando `fake`; padrão `fake`. `pytest` → 48 passed; ruff, format e mypy → 0.

- [x] SPEC-0001-T008 — CLI `assistance-agent chat` (`--tenant`, `--conversation`, `--message`, modo interativo, `/sair`, EOF, códigos de saída)
  Status: completed
  Requirements: REQ-007, REQ-008
  Depends on: SPEC-0001-T007
  Done when: os testes do AC-007, AC-008 e AC-009 passam; `uv run python -m assistance_agent chat --tenant demo --message "oi"` imprime a resposta fake
  Evidence: 2026-11-19 — `interfaces/cli.py` (argparse; `chat --tenant [--conversation] [--message]`; modo interativo com `/sair` e EOF; códigos 0 (ok), 2 (argumento inválido/mensagem vazia), 1 (configuração), 130 (Ctrl+C)); `__main__.py`; script `assistance-agent = assistance_agent.interfaces.cli:main`. `tests/test_cli.py` (12 casos, incluindo um subprocess real de `python -m assistance_agent`). `pytest` → 59 passed; ruff, format e mypy → 0. Execução manual: `--help` 0 e lista `chat`; `--message "oi"` → `[fake] você disse: oi`, 0; interativo com `oi`, outra frase e `/sair` → 2 respostas, 0; tenant `Inválido!` → stderr, 2; `ASSISTANCE_AGENT_LLM_PROVIDER=inexistente` → "Valores aceitos: fake", 1. Limitação: com a saída redirecionada no Git Bash os acentos saem em cp1252; no PowerShell (console UTF-8) saem certos.

- [x] SPEC-0001-T009 — Atualizar `AGENTS.md` (comandos de qualidade) e rodar a verificação completa no Windows
  Status: completed
  Requirements: REQ-009, REQ-010
  Depends on: SPEC-0001-T008
  Done when: `verification.md` registra AC-001..AC-013 no Windows; o AC-010 (Linux Mint) fica NOT_RUN até o usuário executar
  Evidence: 2026-11-19 — `AGENTS.md` (Convenções de desenvolvimento): `uv run python -m <módulo>` obrigatório (ASR do Defender), os quatro portões de qualidade, como rodar a CLI, a regra de camadas e testes sem rede. Verificação completa no Windows com `.venv` recriado: `verification.md` V-001..V-011 — AC-001..AC-009 e AC-011..AC-013 PASS; AC-010 NOT_RUN (falta o Linux Mint, T010).

- [ ] SPEC-0001-T010 — Verificar no Linux Mint — ação do usuário (passos em `Specs/STATE.md`: clonar, instalar uv, `uv sync`, testes, CLI)
  Status: ready
  Requirements: REQ-009
  Depends on: SPEC-0001-T009
  Done when: o usuário relata `uv sync`, `uv run python -m pytest` e o comando do AC-007 com código 0 no Linux Mint
  Evidence: —
