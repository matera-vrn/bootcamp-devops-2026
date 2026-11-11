#!/bin/bash
# pipeline-show.sh - conteudo extra da Aula 05: a mesma esteira do pipeline.sh, com cores (para no primeiro erro)
set -e -o pipefail
PAUSA="${PAUSA:-2}"

VERDE='\033[1;32m'; VERMELHO='\033[1;31m'; AMARELO='\033[1;33m'
AZUL='\033[1;36m'; CINZA='\033[0;90m'; NEGRITO='\033[1m'; N='\033[0m'

barra() {    # barra de progresso que enche durante a pausa
    local passo; passo=$(awk "BEGIN{print $PAUSA/24}")
    printf "${CINZA}│  ${N}"
    for _ in $(seq 1 24); do printf "${AMARELO}▰${N}"; sleep "$passo"; done
    printf "\n"
}

falhou() {   # tela vermelha: mostra o que NAO rodou
    echo -e "${VERMELHO}└─ ✘ $1 FALHOU${N}"
    shift
    for pulado in "$@"; do echo -e "${CINZA}   ⊘ $pulado nao executou${N}"; done
    echo -e "\n${VERMELHO}╔══════════════════════════════════════════════╗"
    echo -e "║   ✘  PIPELINE VERMELHA - esteira parada      ║"
    echo -e "║   🛡  producao protegida: nada foi publicado  ║"
    echo -e "╚══════════════════════════════════════════════╝${N}"
    exit 1
}

stage() {    # stage NUMERO ICONE NOME SCRIPT [stages seguintes...]
    local num="$1" icone="$2" nome="$3" script="$4" inicio=$SECONDS
    shift 4
    echo -e "\n${AZUL}┌─ ${icone}  STAGE ${num}/3 · ${nome}${N}"
    if "./${script}" 2>&1 | sed "s/^/│  /"; then
        barra
        echo -e "${VERDE}└─ ✔ ${nome} passou${N} ${CINZA}($((SECONDS - inicio))s)${N}"
    else
        falhou "$nome" "$@"
    fi
}

clear
echo -e "${AZUL}"
echo "  ╔══════════════════════════════════════════════╗"
echo "  ║      🏭  ESTEIRA DEVOPS - BOOTCAMP 2026      ║"
echo "  ║         build  ➜  test  ➜  deploy            ║"
echo "  ╚══════════════════════════════════════════════╝"
printf "${N}${CINZA}  iniciada por %s@%s as %s${N}\n" "$(whoami)" "$(hostname)" "$(date '+%H:%M:%S')"

stage 1 "🔨" "BUILD"  build.sh  "TEST" "DEPLOY"
stage 2 "🔎" "TEST"   test.sh   "DEPLOY"
stage 3 "🚀" "DEPLOY" deploy.sh

echo -e "\n${VERDE}╔══════════════════════════════════════════════╗"
echo -e "║   ✔  PIPELINE VERDE - aplicacao em producao  ║"
echo -e "╚══════════════════════════════════════════════╝${N}"
echo -e "${CINZA}  tempo total: ${SECONDS}s · em producao agora:${N}"
echo -e "  ${NEGRITO}$(cat ~/producao/index.html)${N}"
