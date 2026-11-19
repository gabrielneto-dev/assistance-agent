---
id: CTX-QUE-20261119-llm-provider
type: question
title: Qual provedor e modelo de LLM o agente usará?
branch: integrations
tags: [llm, integrations]
status: open
priority: critical
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-QUE-20261119-tech-stack, CTX-QUE-20261119-agent-capabilities]
depends_on: [CTX-QUE-20261119-project-scope-and-users]
resolved_by: null
---

# Qual provedor e modelo de LLM o agente usará?

## Pergunta

Qual(is) provedor(es) e modelo(s) de LLM o agente usa, e via qual SDK/API?

## Por que importa

Determina SDK, custo, limites, suporte a ferramentas e, em parte, a linguagem do projeto.

## O que depende da resposta

- `CTX-QUE-20261119-tech-stack` (disponibilidade de SDK).
- Design de ferramentas e prompts em `agent-design`.
- Variáveis de ambiente de credenciais (registrar só o nome).

## Opções conhecidas

Nenhuma avaliada ainda. Ao pesquisar, registrar um `research` com fontes datadas — preços e modelos mudam (`revisit_at`).

## Como resolver

Decisão do usuário, opcionalmente após um registro de pesquisa comparativa. Resultado → `decision` em `integrations/decisions/`.
