# Specs/ — Spec-Driven Development (SDD)

`Specs/` guarda o trabalho de desenvolvimento: especificações, planos, tarefas e evidências de verificação. Tudo aqui sobrevive à perda total da conversa: **NEW SESSION = ZERO CONVERSATIONAL MEMORY**.

---

## 1. Fontes de verdade

| Componente | Responsabilidade |
|---|---|
| `AGENTS.md` | Regras permanentes (bloco `SPEC-DRIVEN` = resumo deste manual) |
| `CLAUDE.md` | Importa `AGENTS.md`; sem regras SDD próprias |
| `Context/` | Conhecimento, decisões (`DEC`), perguntas, pesquisas, checkpoints |
| `Specs/` | O que construir (spec), como (plan), passos (tasks), prova (verification) |
| Código-fonte | O que **está** implementado — não prova que os requisitos foram atendidos |
| Sessão | Memória de trabalho temporária |

Regras de fronteira:

- Decisões arquiteturais duráveis ficam em `Context/` como registros `DEC`; specs e planos apontam para elas via `context_refs` (IDs `CTX-...`). Não copie o conteúdo.
- Perguntas que afetam só uma spec ficam na seção "Open Questions" da spec. Perguntas de alcance do projeto ficam em `Context/` (`QUE`).
- O estado operacional detalhado do SDD fica em `Specs/STATE.md`. `Context/STATE.md` só aponta para ele.

## 2. Estrutura

```text
Specs/
├── README.md        # este manual
├── INDEX.md         # registro de todas as specs + próximo ID livre
├── STATE.md         # estado operacional atual do SDD (compacto)
├── _meta/
│   ├── config.yaml  # política SDD (declarações, não automação)
│   └── templates/   # spec, plan, tasks, verification, lightweight
├── features/        # criada com a primeira spec
│   └── SPEC-0001--<slug>/
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       ├── verification.md
│       └── [artefatos opcionais]
└── archive/         # criada quando a primeira spec for arquivada
```

Não crie diretórios vazios nem documentos sem uso. Uma spec de nível 1 (lightweight) usa **só** `spec.md` (template `lightweight.md`).

## 3. Identificação

| Item | Formato | Exemplo | Escopo |
|---|---|---|---|
| Spec (funcionalidade) | `SPEC-NNNN` | `SPEC-0001` | Global, sequencial |
| Pasta da spec | `SPEC-NNNN--<slug-kebab>` | `SPEC-0001--chat-cli` | — |
| Plano / tarefas / verificação | `SPEC-NNNN-PLAN`, `-TASKS`, `-VER` | `SPEC-0001-PLAN` | Documento |
| Requisito | `REQ-NNN` | `REQ-003` | Dentro da spec |
| Critério de aceitação | `AC-NNN` | `AC-002` | Dentro da spec |
| Tarefa | `SPEC-NNNN-TNNN` | `SPEC-0001-T004` | Global |
| Verificação | `V-NNN` | `V-007` | Dentro de `verification.md` |

- Referência global a requisito: `SPEC-0001/REQ-003`.
- IDs nunca são reutilizados. `INDEX.md` guarda o **próximo ID livre**; IDs cancelados continuam listados.
- Requisitos removidos não são apagados: marque `~~REQ-004~~ (removido em AAAA-MM-DD: motivo)`.

### Metadados (YAML frontmatter)

```yaml
---
id: SPEC-0001
type: spec                  # spec | plan | tasks | verification
title: Título curto
status: draft               # ver seção 5
phase: specify              # só em spec.md; ver seção 4
level: full                 # trivial | lightweight | full | critical
priority: normal            # critical | high | normal | low
created_at: 2026-11-19
updated_at: 2026-11-19
dependencies: []            # outras SPEC-NNNN
context_refs: []            # IDs CTX-... relevantes (DEC, QUE, FCT...)
approved_by: null           # obrigatório no nível critical antes de implementar: "user AAAA-MM-DD"
supersedes: null
superseded_by: null
---
```

`plan.md`, `tasks.md` e `verification.md` usam `id: SPEC-NNNN-PLAN|TASKS|VER`, `spec: SPEC-NNNN`, `status`, datas e, quando útil, `context_refs`.

## 4. Ciclo SDD

```text
REQUEST → DISCOVER CONTEXT → CLASSIFY → SPECIFY → PLAN → DECOMPOSE TASKS
        → IMPLEMENT → VERIFY → RECONCILE → PERSIST STATE
```

O campo `phase` da spec registra onde ela está: `specify` → `plan` → `tasks` → `implement` → `verify` → `complete`.

