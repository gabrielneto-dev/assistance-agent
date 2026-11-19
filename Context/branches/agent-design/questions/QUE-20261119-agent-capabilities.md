---
id: CTX-QUE-20261119-agent-capabilities
type: question
title: Quais capacidades, ferramentas e modelo de memória o agente terá?
branch: agent-design
tags: [agent-behavior, tools, memory]
status: open
priority: high
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-QUE-20261119-llm-provider, CTX-DEC-20261119-agent-autonomy-and-memory, CTX-DEC-20261119-repair-shop-ai-attendant]
depends_on: [CTX-QUE-20261119-project-scope-and-users]
resolved_by: null
---

# Quais capacidades, ferramentas e modelo de memória o agente terá?

## Pergunta

Que ações o agente pode executar (ferramentas), como mantém estado/memória entre interações e quais limites de autonomia ele tem?

## Por que importa

Define a arquitetura do agente (loop de ferramentas, armazenamento de memória, guardrails) e quais integrações são necessárias.

## O que depende da resposta

- Integrações necessárias (`CTX-QUE-20261119-llm-provider` e APIs externas).
- Necessidade de persistência (banco, arquivos) em `infrastructure`.

## Opções conhecidas

- Memória: sem memória, histórico da conversa, memória persistente (arquivo/banco/vetorial).
- Autonomia: responde apenas; executa ações com confirmação; executa ações autônomas.

## Como resolver

Responder primeiro `CTX-QUE-20261119-project-scope-and-users`; depois listar casos de uso e derivar as ferramentas.

## Resposta parcial (2026-11-19)

- Decidido: confirmação para ações com efeito externo; memória de conversa, persistente e RAG → `CTX-DEC-20261119-agent-autonomy-and-memory`.
- **Ainda aberto:** lista concreta de ferramentas por finalidade (produtividade, suporte, automação) e como a confirmação aparece em cada canal (API, CLI, WhatsApp).

## Atualização (2026-11-19)

Ferramentas iniciais derivadas do produto (`CTX-DEC-20261119-repair-shop-ai-attendant`):

- consultar ordem de serviço;
- estimar orçamento pela tabela de preços;
- buscar informações da loja;
- registrar aprovação ou recusa de orçamento (com confirmação);
- transferir para humano.

Ainda aberto: os contratos exatos de cada ferramenta e como a confirmação e a transferência aparecem no WhatsApp. Isso será definido nas specs.
