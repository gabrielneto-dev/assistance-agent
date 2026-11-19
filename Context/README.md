# Context/ — Manual da memória do projeto

`Context/` é a memória operacional persistente do projeto. Ela existe para que qualquer agente (Claude Code, Codex ou outro), em uma sessão nova e sem memória conversacional, consiga entender o projeto, recuperar só o contexto necessário e continuar o trabalho.

Princípio: **SESSION ≠ MEMORY**. A sessão é descartável; o conhecimento destilado fica aqui.

Regra de camadas:

```text
COMO trabalhar         → AGENTS.md (CLAUDE.md importa AGENTS.md)
O QUE se sabe          → Context/
O QUE se constrói      → Specs/ (specs, planos, tarefas, verificações — ver Specs/README.md)
Trabalho em curso      → sessão atual (temporária)
```

---

## 1. Estrutura

```text
Context/
├── README.md            # este manual
├── MAP.md               # L0 — roteador: pergunta → branch → índice → registro
├── STATE.md             # L0 — estado atual (não histórico)
├── _meta/
│   ├── config.yaml      # configuração da estratégia de contexto
│   ├── taxonomy.yaml    # tags canônicas, status, níveis de confiança
│   ├── catalog.jsonl    # índice derivado (1 linha por registro)
│   ├── changelog.md     # mudanças estruturais da memória
│   └── templates/       # modelos de registro
├── core/                # fundamentos estáveis: overview, goals, constraints, glossary
├── branches/<branch>/   # L1 _index.md + L2 registros por tipo
│   ├── _index.md
│   └── facts/ research/ decisions/ assumptions/ questions/ plans/ risks/ experiments/ notes/
├── global/              # registros transversais (decisions, assumptions, questions, plans, risks)
├── checkpoints/         # fotografias destiladas de sessões/marcos
├── sources/             # L3 — proveniência e evidências
├── future/              # ideias e possibilidades não aprovadas
└── archive/             # material histórico fora do conjunto ativo
```

Subpastas vazias são omitidas; crie-as quando o primeiro registro daquele tipo surgir.

## 2. Fontes de verdade

| Arquivo/pasta | Responde |
|---|---|
| `AGENTS.md` | Como os agentes devem trabalhar (regras permanentes) |
| `MAP.md` | Onde está cada tipo de informação |
| `STATE.md` | Onde o projeto está agora |
| `core/` | O que o projeto é, objetivos, restrições, vocabulário |
| `branches/*/_index.md` | Resumo e rotas de cada domínio |
| Registros atômicos (`.md` com frontmatter) | Conhecimento canônico detalhado |
| `sources/` | De onde veio a informação |
| `_meta/catalog.jsonl` | Índice derivado — **não** é fonte primária |
| `../Specs/` (raiz do projeto) | Specs, planos, tarefas, verificações e estado do desenvolvimento (`Specs/STATE.md`) |

`Context/` não duplica o conteúdo de `Specs/`: registros e checkpoints referenciam specs por ID (`SPEC-NNNN`, `SPEC-NNNN-TNNN`), e specs referenciam registros de contexto por `context_refs` (`CTX-...`).

Se o catálogo divergir dos arquivos Markdown, os arquivos vencem: reconstrua o catálogo (seção 19).

## 3. Níveis de contexto

| Nível | Conteúdo | Quando carregar |
|---|---|---|
| L0 | `MAP.md`, `STATE.md` | Sempre, em tarefa não trivial |
| L1 | `branches/<branch>/_index.md` | Para as branches relevantes |
| L2 | Registros atômicos | Quando a tarefa exigir o detalhe |
| L3 | `sources/`, datasets, resultados brutos | Só para evidência/validação |

Objetivo: máxima informação relevante com mínimo contexto carregado.

## 4. Tipos de registro

