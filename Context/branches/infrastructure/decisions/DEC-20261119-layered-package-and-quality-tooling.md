---
id: CTX-DEC-20261119-layered-package-and-quality-tooling
type: decision
title: Código em um único pacote Python em camadas, com pytest, ruff, mypy e pre-commit
branch: infrastructure
tags: [stack, tooling]
status: active
confidence: high
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: []
related: [CTX-DEC-20261119-python-uv-stack, CTX-DEC-20261119-local-cross-platform-runtime, CTX-DEC-20261119-multi-tenant-saas-product]
depends_on: [CTX-DEC-20261119-python-uv-stack]
supersedes: null
superseded_by: null
revisit_at: null
---

# Pacote único em camadas + ferramentas de qualidade

## Contexto

Planejamento de `SPEC-0001` (esqueleto do projeto). O usuário confirmou as escolhas abaixo em 2026-11-19, escolhendo entre opções propostas pelo agente.

## Decisão

- **Python ≥ 3.13**, gerenciado por uv (`CTX-DEC-20261119-python-uv-stack`).
- **Um único pacote** `src/assistance_agent/`, organizado em camadas:
  - `core/` — domínio (tenant, conversa, regras), sem dependência de infraestrutura;
  - `ports/` — interfaces (LLM, embeddings, armazenamento);
  - `adapters/` — implementações das portas (fakes hoje; provedores reais depois);
  - `interfaces/` — pontos de entrada (CLI hoje; API e WhatsApp depois).
  - Regra de dependência: `core` e `ports` não importam `adapters` nem `interfaces`.
- **Qualidade:** pytest (testes), ruff (lint e formatação), mypy (tipos), pre-commit (roda as checagens antes de cada commit).

## Opções consideradas

- uv workspace com vários pacotes → preterido: separação mais rígida, porém mais configuração para um projeto inicial. Pode ser adotado depois se as camadas crescerem.

## Consequências

- Trocar o provedor de LLM/embeddings ou adicionar canais significa criar um adapter/interface novo, sem tocar no `core`.
- Os comandos de qualidade entram em `AGENTS.md` quando o esqueleto existir (`SPEC-0001`).
