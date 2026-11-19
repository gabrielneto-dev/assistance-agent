# Project State

Last updated: 2026-11-19
Latest checkpoint: `Context/checkpoints/CP-20261119-1641-product-idea-and-skeleton.md` (`CTX-CP-20261119-1641-product-idea-and-skeleton`)

## Objetivo atual

Construir o atendente de IA no WhatsApp para assistências técnicas de eletrônicos (`CTX-DEC-20261119-repair-shop-ai-attendant`), a partir do esqueleto já implementado (`SPEC-0001`). As definições fundamentais foram respondidas em 2026-11-19, exceto provedor de LLM e integração com WhatsApp.

Estado do desenvolvimento (specs, tarefas, verificações): `Specs/STATE.md`.

## Funcionando

- Repositório git em `main`, com remoto `origin` no GitHub (`gabrielneto-dev/assistance-agent`); push só sob pedido. Último commit: `e35a0ae` (produto definido + esqueleto da SPEC-0001).
- Sistema de contexto e SDD.
- Esqueleto Python (`SPEC-0001`): núcleo multi-tenant, LLM e embeddings fake, CLI `uv run python -m assistance_agent chat --tenant <id>`. 59 testes, ruff, mypy strict e pre-commit OK no Windows.

## Em andamento

- `SPEC-0001` em `verify`. **Próximo passo:** o usuário clona o repositório no Linux Mint e roda a verificação (`SPEC-0001-T010`; passos em `Specs/STATE.md`).

## Bloqueios

- Funcionalidades que chamam um LLM real dependem de `CTX-QUE-20261119-llm-provider`; o atendimento no WhatsApp depende também de `CTX-QUE-20261119-whatsapp-integration-method`.
- No Windows de desenvolvimento, ferramentas só via `uv run python -m` (`CTX-FCT-20261119-windows-asr-blocks-venv-exes`).

## Decisões ativas

- Ideia: atendente de IA humanizado para assistências técnicas; IA primeiro, gestão depois; valores finais sempre com humano → `CTX-DEC-20261119-repair-shop-ai-attendant`
- Formato: SaaS multi-tenant; API, CLI e WhatsApp → `CTX-DEC-20261119-multi-tenant-saas-product`
- Agente: confirmação para ações externas; memória de conversa, persistente e RAG → `CTX-DEC-20261119-agent-autonomy-and-memory`
- Stack: Python + uv → `CTX-DEC-20261119-python-uv-stack`
- Execução local, portável Windows 11 / Linux Mint, código modular → `CTX-DEC-20261119-local-cross-platform-runtime`
- Pacote único em camadas; Python ≥ 3.13; pytest, ruff, mypy, pre-commit → `CTX-DEC-20261119-layered-package-and-quality-tooling`
- Processo: SDD integrado ao contexto → `CTX-DEC-20261119-adopt-sdd-with-context-engineering`
- Convenção do contexto: conteúdo em português; arquivos, IDs, tags em inglês.

## Perguntas em aberto

- Provedor/modelo de LLM (crítica; preços pesquisados em `CTX-RES-20261119-llm-provider-comparison`, falta avaliar qualidade) → `CTX-QUE-20261119-llm-provider`
- Meio de integração com WhatsApp → `CTX-QUE-20261119-whatsapp-integration-method`
- Loja piloto e dados reais anonimizados → `CTX-QUE-20261119-pilot-shop`
- Framework da API, banco, armazenamento vetorial → `CTX-QUE-20261119-tech-stack`
- Ferramentas concretas e confirmação por canal → `CTX-QUE-20261119-agent-capabilities`

## Próximos passos prováveis

1. Usuário verifica a `SPEC-0001` no Linux Mint (T010); fechar a spec.
2. Loja piloto (`CTX-QUE-20261119-pilot-shop`) e avaliação pequena para escolher o provedor de LLM.
3. Pesquisa e decisão da integração com WhatsApp; depois a spec do atendimento (nível critical: dados reais de clientes).
