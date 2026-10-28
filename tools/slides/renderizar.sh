#!/usr/bin/env bash
# Gera o .odp de um roteiro JSON e renderiza as paginas em PNG (para conferencia visual).
# Uso: tools/slides/renderizar.sh aulas/aula-01-devops-overview/slides/aula-01.json [pasta-de-saida] [dpi]
set -euo pipefail
JSON="$1"; OUT="${2:-$(dirname "$JSON")/render}"; DPI="${3:-50}"
ODP="${JSON%.json}.odp"
python3 "$(dirname "$0")/gerar_slides.py" "$JSON" "$ODP"
mkdir -p "$OUT"
timeout 180 soffice --headless --convert-to pdf --outdir "$OUT" "$ODP" >/dev/null 2>&1
pdftoppm -png -r "$DPI" "$OUT/$(basename "${ODP%.odp}").pdf" "$OUT/slide"
ls "$OUT"/slide-*.png | wc -l | xargs -I{} echo "{} paginas renderizadas em $OUT"
