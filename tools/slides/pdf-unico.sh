#!/usr/bin/env bash
# Converte os 10 decks .odp em PDF e junta tudo em um unico arquivo, na ordem das aulas.
# Uso: tools/slides/pdf-unico.sh [saida.pdf]   (requer LibreOffice e pdfunite; instale a fonte Poppins para o visual exato)
set -euo pipefail
OUT="${1:-aulas/slides-bootcamp-devops-2026.pdf}"
TMP=$(mktemp -d)
for odp in aulas/aula-*/slides/aula-*.odp; do
  timeout 300 soffice --headless --convert-to pdf --outdir "$TMP" "$odp" >/dev/null 2>&1
done
pdfunite "$TMP"/aula-*.pdf "$OUT"
rm -rf "$TMP"
echo "$OUT: $(pdfinfo "$OUT" | awk '/^Pages/{print $2}') paginas"
