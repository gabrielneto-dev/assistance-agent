---
id: CTX-SRC-20261119-user-bootstrap-answers
type: source
title: Respostas do usuário durante o bootstrap de contexto
branch: global
tags: [context-engineering, scope]
status: active
confidence: verified
created_at: 2026-11-19
updated_at: 2026-11-19
related: [CTX-CP-20261119-0928-context-bootstrap, CTX-CP-20261119-1149-sdd-install-and-tooling]
---

# Respostas do usuário durante o bootstrap de contexto

## Origem

Usuário (dono do projeto), em sessão do Claude Code, 2026-11-19, respondendo a perguntas de clarificação do bootstrap.

## Conteúdo obtido

| Pergunta | Resposta |
|---|---|
| O que é o projeto? | Assistente/agente de IA em código (software) |
| Idioma dos documentos de `Context/` | Português (arquivos, IDs, chaves e tags em inglês) |
| Inicializar git? | Sim, `git init` (sem commit) |
| Salvar o script de validação no projeto? | Sim → `Context/_meta/validate.sh` |
| Identidade dos commits | Nome do usuário e e-mail da conta Claude, configurados só no repositório (valor não registrado aqui) |
| `.gitattributes` forçando LF em `*.sh`? | Sim |
| Instalar SDD integrado ao contexto? | Sim (prompt de bootstrap SDD colado pelo usuário) → `CTX-DEC-20261119-adopt-sdd-with-context-engineering` |
| Commits | Feitos a pedido explícito do usuário, um por etapa; sem push |

## Confiabilidade

Alta — declaração direta do usuário. Não inclui escopo, stack nem provedor de LLM (registrados como perguntas abertas).
