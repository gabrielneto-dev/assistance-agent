# Branch: integrations

Última revisão: 2026-11-19

## Propósito

Conhecimento sobre **serviços externos** usados pelo agente: provedor(es) e modelo(s) de LLM, APIs de terceiros, autenticação com esses serviços (somente nomes de variáveis, nunca valores).

## Escopo

Inclui: provedor de LLM, SDKs, limites/preços de APIs (sempre com data), integrações com terceiros.
Não inclui: comportamento do agente (→ `agent-design`), runtime/deploy (→ `infrastructure`).

## Estado atual

Nada definido.

## Decisões ativas

- Nenhuma.

## Perguntas abertas

- `CTX-QUE-20261119-llm-provider` — qual provedor/modelo de LLM usar.

## Riscos

- Nenhum registrado.

## Relações com outras branches

- `agent-design`: capacidades do agente dependem das integrações disponíveis.
- `infrastructure`: o SDK do provedor influencia a escolha de linguagem.

## Rotas

- Registros: `questions/`. Informação temporal (preço, versão de modelo, limites) exige `valid_from`/`revisit_at` e `source_ids`.
