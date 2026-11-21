---
id: CTX-QUE-20261119-whatsapp-integration-method
type: question
title: Como o agente vai se conectar ao WhatsApp?
branch: integrations
tags: [integrations, external-apis]
status: open
priority: high
created_at: 2026-11-19
updated_at: 2026-11-21
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

## O que falta o usuário responder (levantado em 2026-11-21)

1. A loja piloto já usa o WhatsApp Business? O número do atendimento pode ser dedicado ao bot?
2. A loja tem CNPJ e aceita verificar uma conta empresarial na Meta?
3. API oficial da Meta ou um intermediário (BSP) que revende a mesma API?
4. Onde o sistema roda no piloto: túnel a partir da máquina local (por exemplo, Cloudflare Tunnel) ou um servidor? O webhook precisa de um endereço público, o que revê `CTX-DEC-20261119-local-cross-platform-runtime`.

## Considerações preliminares do agente (não pesquisadas)

Conhecimento geral do agente, sem fonte datada; confirmar na pesquisa antes de decidir:

- Um número conectado à API normalmente deixa de funcionar no aplicativo comum do WhatsApp.
- A API oficial exige uma conta empresarial verificada na Meta.
- Existem bibliotecas não oficiais que simulam o WhatsApp Web. Elas violam os termos de uso e arriscam o banimento do número; o agente recomenda descartá-las para um produto pago.

## Próximo passo

Pesquisa comparativa com fontes datadas (`research`, com `revisit_at`): requisitos, custos e modelo de cobrança da API oficial e de 2–3 BSPs, e como cada tenant conecta o próprio número. A pesquisa ainda não foi feita.
