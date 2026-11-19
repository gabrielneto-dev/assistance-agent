---
id: CTX-CP-20261119-1641-product-idea-and-skeleton
type: checkpoint
title: Definições do produto, pesquisa de LLM, ideia (assistências técnicas) e esqueleto implementado
branch: global
tags: [scope, stack, tooling, context-engineering]
status: active
created_at: 2026-11-19
updated_at: 2026-11-19
related:
  - CTX-CP-20261119-1149-sdd-install-and-tooling
  - CTX-DEC-20261119-repair-shop-ai-attendant
  - CTX-DEC-20261119-multi-tenant-saas-product
  - CTX-DEC-20261119-layered-package-and-quality-tooling
  - CTX-RES-20261119-llm-provider-comparison
  - CTX-FCT-20261119-windows-asr-blocks-venv-exes
---

# Session Checkpoint — Do produto definido ao esqueleto implementado

## Objetivo

Responder as perguntas fundamentais, pesquisar provedores de LLM, definir a ideia concreta do produto e construir o esqueleto do código pela primeira spec.

## O que mudou

- Perguntas fundamentais respondidas pelo usuário. Viraram decisões de produto, agente, stack e runtime, e a fonte `CTX-SRC-20261119-user-definition-answers`.
- Pesquisa de preços de LLM e embeddings, só com fontes oficiais.
- Ideia do produto definida: atendente de IA para assistências técnicas de eletrônicos.
- `SPEC-0001` (esqueleto, nível full) especificada, planejada e implementada. Código em `src/assistance_agent/` e `tests/`; `pyproject.toml`, `uv.lock` e pre-commit configurados.
- `AGENTS.md` ganhou a seção "Convenções de desenvolvimento" (uv, `python -m`, portões de qualidade, camadas, testes sem rede).
- `validate.sh`: corrigido um falso positivo de segredo (`RSK-` continha `sk-`).
- **Nada desta sessão foi commitado** (último commit: `b4bf2d6`).

## Decisões

- `CTX-DEC-20261119-multi-tenant-saas-product` — SaaS multi-tenant; API, CLI e WhatsApp.
- `CTX-DEC-20261119-repair-shop-ai-attendant` — assistências técnicas; atendimento humanizado no WhatsApp; IA primeiro, gestão depois; valores finais sempre com humano.
- `CTX-DEC-20261119-agent-autonomy-and-memory` — confirmação para ações externas; memória de conversa, persistente e RAG.
- `CTX-DEC-20261119-python-uv-stack`, `CTX-DEC-20261119-local-cross-platform-runtime`, `CTX-DEC-20261119-layered-package-and-quality-tooling`.

## Descobertas

- Os preços de LLM se equivalem entre Anthropic, OpenAI e Google em cada faixa; a qualidade é que vai decidir (`CTX-RES-20261119-llm-provider-comparison`).
- O Defender da TI bloqueia os `.exe` do `.venv` no Windows (`CTX-FCT-20261119-windows-asr-blocks-venv-exes`).
- Armadilhas do ferramental: ruff formatando Markdown, pre-commit, acentos no Git Bash (`CTX-NTE-20261119-python-tooling-pitfalls`).

## Problemas resolvidos

- Lançadores bloqueados → tudo via `uv run python -m`.
- ruff alcançando Context/Specs → `include = ["*.py", "*.pyi"]`.
- Import circular core↔ports → `Message`/`ConversationId` movidos para `core/messages.py`.
- Falso positivo de segredo no validador.

## Abordagens que falharam (vale lembrar)

- Rodar `uv run assistance-agent` / `uv run pytest` no Windows (bloqueado pela ASR).
- Agregadores de preço de LLM: divergentes entre si; usar só as páginas oficiais.

## Estado atual

Produto definido em linhas gerais; esqueleto funcional com LLM e embeddings fake. Faltam: provedor de LLM, integração com WhatsApp, loja piloto. Ver `Context/STATE.md`.

## Estado SDD

`SPEC-0001` — `in_progress`, fase `verify`. Tarefas T001–T009 concluídas. Próxima: `SPEC-0001-T010` (usuário verifica no Linux Mint). Verificação: 12 AC PASS, AC-010 NOT_RUN (`Specs/features/SPEC-0001--project-skeleton/verification.md`). Fonte: `Specs/STATE.md`. Reconciliado em 2026-11-19 16:41: 59 testes passando.

## Perguntas abertas

- `CTX-QUE-20261119-llm-provider` (crítica)
- `CTX-QUE-20261119-whatsapp-integration-method`
- `CTX-QUE-20261119-pilot-shop`
- `CTX-QUE-20261119-tech-stack` (framework da API, banco, vetores)
- `CTX-QUE-20261119-agent-capabilities` (contratos das ferramentas, confirmação e transferência no WhatsApp)

## Próximos passos

1. Usuário: verificar a SPEC-0001 no Linux Mint (T010) e fechar a spec.
2. Commitar o esqueleto e os registros desta sessão (sob pedido do usuário).
3. Responder a pergunta da loja piloto; montar uma avaliação pequena para escolher o provedor de LLM.
4. Pesquisar a integração com WhatsApp; depois a spec do atendimento (nível critical).

## Arquivos ou artefatos afetados

`AGENTS.md`, `.gitattributes`, `.gitignore`, `.env.example`, `.pre-commit-config.yaml`, `.python-version`, `pyproject.toml`, `uv.lock`, `src/**`, `tests/**`, `Context/**`, `Specs/**`.

## Registros de contexto criados/atualizados

- Criados:
  - `CTX-SRC-20261119-user-definition-answers`
  - `CTX-DEC-20261119-multi-tenant-saas-product`
  - `CTX-DEC-20261119-agent-autonomy-and-memory`
  - `CTX-DEC-20261119-python-uv-stack`
  - `CTX-DEC-20261119-local-cross-platform-runtime`
  - `CTX-DEC-20261119-layered-package-and-quality-tooling`
  - `CTX-DEC-20261119-repair-shop-ai-attendant`
  - `CTX-QUE-20261119-whatsapp-integration-method`
  - `CTX-QUE-20261119-pilot-shop`
  - `CTX-RES-20261119-llm-provider-comparison`
  - `CTX-RSK-20261119-ai-wrong-quote-or-status`
  - `CTX-FCT-20261119-windows-asr-blocks-venv-exes`
  - `CTX-NTE-20261119-python-tooling-pitfalls`
- Atualizados:
  - perguntas de escopo, deployment e stack (respondidas ou parciais);
  - perguntas de capacidades e LLM;
  - `CTX-ASM-20261119-single-developer-project`, `CTX-FCT-20261119-repository-initialized`, `CTX-NTE-20261119-validate-script-pitfalls`.
