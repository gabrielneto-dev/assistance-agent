# assistance-agent — Instruções para agentes

Projeto de um assistente/agente de IA em código. O que o projeto sabe, decidiu e planeja fica em `Context/`; este arquivo diz apenas **como trabalhar**.

<!-- CONTEXT-ENGINEERING:START -->

# Sistema de contexto do projeto

Este projeto usa `Context/` como memória persistente e sistema de conhecimento. A sessão é descartável; o conhecimento do projeto fica nos arquivos.

## Descoberta de contexto

Para toda tarefa não trivial:

1. Leia `Context/MAP.md`.
2. Leia `Context/STATE.md`.
3. Determine quais branches de contexto são relevantes.
4. Leia apenas os `_index.md` dessas branches.
5. Recupere registros atômicos somente quando necessário.
6. Siga `related`, `depends_on`, `source_ids`, `supersedes` e `superseded_by` apenas quando afetarem materialmente a tarefa (padrão: 1 salto).
7. Não carregue recursivamente o diretório `Context/` inteiro.

Use carregamento progressivo (L0 → L1 → L2 → L3). Detalhes em `Context/README.md`.

## Fontes de verdade

- `AGENTS.md` — instruções operacionais permanentes.
- `Context/MAP.md` — roteamento e navegação do contexto.
- `Context/STATE.md` — estado atual do projeto.
- `Context/core/**` — fundamentos estáveis do projeto.
- `Context/branches/**` — conhecimento por domínio.
- `Context/global/**` — decisões, perguntas, hipóteses, riscos e planos transversais.
- `Context/checkpoints/**` — checkpoints destilados de sessões/marcos.
- `Context/sources/**` — proveniência e evidências.
- `Context/_meta/**` — configuração, taxonomia, catálogo e metadados de manutenção.

Registros com status `superseded`, `deprecated` ou `archived` não representam o estado atual: verifique o sucessor.

## Política de escrita de contexto

Ler contexto é automático em trabalho não trivial. Persistir contexto é controlado.

Não escreva documentação a cada mensagem da conversa.

Execute o **Context Save Protocol** quando o usuário expressar intenção equivalente a:

- `salvar contexto` / `salve o contexto` / `save context`
- `persistir contexto` / `atualizar contexto` / `atualizar memória do projeto`
- `criar checkpoint` / `checkpoint da sessão`

Reconheça a intenção, não a string exata. Ao ser acionado, siga `Context/README.md` (seção "Context Save Protocol"). Use `git status` / `git diff` como evidência do que realmente mudou.

Não copie a conversa literalmente. Persista conhecimento destilado e durável. Hipótese não é fato; pesquisa não é decisão; ideia não é plano aprovado.

## Segurança

Nunca persista senhas, tokens de acesso, API keys, chaves privadas, cookies de sessão ou valores de credenciais em `Context/`.

Referências a nomes de variáveis de ambiente ou locais em gerenciadores de segredos são permitidas.

## Manutenção

Se surgir uma regra operacional durável para todo o projeto (como trabalhar), avalie incluí-la neste arquivo.

Não coloque estado transitório nem conhecimento detalhado em `AGENTS.md`.

## Idioma

O conteúdo de `Context/` é escrito em português. Nomes de arquivo, IDs, chaves YAML, tipos e tags ficam em inglês (`kebab-case`).

<!-- CONTEXT-ENGINEERING:END -->
