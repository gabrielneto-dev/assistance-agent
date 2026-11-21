---
id: SPEC-0001
type: spec
title: Esqueleto do projeto — núcleo multi-tenant, portas de LLM/embeddings fake e CLI
status: done
phase: complete
level: full
priority: high
created_at: 2026-11-19
updated_at: 2026-11-19
dependencies: []
context_refs:
  - CTX-DEC-20261119-multi-tenant-saas-product
  - CTX-DEC-20261119-agent-autonomy-and-memory
  - CTX-DEC-20261119-python-uv-stack
  - CTX-DEC-20261119-local-cross-platform-runtime
  - CTX-DEC-20261119-layered-package-and-quality-tooling
  - CTX-QUE-20261119-llm-provider
  - CTX-RES-20261119-llm-provider-comparison
approved_by: null
supersedes: null
superseded_by: null
---

# SPEC-0001 — Esqueleto do projeto

## Problem

O repositório não tem código. Toda funcionalidade futura (API, WhatsApp, RAG, provedores reais de LLM) precisa de uma base comum. Essa base deve:

- isolar cada tenant;
- esconder o provedor de LLM e de embeddings atrás de interfaces, porque o provedor ainda não foi escolhido;
- rodar igual no Windows 11 e no Linux Mint.

## Objective

Criar o projeto Python executável com:

- as quatro camadas (`core`, `ports`, `adapters`, `interfaces`);
- contexto de tenant obrigatório e histórico de conversa isolado por tenant;
- portas de LLM e de embeddings com implementações fake;
- uma CLI mínima de conversa que usa o LLM fake;
- portões de qualidade automatizados.

Tudo sem rede e sem credenciais.

## Scope

- `pyproject.toml` e `uv.lock`, com Python ≥ 3.13.
- Estrutura do pacote `src/assistance_agent/` em camadas.
- Domínio: identificador de tenant, mensagens, conversa e serviço de conversa.
- Portas: LLM, embeddings e armazenamento de histórico. Adapters: LLM fake, embeddings fake e histórico em memória.
- Configuração por variáveis de ambiente, com `.env.example` listando só os nomes.
- CLI `assistance-agent`.
- pytest, ruff, mypy e pre-commit configurados; `.gitignore`; LF para `*.py`.

## Out of Scope

- Provedores reais de LLM e embeddings (decisão pendente em `CTX-QUE-20261119-llm-provider`).
- RAG (indexação e busca), memória persistente entre conversas e banco de dados.
- API HTTP, bot de WhatsApp, autenticação e autorização.
- Ferramentas do agente e fluxo de confirmação de ações externas.
- Hospedagem, CI e observabilidade.

## Functional Requirements

- **REQ-001** — O projeto se instala com `uv sync` e roda com `uv run python -m assistance_agent`, que é a forma portável. O script `assistance-agent` também é instalado. O lockfile é versionado. *(Alterado em 2026-11-19; ver Change Log.)*
- **REQ-002** — O código fica em `src/assistance_agent/`, nas camadas `core`, `ports`, `adapters` e `interfaces`. `core` e `ports` não importam `adapters` nem `interfaces`.
- **REQ-003** — Toda operação de conversa exige um `TenantId` explícito e válido. Não existe tenant padrão nem global. Um identificador vazio ou fora do formato permitido é rejeitado com erro de domínio.
- **REQ-004** — O histórico é armazenado por (tenant, conversa). Uma operação feita com o tenant A nunca lê nem altera o histórico do tenant B, mesmo com o mesmo ID de conversa.
- **REQ-005** — A porta de LLM recebe o histórico e devolve a resposta do assistente. O adapter fake é determinístico e não usa rede.
- **REQ-006** — A porta de embeddings recebe textos e o tipo de entrada (`query` | `document`). Ela devolve vetores de dimensão fixa, junto com o identificador do modelo que os gerou. O adapter fake é determinístico (texto igual → vetor igual) e não usa rede.
- **REQ-007** — `assistance-agent chat --tenant <id>` abre uma conversa interativa no terminal usando o serviço de conversa. A conversa termina com `/sair` ou com fim de entrada (EOF). `--message "<texto>"` envia uma única mensagem, imprime a resposta e encerra.
- **REQ-008** — O adapter de LLM é escolhido pela variável `ASSISTANCE_AGENT_LLM_PROVIDER`; o padrão é `fake`. Um valor desconhecido gera um erro claro que lista os valores aceitos. `.env.example` lista as variáveis sem valores secretos, e `.env` não é versionado.

