# Objetivos

Última revisão: 2026-11-19 · Fonte: `CTX-DEC-20261119-multi-tenant-saas-product`

## Objetivos

- **Produto:** SaaS multi-tenant que atende os clientes de assistências técnicas pelo WhatsApp de forma humanizada, com IA, e depois organiza a loja (ordens de serviço, orçamentos) → `CTX-DEC-20261119-repair-shop-ai-attendant`.
- **Arquitetura:** núcleo do agente modular e independente de canal e de ambiente (local hoje, nuvem depois).
- **Processo (confirmado):** continuidade entre sessões de agentes via `Context/`; desenvolvimento por specs (`Specs/`, `CTX-DEC-20261119-adopt-sdd-with-context-engineering`).

## Não objetivos (por enquanto)

- Chat web próprio (não está entre as interfaces iniciais).
- Hospedagem em produção (execução local por enquanto).
- Ações externas sem confirmação do usuário.
- IA definindo valor final ou negociando preço (sempre com humano).

## Critérios de sucesso

*A detalhar por spec.* Mínimos já implícitos nas decisões:

- Nenhum dado, memória ou documento de um tenant acessível a outro.
- O mesmo código roda em Windows 11 e Linux Mint com `uv sync` + `uv run`.
- Nenhuma ação com efeito externo sem confirmação explícita.
- O cliente da loja recebe status e estimativas corretos, ou é transferido para um humano (`CTX-RSK-20261119-ai-wrong-quote-or-status`).
