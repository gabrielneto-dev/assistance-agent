# Restrições

Última revisão: 2026-11-19

Somente restrições confirmadas. Restrições financeiras e de prazo ainda não foram definidas.

## Ambiente

- Desenvolvimento em **duas máquinas**: Windows 11 (PowerShell e Git Bash) e Linux Mint (PC de casa). Código, scripts e comandos devem funcionar nas duas → `CTX-DEC-20261119-local-cross-platform-runtime`.
- Execução local por enquanto; nada de dependência de nuvem obrigatória.
- No Windows de desenvolvimento (máquina gerenciada), o Defender bloqueia os `.exe` do `.venv`: ferramentas sempre via `uv run python -m` → `CTX-FCT-20261119-windows-asr-blocks-venv-exes`.

## Stack

- Python, com uv para pacotes, versão do Python e ambiente → `CTX-DEC-20261119-python-uv-stack`.

## Produto

- Multi-tenant desde o primeiro código → `CTX-DEC-20261119-multi-tenant-saas-product`.
- Ações com efeito externo exigem confirmação → `CTX-DEC-20261119-agent-autonomy-and-memory`.

## Segurança

- Nenhum segredo/credencial em `Context/` ou `Specs/` (ver `AGENTS.md`). Referenciar apenas nomes de variáveis de ambiente.

## Documentação

- Conteúdo de `Context/` em português; nomes de arquivo, IDs, chaves YAML e tags em inglês.

## A definir

- Provedor de LLM e custos (`CTX-QUE-20261119-llm-provider`), meio de integração com WhatsApp (`CTX-QUE-20261119-whatsapp-integration-method`).