## Non-Functional Requirements

- **REQ-009** — Os mesmos comandos (`uv sync`, `uv run python -m pytest`, `uv run python -m assistance_agent ...`) funcionam no Windows 11 e no Linux Mint. Não há caminhos absolutos nem scripts exclusivos de PowerShell ou Bash.
- **REQ-010** — Os portões de qualidade passam:
  - `uv run python -m pytest`;
  - `uv run python -m ruff check`;
  - `uv run python -m ruff format --check`;
  - `uv run python -m mypy` em modo estrito sobre `src/`.

  O pre-commit (`uv run python -m pre_commit`) roda ruff e mypy pelo ambiente do uv.
- **REQ-011** — Os testes e a CLI com adapters fake não fazem chamadas de rede e não exigem credenciais.
- **REQ-012** — `.gitignore` cobre Python, uv e `.env`. `.gitattributes` força LF em `*.py`.

## Business Rules

- O tenant é sempre explícito; nada é inferido de estado global.
- Formato do `TenantId` (hipótese A1): 1–64 caracteres em `[a-z0-9-]`, começando por letra ou dígito.

## User Scenarios

1. O desenvolvedor clona o repositório numa das duas máquinas, roda `uv sync` e depois `uv run python -m assistance_agent chat --tenant demo`. Ele conversa com o assistente fake.
2. O desenvolvedor roda os portões de qualidade antes de commitar; o pre-commit bloqueia o commit se algum deles falhar.

## Inputs and Outputs

- **CLI:**
  - entrada: `--tenant` (obrigatório), `--conversation` (opcional, padrão `default`), `--message` (opcional), stdin no modo interativo;
  - saída: a resposta em stdout e os erros em stderr, com código de saída ≠ 0.
- **LLM fake:** responde de forma determinística a partir da última mensagem do usuário. Exemplo: `"[fake] você disse: <texto>"`.

## Error Scenarios and Edge Cases

- `--tenant` ausente ou inválido → mensagem de erro e código de saída 2.
- `ASSISTANCE_AGENT_LLM_PROVIDER` desconhecido → mensagem de erro com os valores aceitos e código ≠ 0.
- Mensagem vazia no modo interativo → ignorada, sem chamar o LLM.
- EOF (Ctrl+D / Ctrl+Z) → encerra a conversa sem traceback.

## Acceptance Criteria

