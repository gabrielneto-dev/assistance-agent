# Branch: infrastructure

Última revisão: 2026-11-19

## Propósito

Conhecimento sobre **onde e com o quê** o projeto é construído e executado: linguagem, framework, gerenciador de pacotes, runtime, deploy, CI, observabilidade, repositório.

## Escopo

Inclui: stack, tooling, estrutura do repositório, ambiente de execução, deploy.
Não inclui: comportamento do agente (→ `agent-design`), APIs externas (→ `integrations`).

## Estado atual

- Repositório git inicializado vazio, sem commits, sem `.gitignore` → `CTX-FCT-20261119-repository-initialized`.
- Ambiente de desenvolvimento: Windows 11 (ver `core/constraints.md`).

## Decisões ativas

- Nenhuma.

## Perguntas abertas

- `CTX-QUE-20261119-tech-stack` — linguagem, framework, gerenciador de pacotes.
- `CTX-QUE-20261119-deployment-target` — onde o agente roda.

## Riscos

- Nenhum registrado.

## Relações com outras branches

- `integrations`: disponibilidade de SDK do provedor de LLM influencia a stack.

## Rotas

- Registros: `facts/`, `questions/`.
