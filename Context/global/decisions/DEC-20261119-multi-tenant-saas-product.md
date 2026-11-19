---
id: CTX-DEC-20261119-multi-tenant-saas-product
type: decision
title: assistance-agent é um SaaS multi-tenant de assistente de IA, acessado por API, CLI e WhatsApp
branch: global
tags: [scope, users, goals]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-QUE-20261119-project-scope-and-users, CTX-DEC-20261119-agent-autonomy-and-memory, CTX-QUE-20261119-whatsapp-integration-method, CTX-DEC-20261119-repair-shop-ai-attendant]
depends_on: []
supersedes: null
superseded_by: null
revisit_at: null
---

# assistance-agent é um SaaS multi-tenant de assistente de IA

## Contexto

Até 2026-11-19 só se sabia que o projeto era "um assistente/agente de IA em código" (`CTX-QUE-20261119-project-scope-and-users`).

## Decisão

- **Modelo de produto:** SaaS para terceiros.
- **Multi-tenant desde o início:** dados, memória, base de conhecimento e configurações isolados por cliente (tenant) desde o primeiro código.
- **Finalidades (casos de uso):**
  - produtividade pessoal;
  - atendimento/suporte (respostas sobre a base de conhecimento do cliente);
  - automação de processos.
- **Interfaces iniciais ("por agora"):** API, CLI e bot de mensageria — **WhatsApp** primeiro. Chat web não está no escopo inicial.

## Motivo

Escolha do usuário (`CTX-SRC-20261119-user-definition-answers`).

## Consequências

- Todo modelo de dados, memória e índice de RAG precisa de escopo de tenant; vazamento entre tenants é o principal risco de design.
- As interfaces devem ser adaptadores finos sobre um núcleo comum do agente (API, CLI e WhatsApp chamam o mesmo serviço).
- Autenticação/identificação de tenant e de usuário será necessária na API e no canal WhatsApp (mecanismo ainda não definido).
- Três finalidades amplas. **Refinado em 2026-11-19:** o produto é vertical, para assistências técnicas de eletrônicos, com o atendimento no WhatsApp como primeiro caso de uso → `CTX-DEC-20261119-repair-shop-ai-attendant`.

## Riscos

- Escopo amplo para um único desenvolvedor (`CTX-ASM-20261119-single-developer-project`); mitigar com specs pequenas e incrementais.