| Código | Tipo | Significado |
|---|---|---|
| FCT | fact | Informação considerada verdadeira no escopo atual |
| ASM | assumption | Hipótese usada para seguir sem confirmação completa |
| QUE | question | Pergunta aberta (elemento de primeira classe) |
| RES | research | Investigação: pergunta, fontes, achados, limitações |
| DEC | decision | Escolha tomada, com contexto, opções e motivo |
| PLN | plan | Trabalho previsto (`candidate` → `planned` → `in-progress` → `completed`/`cancelled`) |
| RSK | risk | Risco: causa, impacto, probabilidade, sinais, mitigação |
| EXP | experiment | Hipótese testada, setup, resultado, interpretação |
| NTE | note | Observação útil que não cabe em outro tipo |
| SRC | source | Proveniência: origem, data, confiabilidade |
| SUM | summary | Consolidação de vários registros |
| CP | checkpoint | Fotografia de continuidade de uma sessão/marco |

Separação epistemológica obrigatória: hipótese não é fato; pesquisa não é decisão; ideia futura não é plano aprovado.

### Conteúdo esperado por tipo

- **fact**: afirmação, escopo, evidência/`source_ids`; use `valid_from`/`valid_until`/`revisit_at` se puder mudar.
- **assumption**: Hipótese · Por que assumimos · O que depende dela · Como validar · Consequência se falsa.
- **question**: Pergunta · Por que importa · O que depende da resposta · Opções conhecidas · Como resolver. Ao responder: `status: answered`, seção "Resposta" com evidência, `resolved_by: CTX-...`. **Nunca apague perguntas.**
- **research**: pergunta investigada, escopo, fontes, data, evidências, achados, limitações, confiança, implicações, questões abertas.
- **decision**: Contexto · Problema · Opções consideradas · Decisão · Motivo · Consequências · Riscos · Registros relacionados.
- **plan**: objetivo, passos, status, dependências, critério de conclusão.
- **risk**: risco, causa, impacto, probabilidade, sinais, mitigação, owner, status.
- **experiment**: hipótese, setup, variável, condições, resultado, interpretação, limitações, artefatos (aponte para L3; não cole resultados brutos grandes).

Modelos em `_meta/templates/`.

## 5. Schema de metadados (YAML frontmatter)

```yaml
---
id: CTX-DEC-20261119-example-slug      # obrigatório, estável, único
type: decision                         # obrigatório
title: Título curto em português       # obrigatório
branch: agent-design                   # obrigatório (ou "global")
tags: [llm, architecture]              # obrigatório, tags canônicas
status: active                         # obrigatório (ver taxonomy.yaml)
created_at: 2026-11-19                 # obrigatório
updated_at: 2026-11-19                 # obrigatório
confidence: high                       # opcional: low | medium | high | verified
source_ids: []                         # opcional: CTX-SRC-...
related: []                            # opcional: IDs relacionados
depends_on: []                         # opcional: IDs dos quais depende
supersedes: null                       # opcional
superseded_by: null                    # opcional
resolved_by: null                      # opcional (questions)
priority: null                         # opcional (questions/plans/risks): critical | high | normal | low
valid_from: null                       # opcional (temporalidade)
valid_until: null
revisit_at: null
---
```

Relações usam **IDs**, nunca só caminhos de arquivo — IDs continuam válidos após reorganizações.

## 6. Nomenclatura

- Arquivo: `<TYPE>-<YYYYMMDD>-<slug-descritivo>.md` (ex.: `DEC-20261119-use-postgresql.md`).
- ID: `CTX-<TYPE>-<YYYYMMDD>-<slug>` (ex.: `CTX-DEC-20261119-use-postgresql`).
- Checkpoint: arquivo `CP-YYYYMMDD-HHMM-<slug>.md`, ID `CTX-CP-YYYYMMDD-HHMM-<slug>`.
- Sempre `kebab-case`, em inglês. Evite nomes genéricos (`novo.md`, `notes2.md`, `final-final.md`).
- A data é a de criação; não mude o ID se o arquivo for movido ou o título alterado.
- Antes de criar, verifique que o ID não existe (`rg "id: CTX-..." Context/`).

## 7. Tags

- Tags são índice transversal; formato `kebab-case`, em inglês.
- Antes de criar uma tag nova: procure equivalente em `_meta/taxonomy.yaml` e reutilize a forma canônica.
- Ao criar uma tag realmente nova, adicione-a a `taxonomy.yaml` no mesmo save.
- Evite sinônimos (`postgres`, `pg`, `postgresql` → escolha um).

