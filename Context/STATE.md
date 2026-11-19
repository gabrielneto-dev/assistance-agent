# Project State

Last updated: 2026-11-19
Latest checkpoint: `Context/checkpoints/CP-20261119-0928-context-bootstrap.md` (`CTX-CP-20261119-0928-context-bootstrap`)

## Objetivo atual

Definir os fundamentos do assistente de IA (escopo, stack, provedor de LLM, ambiente de execução) antes de escrever código.

Estado do desenvolvimento (specs, tarefas, verificações): `Specs/STATE.md`.

## Funcionando

- Repositório git em `main`, só local (sem remoto).
- Sistema de contexto instalado: `AGENTS.md`, `CLAUDE.md`, `Context/`.
- Sistema SDD instalado: `Specs/` (nenhuma spec ainda).

## Em andamento

- Nada além da definição inicial do projeto.

## Bloqueios

- Não há código nem decisões técnicas: todo o trabalho de implementação depende das perguntas críticas abaixo.
- Não existe `.gitignore`; criar quando a stack for definida.

## Decisões ativas

- Nenhuma decisão técnica registrada ainda.
- Convenção do contexto: conteúdo em português; arquivos, IDs, tags em inglês.

## Perguntas críticas em aberto

- Escopo e usuários do assistente → `CTX-QUE-20261119-project-scope-and-users`
- Stack técnica → `CTX-QUE-20261119-tech-stack`
- Provedor/modelo de LLM → `CTX-QUE-20261119-llm-provider`
- Capacidades/ferramentas do agente → `CTX-QUE-20261119-agent-capabilities`
- Ambiente de execução/deploy → `CTX-QUE-20261119-deployment-target`

## Próximos passos prováveis

1. Responder escopo e usuários (define o resto).
2. Decidir stack e provedor de LLM (registrar como `decision`).
3. Primeira funcionalidade via `iniciar spec` (`Specs/README.md`); criar estrutura do código e `.gitignore` da stack.
4. `salvar contexto` ao fim da sessão de definição.
