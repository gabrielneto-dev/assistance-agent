---
id: CTX-DEC-20261119-agent-autonomy-and-memory
type: decision
title: Agente pede confirmação para ações externas e tem memória de conversa, persistente e RAG
branch: agent-design
tags: [agent-behavior, memory, tools]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-QUE-20261119-agent-capabilities, CTX-DEC-20261119-multi-tenant-saas-product]
depends_on: [CTX-DEC-20261119-multi-tenant-saas-product]
supersedes: null
superseded_by: null
revisit_at: null
---

# Autonomia e memória do agente

## Decisão

**Autonomia:** o agente responde livremente, mas **toda ação com efeito externo** (enviar mensagem, chamar sistema de terceiros, alterar dados) exige confirmação do usuário antes de ser executada.

**Memória (três camadas):**

1. Histórico da conversa — contexto da sessão atual.
2. Memória persistente — fatos e preferências do usuário entre conversas.
3. Base de conhecimento (RAG) — busca em documentos do cliente, para atendimento/suporte.

Todas as camadas com escopo de tenant (`CTX-DEC-20261119-multi-tenant-saas-product`).

## Motivo

Escolha do usuário (`CTX-SRC-20261119-user-definition-answers`).

## Consequências

- O loop de ferramentas precisa distinguir ferramentas de leitura (livres) de ferramentas com efeito (confirmação), e o fluxo de confirmação precisa funcionar em todos os canais (API, CLI, WhatsApp).
- Exige persistência (banco) e um mecanismo de busca para RAG; ambos ainda indefinidos (`CTX-QUE-20261119-tech-stack`).

## Em aberto

- Lista concreta de ferramentas e como a confirmação é representada em cada canal → `CTX-QUE-20261119-agent-capabilities`.
