# Context Map

Roteador: pergunta → branch → índice → registro. Não é a documentação completa. Manual: `README.md`.

## Projeto

- Visão geral: `core/overview.md`
- Objetivos: `core/goals.md`
- Restrições: `core/constraints.md`
- Glossário: `core/glossary.md`
- Estado atual: `STATE.md`

## Branches

### agent-design
Path: `branches/agent-design/`
Status: active (fase de definição)
Tags principais: agent-behavior, prompts, tools, memory

Rotas:
- Autonomia e memória do agente → `CTX-DEC-20261119-agent-autonomy-and-memory`
- Ferramentas concretas (aberto) → `CTX-QUE-20261119-agent-capabilities`

### integrations
Path: `branches/integrations/`
Status: active (fase de definição)
Tags principais: llm, external-apis, integrations

Rotas:
- Provedor/modelo de LLM → `CTX-QUE-20261119-llm-provider`
- Preços de LLM e embeddings (2026-11-19) → `CTX-RES-20261119-llm-provider-comparison`
- Integração com WhatsApp → `CTX-QUE-20261119-whatsapp-integration-method`
- Serviços externos → `branches/integrations/_index.md`

### infrastructure
Path: `branches/infrastructure/`
Status: active (fase de definição)
Tags principais: stack, runtime, deployment, tooling

Rotas:
- Linguagem e pacotes (Python + uv) → `CTX-DEC-20261119-python-uv-stack`
- Framework, banco, vetores (aberto) → `CTX-QUE-20261119-tech-stack`
- Onde roda (local, Windows + Linux Mint) → `CTX-DEC-20261119-local-cross-platform-runtime`
- Estado do repositório → `CTX-FCT-20261119-repository-initialized`
- Script de validação (uso e armadilhas) → `CTX-NTE-20261119-validate-script-pitfalls`
- Layout em camadas e ferramentas de qualidade → `CTX-DEC-20261119-layered-package-and-quality-tooling`
- Defender bloqueia `.exe` do `.venv` (usar `python -m`) → `CTX-FCT-20261119-windows-asr-blocks-venv-exes`
- Armadilhas do ferramental Python → `CTX-NTE-20261119-python-tooling-pitfalls`

## Desenvolvimento (SDD) — `Specs/` na raiz do projeto

- Specs, planos, tarefas e verificações: `Specs/features/` (manual `Specs/README.md`)
- Funcionalidades registradas: `Specs/INDEX.md`
- Estado operacional do desenvolvimento: `Specs/STATE.md`

## Transversal (`global/`)

- Ideia do produto (atendente de IA para assistências técnicas) → `CTX-DEC-20261119-repair-shop-ai-attendant`
- Formato do produto (SaaS multi-tenant, API/CLI/WhatsApp) → `CTX-DEC-20261119-multi-tenant-saas-product`
- Loja piloto → `CTX-QUE-20261119-pilot-shop`
- Riscos transversais → `global/risks/`
- Processo de desenvolvimento (SDD + contexto) → `CTX-DEC-20261119-adopt-sdd-with-context-engineering`
- Decisões transversais → `global/decisions/`
- Hipóteses gerais → `global/assumptions/`

## Continuidade e evidência

- Checkpoints: `checkpoints/` (o mais recente está em `STATE.md`)
- Fontes: `sources/`
- Ideias não aprovadas: `future/`
- Histórico inativo: `archive/`
- Índice de registros: `_meta/catalog.jsonl` · Tags: `_meta/taxonomy.yaml`
