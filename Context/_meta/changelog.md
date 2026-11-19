# Context changelog

Somente mudanças estruturais da memória (branches, taxonomia, protocolo, schema, consolidações). Não é log de conversa.

## 2026-11-19 — Bootstrap da arquitetura de contexto

- Criados `AGENTS.md` (bloco `CONTEXT-ENGINEERING`) e `CLAUDE.md` (`@AGENTS.md`).
- Criada a estrutura `Context/` (README, MAP, STATE, `_meta/`, `core/`, `global/`, `checkpoints/`, `sources/`, `future/`, `archive/`).
- Branches iniciais: `agent-design`, `integrations`, `infrastructure`.
- Taxonomia v1 e schema de frontmatter v1.
- Checkpoint: `CTX-CP-20261119-0928-context-bootstrap`.
- Adicionado `_meta/validate.sh` (validação estrutural somente leitura), referenciado no README (pipeline do save e auditoria).