| Fase | Resultado observável |
|---|---|
| Discover | MAP/STATE de `Context/` e `Specs/` lidos; spec existente localizada ou confirmado que não existe |
| Classify | Nível registrado em `level` (ou decisão de nível 0 sem spec) |
| Specify | `spec.md` com REQ e AC testáveis |
| Plan | `plan.md` baseado na arquitetura real; decisões duráveis em `Context/` |
| Tasks | `tasks.md` com tarefas pequenas ligadas a REQ |
| Implement | Código alterado + tarefa atualizada com o resultado observado |
| Verify | `verification.md` com PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE por AC |
| Reconcile | Divergências corrigidas ou registradas (seção 11) |
| Persist | `tasks.md`, `verification.md`, `Specs/STATE.md`, `INDEX.md` atualizados |

**Implementação iniciada não é implementação concluída.**

## 5. Estados

**Spec (`status`)**: `draft` (escrevendo) · `ready` (requisitos e plano suficientes para implementar) · `in_progress` · `blocked` · `done` · `cancelled` · `superseded`.

**Plano**: `draft` · `ready` · `superseded`.

**Tarefa**: `pending` · `ready` (dependências resolvidas) · `in_progress` · `blocked` · `completed` · `cancelled`.

**Verificação**: `PASS` · `FAIL` · `BLOCKED` · `NOT_RUN` · `NOT_APPLICABLE`.

Uma spec só passa a `done` pelos critérios da seção 12.

## 6. Classificação de complexidade

Classifique pelo **impacto real**, não pelo número de linhas.

| Nível | Exemplos | O que exigir |
|---|---|---|
| 0 — trivial | typo, mensagem, config isolada sem efeito relevante | Executar direto após consultar o contexto necessário; verificação proporcional; sem spec. Registrar só se houver impacto durável |
| 1 — lightweight | bug pequeno, endpoint simples, ajuste localizado | `spec.md` único (template `lightweight.md`): objetivo, comportamento, AC, passos, verificação |
| 2 — full | nova funcionalidade, integração externa, banco de dados, refatoração relevante, vários módulos | spec + plan + tasks + verification, implementação incremental, persistência de progresso |
| 3 — critical | autenticação/autorização, operações financeiras, migração destrutiva, segurança/privacidade, produção, transformação arquitetural ampla | Full + análise de riscos, compatibilidade, rollback, critérios de segurança/integridade, efeitos colaterais, `approved_by` do usuário antes de implementar e antes de qualquer ação destrutiva/irreversível |

Na dúvida entre dois níveis, use o maior. Reclassifique (e registre) se o escopo crescer.

## 7. Specify

Crie/atualize `spec.md` (template `_meta/templates/spec.md`). A spec responde: problema, objetivo, quem usa, comportamentos, regras, entradas/saídas, erros, restrições, fora de escopo e como provar que está correto.

- Requisitos relevantes recebem `REQ-NNN`; critérios de aceitação `AC-NNN`, objetivos e testáveis (Given/When/Then quando útil), cada um ligado a REQ.
- Separe fatos, hipóteses (`Assumptions`) e decisões (`context_refs`). Não invente requisitos como confirmados.
- Ambiguidade de baixo risco → hipótese explícita e reversível na spec. Ambiguidade que altera comportamento crítico → perguntar ao usuário **antes** da implementação afetada.
- Não acrescente funcionalidades silenciosamente. Não altere requisitos aprovados para fazer testes passarem.
- A spec descreve comportamento, não implementação.

## 8. Plan

Crie/atualize `plan.md` **depois de inspecionar a arquitetura real**. Aborde só o que se aplica: tecnologias existentes, componentes e arquivos afetados, dados e fluxos, contratos de API, integrações, auth, segurança/privacidade, performance, compatibilidade, migrações, testes, deploy, observabilidade, rollback, riscos, trade-offs.

- Preserve a arquitetura existente, salvo justificativa técnica e autorização compatível com o escopo.
- **Decisões duráveis**: quando o usuário confirmar uma decisão arquitetural durável durante o planejamento, registre-a em `Context/` como `DEC` (exceção estreita à escrita controlada; ver `Context/README.md` seção 9) e cite o ID em `context_refs` do plano. Decisões locais à funcionalidade ficam no próprio plano.

## 9. Tasks e Implement

`tasks.md` (template `_meta/templates/tasks.md`) — cada tarefa tem ID, objetivo, `Requirements`, `Depends on`, `Done when`, `Status` e, quando concluída, `Evidence`. Tarefas devem ser pequenas o bastante para retomar com segurança após um reset.

Formato obrigatório (o validador confere checkbox × status):

