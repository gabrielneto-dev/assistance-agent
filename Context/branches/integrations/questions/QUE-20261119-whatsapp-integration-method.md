---
id: CTX-QUE-20261119-whatsapp-integration-method
type: question
title: Como o agente vai se conectar ao WhatsApp?
branch: integrations
tags: [integrations, external-apis]
status: open
priority: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-DEC-20261119-multi-tenant-saas-product, CTX-DEC-20261119-local-cross-platform-runtime]
depends_on: []
resolved_by: null
---

# Como o agente vai se conectar ao WhatsApp?

## Pergunta

Por qual meio o bot de WhatsApp será integrado, e como cada tenant conecta seu próprio número?

## Por que importa

WhatsApp é o primeiro canal de mensageria (`CTX-DEC-20261119-multi-tenant-saas-product`). O meio de integração define custo, requisitos de cadastro e como receber mensagens (webhook público) enquanto o sistema roda localmente (`CTX-DEC-20261119-local-cross-platform-runtime`).

## Opções conhecidas (não avaliadas)

- API oficial da Meta (WhatsApp Business Cloud API).
- Provedor intermediário (BSP) que revende a API oficial.

Requisitos, preços e regras mudam: pesquisar com fontes datadas (`research`, com `revisit_at`) antes de decidir.

## Como resolver

Pesquisa comparativa + decisão do usuário → `decision` em `integrations/decisions/`.
