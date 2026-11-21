# SDD State

Last updated: 2026-11-19

## Funcionalidade ativa

Nenhuma. A `SPEC-0001` (esqueleto do projeto, `features/SPEC-0001--project-skeleton/`) foi concluída em 2026-11-19: `status: done`, `phase: complete`.

## Fase atual

Entre funcionalidades. A próxima spec do produto (atendimento no WhatsApp) ainda não foi criada.

## Tarefa atual / próxima

Nenhuma tarefa aberta. Antes da próxima spec, o usuário precisa responder as perguntas que a bloqueiam (ver Bloqueios).

## Tarefas concluídas

- `SPEC-0001-T001`..`T010` — todas `completed`. A `T010` (Linux Mint) foi executada pelo agente no Linux Mint 22.3 em 2026-11-19.

## Bloqueios

- Próxima spec com LLM real: depende de `CTX-QUE-20261119-llm-provider`.
- Atendimento no WhatsApp: depende também de `CTX-QUE-20261119-whatsapp-integration-method` e, para dados reais, de `CTX-QUE-20261119-pilot-shop`.
- No Windows de desenvolvimento, ferramentas só via `uv run python -m` (ASR do Defender).

## Última validação conhecida

2026-11-19 — SPEC-0001: 13 AC PASS (`verification.md`). Windows 11 e Linux Mint 22.3: 59 testes, ruff, format, mypy strict e pre-commit OK. `validate.sh`: PASS.

## Arquivos relevantes

- `features/SPEC-0001--project-skeleton/{spec,plan,tasks,verification}.md`
- Código: `src/assistance_agent/` (core, ports, adapters, interfaces, config), `tests/`, `pyproject.toml`, `uv.lock`, `.pre-commit-config.yaml`.

## Próxima ação recomendada

Definir o provedor de LLM e o meio de integração com o WhatsApp; depois `iniciar spec` do atendimento (provável nível critical, por envolver dados reais de clientes). Uma spec intermediária possível, sem esses bloqueios, é a persistência do histórico por tenant.

## Contexto necessário

`Context/STATE.md` (perguntas em aberto) e os `context_refs` da SPEC-0001.
