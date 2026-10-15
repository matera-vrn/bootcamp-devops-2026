# Aula 04 — Linux 3: Shell Script

> **Objetivo:** transformar comandos em **automação**. Escrever, entender e executar os primeiros shell scripts — a porta de entrada para tudo que vem depois (pipelines!).

## 🔁 Revisão da Aula 03 (5 min)

- Permissões (`chmod +x` — lembram do `x`? Hoje ele brilha!), processos (`ps`, `top`), pacotes (`apt`) e pipes (`|`).
- Rede: IP é o endereço, porta é a porta da casa, DNS é a agenda, HTTP é o idioma.
- Fechamos gerando um `relatorio.txt` encadeando vários comandos... digitados um a um. 😓
- **Gancho:** e se aquele relatório se gerasse sozinho, com um único comando? Hoje seus comandos viram **scripts**.

---

## Parte 1 — Automatizando a vida com Shell Script

> 📚 Material de apoio recomendado: [Shell Script — um guia básico (Diego Mariano)](https://diegomariano.com/shell-script-um-guia-basico/)

### 1. O que é um shell script?

Um **arquivo de texto com comandos** que o shell executa em sequência, de cima para baixo. Tudo que você digita no terminal pode virar script. É a forma mais antiga — e ainda a mais usada — de automação em DevOps.

> 💡 Toda pipeline de CI/CD que você verá na carreira é, no fundo, uma sequência de shell scripts executados por um robô.

### 2. Anatomia de um script

```bash
#!/bin/bash
# Meu primeiro script (isto é um comentário)

echo "Olá, bootcamp!"
```

- `#!/bin/bash` — o **shebang**: diz qual interpretador executa o arquivo.
- `#` — comentários: explique o *porquê*, o computador ignora.
- Para executar: `chmod +x script.sh` (a Aula 03 preparou você!) e depois `./script.sh`.

### 3. Variáveis

```bash
NOME="Matera"
echo "Bootcamp $NOME"        # usa a variável
DATA=$(date +%d/%m/%Y)        # guarda a SAÍDA de um comando
echo "Hoje é $DATA"
```

Regras: sem espaço em volta do `=`; use `$VARIAVEL` para ler; `$(comando)` captura a saída de um comando.

### 4. Condicionais: o script que decide

```bash
if ping -c 1 matera.com > /dev/null 2>&1; then
    echo "[OK] Internet"
else
    echo "[FALHA] Sem internet"
fi
```

O `if` testa se o comando deu certo (código de saída 0 = sucesso). Todo comando devolve um código — é assim que pipelines sabem se um passo falhou!

### 5. Loops: repetição sem sofrimento

```bash
for SERVICO in ssh cron systemd-resolved; do
    echo "Verificando $SERVICO..."
    systemctl is-active "$SERVICO"
done
```

### 6. Lendo entrada do usuário e parâmetros

```bash
read -p "Seu nome: " NOME     # pergunta interativa
echo "Bem-vindo, $NOME!"

# ou por parâmetro: ./script.sh Maria
echo "Olá, $1!"               # $1 = primeiro parâmetro
```

### 7. Boas práticas desde o primeiro script

- Comece com `set -e` (o script **para no primeiro erro** — em automação, falhar rápido é uma virtude).
- Nomes de variáveis MAIÚSCULOS e descritivos.
- **Nunca** coloque senhas ou tokens dentro do script — segredos ficam fora do código (você verá onde na Aula 10!).

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: você vai escrever um **health check** — o script que verifica a saúde da sua VM — e ele ficará no projeto até o fim do bootcamp.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 05:** "Seu script executa 3 verificações em 2 segundos. Agora imagine encadear scripts de build, teste e deploy, executados por um robô a cada mudança de código. Isso tem nome: **pipeline**. É o assunto da próxima aula — o coração do DevOps."
