# Prática 04 — Seus primeiros scripts 🩺

**Objetivo:** transformar comandos em automação. Primeiro, o relatório da Aula 03 vira um script de cinco linhas (vitória rápida). Depois, um **health check** — o script que verifica a saúde da VM e responde `[OK]` ou `[FALHA]` — que fica no projeto até o fim do bootcamp.

**Onde:** no terminal conectado à VM via SSH (como no [setup](../../setup/instalacao-ubuntu-vm.md)). A janela do VirtualBox também serve, mas sem copiar e colar.

> ⌨️ Os scripts usam só caracteres do teclado (sem emoji nem acento). Digite com calma — errar e corrigir faz parte — ou, se estiver via SSH, cole. Travou na digitação? No fim da página há como baixar as versões prontas.

## Passo 1 — O relatório vira script (5 linhas)

Lembra do relatório da Aula 03, montado comando por comando? Vamos gravá-lo num arquivo para nunca mais digitar aquilo tudo:

```bash
cd ~/meu-projeto-devops/scripts
nano relatorio.sh
```

> ✏️ **nano em 1 minuto** — o `nano` é um editor de texto que roda no terminal. O mouse **não** funciona: mova-se com as setas.
>
> | Tecla | Faz |
> |-------|-----|
> | `Ctrl + O`, depois `Enter` | **Salva** (ele mostra o nome do arquivo; confirme com Enter) |
> | `Ctrl + X` | **Sai** (se houver mudança não salva, pergunta `Save modified buffer?` — responda `Y` e Enter) |
> | `Ctrl + K` / `Ctrl + U` | Recorta a linha / cola de volta |
> | `Ctrl + W` | Procura um texto |
> | `Alt + U` | Desfaz |
>
> Na barra de baixo, `^` significa `Ctrl`. Via SSH, cole com `Ctrl + V` (Windows), `Cmd + V` (Mac) ou `Ctrl + Shift + V` (Linux).

Conteúdo:

```bash
#!/bin/bash
echo "=== Relatorio do sistema ==="
date
uptime
df -h / | grep -v Filesystem
```

Salve (`Ctrl + O`, Enter) e saia (`Ctrl + X`). A primeira linha, `#!/bin/bash`, é o **shebang**: diz que o `bash` deve executar este arquivo. As outras quatro você já conhece da Aula 03.

## Passo 2 — Dê permissão e execute

```bash
chmod +x relatorio.sh
./relatorio.sh
```

Resultado esperado (com os seus números):

```text
=== Relatorio do sistema ===
Fri Nov  6 20:40:12 UTC 2026
 20:40:12 up 25 min,  1 user,  load average: 0.00, 0.01, 0.00
/dev/sda2        37G  5.9G   29G  17% /
```

Quatro comandos, um só toque. **Isso é automação.** O `./` na frente significa "o script que está nesta pasta"; o `x` do `chmod` é o da Aula 03.

## Passo 3 — O health check (versão mínima)

Agora um script que **decide**: verifica internet e disco e responde `[OK]` ou `[FALHA]`.

```bash
nano healthcheck.sh
```

Conteúdo:

```bash
#!/bin/bash
# healthcheck.sh - verifica a saude basica da maquina
set -e
echo "=== Health Check - $(hostname) - $(date '+%d/%m/%Y %H:%M') ==="

# 1) Internet: o ping respondeu?
if ping -c 1 ubuntu.com > /dev/null 2>&1; then
    echo "[OK] Internet"
else
    echo "[FALHA] Internet"
fi

# 2) Disco: acima de 80% de uso, alerta
USO_DISCO=$(df / --output=pcent | tail -1 | tr -d ' %')
if [ "$USO_DISCO" -lt 80 ]; then
    echo "[OK] Disco: ${USO_DISCO}% usado"
else
    echo "[FALHA] Disco: ${USO_DISCO}% usado (acima de 80%!)"
fi

echo "=== Fim do health check ==="
```