## 8. Protocolo de recuperação

**Etapa A — Entender a solicitação.** Extraia objetivo, entidades, branches e tags prováveis, tipo de conhecimento necessário, restrições e temporalidade.

**Etapa B — Carregar L0.** Leia `MAP.md` e `STATE.md`. Não leia a pasta inteira.

**Etapa C — Selecionar branches.** Leia apenas os `_index.md` relevantes.

**Etapa D — Recuperação direcionada.** Busque por ID, título, tags, tipo, status, palavras-chave. Exemplos (não obrigatórios; use o mecanismo disponível):

```bash
rg "tags:.*llm" Context/
rg "type: decision" Context/branches/
rg "status: open" Context/
rg -l "CTX-QUE-20261119-tech-stack" Context/
```

Alternativa rápida: filtrar `_meta/catalog.jsonl` por `branch`, `type`, `tags`, `status`.

**Etapa E — Expansão por relações.** No registro encontrado, confira `related`, `depends_on`, `source_ids`, `supersedes`/`superseded_by` e siga apenas o necessário. Profundidade padrão: **1 salto**.

### Priorização de resultados

1. correspondência direta com a tarefa; 2. branch correspondente; 3. tags; 4. status ativo; 5. relações explícitas; 6. mais recente; 7. maior confiança; 8. melhor fonte; 9. validade temporal.

Registros `superseded`, `deprecated` ou `archived` não são estado atual — siga `superseded_by`.

### Orçamento de contexto

- `MAP.md` e `STATE.md`: pequenos. `_index.md`: resumo + rotas. Registros: detalhe. `sources/`: evidência.
- `_index.md` grande demais → compacte e mova detalhes para registros atômicos.
- Registro com vários assuntos independentes → divida e relacione por ID.
- Nunca duplique a decisão completa em MAP, STATE, índice e registro: cada camada tem profundidade diferente.

## 9. Política de escrita

```text
READ  = automático quando necessário
WRITE = controlado (gatilho explícito do usuário)
```

Fora do save, o agente pode corrigir um registro factualmente errado que esteja atrapalhando a tarefa, mas não deve criar documentação a cada mensagem.

**Exceção SDD (estreita):** quando, no planejamento de uma spec (`Specs/README.md` seção 8), o usuário confirmar uma decisão arquitetural durável, o agente registra imediatamente o `DEC` correspondente (registro + linha no catálogo + `_index.md` da branch) para que o plano possa citá-lo em `context_refs`. Nada mais em `Context/` é escrito por esse motivo — checkpoint, STATE e demais registros continuam esperando `salvar contexto`. A persistência automática do SDD acontece só em `Specs/`.

## 10. Context Save Protocol (`salvar contexto`)

Gatilhos (por intenção): `salvar contexto`, `salve o contexto`, `save context`, `persistir contexto`, `atualizar contexto`, `atualizar memória do projeto`, `criar checkpoint`, `checkpoint da sessão`.

**Não faça só um resumo da conversa.** Reconstrua semanticamente a sessão: objetivo, tarefas executadas, problemas e causas, tentativas relevantes, abordagens que falharam, soluções validadas, decisões e motivos, mudanças e arquivos afetados, testes e resultados, novos fatos, assumptions, perguntas abertas/respondidas, riscos, pendências, próximos passos, mudanças de estado, informações obsoletas, regras operacionais descobertas.

Use evidência do projeto, não só a memória da conversa: `git status`, `git diff`, `git log` e os próprios arquivos.

Inclua o estado do SDD: leia `Specs/STATE.md` e `Specs/INDEX.md` e registre no checkpoint (seção "Estado SDD") as specs ativas, fase, próxima tarefa e última verificação **por referência** (IDs e caminhos), sem copiar specs, planos ou tarefas. Se `Specs/STATE.md` estiver desatualizado em relação ao código, reconcilie-o primeiro (`Specs/README.md` seção 13).

