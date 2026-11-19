# Visão geral

Última revisão: 2026-11-19 · Fontes: `CTX-SRC-20261119-user-bootstrap-answers`, `CTX-SRC-20261119-user-definition-answers`

## O que é

`assistance-agent` é um **SaaS multi-tenant de atendimento por IA para assistências técnicas de eletrônicos** (`CTX-DEC-20261119-repair-shop-ai-attendant`, `CTX-DEC-20261119-multi-tenant-saas-product`):

- **Cliente (tenant):** a loja de assistência. **Usuário final:** o cliente da loja, no WhatsApp.
- **Dor e diferencial:** a loja é desorganizada; o diferencial é o atendimento humanizado por IA.
- **Primeiro caso de uso:** responder clientes no WhatsApp (status do reparo, estimativa de orçamento, informações da loja, aprovação de orçamento), passando para um humano quando necessário. A gestão da loja (ordens de serviço etc.) cresce depois.
- **Interfaces iniciais:** API, CLI e bot de WhatsApp, como adaptadores sobre um núcleo comum.
- **Comportamento:** responde livremente; ações com efeito externo pedem confirmação. Memória de conversa, persistente e RAG, isoladas por tenant (`CTX-DEC-20261119-agent-autonomy-and-memory`).
- **Stack:** Python + uv (`CTX-DEC-20261119-python-uv-stack`), rodando localmente por enquanto, portável entre Windows 11 e Linux Mint (`CTX-DEC-20261119-local-cross-platform-runtime`).

Fase atual: esqueleto implementado (`SPEC-0001`: núcleo multi-tenant, portas de LLM e embeddings com fakes, CLI). Não há provedor real nem integração com WhatsApp ainda (`CTX-FCT-20261119-repository-initialized`).

## Componentes previstos (áreas de conhecimento)

- **Design do agente** — comportamento, prompts, ferramentas, memória → `branches/agent-design/`
- **Integrações** — provedor de LLM, WhatsApp, serviços externos → `branches/integrations/`
- **Infraestrutura** — stack, runtime, deploy, tooling → `branches/infrastructure/`

## Ainda indefinido

- Provedor/modelo de LLM → `CTX-QUE-20261119-llm-provider`
- Meio de integração com WhatsApp → `CTX-QUE-20261119-whatsapp-integration-method`
- Framework da API, banco, armazenamento vetorial → `CTX-QUE-20261119-tech-stack`
- Ferramentas concretas do agente e confirmação por canal → `CTX-QUE-20261119-agent-capabilities`
- Hospedagem do SaaS (adiada; hoje é local)
- Loja piloto e dados reais → `CTX-QUE-20261119-pilot-shop`
- Hipótese em uso: projeto de um único desenvolvedor → `CTX-ASM-20261119-single-developer-project`