- **AC-001** (REQ-001) — Given um clone limpo com uv instalado, when `uv sync` e `uv run python -m assistance_agent --help` são executados, then ambos terminam com código 0 e a ajuda lista o subcomando `chat`.
- **AC-002** (REQ-002) — Given o pacote, when o teste de arquitetura inspeciona os imports de `core` e `ports`, then nenhum importa `assistance_agent.adapters` nem `assistance_agent.interfaces`.
- **AC-003** (REQ-003) — Given um identificador vazio, com maiúsculas, com espaço ou com mais de 64 caracteres, when um `TenantId` é criado, then é lançado um erro de domínio. Given um identificador válido, then a criação funciona.
- **AC-004** (REQ-004) — Given as conversas `c1` dos tenants `a` e `b`, cada uma com mensagens próprias, when o histórico de `a/c1` é lido, then só aparecem as mensagens de `a`.
- **AC-005** (REQ-005) — Given o histórico `[user: "oi"]`, when o LLM fake é chamado duas vezes, then as duas respostas são iguais e não há nenhuma chamada de rede.
- **AC-006** (REQ-006) — Given os textos `["x", "x", "y"]`, when o fake de embeddings os processa, then os vetores de `"x"` são iguais entre si e diferentes do de `"y"`, todos têm a mesma dimensão, e o resultado informa o identificador do modelo.
- **AC-007** (REQ-007) — Given `uv run python -m assistance_agent chat --tenant demo --message "oi"`, when executado, then imprime a resposta fake e sai com 0. Given o modo interativo com a entrada `"oi\n/sair\n"`, then imprime uma resposta e sai com 0.
- **AC-008** (REQ-007) — Given `--tenant "Inválido!"` ou `--tenant` ausente, when a CLI é executada, then o erro vai para stderr e o código de saída é 2.
- **AC-009** (REQ-008) — Given `ASSISTANCE_AGENT_LLM_PROVIDER=inexistente`, when a CLI é executada, then a mensagem lista os valores aceitos e o código é ≠ 0. Given a variável ausente, then o adapter usado é o fake.
- **AC-010** (REQ-009) — Given o Windows 11 e o Linux Mint, when `uv sync`, `uv run python -m pytest` e o AC-007 são executados em cada máquina, then todos passam.
- **AC-011** (REQ-010) — Given o repositório, when os quatro comandos de qualidade são executados, then todos terminam com código 0. Given `uv run python -m pre_commit run --all-files`, then também passa.
- **AC-012** (REQ-011) — Given a suíte de testes, when executada com a rede bloqueada para sockets (verificação dentro dos testes), then passa sem nenhuma variável de credencial definida.
- **AC-013** (REQ-012) — Given `git check-ignore .env .venv` e `git check-attr eol -- src/assistance_agent/__init__.py`, when executados, then os dois caminhos aparecem como ignorados e o atributo é `eol: lf`.

## Dependencies

- Ferramenta **uv** instalada nas duas máquinas. Em 2026-11-19 o uv **não está instalado** no Windows (`uv: command not found`).

## Assumptions

- **A1** — O formato do `TenantId` acima é suficiente até existir autenticação. É reversível.
- **A2** — Ports assíncronas (`async`) desde já, pensando na API HTTP e no webhook do WhatsApp. Decisão local do plano.
- **A3** — A CLI usa `argparse` (biblioteca padrão) para evitar dependência extra. Decisão local, reversível.

## Open Questions

- Nenhuma bloqueante.

## Risks

- O isolamento por tenant aqui é só lógico (em memória). Quando houver dados reais, autenticação ou banco, a spec que os trouxer deve ser de nível **critical**.
- Hooks do pre-commit que baixam código da internet são evitados: os hooks são locais e usam `uv run`.

## Context References

- `CTX-DEC-20261119-multi-tenant-saas-product` — isolamento por tenant desde o primeiro código.
- `CTX-DEC-20261119-agent-autonomy-and-memory` — histórico de conversa (as outras camadas de memória ficam fora daqui).
- `CTX-DEC-20261119-python-uv-stack`, `CTX-DEC-20261119-layered-package-and-quality-tooling` — stack, layout e qualidade.
- `CTX-DEC-20261119-local-cross-platform-runtime` — portabilidade entre Windows e Linux Mint.
- `CTX-QUE-20261119-llm-provider`, `CTX-RES-20261119-llm-provider-comparison` — motivo das portas com fake.

## Change Log

- 2026-11-19 — Spec concluída: AC-010 verificado no Linux Mint 22.3 (V-008); todos os AC em PASS.
- 2026-11-19 — REQ-001, REQ-009, REQ-010 e os AC correspondentes passam a usar `uv run python -m <módulo>`. Motivo: no Windows de desenvolvimento, uma regra de redução de superfície de ataque do Microsoft Defender, gerenciada pela TI (ID `01443614-CD74-433A-B99E-2ECDC07BFC25`), bloqueia os lançadores `.exe` que o uv cria em `.venv/Scripts` (`assistance-agent.exe`, `pytest.exe` etc.). `python -m` funciona nas duas máquinas e não depende desses lançadores. A política não foi alterada.
- 2026-11-19 — Spec criada. Escopo confirmado pelo usuário: núcleo + CLI fake, um pacote em camadas, pytest/ruff/mypy/pre-commit, Python 3.13.
