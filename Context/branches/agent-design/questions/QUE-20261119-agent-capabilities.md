---
id: CTX-QUE-20261119-agent-capabilities
type: question
title: Quais capacidades, ferramentas e modelo de memória o agente terá?
branch: agent-design
tags: [agent-behavior, tools, memory]
status: open
priority: high
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-QUE-20261119-llm-provider]
depends_on: [CTX-QUE-20261119-project-scope-and-users]
resolved_by: null
---

# Quais capacidades, ferramentas e modelo de memória o agente terá?

## Pergunta

Que ações o agente pode executar (ferramentas), como mantém estado/memória entre interações e quais limites de autonomia ele tem?

## Por que importa

Define a arquitetura do agente (loop de ferramentas, armazenamento de memória, guardrails) e quais integrações são necessárias.

## O que depende da resposta

- Integrações necessárias (`CTX-QUE-20261119-llm-provider` e APIs externas).
- Necessidade de persistência (banco, arquivos) em `infrastructure`.

## Opções conhecidas

- Memória: sem memória, histórico da conversa, memória persistente (arquivo/banco/vetorial).
- Autonomia: responde apenas; executa ações com confirmação; executa ações autônomas.

## Como resolver

Responder primeiro `CTX-QUE-20261119-project-scope-and-users`; depois listar casos de uso e derivar as ferramentas.