```md
- [ ] SPEC-0001-T001 — Objetivo da tarefa
  Status: pending
  Requirements: REQ-001
  Depends on: none
  Done when: critério observável
  Evidence: —
```

`[x]` somente com `Status: completed`; `[ ]` para todos os outros estados.

Implementação controlada:

1. Recupere spec, plano e dependências da tarefa.
2. Inspecione o código existente.
3. Faça o menor conjunto coerente de alterações; reutilize o que existe.
4. Execute testes/verificações adequados.
5. Revise efeitos colaterais.
6. Atualize a tarefa com o resultado **observado** (persistência incremental, seção 10).
7. Só então siga para a próxima tarefa elegível.

Sem funcionalidades futuras não aprovadas, sem refatorações não relacionadas. Impedimento técnico → `Status: blocked` com o motivo, nunca `completed`. Migração destrutiva, ação em produção ou operação irreversível → só com autorização explícita do usuário.

## 10. Verify

`verification.md` compara **spec ↕ implementação ↕ resultados de testes**. Para cada verificação relevante registre: ID `V-NNN`, AC/REQ, comando/teste/procedimento, resultado (`PASS|FAIL|BLOCKED|NOT_RUN|NOT_APPLICABLE`), data, evidência, limitações.

- Nunca registre PASS para algo que não foi executado: use `NOT_RUN`.
- Código escrito não é funcionalidade pronta.
- Requisito não atendido → crie ou reabra tarefas.

## 11. Persistência operacional automática

O progresso do SDD é gravado **nos arquivos, durante o trabalho**, sem pedido do usuário. Pontos obrigatórios de escrita:

| Evento | Atualizar |
|---|---|
| Spec criada/alterada | `spec.md`, `INDEX.md`, `Specs/STATE.md` |
| Plano criado/alterado | `plan.md`, `Specs/STATE.md` |
| Tarefas criadas/reorganizadas | `tasks.md`, `Specs/STATE.md` |
| Tarefa muda de estado / bloqueio | `tasks.md`, `Specs/STATE.md` |
| Tarefa concluída | verificar → `tasks.md` (status + evidência) → `verification.md` se relevante → `Specs/STATE.md` |
| Verificação altera estado conhecido | `verification.md`, `Specs/STATE.md`, `INDEX.md` se mudar status/fase |
| Fase concluída | `phase` da spec, `INDEX.md`, `Specs/STATE.md` |
| Antes de trocar de funcionalidade | `Specs/STATE.md` da funcionalidade atual |

Atualize só o necessário. Não prometa "vou atualizar depois": grave no ponto definido.

### SDD Operational Persistence × Context Save Protocol

| | SDD operacional | `salvar contexto` |
|---|---|---|
| Quando | Automático, nos eventos acima | Pedido explícito do usuário |
| Onde | Somente `Specs/` | `Context/` (registros, checkpoint, STATE, catálogo) |
| Conteúdo | Estado de specs, tarefas, verificações | Conhecimento destilado da sessão |

A persistência automática do SDD **não** autoriza criar memórias gerais, pesquisas ou checkpoints em `Context/`. Única exceção: decisões duráveis confirmadas no planejamento (seção 8).

Quando `salvar contexto` for pedido, o checkpoint inclui um resumo do SDD (specs ativas, fase, próxima tarefa, última verificação) **por referência** a `Specs/STATE.md` e às specs, sem copiar specs inteiras.

### Commits

Não faça commit nem push automaticamente. Commit só com pedido do usuário ou política explícita registrada em `AGENTS.md`.

## 12. Critérios de conclusão (spec → `done`)

1. Requisitos aplicáveis suficientemente definidos.
2. Tarefas do escopo `completed` ou `cancelled` com motivo.
3. Implementação consistente com a spec.
4. Todos os AC verificados com resultado registrado (`PASS`, ou `NOT_APPLICABLE` justificado).
5. Riscos e limitações remanescentes documentados.
6. `tasks.md`, `verification.md`, `INDEX.md`, `Specs/STATE.md` atualizados.
7. Nenhuma divergência crítica conhecida sem tratamento.

Se algo não puder ser atendido, mantenha o status real (`in_progress`/`blocked`) e registre a limitação.

## 13. Protocolo de nova sessão (`retomar desenvolvimento`)

1. Ler `AGENTS.md`.
2. Ler `Context/MAP.md` e `Context/STATE.md`.
3. Ler `Specs/INDEX.md` e `Specs/STATE.md`.
4. Identificar a funcionalidade relevante.
5. Ler sua `spec.md`.
6. Ler `plan.md` e as tarefas necessárias em `tasks.md`.
7. Carregar só as branches de `Context/` citadas em `context_refs` ou necessárias.
8. Inspecionar código, `git status`, `git log` recente e testes relevantes.
9. Reconciliar estado documentado × real (abaixo).
10. Identificar a próxima tarefa válida e continuar.

