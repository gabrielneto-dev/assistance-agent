---
id: CTX-DEC-20261119-local-cross-platform-runtime
type: decision
title: Execução local por enquanto, com código modular e portável entre Windows e Linux Mint
branch: infrastructure
tags: [runtime, deployment]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: [CTX-SRC-20261119-user-definition-answers]
related: [CTX-QUE-20261119-deployment-target, CTX-DEC-20261119-python-uv-stack, CTX-DEC-20261119-multi-tenant-saas-product]
depends_on: []
supersedes: null
superseded_by: null
revisit_at: null
---

# Execução local, portável entre Windows e Linux Mint

## Decisão

- **Por enquanto** o sistema roda localmente; a hospedagem do SaaS será decidida depois.
- O desenvolvimento acontece em duas máquinas: **Windows 11** (atual) e **Linux Mint** (PC de casa). Tudo deve funcionar nas duas.
- Código **modular**: núcleo do agente separado das interfaces e dos adaptadores de infraestrutura, para que a troca de ambiente (local → nuvem) não exija reescrita.

## Motivo

Palavras do usuário: "local por agora, mas tem que ser modular", porque vai programar em Windows e em Linux Mint.

## Consequências

- Sem caminhos absolutos nem separadores fixos (usar `pathlib`); configuração por variáveis de ambiente/arquivo `.env` não versionado (só nomes de variáveis em `Context/`).
- Scripts de projeto preferencialmente em Python via `uv run`, não em PowerShell ou Bash exclusivos.
- Dependências de serviços (banco, vetores) devem rodar nas duas máquinas (ex.: via container ou embarcados) — escolha em `CTX-QUE-20261119-tech-stack`.
- Atenção a fim de linha: `.gitattributes` já força LF em `*.sh`; avaliar o mesmo para `*.py` quando houver código.

## Revisar quando

Houver decisão de hospedar o SaaS (a pergunta de hospedagem volta a ser aberta).
