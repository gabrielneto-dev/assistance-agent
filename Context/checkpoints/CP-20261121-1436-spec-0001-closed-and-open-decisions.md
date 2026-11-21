---
id: CTX-CP-20261121-1436-spec-0001-closed-and-open-decisions
type: checkpoint
title: SPEC-0001 fechada no Linux Mint e decisões pendentes mapeadas
branch: global
tags: [tooling, runtime, llm, integrations]
status: active
created_at: 2026-11-21
updated_at: 2026-11-21
related:
  - CTX-CP-20261119-1641-product-idea-and-skeleton
  - CTX-DEC-20261119-local-cross-platform-runtime
  - CTX-QUE-20261119-llm-provider
  - CTX-QUE-20261119-whatsapp-integration-method
  - CTX-QUE-20261119-pilot-shop
---

# Session Checkpoint — SPEC-0001 fechada e decisões pendentes mapeadas

## Objetivo

Retomar o desenvolvimento, concluir a verificação da `SPEC-0001` no Linux Mint e preparar as decisões que bloqueiam a próxima spec (atendimento no WhatsApp).

## O que mudou

- A sessão rodou no próprio Linux Mint 22.3, então o agente executou a `SPEC-0001-T010`, que antes estava prevista como ação do usuário. Todos os comandos passaram.
- `SPEC-0001` fechada: `status: done`, `phase: complete`; 13 AC em PASS. Atualizados `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `Specs/INDEX.md` e `Specs/STATE.md`.
- O agente levantou, para cada decisão pendente, as perguntas que só o usuário pode responder. Elas foram gravadas nas próprias `question`s.
- **Nada desta sessão foi commitado.** O trabalho está na worktree `.claude/worktrees/continuar-desenvolvimento-d63219` (branch `claude/continuar-desenvolvimento-d63219`, base `15bf92e` = `origin/main`).

## Decisões

Nenhuma decisão nova. O usuário pediu e recebeu um resumo do que já está decidido (as sete `DEC` ativas listadas em `Context/STATE.md`).

## Descobertas

- A portabilidade está confirmada: no Linux Mint (uv 0.11.7, CPython 3.13.13), com o mesmo `uv.lock`, passam `uv sync`, os 59 testes, ruff, mypy strict, pre-commit e a CLI. No Linux o script `assistance-agent` funciona, ao contrário do Windows com a ASR → `CTX-DEC-20261119-local-cross-platform-runtime`, `CTX-FCT-20261119-windows-asr-blocks-venv-exes`.
- No clone do Linux Mint o hook do pre-commit não está instalado → `CTX-FCT-20261119-repository-initialized`. Regra adicionada ao `AGENTS.md`.
- O webhook do WhatsApp precisa de um endereço público, o que conflita com a execução só local. Ficou como pergunta em `CTX-QUE-20261119-whatsapp-integration-method`.

## Problemas resolvidos

- O AC-010 (portabilidade) estava `NOT_RUN` por falta de acesso ao Linux Mint. Resolvido executando-o na sessão.

## Abordagens que falharam (vale lembrar)

- Nenhuma relevante.

## Estado atual

Esqueleto completo e verificado nas duas máquinas. O produto está definido em linhas gerais. A próxima funcionalidade está bloqueada por três perguntas do usuário: loja piloto, provedor de LLM e integração com o WhatsApp. Ver `Context/STATE.md`.

## Estado SDD

- `SPEC-0001` — `done` / `complete`; T001–T010 `completed`; última verificação: 13 AC PASS (`Specs/features/SPEC-0001--project-skeleton/verification.md`).
- Nenhuma spec ativa; próximo ID livre: `SPEC-0002`. Fonte: `Specs/STATE.md`, `Specs/INDEX.md`.

## Perguntas abertas

- `CTX-QUE-20261119-pilot-shop` — responder primeiro: o material dela alimenta a avaliação do LLM.
- `CTX-QUE-20261119-llm-provider` (crítica) — cinco perguntas ao usuário listadas no registro.
- `CTX-QUE-20261119-whatsapp-integration-method` — quatro perguntas ao usuário; a pesquisa ainda não foi feita.
- `CTX-QUE-20261119-tech-stack` (framework da API, banco, vetores) e `CTX-QUE-20261119-agent-capabilities` (contratos das ferramentas; confirmação e transferência no WhatsApp), sem mudança.

## Próximos passos

1. Commitar o fechamento da `SPEC-0001` e este save de contexto (sob pedido do usuário); no Linux Mint, rodar antes `uv run python -m pre_commit install`.
2. Usuário responde a pergunta da loja piloto.
3. Agente pesquisa a integração com o WhatsApp (fontes datadas); usuário decide.
4. Avaliação pequena de 2–3 modelos de LLM com o material da loja; usuário decide.
5. Spec do atendimento no WhatsApp (nível critical). Alternativa sem bloqueio: spec de persistência do histórico por tenant.

## Arquivos ou artefatos afetados

`AGENTS.md`, `Specs/INDEX.md`, `Specs/STATE.md`, `Specs/features/SPEC-0001--project-skeleton/{spec,plan,tasks,verification}.md`, `Context/STATE.md`, `Context/_meta/catalog.jsonl`, `_index.md` de `infrastructure` e `integrations`, e os registros abaixo.

## Registros de contexto criados/atualizados

- Criado: este checkpoint.
- Atualizados:
  - `CTX-DEC-20261119-local-cross-platform-runtime` (seção "Validação");
  - `CTX-FCT-20261119-repository-initialized` (clone no Linux, worktree, hook ausente);
  - `CTX-FCT-20261119-windows-asr-blocks-venv-exes` (script confirmado no Linux);
  - `CTX-QUE-20261119-llm-provider`, `CTX-QUE-20261119-whatsapp-integration-method`, `CTX-QUE-20261119-pilot-shop` (perguntas ao usuário).
