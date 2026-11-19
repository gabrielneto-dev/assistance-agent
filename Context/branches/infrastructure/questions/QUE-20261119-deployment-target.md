---
id: CTX-QUE-20261119-deployment-target
type: question
title: Onde o agente será executado?
branch: infrastructure
tags: [deployment, runtime]
status: answered
priority: high
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-QUE-20261119-tech-stack, CTX-DEC-20261119-local-cross-platform-runtime]
depends_on: [CTX-QUE-20261119-project-scope-and-users]
resolved_by: CTX-DEC-20261119-local-cross-platform-runtime
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

## Resposta (2026-11-19)

Local por enquanto, portável entre Windows 11 e Linux Mint, com código modular → `CTX-DEC-20261119-local-cross-platform-runtime`. A hospedagem do SaaS (nuvem/VPS) fica para depois; reabrir como nova pergunta quando for necessária.