### Comandos novos nesta prática

| Trecho | O que faz |
|--------|-----------|
| `set -e` | Se qualquer comando falhar, o script para na hora (em automação, falhar rápido é virtude) |
| `$(comando)` | Executa o comando e usa a saída dele no lugar — `$(hostname)` vira `bootcamp` |
| `> /dev/null 2>&1` | Joga fora o que o comando imprime; só nos interessa se ele deu certo |
| `df / --output=pcent` | Mostra só a coluna de percentual de uso do disco |
| `tail -1` | Pega só a última linha |
| `tr -d ' %'` | Apaga os espaços e o `%`, sobrando só o número |
| `[ "$USO_DISCO" -lt 80 ]` | Testa se o número é menor que (*less than*) 80 |
| `${USO_DISCO}` | O mesmo que `$USO_DISCO`, com chaves para não grudar no texto ao lado |

## Passo 4 — Execute! 🚀

```bash
chmod +x healthcheck.sh
./healthcheck.sh
```

Resultado esperado:

```text
=== Health Check - bootcamp - 06/11/2026 20:45 ===
[OK] Internet
[OK] Disco: 17% usado
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

## Travou na digitação? Baixe a versão pronta

Os dois scripts estão neste repositório. Via SSH, baixe-os direto para a pasta certa — e **leia antes de executar** (`cat healthcheck.sh`), hábito de quem leva segurança a sério:

```bash
cd ~/meu-projeto-devops/scripts
curl -O https://raw.githubusercontent.com/matera-vrn/bootcamp-devops-2026/main/aulas/aula-04-linux-shell-script/scripts/relatorio.sh
curl -O https://raw.githubusercontent.com/matera-vrn/bootcamp-devops-2026/main/aulas/aula-04-linux-shell-script/scripts/healthcheck.sh
chmod +x relatorio.sh healthcheck.sh
```

Compare com o que você digitou, linha a linha: a diferença é o seu erro — e é assim que se aprende.

## Desafio bônus 🏆

1. **Memória:** adicione uma 3ª verificação antes da última linha: `echo "[OK] Memoria disponivel: $(free -m | grep Mem | awk '{print $7}') MB"` (`free -m` mostra a memória em MB; `awk '{print $7}'` pega a 7ª coluna, a *available*).
2. **Processos:** mais uma linha com quantos processos estão rodando (`ps aux | wc -l`).
3. **Parâmetro:** faça o script receber o site do teste de internet como parâmetro (`$1`), com `ubuntu.com` como padrão. Dica: `SITE=${1:-ubuntu.com}` e depois `ping -c 1 "$SITE"`.

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `Permission denied` | Faltou o `chmod +x` |
| `command not found` ao rodar | Use `./healthcheck.sh` (com `./` na frente) |
| `No such file or directory` | Você não está na pasta `scripts` — `cd ~/meu-projeto-devops/scripts` |
| `syntax error near unexpected token` | Algum `if`/`then`/`fi` incompleto — compare com o modelo linha a linha |
| `integer expression expected` | A linha `USO_DISCO=` não produziu um número — compare-a com o modelo, caractere por caractere (`df / --output=pcent`, `tail -1`, `tr -d ' %'`) |
| O terminal "travou" | `Ctrl + C` — e se foi o `ping`, confira se escreveu `-c 1` |

## Missão até a próxima aula 📌

1. Toda vez que ligar a VM esta semana, rode `~/meu-projeto-devops/scripts/healthcheck.sh >> ~/meu-projeto-devops/healthcheck.log` e veja o log crescer com `tail -5 ~/meu-projeto-devops/healthcheck.log`.
2. Faça o desafio bônus 3 (site como parâmetro `$1`): é a diferença entre um script que só serve para você e um que serve para qualquer um.
3. Automatize uma chatice sua: um script de 3 linhas que cria a pasta do dia (`mkdir ~/rascunho-$(date +%d-%m)`) já conta.
