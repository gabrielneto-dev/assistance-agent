# Branch: agent-design

Última revisão: 2026-11-19

## Propósito

Conhecimento sobre **como o agente se comporta**: papel, prompts, ferramentas (tools), loop de execução, memória/estado do agente, guardrails.

## Escopo

Inclui: comportamento, prompts, definição de ferramentas, memória do agente, avaliação de qualidade das respostas.
Não inclui: escolha do provedor de LLM e APIs externas (→ `integrations`), stack/deploy (→ `infrastructure`).

## Estado atual

Nada definido. Depende do escopo do projeto.

## Decisões ativas

- Nenhuma.

## Perguntas abertas

- `CTX-QUE-20261119-agent-capabilities` — quais capacidades, ferramentas e modelo de memória o agente terá.

## Riscos

- Nenhum registrado.

## Relações com outras branches

- `integrations`: ferramentas do agente costumam depender de APIs externas e do provedor de LLM.
- `global`: depende de `CTX-QUE-20261119-project-scope-and-users`.

## Rotas

- Registros: `questions/` (crie `decisions/`, `research/` etc. quando necessário).
