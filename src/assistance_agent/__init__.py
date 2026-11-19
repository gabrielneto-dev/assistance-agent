"""assistance-agent: atendente de IA no WhatsApp para assistências técnicas (SaaS multi-tenant).

Camadas: `core` (domínio) → `ports` (interfaces) ← `adapters` (implementações);
`interfaces` (CLI, futuramente API e WhatsApp) ligam tudo via `config`.
"""
