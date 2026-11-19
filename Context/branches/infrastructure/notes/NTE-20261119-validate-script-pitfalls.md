---
id: CTX-NTE-20261119-validate-script-pitfalls
type: note
title: Cuidados ao executar e alterar Context/_meta/validate.sh
branch: infrastructure
tags: [tooling, git]
status: active
confidence: verified
created_at: 2026-11-19
updated_at: 2026-11-19
source_ids: []
related: [CTX-FCT-20261119-repository-initialized, CTX-DEC-20261119-adopt-sdd-with-context-engineering]
depends_on: []
---

# Cuidados ao executar e alterar `Context/_meta/validate.sh`

## Uso

`bash Context/_meta/validate.sh` (Git Bash, a partir da raiz). Somente leitura; imprime `RESULT: PASS|FAIL` e sai com código 1 em falha. Cobre `Context/` (IDs, relações, catálogo, tags/branches da taxonomia, segredos, checkpoint mais recente) e `Specs/` (marcadores em `AGENTS.md`, pastas × IDs, estados, INDEX, tarefas, `context_refs`).

## Armadilhas já encontradas (verificadas em 2026-11-19)

- **Fim de linha:** com `core.autocrlf=true` (Windows), o script em CRLF quebra no Bash. `.gitattributes` força `*.sh text eol=lf`; não remover.
- **Subshell:** `... | while read` roda em subshell e não propaga `fail=1`. Use `for`/redirecionamento (`while ...; done < <(...)`) ao adicionar checagens.
- **Exemplos de schema:** `Context/README.md` contém `id:` em blocos de exemplo; é excluído da varredura de registros (assim como `_meta/templates/`). Novos arquivos de documentação com exemplos de frontmatter precisam da mesma exclusão.
- **Tags:** o frontmatter aceita forma inline (`[a, b]`) e lista YAML; o parser (`fm_tags`, awk) trata as duas.
- **Teste negativo:** ao alterar o script, plante erros numa cópia temporária (ref quebrada, tag inválida, padrão de segredo, inconsistências de spec) e confirme que cada um é apontado; PASS sozinho não prova a checagem.
- **Falso positivo de segredo:** o padrão `sk-...` casava com IDs `CTX-RSK-...`. Agora exige início de palavra (`(^|[^a-z0-9])sk-`) e também pega chaves com hífen (`sk-ant-...`). Corrigido e testado (positivo e negativo) em 2026-11-19.
