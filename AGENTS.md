# assistance-agent — Instruções para agentes

Projeto de um assistente/agente de IA em código. O que o projeto sabe, decidiu e planeja fica em `Context/`; o que está sendo construído (specs, planos, tarefas, verificações) fica em `Specs/`; este arquivo diz apenas **como trabalhar**.

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

Após alterar `Context/` ou `Specs/`, rode `bash Context/_meta/validate.sh` (Git Bash) e corrija o que falhar.

Se surgir uma regra operacional durável para todo o projeto (como trabalhar), avalie incluí-la neste arquivo.

Não coloque estado transitório nem conhecimento detalhado em `AGENTS.md`.

## Idioma

O conteúdo de `Context/` é escrito em português. Nomes de arquivo, IDs, chaves YAML, tipos e tags ficam em inglês (`kebab-case`).

<!-- CONTEXT-ENGINEERING:END -->

<!-- SPEC-DRIVEN:START -->

# Spec-Driven Development (SDD)

Desenvolvimento segue `Specs/README.md` (protocolo completo). Resumo obrigatório:

1. **Descubra antes de agir.** Em tarefa de desenvolvimento não trivial, após `Context/MAP.md` e `Context/STATE.md`, leia `Specs/INDEX.md` e `Specs/STATE.md`. Procure spec existente antes de criar outra; mudança em funcionalidade existente atualiza a spec dela.
2. **Classifique a complexidade** pelo impacto real: `trivial` (sem spec), `lightweight` (`spec.md` único), `full` (spec + plan + tasks + verification), `critical` (full + riscos, rollback e aprovação do usuário em `approved_by`). Na dúvida, o nível maior.
3. **Não implemente mudanças significativas** sem requisitos (`REQ`), critérios de aceitação testáveis (`AC`) e plano suficientes. Não invente requisitos nem amplie o escopo silenciosamente.
4. **Siga as tarefas** (`SPEC-NNNN-TNNN`) e seus critérios de conclusão. Bloqueio → `blocked`, nunca `completed`.
5. **Verifique** contra os AC e registre o resultado real (`PASS|FAIL|BLOCKED|NOT_RUN|NOT_APPLICABLE`). Código escrito não é funcionalidade pronta.
6. **Persista o progresso automaticamente**, durante o trabalho, nos eventos de `Specs/README.md` seção 11 (tarefas, verificação, `Specs/STATE.md`, `Specs/INDEX.md`). Isso vale só para `Specs/`; `Context/` continua sob a política de escrita controlada (exceção: decisões duráveis confirmadas no planejamento viram `DEC`).
7. **Após reset de sessão**, retome por `Specs/STATE.md` e reconcilie o estado documentado com o código e o git antes de continuar.
8. **Sem commit/push automático**, sem ações destrutivas, irreversíveis ou em produção sem autorização explícita, sem segredos em `Specs/`.

Intenções: `iniciar spec`, `planejar spec`, `gerar tarefas`, `implementar spec`, `validar spec`, `status sdd`, `retomar desenvolvimento`, `auditar sdd`.

<!-- SPEC-DRIVEN:END -->

# Convenções de desenvolvimento

- Python gerenciado com **uv**: `uv add` para dependências, `uv run` para executar, `uv sync` para instalar. Não use `pip install` direto.
- O projeto é desenvolvido em Windows 11 e Linux Mint: código, scripts e comandos documentados devem funcionar nos dois (use `pathlib`, nada de caminhos absolutos; scripts de projeto em Python via `uv run`, não só PowerShell ou só Bash).
- Execute ferramentas sempre como **`uv run python -m <módulo>`**, nunca pelos `.exe` de `.venv/Scripts`: no Windows de desenvolvimento uma regra ASR do Defender, gerenciada pela TI, bloqueia esses executáveis. Não tente contornar nem alterar a política.
- Portões de qualidade (todos devem passar antes de commitar; o pre-commit roda ruff e mypy):

  ```text
  uv run python -m pytest
  uv run python -m ruff check
  uv run python -m ruff format --check
  uv run python -m mypy
  ```

- Rodar a CLI: `uv run python -m assistance_agent chat --tenant <id> [--message "<texto>"]`.
- Camadas em `src/assistance_agent/`: `core` e `ports` nunca importam `adapters` nem `interfaces` (`tests/test_architecture.py` garante isso).
- Testes não acessam a rede (fixture em `tests/conftest.py`); use os adapters fake.
