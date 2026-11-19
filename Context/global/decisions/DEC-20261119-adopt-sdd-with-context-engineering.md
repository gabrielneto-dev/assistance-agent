---
id: CTX-DEC-20261119-adopt-sdd-with-context-engineering
type: decision
title: Desenvolvimento segue Spec-Driven Development integrado ao sistema de contexto
branch: global
tags: [context-engineering, project-setup]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-bootstrap-answers]
related: [CTX-NTE-20261119-validate-script-pitfalls]
depends_on: []
supersedes: null
superseded_by: null
revisit_at: null
---

# Desenvolvimento segue Spec-Driven Development integrado ao sistema de contexto

## Contexto

Projeto recém-criado, sem código. O usuário pediu explicitamente (2026-11-19) a instalação de um processo SDD sobre o sistema de contexto já existente.

## Problema

Separar o que o projeto **sabe/decidiu** (memória durável) do que **está sendo construído** (specs, planos, tarefas, verificações), sem que um sistema duplique ou contradiga o outro.

## Opções consideradas

- Sistema de contexto sozinho, com planos como registros `PLN` → descartado: não rastreia requisitos, critérios de aceitação nem tarefas.
- `Specs/` independente de `Context/` → descartado: duplicaria decisões e estado.
- **`Specs/` integrado a `Context/`** → escolhido.

## Decisão

- `Context/` = conhecimento (fatos, decisões, perguntas, estado do projeto). Escrita controlada por `salvar contexto`.
- `Specs/` = desenvolvimento (`SPEC-NNNN`, `REQ`/`AC`, `SPEC-NNNN-TNNN`, verificações). Persistência operacional **automática** durante o trabalho (`Specs/README.md` seção 11).
- Rigor adaptativo: `trivial`, `lightweight`, `full`, `critical` (este exige `approved_by`).
- Ponte: specs citam `Context/` via `context_refs`; decisão durável confirmada no planejamento vira `DEC` imediatamente (exceção estreita, `Context/README.md` seção 9); checkpoints registram o estado SDD só por referência.
- Sem commit/push automático.

## Motivo

Rastreabilidade (requisito → tarefa → verificação) sem duplicar conhecimento, e retomada confiável após reset de sessão via `Specs/STATE.md`.

## Consequências

- Mudança não trivial exige spec antes do código; `Specs/STATE.md` e `Specs/INDEX.md` devem acompanhar o trabalho.
- `Context/_meta/validate.sh` verifica a consistência dos dois sistemas.

## Riscos

- Overhead em projeto pequeno; mitigado pelos níveis `trivial`/`lightweight`.

## Registros relacionados

- `AGENTS.md` (blocos `CONTEXT-ENGINEERING` e `SPEC-DRIVEN`), `Specs/README.md`, `Context/README.md`.
