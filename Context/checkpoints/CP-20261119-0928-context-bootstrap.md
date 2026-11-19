---
id: CTX-CP-20261119-0928-context-bootstrap
type: checkpoint
title: Bootstrap do sistema de contexto em projeto vazio
branch: global
tags: [context-engineering, project-setup]
status: active
created_at: 2026-11-19
updated_at: 2026-11-19
related:
  - CTX-FCT-20261119-repository-initialized
  - CTX-SRC-20261119-user-bootstrap-answers
  - CTX-QUE-20261119-project-scope-and-users
---

# Session Checkpoint — Bootstrap do sistema de contexto

## Objetivo

Instalar a arquitetura persistente de contexto (AGENTS.md, CLAUDE.md, `Context/`) para que futuras sessões continuem o projeto sem depender da conversa.

## O que mudou

- `git init` na raiz (sem commit).
- Criados `AGENTS.md` (bloco único `CONTEXT-ENGINEERING`) e `CLAUDE.md` (`@AGENTS.md` + bloco `CLAUDE-SPECIFIC` vazio).
- Criada a estrutura `Context/` completa, com branches `agent-design`, `integrations`, `infrastructure`.

## Decisões

- Conteúdo de `Context/` em português; arquivos, IDs, chaves YAML e tags em inglês (preferência do usuário, `CTX-SRC-20261119-user-bootstrap-answers`).
- Apenas três branches iniciais, coerentes com um projeto de agente de IA em código; outras só quando surgir conhecimento real.

## Descobertas

- A pasta estava vazia: não havia documentação nem instruções de agentes a preservar ou migrar.

## Problemas resolvidos

- Nenhum.

## Abordagens que falharam (vale lembrar)

- Nenhuma.

## Estado atual

Sistema de contexto pronto; projeto sem definições de produto ou técnicas. Ver `Context/STATE.md`.

## Perguntas abertas

- `CTX-QUE-20261119-project-scope-and-users` (crítica)
- `CTX-QUE-20261119-tech-stack` (crítica)
- `CTX-QUE-20261119-llm-provider` (crítica)
- `CTX-QUE-20261119-agent-capabilities`
- `CTX-QUE-20261119-deployment-target`

## Próximos passos

1. Definir escopo e usuários.
2. Decidir stack e provedor de LLM.
3. Criar estrutura de código, `.gitignore` e primeiro commit.

## Arquivos ou artefatos afetados

`.git/`, `AGENTS.md`, `CLAUDE.md`, `Context/**`.

## Registros de contexto criados/atualizados

- `CTX-QUE-20261119-project-scope-and-users`
- `CTX-ASM-20261119-single-developer-project`
- `CTX-QUE-20261119-agent-capabilities`
- `CTX-QUE-20261119-llm-provider`
- `CTX-QUE-20261119-tech-stack`
- `CTX-QUE-20261119-deployment-target`
- `CTX-FCT-20261119-repository-initialized`
- `CTX-SRC-20261119-user-bootstrap-answers`
