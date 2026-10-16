#!/bin/bash
set -e
echo "[TEST] Verificando a aplicacao..."
if grep -q "Bootcamp DevOps" ~/meu-projeto-devops/app/index.html; then
    echo "[TEST] OK - conteudo esperado encontrado."
else
    echo "[TEST] FALHOU - conteudo esperado nao encontrado!"
    exit 1
fi
