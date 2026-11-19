#!/usr/bin/env bash
# Validação estrutural de Context/ (somente leitura).
# Uso (Git Bash), a partir de qualquer pasta:  bash Context/_meta/validate.sh [raiz-do-projeto]
# Sem argumento, usa a raiz do projeto deduzida a partir da localização deste script.
# Verifica: bloco CONTEXT-ENGINEERING único, import em CLAUDE.md, IDs únicos e coerentes com o nome
# do arquivo, referências CTX-* válidas, catálogo == registros (ids, paths, status), tags/branches na
# taxonomia, _index.md em cada branch, ausência de segredos, arquivos obrigatórios, último checkpoint.
# Seção "Specs": marcadores únicos em AGENTS.md, arquivos de Specs/, pasta × ID, status/fase/nível,
# INDEX × specs e próximo ID livre, documentos exigidos pela fase, approved_by em critical, IDs e
# status de tarefas, checkbox × status, evidência em completed, referências CTX/SPEC/tarefa.
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
s=$(grep -rniE 'sk-[a-z0-9]{8,}|BEGIN [A-Z ]*PRIVATE KEY|(password|passwd|secret|token|api[_-]?key)[[:space:]]*[=:][[:space:]]*["'"'"']?[A-Za-z0-9/+_-]{8,}' Context Specs AGENTS.md CLAUDE.md 2>/dev/null)
[ -z "$s" ] && echo "secrets: none" || { echo "SECRETS? $s"; fail=1; }
echo "== required files"
for f in AGENTS.md CLAUDE.md Context/README.md Context/MAP.md Context/STATE.md Context/_meta/config.yaml Context/_meta/taxonomy.yaml Context/_meta/catalog.jsonl Context/_meta/changelog.md Context/core/overview.md Context/core/goals.md Context/core/constraints.md Context/core/glossary.md; do [ -f "$f" ] || { echo "MISSING $f"; fail=1; }; done
cp=$(grep -m1 'Latest checkpoint' Context/STATE.md | grep -oE 'Context/checkpoints/[^`]+'); [ -f "$cp" ] && echo "latest checkpoint exists: $cp" || { echo "CHECKPOINT MISSING"; fail=1; }

# ---------------------------------------------------------------- Specs (SDD)
echo "== Specs"
bad() { echo "$1"; fail=1; }
inlist() { case " $2 " in *" $1 "*) return 0;; esac; return 1; }
# Valor de uma chave do frontmatter (sem comentário final).
fmval() { awk -v k="$2" 'NR==1&&/^---/{fm=1;next} fm&&/^---/{exit} fm&&$0 ~ "^"k":"{v=$0; sub("^"k":[[:space:]]*","",v); sub(/[[:space:]]+#.*$/,"",v); gsub(/^[[:space:]]+|[[:space:]]+$/,"",v); print v; exit}' "$1"; }
for m in CONTEXT-ENGINEERING:START CONTEXT-ENGINEERING:END SPEC-DRIVEN:START SPEC-DRIVEN:END; do
  c=$(grep -c "$m" AGENTS.md); [ "$c" = 1 ] || bad "AGENTS.md: marker $m count=$c (expected 1)"
