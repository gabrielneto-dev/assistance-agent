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
- Capacidades, ferramentas e memória do agente → `branches/agent-design/_index.md`
- Pergunta aberta sobre capacidades → `CTX-QUE-20261119-agent-capabilities`

### integrations
Path: `branches/integrations/`
Status: active (fase de definição)
Tags principais: llm, external-apis, integrations

Rotas:
- Provedor/modelo de LLM → `CTX-QUE-20261119-llm-provider`
- Serviços externos → `branches/integrations/_index.md`

### infrastructure
Path: `branches/infrastructure/`
Status: active (fase de definição)
Tags principais: stack, runtime, deployment, tooling

Rotas:
- Linguagem/framework/pacotes → `CTX-QUE-20261119-tech-stack`
- Onde o agente roda → `CTX-QUE-20261119-deployment-target`
- Estado do repositório → `CTX-FCT-20261119-repository-initialized`

## Transversal (`global/`)

- Escopo e usuários do projeto → `CTX-QUE-20261119-project-scope-and-users`
- Hipóteses gerais → `global/assumptions/`

## Continuidade e evidência

- Checkpoints: `checkpoints/` (o mais recente está em `STATE.md`)
- Fontes: `sources/`
- Ideias não aprovadas: `future/`
- Histórico inativo: `archive/`
- Índice de registros: `_meta/catalog.jsonl` · Tags: `_meta/taxonomy.yaml`
