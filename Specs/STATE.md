# SDD State

Last updated: 2026-11-19

## Funcionalidade ativa

`SPEC-0001` — Esqueleto do projeto (`features/SPEC-0001--project-skeleton/`). Nível full, status `in_progress`.

## Fase atual

`verify`: implementação concluída no Windows em 2026-11-19; falta só o AC-010 no Linux Mint.

## Tarefa atual / próxima

`SPEC-0001-T010` — **ação do usuário**: no Linux Mint, rodar `uv sync`, `uv run python -m pytest` e `uv run python -m assistance_agent chat --tenant demo --message "oi"`, e relatar o resultado.

## Tarefas concluídas

- `SPEC-0001-T009` — Atualizar `AGENTS.md` (comandos de qualidade) e rodar a verificação completa no Windows
- `SPEC-0001-T008` — CLI `assistance-agent chat` (`--tenant`, `--conversation`, `--message`, modo interativo, `/sair`, EOF, códigos de saída)
- `SPEC-0001-T007` — `ConversationService` e composition root (`config.py`) com `ASSISTANCE_AGENT_LLM_PROVIDER`
- `SPEC-0001-T006` — Adapters fake (LLM, embeddings) e histórico em memória
- `SPEC-0001-T005` — Domínio: `TenantId`, `Message`, `ConversationId` e portas (LLM, embeddings, histórico)
- `SPEC-0001-T004` — Criar as camadas e o teste de arquitetura (imports proibidos em core/ports), mais a fixture de bloqueio de rede
- `SPEC-0001-T003` — Configurar ruff, mypy (strict), pytest + pytest-asyncio e o pre-commit com hooks locais
- `SPEC-0001-T002` — Inicializar o projeto uv (pyproject, Python 3.13, script `assistance-agent`, lock), `.gitignore`, `.gitattributes` com `*.py` em LF e `.env.example`
- `SPEC-0001-T001` — uv 0.13.9 instalado no Windows (winget).

## Bloqueios

- Nenhum para a SPEC-0001. Observação: um shell aberto antes da instalação não acha o `uv` no PATH; use `%LOCALAPPDATA%/Microsoft/WinGet/Links/uv.exe` ou um terminal novo.
- Provedor de LLM indefinido (`CTX-QUE-20261119-llm-provider`): não bloqueia a SPEC-0001, que usa adapters fake.

## Última validação conhecida

2026-11-19 — Windows 11: `verification.md` V-001..V-011 → 12 AC PASS, AC-010 NOT_RUN (Linux Mint). 59 testes; ruff, format, mypy strict e pre-commit OK. `validate.sh`: PASS.

## Arquivos relevantes

- `features/SPEC-0001--project-skeleton/{spec,plan,tasks,verification}.md`
- Código: `src/assistance_agent/` (core, ports, adapters, interfaces, config), `tests/`, `pyproject.toml`, `uv.lock`, `.pre-commit-config.yaml`.

## Próxima ação recomendada

Após o relato do Linux Mint: registrar V-008 → AC-010 e, se PASS, fechar a SPEC-0001 (`status: done`, `phase: complete`). Em seguida, a próxima spec do produto (atendimento no WhatsApp), que depende da escolha do provedor de LLM e da integração com o WhatsApp.

## Contexto necessário

`context_refs` da SPEC-0001 (DECs de produto, stack, layout e runtime em `Context/`).
