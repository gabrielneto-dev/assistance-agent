# Project State

Last updated: 2026-11-21
Latest checkpoint: `Context/checkpoints/CP-20261121-1436-spec-0001-closed-and-open-decisions.md` (`CTX-CP-20261121-1436-spec-0001-closed-and-open-decisions`)

## Objetivo atual

Construir o atendente de IA no WhatsApp para assistências técnicas de eletrônicos (`CTX-DEC-20261119-repair-shop-ai-attendant`), sobre o esqueleto já concluído (`SPEC-0001`). Antes da próxima spec, o usuário precisa decidir a loja piloto, o provedor de LLM e a integração com o WhatsApp.

Estado do desenvolvimento (specs, tarefas, verificações): `Specs/STATE.md`.

## Funcionando

- Repositório git com remoto `origin` no GitHub (`gabrielneto-dev/assistance-agent`); push só sob pedido. `main` = `origin/main` = `15bf92e`. Clonado no Windows e no Linux Mint.
- Sistema de contexto e SDD.
- Esqueleto Python (`SPEC-0001`, `done`): núcleo multi-tenant, LLM e embeddings fake, CLI `uv run python -m assistance_agent chat --tenant <id>`. 59 testes, ruff, mypy strict e pre-commit OK **no Windows 11 e no Linux Mint 22.3**.

## Em andamento

- **Não commitado:** o fechamento da `SPEC-0001` e o save de contexto de 2026-11-21 estão na worktree `.claude/worktrees/continuar-desenvolvimento-d63219` (branch `claude/continuar-desenvolvimento-d63219`).
- Nenhuma spec ativa. Próximo ID livre: `SPEC-0002`.

## Bloqueios

- A próxima funcionalidade depende de respostas do usuário, já listadas em cada `question`: `CTX-QUE-20261119-pilot-shop`, `CTX-QUE-20261119-llm-provider` e `CTX-QUE-20261119-whatsapp-integration-method`.
- No Windows de desenvolvimento, ferramentas só via `uv run python -m` (`CTX-FCT-20261119-windows-asr-blocks-venv-exes`).
- No clone do Linux Mint, o hook do pre-commit não está instalado (`CTX-FCT-20261119-repository-initialized`).

## Decisões ativas

- Ideia: atendente de IA humanizado para assistências técnicas; IA primeiro, gestão depois; valores finais sempre com humano → `CTX-DEC-20261119-repair-shop-ai-attendant`
- Formato: SaaS multi-tenant; API, CLI e WhatsApp → `CTX-DEC-20261119-multi-tenant-saas-product`
- Agente: confirmação para ações externas; memória de conversa, persistente e RAG → `CTX-DEC-20261119-agent-autonomy-and-memory`
- Stack: Python + uv → `CTX-DEC-20261119-python-uv-stack`
- Execução local, portável Windows 11 / Linux Mint (verificada), código modular → `CTX-DEC-20261119-local-cross-platform-runtime`
- Pacote único em camadas; Python ≥ 3.13; pytest, ruff, mypy, pre-commit → `CTX-DEC-20261119-layered-package-and-quality-tooling`
- Processo: SDD integrado ao contexto → `CTX-DEC-20261119-adopt-sdd-with-context-engineering`
- Convenção do contexto: conteúdo em português; arquivos, IDs, tags em inglês.

## Perguntas em aberto

- Loja piloto e dados reais anonimizados — **responder primeiro** → `CTX-QUE-20261119-pilot-shop`
- Provedor/modelo de LLM (crítica; preços pesquisados em `CTX-RES-20261119-llm-provider-comparison`, falta avaliar qualidade) → `CTX-QUE-20261119-llm-provider`
- Meio de integração com WhatsApp e onde roda o webhook (pesquisa pendente) → `CTX-QUE-20261119-whatsapp-integration-method`
- Framework da API, banco, armazenamento vetorial → `CTX-QUE-20261119-tech-stack`
- Ferramentas concretas e confirmação por canal → `CTX-QUE-20261119-agent-capabilities`

## Próximos passos prováveis

1. Commitar o fechamento da `SPEC-0001` e o contexto (sob pedido); no Linux Mint, antes, `uv run python -m pre_commit install`.
2. Usuário responde a loja piloto.
3. Pesquisa datada da integração com WhatsApp; decisão do usuário.
4. Avaliação pequena de 2–3 modelos de LLM com o material da loja; decisão do usuário.
5. Spec do atendimento no WhatsApp (nível critical). Alternativa sem bloqueio: spec de persistência do histórico por tenant.