### Pipeline

```text
SESSÃO
 → INSPECIONAR MUDANÇAS (git status/diff)
 → ANALISAR → DESTILAR → CLASSIFICAR (tipo correto)
 → DEDUPLICAR (atualizar existente > criar duplicado)
 → RELACIONAR (IDs)
 → CRIAR/ATUALIZAR REGISTROS ATÔMICOS
 → CRIAR CHECKPOINT
 → ATUALIZAR STATE.md
 → ATUALIZAR _index.md das branches afetadas
 → ATUALIZAR MAP.md (se surgiu branch/rota nova)
 → ATUALIZAR catalog.jsonl
 → ATUALIZAR _meta/changelog.md (só mudanças estruturais)
 → AVALIAR regras para AGENTS.md
 → VALIDAR (bash Context/_meta/validate.sh — IDs únicos, relações válidas, sem segredos)
```

### Filtro de persistência

> Um agente em uma nova sessão precisaria saber disso para continuar o projeto, evitar retrabalho ou tomar uma decisão melhor?

Não → descarte. Sim → classifique e persista.

Não salvar: cumprimentos, brainstorming descartado sem valor futuro, tentativas triviais, raciocínio redundante, texto literal da sessão.

### Destilação

Transforme conversa em conhecimento operacional: causa, consequência, decisão, evidência, solução, limitação, aprendizado, regra, estado. Cite literalmente só quando a citação tiver valor documental.

### Deduplicação

Antes de criar: procure assunto, tags, títulos semelhantes, IDs relacionados e branch. Se o conhecimento já existe, **atualize** o registro (e `updated_at`). Se a informação realmente mudou de sentido, use supersession (seção 12).

### Regras operacionais descobertas

Pergunta: "isto é uma instrução durável sobre COMO futuros agentes devem trabalhar?" (ex.: "usar pnpm", "rodar testes antes de alterar X"). Sim → `AGENTS.md`. Se for arquitetura, estado, decisão, pesquisa, fato, hipótese ou plano → `Context/`. Não transforme `AGENTS.md` em wiki.

## 11. Checkpoints

Cada save significativo cria `checkpoints/CP-YYYYMMDD-HHMM-<slug>.md` com as seções:

Objetivo · O que mudou · Decisões · Descobertas · Problemas resolvidos · Abordagens que falharam (vale lembrar) · Estado atual · Estado SDD (por referência) · Perguntas abertas · Próximos passos · Arquivos/artefatos afetados · Registros de contexto criados/atualizados.

O checkpoint é fotografia de continuidade e **não substitui** registros atômicos: conhecimento durável deve ir para o tipo correto. Após criá-lo, atualize `STATE.md` (`Latest checkpoint: ...`) e remova do STATE o que deixou de ser atual (já preservado em registros/checkpoints).

## 12. Supersession e arquivo

Não apague informação importante que deixou de valer.

- Registro antigo: `status: superseded`, `superseded_by: CTX-...`.
- Registro novo: `supersedes: CTX-...`.
- Material sem valor ativo mas com valor histórico → mover para `archive/` (mantendo o ID).

## 13. Fontes e proveniência

Quando o conhecimento vier de documentação externa, site, paper, API, reunião, arquivo, benchmark, experimento, usuário, dataset ou relatório, registre um `SRC` em `sources/` (origem, data, o que foi obtido, confiabilidade) e referencie via `source_ids`. Informação externa temporal (preços, versões, limites de API) nunca vira fato absoluto sem data/origem — use `valid_from`/`revisit_at`.

## 14. Conflitos

Não escolha silenciosamente. Compare data, status, escopo, origem, confiança, decisões posteriores e validade temporal. Se continuar ambíguo, crie/atualize uma `question` e registre o conflito em ambos os registros (`related`).

## 15. Conhecimento negativo

Falhas importantes são memória. Registre uma abordagem que falhou quando houver risco razoável de alguém repeti-la: abordagem, condição do teste, resultado, causa conhecida, quando tentar de novo. Formato útil: Problema · Investigação (o que **não** era a causa) · Solução validada · Evitar. Não persista erros triviais.

