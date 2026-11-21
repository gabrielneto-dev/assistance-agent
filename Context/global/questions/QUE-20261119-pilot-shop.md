---
id: CTX-QUE-20261119-pilot-shop
type: question
title: Qual loja será o primeiro piloto e com que dados reais?
branch: global
tags: [users, goals]
status: open
priority: high
created_at: 2026-11-19
updated_at: 2026-11-21
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-DEC-20261119-repair-shop-ai-attendant]
depends_on: []
resolved_by: null
---

# Qual loja será o primeiro piloto?

## Pergunta

A assistência onde o usuário trabalha (ou outra) pode ser o primeiro tenant piloto? Que dados reais ela forneceria: perguntas frequentes, tabela de preços, formato das ordens de serviço, exemplos de conversas anonimizados?

## Por que importa

- Exemplos reais de conversa são o melhor material para a avaliação do provedor de LLM (`CTX-QUE-20261119-llm-provider`) e para calibrar o tom humanizado.
- O formato real das ordens de serviço e da tabela de preços define o modelo de dados mínimo.
- Validar com uma loja real reduz o risco de construir algo que ninguém usa.

## Cuidados

Dados de clientes finais são pessoais (LGPD): use só material anonimizado em testes e avaliações, e nunca em `Context/` ou `Specs/`.

## Como resolver

Perguntar ao usuário.

## O que falta o usuário responder (levantado em 2026-11-21)

1. A assistência onde o usuário trabalha pode ser o primeiro tenant piloto? Se não, qual seria?
2. Que material ela fornece, anonimizado: perguntas frequentes, tabela de preços, um exemplo de ordem de serviço, 10–30 conversas reais de WhatsApp sem nomes nem telefones?
3. Quem responde hoje o WhatsApp da loja e quanto tempo isso toma por dia? Isso mostra se o produto resolve um problema real.

É a pergunta a responder primeiro: o material dela alimenta a avaliação do provedor de LLM (`CTX-QUE-20261119-llm-provider`).
