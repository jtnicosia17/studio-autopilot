#!/usr/bin/env bash
# Rebuild every Closer Brain skill from a fresh EVOLV Source Brain export and repackage.
# Usage: tools/refresh.sh <dir containing governed.json and library.json>
set -euo pipefail
SRC="$1"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS="jeremy-miner-discovery hormozi-offer-and-price belfort-tone-and-control daniel-g-closing chris-voss-objections owen-santos-call-review"
TMP="$(mktemp -d)"
python3 -I "$ROOT/tools/build_evolv_refs.py" "$SRC" "$TMP"
for s in $SKILLS evolv-closer-brain; do
  mkdir -p "$ROOT/$s/references/evolv"; cp "$TMP"/*.md "$ROOT/$s/references/evolv/"
done
# Re-bundle each expert's method into the combined skill
for s in $SKILLS; do
  { awk 'BEGIN{c=0} /^---$/{c++; next} c>=2' "$ROOT/$s/SKILL.md"; echo; echo "---"; echo "# Extended playbook"; echo; cat "$ROOT/$s/references/playbook.md"; } > "$ROOT/evolv-closer-brain/references/experts/$s.md"
  cp "$ROOT/$s/references/sources.md" "$ROOT/evolv-closer-brain/references/sources/$s.md"
done
# Repackage (needs the skill-creator skill's packager if available, else plain zip)
mkdir -p "$ROOT/_packaged"
for s in $SKILLS evolv-closer-brain; do
  rm -f "$ROOT/_packaged/$s.skill"; (cd "$ROOT" && zip -qr "_packaged/$s.skill" "$s" -x '*/.DS_Store')
done
echo "Release: $(head -3 "$TMP/evolv-knowledge.md" | grep -o 'release \*\*[^*]*' | sed 's/release \*\*//')"
rm -rf "$TMP"
