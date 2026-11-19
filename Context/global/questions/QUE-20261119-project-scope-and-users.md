---
id: CTX-QUE-20261119-project-scope-and-users
type: question
title: Qual problema o assistente resolve e para quem?
branch: global
tags: [scope, users, goals]
status: answered
priority: critical
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-bootstrap-answers, CTX-SRC-20261119-user-definition-answers]
related: [CTX-ASM-20261119-single-developer-project, CTX-DEC-20261119-multi-tenant-saas-product]
depends_on: []
resolved_by: CTX-DEC-20261119-multi-tenant-saas-product
---

# Qual problema o assistente resolve e para quem?

## Pergunta

Qual é a finalidade concreta do `assistance-agent` (que tarefas ele executa) e quem são seus usuários?

## Por que importa

Sabe-se apenas que é "um assistente/agente de IA em código". Sem escopo, não há como definir objetivos, critérios de sucesso, capacidades nem stack.

## O que depende da resposta

- `core/goals.md` (objetivos, não objetivos, critérios de sucesso)
- `CTX-QUE-20261119-agent-capabilities`
- `CTX-QUE-20261119-tech-stack`, `CTX-QUE-20261119-deployment-target`
- `CTX-ASM-20261119-single-developer-project`

## Opções conhecidas

- Assistente pessoal (uso próprio) vs. produto para terceiros.
- Interface: CLI, chat web, bot de mensageria, API, outra.

## Como resolver

Perguntar ao usuário. Registrar a resposta aqui, atualizar `core/overview.md` e `core/goals.md`.

## Resposta (2026-11-19)

SaaS multi-tenant para terceiros. Finalidades: produtividade pessoal, atendimento/suporte e automação de processos. Interfaces iniciais: API, CLI e WhatsApp. Detalhes e consequências → `CTX-DEC-20261119-multi-tenant-saas-product`.
