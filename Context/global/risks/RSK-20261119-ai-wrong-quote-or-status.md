---
id: CTX-RSK-20261119-ai-wrong-quote-or-status
type: risk
title: IA informar preço, prazo ou status errado ao cliente da loja
branch: global
tags: [agent-behavior, goals]
status: active
confidence: medium
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: []
related: [CTX-DEC-20261119-repair-shop-ai-attendant, CTX-DEC-20261119-agent-autonomy-and-memory]
depends_on: []
---

# IA informar preço, prazo ou status errado

## Risco

O atendente afirma ao cliente final um valor, prazo ou status de reparo que não corresponde aos dados da loja: por alucinação, dado desatualizado ou ordem de serviço errada (por exemplo, de outro cliente ou de outra loja).

## Impacto

Perda de confiança, conflito no balcão, prejuízo financeiro se o cliente cobrar o valor dito pela IA. Vazamento de dados se a ordem consultada for de outro cliente ou tenant.

## Probabilidade

Média sem mitigação. É o comportamento típico de LLMs sem dados fundamentados.

## Mitigações (a detalhar nas specs)

- Valores finais e negociação são sempre feitos por um humano (`CTX-DEC-20261119-repair-shop-ai-attendant`). A IA só dá estimativa e diz isso explicitamente.
- Status e preços vêm só de ferramentas que consultam os dados. A IA não responde de memória e, se não encontrar o dado, transfere para um humano.
- A ordem de serviço só é consultada se pertencer ao número de WhatsApp que pergunta e ao tenant correto.
- A avaliação do provedor de LLM deve incluir casos de "dado ausente" e "pergunta fora do escopo".

## Gatilho para revisar

Primeira spec que implementar consulta de status ou estimativa de orçamento (nível **critical**: dados reais de clientes).
