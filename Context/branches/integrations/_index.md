# Branch: integrations

Última revisão: 2026-11-21

## Propósito

Conhecimento sobre **serviços externos** usados pelo agente: provedor(es) e modelo(s) de LLM, APIs de terceiros, autenticação com esses serviços (somente nomes de variáveis, nunca valores).

## Escopo

Inclui: provedor de LLM, SDKs, limites/preços de APIs (sempre com data), integrações com terceiros.
Não inclui: comportamento do agente (→ `agent-design`), runtime/deploy (→ `infrastructure`).

## Estado atual

- Primeiro canal de mensageria: **WhatsApp** (`CTX-DEC-20261119-multi-tenant-saas-product`); meio de integração indefinido. As perguntas para o usuário estão listadas na própria `question`; a pesquisa ainda não foi feita.
- Provedor de LLM indefinido; critérios em `CTX-QUE-20261119-llm-provider`; preços comparados em `CTX-RES-20261119-llm-provider-comparison` (revisar em 2026-12-01).

## Decisões ativas

- Nenhuma.

## Perguntas abertas

- `CTX-QUE-20261119-llm-provider` — qual provedor/modelo de LLM usar (crítica; preços pesquisados; falta a avaliação de qualidade e as respostas do usuário listadas na `question`).
- `CTX-QUE-20261119-whatsapp-integration-method` — API oficial da Meta ou provedor intermediário; conexão por tenant.

## Riscos

- Nenhum registrado.

## Relações com outras branches

- `agent-design`: capacidades do agente dependem das integrações disponíveis.
- `infrastructure`: o SDK do provedor influencia a escolha de linguagem.

## Rotas

- Registros: `questions/`, `research/`. Informação temporal (preço, versão de modelo, limites) exige `valid_from`/`revisit_at` e `source_ids`.
