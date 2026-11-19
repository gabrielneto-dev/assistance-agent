---
id: CTX-ASM-20261119-single-developer-project
type: assumption
title: O projeto é desenvolvido por uma única pessoa
branch: global
tags: [scope, project-setup]
status: active
confidence: low
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-bootstrap-answers]
related: [CTX-QUE-20261119-project-scope-and-users]
depends_on: []
---

# O projeto é desenvolvido por uma única pessoa

## Hipótese

O projeto é mantido por um único desenvolvedor, sem time nem processo formal de revisão.

## Por que assumimos

O repositório está em uma pasta pessoal, foi criado vazio e não há indicação de colaboradores, remoto git ou convenções de time.

## O que depende dela

- Peso do processo (revisão, branches git, CI) — pode ser leve enquanto valer.
- Nível de formalidade das decisões registradas.

## Como validar

Perguntar ao usuário junto com `CTX-QUE-20261119-project-scope-and-users`, ou observar remoto git/colaboradores.

## Consequência se falsa

Adotar convenções de colaboração (fluxo de branches, PRs, CI) e registrá-las em `AGENTS.md`.
