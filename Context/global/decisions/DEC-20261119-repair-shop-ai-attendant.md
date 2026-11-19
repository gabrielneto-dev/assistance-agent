---
id: CTX-DEC-20261119-repair-shop-ai-attendant
type: decision
title: Produto é um atendente de IA no WhatsApp para assistências técnicas de eletrônicos, com gestão crescendo depois
branch: global
tags: [scope, users, goals]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-DEC-20261119-multi-tenant-saas-product, CTX-DEC-20261119-agent-autonomy-and-memory, CTX-QUE-20261119-agent-capabilities, CTX-RSK-20261119-ai-wrong-quote-or-status, CTX-QUE-20261119-pilot-shop]
depends_on: [CTX-DEC-20261119-multi-tenant-saas-product]
supersedes: null
superseded_by: null
revisit_at: null
---

# Atendente de IA para assistências técnicas

## Contexto

`CTX-DEC-20261119-multi-tenant-saas-product` definiu o formato do produto: SaaS multi-tenant, com API, CLI e WhatsApp. As finalidades eram amplas. Em 2026-11-19 o usuário definiu a ideia concreta. Ele trabalha numa assistência técnica e conhece a dor de perto.

## Decisão

- **Cliente (tenant):** lojas de assistência técnica de eletrônicos (celulares, tablets, notebooks etc.) que fazem orçamentos e manutenção.
- **Usuário final:** os clientes da loja, que falam com ela pelo WhatsApp.
- **Dor principal:** desorganização da loja.
- **Diferencial:** atendimento **humanizado** feito por IA no WhatsApp.
- **Estratégia:** **IA primeiro, gestão depois**.
  - Começa com o atendente e um registro mínimo de ordens de serviço (cliente, aparelho, defeito, status, orçamento).
  - A gestão completa da loja cresce depois.
- **Primeiro caso de uso:** responder os clientes da loja no WhatsApp.
- **O que a IA resolve primeiro:**
  1. Status do reparo — consulta a ordem de serviço.
  2. Pedido de orçamento — **estimativa**, a partir da tabela de preços da loja.
  3. Informações da loja — horário, endereço, garantia, pagamento, prazos (base de conhecimento).
  4. Aprovação de orçamento — o cliente aceita ou recusa o orçamento do técnico. É ação com efeito, então segue a regra de confirmação (`CTX-DEC-20261119-agent-autonomy-and-memory`).
- **A conversa passa para um humano da loja quando:**
  - o cliente pede;
  - a IA não tem certeza ou não encontra o dado;
  - há reclamação ou conflito (por exemplo, garantia contestada);
  - o assunto é **valor final** ou negociação de preço. Valores finais são sempre definidos por um humano.

## Motivo

Escolhas do usuário, a partir de experiência própria numa assistência técnica.

## Consequências

- Isso refina as "finalidades" de `CTX-DEC-20261119-multi-tenant-saas-product`: produtividade e automação passam a servir a esse nicho, não a usos genéricos.
- O modelo de dados mínimo precisa de: loja (tenant), cliente final, aparelho, ordem de serviço (status, orçamento, aprovação) e tabela de preços.
- As ferramentas iniciais do agente ficam definidas (`CTX-QUE-20261119-agent-capabilities`):
  - consultar ordem de serviço;
  - estimar orçamento;
  - buscar na base da loja;
  - registrar aprovação ou recusa, com confirmação;
  - transferir para humano.
- A transferência para humano exige uma forma de a loja assumir a conversa (canal e interface ainda indefinidos).
- O WhatsApp é central: cada loja conecta o próprio número (`CTX-QUE-20261119-whatsapp-integration-method`).
- Todo o conteúdo é em português do Brasil, com tom humanizado: isso entra nos critérios da avaliação do provedor de LLM (`CTX-QUE-20261119-llm-provider`).

## Riscos

- Status ou preço informados errado → `CTX-RSK-20261119-ai-wrong-quote-or-status`.
