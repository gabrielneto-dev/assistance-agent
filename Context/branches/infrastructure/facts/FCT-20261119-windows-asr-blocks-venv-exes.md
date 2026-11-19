---
id: CTX-FCT-20261119-windows-asr-blocks-venv-exes
type: fact
title: No Windows de desenvolvimento, o Defender (ASR da TI) bloqueia os .exe do .venv
branch: infrastructure
tags: [tooling, runtime]
status: active
confidence: verified
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: []
related: [CTX-DEC-20261119-local-cross-platform-runtime, CTX-DEC-20261119-python-uv-stack, CTX-NTE-20261119-python-tooling-pitfalls]
depends_on: []
valid_from: 2026-11-19
valid_until: null
revisit_at: null
---

# O Defender bloqueia os lançadores .exe do .venv no Windows de desenvolvimento

## Fato

O Windows 11 de desenvolvimento é uma máquina gerenciada, num domínio corporativo/institucional. Nela, uma regra de redução de superfície de ataque (ASR) do Microsoft Defender, configurada pela TI, bloqueia executáveis novos ou pouco difundidos:

- regra: "bloquear executáveis que não atendem a critérios de prevalência, idade ou lista confiável";
- ID: `01443614-CD74-433A-B99E-2ECDC07BFC25`.

Os lançadores que o uv cria em `.venv/Scripts` (`assistance-agent.exe`, `pytest.exe` etc.) falham com "Acesso negado" (os error 5). O bloqueio aparece no log `Microsoft-Windows-Windows Defender/Operational` como evento 1121.

Funcionam normalmente: `python.exe` do `.venv`, o uv (instalado via winget) e todas as ferramentas chamadas como `python -m <módulo>`.

## Implicações

- Regra em `AGENTS.md`: sempre `uv run python -m <módulo>`. O pacote tem `__main__.py`, então `python -m assistance_agent` funciona.
- Os hooks do pre-commit chamam `uv run python -m ...`.
- Não contornar nem alterar a política: ela é da TI, não do projeto.
- No Linux Mint não há essa restrição (o script `assistance-agent` deve funcionar lá, a confirmar na `SPEC-0001-T010`).

## Evidência

`SPEC-0001` (`Specs/features/SPEC-0001--project-skeleton/`): Change Log da spec e a evidência da `SPEC-0001-T002`. Eventos 1121 do Defender em 2026-11-19 apontando para `.venv\Scripts\assistance-agent.exe`.