done
for f in Specs/README.md Specs/INDEX.md Specs/STATE.md Specs/_meta/config.yaml; do [ -f "$f" ] || bad "MISSING $f"; done
S_STATUS="draft ready in_progress blocked done cancelled superseded"
S_PHASE="specify plan tasks implement verify complete"
S_LEVEL="lightweight full critical"
T_STATUS="pending ready in_progress blocked completed cancelled"
spec_ids=""; task_ids=""; nspecs=0
for d in Specs/features/*/; do
  [ -d "$d" ] || continue
  name=$(basename "$d"); nspecs=$((nspecs+1))
  echo "$name" | grep -qE '^SPEC-[0-9]{4}--[a-z0-9]+(-[a-z0-9]+)*$' || bad "BAD FEATURE DIR NAME: $name"
  sp="${d}spec.md"; [ -f "$sp" ] || { bad "MISSING ${d}spec.md"; continue; }
  id=$(fmval "$sp" id); [ "$id" = "${name%%--*}" ] || bad "SPEC ID $id != dir $name"
  inlist "$id" "$spec_ids" && bad "DUPLICATE SPEC ID $id"; spec_ids="$spec_ids $id"
  st=$(fmval "$sp" status); ph=$(fmval "$sp" phase); lv=$(fmval "$sp" level)
  inlist "$st" "$S_STATUS" || bad "$id: invalid status '$st'"
  inlist "$ph" "$S_PHASE" || bad "$id: invalid phase '$ph'"
  inlist "$lv" "$S_LEVEL" || bad "$id: invalid level '$lv'"
  grep -qE "^\|[[:space:]]*$id[[:space:]]*\|" Specs/INDEX.md || bad "$id: not listed in Specs/INDEX.md"
  for doc in plan:PLAN tasks:TASKS verification:VER; do
    f="${d}${doc%%:*}.md"; [ -f "$f" ] || continue
    [ "$(fmval "$f" id)" = "$id-${doc##*:}" ] || bad "$f: id must be $id-${doc##*:}"
    [ "$(fmval "$f" spec)" = "$id" ] || bad "$f: spec must be $id"
  done
  if [ "$lv" != lightweight ]; then
    inlist "$ph" "tasks implement verify complete" && { [ -f "${d}plan.md" ] || bad "$id: phase $ph requires plan.md"; }
    inlist "$ph" "implement verify complete" && { [ -f "${d}tasks.md" ] || bad "$id: phase $ph requires tasks.md"; }
    inlist "$ph" "verify complete" && { [ -f "${d}verification.md" ] || bad "$id: phase $ph requires verification.md"; }
  fi
  if [ "$lv" = critical ] && inlist "$st" "in_progress done"; then
    ab=$(fmval "$sp" approved_by); { [ -z "$ab" ] || [ "$ab" = null ]; } && bad "$id: critical spec $st without approved_by"
  fi
  [ "$st" = done ] && [ "$ph" != complete ] && bad "$id: status done but phase $ph"
  # Tarefas: tasks.md (full/critical) ou spec.md (lightweight). Saída do awk: "<id> <checkbox> <status>".
  tf="${d}tasks.md"; [ "$lv" = lightweight ] && tf="$sp"
  [ -f "$tf" ] || continue
  while read -r tid box tst; do
    [ -z "$tid" ] && continue
    case "$tid" in "$id"-T[0-9][0-9][0-9]) ;; *) bad "$tf: task $tid does not belong to $id";; esac
    inlist "$tid" "$task_ids" && bad "DUPLICATE TASK ID $tid"; task_ids="$task_ids $tid"
    inlist "$tst" "$T_STATUS" || bad "$tid: invalid status '$tst'"
    if [ "$box" = x ]; then [ "$tst" = completed ] || bad "$tid: [x] but status $tst"
    else [ "$tst" = completed ] && bad "$tid: status completed but checkbox empty"; fi
    [ "$tst" = completed ] && ! awk -v t="$tid" '$0 ~ t" "{f=1;next} f&&/^- \[/{exit} f&&/^[[:space:]]+Evidence:/{v=$0; sub(/^[[:space:]]+Evidence:[[:space:]]*/,"",v); if(v!="" && v!="—" && v!="-") ok=1} END{exit !ok}' "$tf" && bad "$tid: completed without Evidence"
  done < <(awk 'match($0,/^- \[[ xX]\] SPEC-[0-9]{4}-T[0-9]{3}/){if(t!="")print t, b, (s==""?"missing":s); t=substr($0,7,14); b=(substr($0,4,1)~/[xX]/)?"x":"-"; s=""; next} t!=""&&/^[[:space:]]+Status:/{s=$0; sub(/^[[:space:]]+Status:[[:space:]]*/,"",s); sub(/[[:space:]].*$/,"",s)} END{if(t!="")print t, b, (s==""?"missing":s)}' "$tf")
done
echo "specs: $nspecs, tasks: $(echo $task_ids | wc -w)"
# INDEX: toda linha de spec tem pasta; próximo ID livre maior que todos os existentes.
for r in $(grep -oE '^\|[[:space:]]*SPEC-[0-9]{4}[[:space:]]*\|' Specs/INDEX.md | grep -oE 'SPEC-[0-9]{4}'); do
  inlist "$r" "$spec_ids" || bad "INDEX lists $r but Specs/features/$r--*/spec.md is missing"
done
next=$(grep -oE 'Próximo ID livre: \*\*SPEC-[0-9]{4}\*\*' Specs/INDEX.md | grep -oE '[0-9]{4}')
[ -n "$next" ] || bad "Specs/INDEX.md: 'Próximo ID livre' missing"
for s in $spec_ids; do [ "$((10#${s#SPEC-}))" -lt "$((10#${next:-0}))" ] || bad "INDEX next free id SPEC-$next is not greater than $s"; done
# Referências: CTX-* em Specs devem existir em Context/; SPEC/tarefas citados devem existir.
for r in $(grep -rhoE 'CTX-[A-Z]+-[0-9]{8}(-[0-9]{4})?-[a-z0-9-]+[a-z0-9]' Specs --include='*.md' --exclude-dir=_meta --exclude=README.md | sort -u); do
  echo "$ids" | grep -qx "$r" || bad "Specs: BROKEN CONTEXT REF $r"
done
for r in $(grep -rhoE 'SPEC-[0-9]{4}-T[0-9]{3}' Specs --include='*.md' --exclude-dir=_meta --exclude=README.md | sort -u); do
  inlist "$r" "$task_ids" || bad "Specs: reference to unknown task $r"
done
for r in $(grep -rhoE 'SPEC-[0-9]{4}' Specs Context --include='*.md' --exclude-dir=_meta --exclude=README.md | sort -u); do
  inlist "$r" "$spec_ids" || [ "$r" = "SPEC-$next" ] || bad "reference to unknown spec $r"
done

echo "RESULT: $([ $fail = 0 ] && echo PASS || echo FAIL)"
exit $fail
