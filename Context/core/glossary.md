# Glossário

Última revisão: 2026-11-19

## Sistema de contexto

| Termo | Significado |
|---|---|
| Branch | Área relativamente independente de conhecimento em `Context/branches/` |
| Registro atômico | Arquivo `.md` com frontmatter tratando de um único assunto |
| L0–L3 | Níveis de carregamento: global (MAP/STATE) → branch (`_index.md`) → registros → fontes |
| Checkpoint | Fotografia destilada de uma sessão/marco em `Context/checkpoints/` |
| Supersession | Substituição de um registro por outro (`supersedes`/`superseded_by`) sem apagar o antigo |
| Salvar contexto | Gatilho do Context Save Protocol (ver `Context/README.md`) |

## Desenvolvimento (SDD)

| Termo | Significado |
|---|---|
| SDD | Spec-Driven Development — protocolo em `Specs/README.md` |
| Spec | Especificação de uma funcionalidade, `SPEC-NNNN`, em `Specs/features/` |
| REQ / AC | Requisito (`REQ-NNN`) e critério de aceitação (`AC-NNN`) dentro de uma spec |
| Tarefa | Passo rastreável `SPEC-NNNN-TNNN` em `tasks.md` |
| Nível | Rigor do SDD: trivial, lightweight, full, critical |

## Domínio do projeto

| Termo | Significado |
|---|---|
| Agente / assistente | O software que este projeto constrói. SaaS multi-tenant de assistente de IA (`CTX-DEC-20261119-multi-tenant-saas-product`) |
| LLM | Modelo de linguagem usado pelo agente |
| Ferramenta (tool) | Ação externa que o agente pode invocar |
| Tenant | Loja de assistência técnica que assina o SaaS; dados, memória, base de conhecimento e configurações isolados por tenant |
| Cliente final | Cliente da loja, que conversa com o atendente pelo WhatsApp |
| OS | Ordem de serviço: registro de um reparo (cliente, aparelho, defeito, status, orçamento) |
| Transferência para humano | Passagem da conversa da IA para um atendente da loja |
| RAG | Busca em documentos do tenant para fundamentar respostas (base de conhecimento) |
