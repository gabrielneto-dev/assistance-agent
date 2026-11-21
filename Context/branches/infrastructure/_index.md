# Branch: infrastructure

Última revisão: 2026-11-21

## Propósito

Conhecimento sobre **onde e com o quê** o projeto é construído e executado: linguagem, framework, gerenciador de pacotes, runtime, deploy, CI, observabilidade, repositório.

## Escopo

Inclui: stack, tooling, estrutura do repositório, ambiente de execução, deploy.
Não inclui: comportamento do agente (→ `agent-design`), APIs externas (→ `integrations`).

## Estado atual

- Repositório git em `main`, com remoto `origin` no GitHub (`gabrielneto-dev/assistance-agent`). Esqueleto Python da `SPEC-0001` implementado e commitado (`e35a0ae`); clonado também no Linux Mint, sem o hook do pre-commit instalado → `CTX-FCT-20261119-repository-initialized`.
- Windows de desenvolvimento: o Defender (ASR da TI) bloqueia os `.exe` do `.venv`; use `uv run python -m` → `CTX-FCT-20261119-windows-asr-blocks-venv-exes`.
- Armadilhas do ferramental (ruff com Markdown, pre-commit, acentos no Git Bash) → `CTX-NTE-20261119-python-tooling-pitfalls`.
- Stack: Python + uv → `CTX-DEC-20261119-python-uv-stack`.
- Execução local, portável entre Windows 11 e Linux Mint, verificada nas duas máquinas em 2026-11 → `CTX-DEC-20261119-local-cross-platform-runtime`.
- Validação estrutural: `bash Context/_meta/validate.sh`; cuidados (LF, subshell, exclusões) → `CTX-NTE-20261119-validate-script-pitfalls`.

## Decisões ativas

- `CTX-DEC-20261119-python-uv-stack`
- `CTX-DEC-20261119-local-cross-platform-runtime`
- `CTX-DEC-20261119-layered-package-and-quality-tooling` — pacote único em camadas; Python ≥ 3.13; pytest, ruff, mypy, pre-commit

## Perguntas abertas

- `CTX-QUE-20261119-tech-stack` — parcialmente respondida; ferramentas de qualidade decididas; resta framework da API, banco e armazenamento vetorial.
- Respondida: `CTX-QUE-20261119-deployment-target` (local por enquanto).

## Riscos

- Nenhum registrado.

## Relações com outras branches

- `integrations`: disponibilidade de SDK do provedor de LLM influencia a stack.

## Rotas

- Registros: `decisions/`, `facts/`, `notes/`, `questions/`.
