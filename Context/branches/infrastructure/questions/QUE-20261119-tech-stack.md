---
id: CTX-QUE-20261119-tech-stack
type: question
title: Qual linguagem, framework e gerenciador de pacotes o projeto usará?
branch: infrastructure
tags: [stack, tooling]
status: open
priority: critical
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-QUE-20261119-llm-provider, CTX-QUE-20261119-deployment-target]
depends_on: [CTX-QUE-20261119-project-scope-and-users]
resolved_by: null
---

# Qual linguagem, framework e gerenciador de pacotes o projeto usará?

## Pergunta

Em qual linguagem o agente será escrito, com qual framework (se algum) e qual gerenciador de pacotes/ambiente?

## Por que importa

Nenhum código pode ser criado sem isso. Também define `.gitignore`, comandos de teste/lint e regras operacionais em `AGENTS.md`.

## O que depende da resposta

- Estrutura inicial do repositório, `.gitignore`, primeiro commit.
- Regras de trabalho (ex.: "usar X para instalar dependências") → `AGENTS.md`.

## Opções conhecidas

Nenhuma avaliada. Critérios: SDK do provedor de LLM, preferência do usuário, ambiente de execução.

## Como resolver

Decisão do usuário. Resultado → `decision` em `infrastructure/decisions/`; regras de comando → `AGENTS.md`.
