---
id: CTX-CP-20261119-1149-sdd-install-and-tooling
type: checkpoint
title: Validador, LF em scripts, SDD instalado e commits iniciais
branch: global
tags: [context-engineering, project-setup, tooling]
status: active
created_at: 2026-11-19
updated_at: 2026-11-19
related:
  - CTX-CP-20261119-0928-context-bootstrap
  - CTX-DEC-20261119-adopt-sdd-with-context-engineering
  - CTX-NTE-20261119-validate-script-pitfalls
  - CTX-FCT-20261119-repository-initialized
---

# Session Checkpoint — Validador, LF em scripts, SDD instalado e commits iniciais

## Objetivo

Continuar a sessão de bootstrap: tornar a validação do contexto reprodutível, fazer os primeiros commits e instalar o processo Spec-Driven Development integrado a `Context/`.

## O que mudou

- `Context/_meta/validate.sh` adicionado (somente leitura) e referenciado em `Context/README.md` e `Specs/README.md`.
- `.gitattributes` com `*.sh text eol=lf`.
- `Specs/` criado (README, INDEX, STATE, `_meta/config.yaml`, templates) e bloco `SPEC-DRIVEN` em `AGENTS.md`; `Context/README.md`, `MAP.md`, `STATE.md`, glossário e template de checkpoint integrados ao SDD.
- Três commits em `main` (bootstrap de contexto → `.gitattributes` → SDD), todos a pedido do usuário; sem remoto, sem push.
- Neste save: regra em `AGENTS.md` para rodar o validador após alterar `Context/`/`Specs/`.

## Decisões

- Processo de desenvolvimento = SDD integrado ao contexto → `CTX-DEC-20261119-adopt-sdd-with-context-engineering`.
- Identidade git só local ao repositório (preferência do usuário) → `CTX-FCT-20261119-repository-initialized`.

## Descobertas

- `core.autocrlf=true` neste ambiente: scripts `.sh` precisam de LF forçado para rodar no Git Bash.

## Problemas resolvidos

- Falsos registros vindos de exemplos de schema no README; checagens em `| while read` que nunca falhavam; tags em lista YAML não reconhecidas — todos corrigidos no validador (`CTX-NTE-20261119-validate-script-pitfalls`).
- Registros que ainda diziam "sem commits" foram atualizados.

## Abordagens que falharam (vale lembrar)

- Checagens dentro de pipelines com `while read` (subshell não propaga falha).

## Estado atual

Infraestrutura de contexto e SDD prontas e validadas (PASS, incluindo testes negativos). Nenhum código, nenhuma definição de produto ou stack. Ver `Context/STATE.md`.

## Estado SDD

Nenhuma spec; próximo ID livre `SPEC-0001` (`Specs/INDEX.md`). Sem tarefa ativa. Última validação: PASS em 2026-11-19 (`Specs/STATE.md`). Reconciliado com o repositório: consistente.

## Perguntas abertas

- `CTX-QUE-20261119-project-scope-and-users` (crítica)
- `CTX-QUE-20261119-tech-stack` (crítica)
- `CTX-QUE-20261119-llm-provider` (crítica)
- `CTX-QUE-20261119-agent-capabilities`
- `CTX-QUE-20261119-deployment-target`

## Próximos passos

1. Definir escopo e usuários.
2. Decidir stack e provedor de LLM (`DEC`).
3. Primeira funcionalidade via `iniciar spec`; `.gitignore` da stack.

## Arquivos ou artefatos afetados

`.gitattributes`, `AGENTS.md`, `Context/README.md`, `Context/MAP.md`, `Context/STATE.md`, `Context/_meta/**`, `Context/core/glossary.md`, `Context/branches/infrastructure/**`, `Context/global/decisions/`, `Context/sources/`, `Specs/**`.

## Registros de contexto criados/atualizados

- Criados: `CTX-DEC-20261119-adopt-sdd-with-context-engineering`, `CTX-NTE-20261119-validate-script-pitfalls`, este checkpoint.
- Atualizados: `CTX-FCT-20261119-repository-initialized`, `CTX-SRC-20261119-user-bootstrap-answers`.
