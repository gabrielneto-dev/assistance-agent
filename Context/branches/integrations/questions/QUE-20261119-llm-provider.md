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
related: [CTX-QUE-20261119-tech-stack, CTX-QUE-20261119-agent-capabilities, CTX-DEC-20261119-python-uv-stack, CTX-RES-20261119-llm-provider-comparison]
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

## Situação (2026-11-19)

O usuário ainda não decidiu. Critérios já conhecidos: SDK Python (`CTX-DEC-20261119-python-uv-stack`), suporte a tool use, custo por tenant em SaaS, embeddings para RAG (`CTX-DEC-20261119-agent-autonomy-and-memory`). Próximo passo: pesquisa comparativa datada (`research`) antes da decisão; até lá, isolar a chamada ao LLM atrás de uma interface no código.

## Pesquisa (2026-11-19)

`CTX-RES-20261119-llm-provider-comparison`: os preços de lista de Anthropic, OpenAI e Google se equivalem em cada faixa, então preço não decide. A Anthropic não tem embeddings próprios (indica a Voyage AI). Próximo passo para decidir: uma avaliação pequena com as mesmas tarefas em 2–3 candidatos de faixa intermediária, com o código já atrás de interfaces de LLM e de embeddings.
