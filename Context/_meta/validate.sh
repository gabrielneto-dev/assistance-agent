#!/usr/bin/env bash
# Validação estrutural de Context/ (somente leitura).
# Uso (Git Bash), a partir de qualquer pasta:  bash Context/_meta/validate.sh [raiz-do-projeto]
# Sem argumento, usa a raiz do projeto deduzida a partir da localização deste script.
# Verifica: bloco CONTEXT-ENGINEERING único, import em CLAUDE.md, IDs únicos e coerentes com o nome
# do arquivo, referências CTX-* válidas, catálogo == registros (ids, paths, status), tags/branches na
# taxonomia, _index.md em cada branch, ausência de segredos, arquivos obrigatórios, último checkpoint.
# Sai com código 1 se algo falhar.
set -u
ROOT="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$ROOT" || exit 1
fail=0
echo "== AGENTS/CLAUDE"
n=$(grep -c 'CONTEXT-ENGINEERING:START' AGENTS.md); echo "CE START blocks: $n"; [ "$n" = 1 ] || fail=1
grep -qx '@AGENTS.md' CLAUDE.md && echo "CLAUDE imports AGENTS: ok" || { echo "CLAUDE import MISSING"; fail=1; }
recs=$(grep -rl --include='*.md' '^id: CTX-' Context | grep -v '_meta/templates/' | grep -v 'README.md')
echo "== IDs"
ids=$(for f in $recs; do grep -m1 '^id: ' "$f" | sed 's/^id: //'; done | sort)
echo "$ids" | wc -l | xargs echo "records:"
d=$(echo "$ids" | uniq -d); [ -z "$d" ] && echo "duplicates: none" || { echo "DUP: $d"; fail=1; }
echo "== filename/id consistency"
for f in $recs; do id=$(grep -m1 '^id: ' "$f" | sed 's/^id: //'); b=$(basename "$f" .md); [ "CTX-$b" = "$id" ] || { echo "MISMATCH $f $id"; fail=1; }; done
echo "== referenced IDs"
refs=$(grep -rhoE 'CTX-[A-Z]+-[0-9]{8}(-[0-9]{4})?-[a-z0-9-]+[a-z0-9]' Context AGENTS.md --include='*.md' --include='*.jsonl' --exclude=README.md | grep -v '_meta/templates' | sort -u)
for r in $refs; do echo "$ids" | grep -qx "$r" || { echo "BROKEN REF: $r"; fail=1; }; done
echo "unique refs checked: $(echo "$refs" | wc -l)"
echo "== catalog"
cids=$(grep -oE '"id":"[^"]+"' Context/_meta/catalog.jsonl | sed 's/"id":"//;s/"//' | sort)
[ "$cids" = "$ids" ] && echo "catalog ids match records" || { echo "CATALOG DIVERGES"; diff <(echo "$cids") <(echo "$ids"); fail=1; }
for p in $(grep -oE '"path":"[^"]+"' Context/_meta/catalog.jsonl | sed 's/"path":"//;s/"//'); do [ -f "Context/$p" ] || { echo "MISSING PATH $p"; fail=1; }; done
while IFS= read -r line; do id=$(echo "$line" | grep -oE '"id":"[^"]+"' | sed 's/"id":"//;s/"//'); st=$(echo "$line" | grep -oE '"status":"[^"]+"' | sed 's/"status":"//;s/"//'); p=$(echo "$line" | grep -oE '"path":"[^"]+"' | sed 's/"path":"//;s/"//'); fst=$(grep -m1 '^status: ' "Context/$p" | sed 's/status: //'); [ "$st" = "$fst" ] || { echo "STATUS MISMATCH $id"; fail=1; }; done < Context/_meta/catalog.jsonl
echo "== tags in taxonomy"
# Lê tags do frontmatter nos dois formatos: `tags: [a, b]` e lista em linhas `  - a`.
fm_tags() { awk 'NR==1&&/^---/{fm=1;next} fm&&/^---/{exit} fm&&/^tags:/{intags=1; s=$0; sub(/^tags:[[:space:]]*/,"",s); if(s ~ /^\[/){gsub(/[][ ]/,"",s); n=split(s,a,","); for(i=1;i<=n;i++) if(a[i]!="") print a[i]; intags=0}; next} fm&&intags&&/^[[:space:]]+-[[:space:]]/{s=$0; sub(/^[[:space:]]+-[[:space:]]*/,"",s); print s; next} fm&&intags{intags=0}' "$1"; }
for t in $(for f in $recs; do fm_tags "$f"; done | sort -u); do
  grep -qE "^    - $t\$" Context/_meta/taxonomy.yaml || { echo "TAG NOT IN TAXONOMY: $t"; fail=1; }
done
echo "== branches in taxonomy"
for b in $(for f in $recs; do grep -m1 '^branch: ' "$f" | sed 's/branch: //'; done | sort -u); do
  grep -qE "^  - $b\$" Context/_meta/taxonomy.yaml || { echo "BRANCH NOT IN TAXONOMY: $b"; fail=1; }
done
for d in Context/branches/*/; do [ -f "$d/_index.md" ] || { echo "NO _index in $d"; fail=1; }; done
echo "== secrets scan"
s=$(grep -rniE 'sk-[a-z0-9]{8,}|BEGIN [A-Z ]*PRIVATE KEY|(password|passwd|secret|token|api[_-]?key)[[:space:]]*[=:][[:space:]]*["'"'"']?[A-Za-z0-9/+_-]{8,}' Context AGENTS.md CLAUDE.md)
[ -z "$s" ] && echo "secrets: none" || { echo "SECRETS? $s"; fail=1; }
echo "== required files"
for f in AGENTS.md CLAUDE.md Context/README.md Context/MAP.md Context/STATE.md Context/_meta/config.yaml Context/_meta/taxonomy.yaml Context/_meta/catalog.jsonl Context/_meta/changelog.md Context/core/overview.md Context/core/goals.md Context/core/constraints.md Context/core/glossary.md; do [ -f "$f" ] || { echo "MISSING $f"; fail=1; }; done
cp=$(grep -m1 'Latest checkpoint' Context/STATE.md | grep -oE 'Context/checkpoints/[^`]+'); [ -f "$cp" ] && echo "latest checkpoint exists: $cp" || { echo "CHECKPOINT MISSING"; fail=1; }
echo "RESULT: $([ $fail = 0 ] && echo PASS || echo FAIL)"
exit $fail