## 16. Segurança

Nunca persista valores de senha, token, API key, chave privada, cookie, segredo, credencial ou código de recuperação.

- Permitido: "A integração usa a variável `ANTHROPIC_API_KEY`."
- Proibido: o valor da variável.

Se encontrar um segredo em `Context/`: não o replique, remova/mascare e mantenha só a referência segura.

## 17. Temporalidade

Use `valid_from`, `valid_until`, `revisit_at` para preços, APIs, versões, modelos de LLM, benchmarks, fornecedores, métricas, dependências, legislação e planejamento.

## 18. Comandos semânticos

Intenções reconhecidas (sem parser formal):

| Intenção | Ação |
|---|---|
| `salvar contexto` | Context Save Protocol completo + checkpoint |
| `carregar contexto` | Ler explicitamente MAP, STATE e branches relevantes antes de continuar |
| `buscar contexto <assunto>` | Buscar por tags, títulos, conteúdo, IDs e relações; retornar primeiro os mais relevantes |
| `status do contexto` | Resumir estado atual, último checkpoint, branches, perguntas críticas, bloqueios |
| `auditar contexto` | Executar a auditoria (seção 20) |

## 19. Manutenção

### Adicionar uma branch

1. Confirme que é uma área de conhecimento relativamente independente (não crie branches artificiais).
2. Crie `branches/<nome-kebab>/_index.md` (propósito, escopo, estado, conceitos, registros importantes, decisões ativas, perguntas abertas, riscos, relações, rotas).
3. Adicione a branch ao `MAP.md` e ao `taxonomy.yaml` (campo `branches`).
4. Registre em `_meta/changelog.md`.

### Reconstruir o catálogo

`catalog.jsonl` tem uma linha JSON por registro com frontmatter `id:` (exceto README/índices):

```json
{"id":"...","type":"...","title":"...","branch":"...","tags":["..."],"status":"...","updated_at":"YYYY-MM-DD","path":"<relativo a Context/>"}
```

Para reconstruir: percorra todos os `.md` de `Context/` (exceto `README.md`, `MAP.md`, `STATE.md`, `_index.md`, `_meta/templates/`), leia o frontmatter e regenere o arquivo inteiro. Caminhos com `/`.

### Changelog

`_meta/changelog.md` registra só mudanças estruturais (branch criada/removida, migração de taxonomia, mudança de protocolo/schema, consolidações). Não é log de conversa.

## 20. Auditoria (`auditar contexto`)

Verifique e corrija preservando o histórico:

- IDs duplicados; IDs referenciados inexistentes; links quebrados;
- tags duplicadas/sinônimas ou fora da taxonomia;
- registros contraditórios; status incorretos; questions resolvidas ainda `open`;
- registros `superseded` apresentados como ativos;
- branches redundantes ou grandes demais; documentos grandes demais;
- registros sem classificação ou sem origem quando necessária;
- `MAP.md` desatualizado; `STATE.md` com histórico demais;
- `catalog.jsonl` divergente;
- instruções duplicadas entre `AGENTS.md` e `CLAUDE.md`;
- segredos persistidos acidentalmente.

### Validação automática

Grande parte dessas verificações é feita por `_meta/validate.sh` (somente leitura; requer Git Bash):

```bash
bash Context/_meta/validate.sh
```

Ele confere os blocos únicos `CONTEXT-ENGINEERING` e `SPEC-DRIVEN` em `AGENTS.md`, o import em `CLAUDE.md`, a estrutura e os IDs de `Specs/` (ver `Specs/README.md` seção 15), IDs únicos e coerentes com o nome do arquivo, referências `CTX-*` válidas, catálogo igual aos registros (IDs, paths, status), tags e branches presentes na taxonomia, `_index.md` em cada branch, segredos, arquivos obrigatórios e o checkpoint mais recente. Termina com `RESULT: PASS|FAIL` (código de saída 1 em falha). Rode-o ao final de todo `salvar contexto` e de toda auditoria; contradições, status semânticos e tamanho de documentos continuam sendo revisão manual.
