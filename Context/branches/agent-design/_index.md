# Branch: agent-design

Última revisão: 2026-11-19

## Propósito

Conhecimento sobre **como o agente se comporta**: papel, prompts, ferramentas (tools), loop de execução, memória/estado do agente, guardrails.

## Escopo

Inclui: comportamento, prompts, definição de ferramentas, memória do agente, avaliação de qualidade das respostas.
Não inclui: escolha do provedor de LLM e APIs externas (→ `integrations`), stack/deploy (→ `infrastructure`).

## Estado atual

Autonomia e memória definidas: confirmação para ações externas; memória de conversa, persistente e RAG, isoladas por tenant. Ferramentas iniciais derivadas do produto: consultar OS, estimar orçamento, informações da loja, aprovar orçamento, transferir para humano (`CTX-DEC-20261119-repair-shop-ai-attendant`).

## Decisões ativas

- `CTX-DEC-20261119-agent-autonomy-and-memory` — confirmação para ações externas; três camadas de memória.

## Perguntas abertas

- `CTX-QUE-20261119-agent-capabilities` — parcialmente respondida; resta a lista de ferramentas e a confirmação por canal.

## Riscos

- `CTX-RSK-20261119-ai-wrong-quote-or-status` — informar preço, prazo ou status errado.

## Relações com outras branches

- `integrations`: ferramentas do agente costumam depender de APIs externas e do provedor de LLM.
- `global`: decorre de `CTX-DEC-20261119-multi-tenant-saas-product`.

## Rotas

- Registros: `decisions/`, `questions/`.
