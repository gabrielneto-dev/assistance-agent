---
id: CTX-RES-20261119-llm-provider-comparison
type: research
title: Comparação de preços de LLM e embeddings — Anthropic, OpenAI, Google, Voyage (2026-11-19)
branch: integrations
tags: [llm, integrations]
status: active
confidence: medium
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: []
related: [CTX-QUE-20261119-llm-provider, CTX-DEC-20261119-agent-autonomy-and-memory, CTX-DEC-20261119-python-uv-stack]
valid_from: 2026-11-19
revisit_at: 2026-12-01
---

# Comparação de preços de LLM e embeddings (2026-11-19)

## Pergunta investigada

Quais provedores de LLM e de embeddings atendem o SaaS multi-tenant em Python (`CTX-QUE-20261119-llm-provider`) e quanto custam?

Requisitos: SDK Python, tool use, cache de prompt (o custo por tenant cai quando o prefixo é reaproveitado) e embeddings para RAG.

## Escopo

- Coberto: **preço de lista** (USD por 1M tokens, tier padrão, prompts curtos), cache e embeddings.
- **Não avaliado:**
  - qualidade em português e em tool use;
  - latência e rate limits;
  - retenção de dados, LGPD e residência de dados.

## Fontes (com data de acesso: 2026-11-19)

- Anthropic: `platform.claude.com/docs/en/about-claude/pricing` e `.../build-with-claude/embeddings`. Também a referência de modelos da skill `claude-api` do Claude Code (cache de 2026-11-03).
- OpenAI: `developers.openai.com/api/docs/pricing` (a página não tem data).
- Google: `aistudio.google.com/docs/pricing` (nova URL de `ai.google.dev/gemini-api/docs/pricing`; a parte de embeddings não foi lida porque a página veio truncada).
- Voyage AI: `docs.voyageai.com/pricing`.
- Agregadores de terceiros (CloudZero, G2, Puter, Requesty, Costbench) foram **descartados**: divergiam entre si e das páginas oficiais.

## Evidências — modelos de chat (input / cache hit / output, USD por 1M tokens)

| Faixa | Anthropic | OpenAI | Google |
|---|---|---|---|
| Topo | Claude Opus 5.5: 4 / 0,20 / 20 | gpt-6.2-astra: 8 / 0,40 / 40 | Gemini 4 Neon: 3 / 0,15 / 15 |
| Intermediária | Claude Sonnet 5.5: 2 / 0,10 / 10 | gpt-6.2-sol: 2 / 0,10 / 10 · gpt-6.1-terra: 1 / 0,05 / 5 | Gemini 4 Carbon/Argon: 2 / 0,10 / 10 (**dobra em 2026-12-01**) · Gemini 4 Hydrogen: 1,50 / 0,075 / 7,50 |
| Barata | Claude Haiku 5.5: 0,10 / 0,01 / 0,50 (até 100k tokens no prompt; acima disso 0,50 / 0,05 / 2,50) | gpt-6-luna: 0,10 / 0,01 / 0,50 | Gemini 3.8/3.6 Flash: 0,75 / 0,075 / 3,75 (**dobra em 2027-01-01**) · Gemini 2.5 Flash-Lite: 0,10 / 0,01 / 0,40 |

Outros pontos de custo:

- **Anthropic:** escrita de cache custa 1,25× o input (5 min) ou 2× (1 h). O Batch API dá 50% de desconto e combina com o cache. US-only (`inference_geo`) custa 1,1×.
- **OpenAI:** prompts acima de 272k tokens têm outro preço.
- **Google:**
  - o tier gratuito usa o conteúdo para melhorar produtos; o pago não;
  - alguns modelos cobram armazenamento de cache por hora;
  - Gemini 2.5 Pro e 2.5 Flash estão deprecados e passam a ser redirecionados para outros modelos em 2026-12-01.

## Evidências — embeddings (USD por 1M tokens)

| Provedor | Modelos |
|---|---|
| Anthropic | **Não tem modelo próprio**; a documentação aponta a Voyage AI (MongoDB) |
| Voyage AI | voyage-4-large 0,12 · voyage-4 0,06 · voyage-4-lite 0,02 · 200M tokens grátis na família 4 · rerank-3 0,05 / rerank-3-lite 0,02 · pacote Python `voyageai` · voyage-4-nano tem pesos abertos (Apache 2.0) |
| OpenAI | text-embedding-3-small 0,02 · text-embedding-3-large 0,13 |
| Google | Não confirmado na fonte oficial (agregadores citam ~0,20 para texto no Gemini Embedding 2) |

## Achados

1. **Os preços se equivalem nas três faixas.** Anthropic, OpenAI e Google têm opções quase idênticas: cerca de 2 / 10 na intermediária e 0,10 / 0,50 na barata. Preço de lista não decide a escolha. Exceção: o Google tem aumentos já agendados (dez/2026 e jan/2027).
2. **O provedor de embeddings pode ser diferente do de chat.** Os embeddings são a escolha mais difícil de trocar: mudar de modelo exige reindexar a base de todos os tenants.
3. Todos os provedores oferecem cache de prompt com hit a ~5–10% do input. Para multi-tenant, isso favorece um prefixo estável (system prompt e ferramentas fixos) com o conteúdo do tenant depois do prefixo.
4. Usar dois modelos (um intermediário para raciocínio e um barato para classificação e roteamento) é viável nos três provedores.

## Limitações

- Não há comparação de **qualidade**. O que vai decidir é o desempenho nas tarefas reais (português, tool use, suporte com RAG), e isso exige uma avaliação própria.
- Os nomes e preços dos modelos mudam rápido; a página da OpenAI não tem data.
- Esta pesquisa foi feita pelo Claude, um modelo da Anthropic, que é uma das empresas comparadas. Por isso foram usadas só fontes oficiais de cada empresa.

## Confiança

- **Alta** para os preços das páginas oficiais na data de acesso.
- **Baixa** para qualquer conclusão sobre qualidade (não medida).

## Implicações

- A decisão (`CTX-QUE-20261119-llm-provider`) deveria sair de uma avaliação pequena: as mesmas tarefas rodadas em 2–3 candidatos de faixa intermediária.
- Enquanto isso, o código deve chamar o LLM e os embeddings por interfaces próprias, para trocar o provedor sem reescrever (`CTX-DEC-20261119-local-cross-platform-runtime`).
- Os vetores precisam guardar o modelo de embedding usado, para permitir reindexação.

## Questões ainda abertas

- Qual provedor tem melhor qualidade nas tarefas do produto, em português?
- Quais exigências de privacidade e retenção de dados vêm dos tenants (LGPD)?
- Qual o preço oficial de embeddings do Google?
