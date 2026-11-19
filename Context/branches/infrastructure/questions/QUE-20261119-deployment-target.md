---
id: CTX-QUE-20261119-deployment-target
type: question
title: Onde o agente será executado?
branch: infrastructure
tags: [deployment, runtime]
status: open
priority: high
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-QUE-20261119-tech-stack]
depends_on: [CTX-QUE-20261119-project-scope-and-users]
resolved_by: null
---

# Onde o agente será executado?

## Pergunta

O agente roda localmente (CLI/desktop), em servidor próprio, em nuvem/serverless ou integrado a outra plataforma?

## Por que importa

Afeta stack, persistência de memória, gestão de segredos, custo e observabilidade.

## O que depende da resposta

- `CTX-QUE-20261119-tech-stack`.
- Estratégia de configuração e segredos (somente nomes de variáveis em `Context/`).

## Opções conhecidas

- Local na máquina do desenvolvedor (Windows 11).
- Servidor/VPS ou nuvem.
- Bot hospedado em plataforma de mensageria.

## Como resolver

Decorre do escopo e da interface do assistente. Resultado → `decision` em `infrastructure/decisions/`.