Não carregue todas as specs nem toda a memória.

### Reconciliação

Quando documentação e código divergirem: não presuma que o documento está certo, nem que o código atende aos critérios. Analise diffs, commits e evidências; determine o que foi de fato concluído; corrija estados operacionais incorretos preservando histórico; informe ao usuário ambiguidades que não puder resolver com segurança.

Após retomar, o agente deve saber responder: funcionalidade em curso, spec vigente, fase, tarefas concluídas, em andamento, bloqueios, testes executados, próxima ação e contexto adicional necessário. Tudo isso deve estar em `Specs/STATE.md` + `tasks.md` + `verification.md`.

## 14. Mudanças de escopo

1. Localize a spec afetada (não crie spec duplicada para uma funcionalidade existente).
2. Compare comportamento atual × pedido; analise impacto.
3. Identifique REQ, AC, tarefas e verificações afetados.
4. Atualize a spec com rastreabilidade: novos REQ recebem novos IDs; REQ alterados registram a mudança e a data; nunca mude silenciosamente o significado de um REQ aceito.
5. Ajuste plano e tarefas (tarefas afetadas voltam a `pending` ou ganham tarefas novas; não apague tarefas — use `cancelled`).
6. Implemente conforme o novo escopo.

Spec substituída por outra: `status: superseded`, `superseded_by: SPEC-NNNN`; na nova, `supersedes`. Mova a antiga para `archive/` só quando não houver mais trabalho ativo referenciando-a.

## 15. Controle de divergências (`auditar sdd`)

Verifique e corrija ou registre:

- REQ sem tarefa; REQ sem AC; AC sem verificação.
- Tarefa `completed` sem evidência; checkbox inconsistente com status.
- Código implementado sem spec/tarefa correspondente (níveis ≥ 1).
- Teste falhando com spec `done`.
- Mudança arquitetural sem `DEC` em `Context/`.
- `Specs/STATE.md` apontando tarefa ativa já concluída; `INDEX.md` divergente das specs.
- Implementação fora do escopo aprovado.
- `context_refs` ou `dependencies` apontando para IDs inexistentes.

Nunca altere requisitos só para justificar o código existente.

Verificações estruturais automáticas: `bash Context/_meta/validate.sh` (seção "Specs" do script — bloco `SPEC-DRIVEN` único, IDs, pasta × ID, INDEX × specs, IDs de tarefa, checkbox × status, estados válidos, `context_refs`, dependências, segredos). Rastreabilidade semântica (REQ ↔ AC ↔ tarefas ↔ verificações) é revisão do agente.

## 16. Comandos semânticos

Intenções em linguagem natural (sem parser):

| Intenção | Ação |
|---|---|
| `iniciar spec` | Descobrir contexto, procurar spec equivalente, classificar, criar/atualizar `spec.md`, registrar em `INDEX.md` |
| `planejar spec` | Inspecionar arquitetura e criar/revisar `plan.md` |
| `gerar tarefas` | Decompor o plano em `tasks.md` |
| `implementar spec` | Executar tarefas elegíveis com persistência incremental |
| `validar spec` | Preencher/atualizar `verification.md`; reabrir tarefas se necessário |
| `status sdd` | Resumir specs ativas, fase, progresso, bloqueios e próximos passos a partir de `Specs/STATE.md` e `INDEX.md` |
| `retomar desenvolvimento` | Protocolo da seção 13 |
| `auditar sdd` | Seção 15 + validador |
| `salvar contexto` | Protocolo de `Context/README.md`, incluindo resumo do SDD por referência |

## 17. Segurança e qualidade

- Sem credenciais, tokens ou chaves nas specs (só nomes de variáveis de ambiente).
- Sem operações destrutivas, irreversíveis ou em produção sem autorização explícita — uma tarefa planejada não é autorização.
- Sem requisitos declarados implementados sem evidência; sem suposições apresentadas como fatos.
- Sem dependências instaladas apenas para documentação; sem hooks/serviços permanentes sem necessidade demonstrada.
- Rigor proporcional ao risco.

## 18. Manutenção e idempotência

Reexecuções do bootstrap SDD são auditorias: `INSPECT → REUSE → MERGE → UPDATE → VALIDATE`. Nunca duplicar o bloco `SPEC-DRIVEN`, recriar specs com novos IDs, apagar tarefas, resetar `STATE.md` ou duplicar conhecimento de `Context/`. Mudanças estruturais do SDD são registradas em `Context/_meta/changelog.md`.
