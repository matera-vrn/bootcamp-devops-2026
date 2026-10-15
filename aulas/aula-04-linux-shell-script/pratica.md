# Prática 04 — Seu primeiro script: o health check 🩺

**Objetivo:** escrever um script que verifica a "saúde" da VM — internet, disco e memória — e responde com ✅ ou ❌. Esse script fica no projeto e será reaproveitado nas próximas aulas!

**Onde:** no terminal conectado à VM via SSH (como no [setup](../../setup/instalacao-ubuntu-vm.md)). A janela do VirtualBox também serve, mas sem copiar e colar.

## Passo 1 — Crie o arquivo

```bash
cd ~/meu-projeto-devops/scripts
nano healthcheck.sh
```

> O `nano` é um editor simples de terminal: digite normalmente, salve com `Ctrl+O` + `Enter` e saia com `Ctrl+X`.

## Passo 2 — Digite o script

Copie para dentro do `healthcheck.sh` (digite mesmo — errar e corrigir faz parte!):

```bash
#!/bin/bash
# healthcheck.sh — verifica a saude basica da maquina
set -e

echo "=== Health Check — $(hostname) — $(date '+%d/%m/%Y %H:%M') ==="

# 1) Internet
if ping -c 1 ubuntu.com > /dev/null 2>&1; then
    echo "✅ Internet: OK"
else
    echo "❌ Internet: FALHOU"
fi

# 2) Espaco em disco (alerta se uso > 80%)
USO_DISCO=$(df / --output=pcent | tail -1 | tr -d ' %')
if [ "$USO_DISCO" -lt 80 ]; then
    echo "✅ Disco: ${USO_DISCO}% usado"
else
    echo "❌ Disco: ${USO_DISCO}% usado (acima de 80%!)"
fi

# 3) Memoria livre
MEM_LIVRE=$(free -m | grep Mem | awk '{print $7}')
echo "✅ Memoria disponivel: ${MEM_LIVRE} MB"

echo "=== Fim do health check ==="
```

## Passo 3 — Dê permissão de execução

```bash
chmod +x healthcheck.sh
ls -l healthcheck.sh
```

Resultado esperado: `-rwxrwxr-x` — o `x` da Aula 03 em ação!

## Passo 4 — Execute! 🚀

```bash
./healthcheck.sh
```

Resultado esperado:

```text
=== Health Check — bootcamp — 10/11/2026 20:45 ===
✅ Internet: OK
✅ Disco: 32% usado
✅ Memoria disponivel: 1450 MB
=== Fim do health check ===
```

Tire um print e poste no chat! 🎉

## Passo 5 — Grave o resultado em um log

Automação de verdade guarda histórico:

```bash
./healthcheck.sh >> ~/meu-projeto-devops/healthcheck.log
cat ~/meu-projeto-devops/healthcheck.log
```

Execute 2–3 vezes e veja o log crescer — cada execução com seu horário.

## Desafio bônus 🏆

1. Adicione uma 4ª verificação: quantos processos estão rodando (`ps aux | wc -l`).
2. Faça o script receber o site do teste de internet como parâmetro (`$1`), com `ubuntu.com` como padrão. Dica: `SITE=${1:-ubuntu.com}`.

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `Permission denied` | Faltou o `chmod +x healthcheck.sh` |
| `command not found` ao rodar | Use `./healthcheck.sh` (com `./` na frente) |
| `syntax error near unexpected token` | Algum `if`/`then`/`fi` incompleto — compare com o modelo linha a linha |
| Números estranhos no disco/memória | Confira se copiou os comandos `df`/`free` exatamente como no modelo |
