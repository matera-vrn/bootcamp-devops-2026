# Prática 06 — Versionando o projeto com Git 🌳

**Objetivo:** transformar o `meu-projeto-devops` em um repositório Git, fazer os primeiros commits, criar uma branch, e fazer um merge.

**Onde:** no terminal conectado à VM via SSH (como no [setup](../../setup/instalacao-ubuntu-vm.md)). A janela do VirtualBox também serve, mas sem copiar e colar.

## Passo 1 — Apresente-se ao Git

O Git já vem instalado no Ubuntu Server. Confirme:

```bash
git --version
```

Resultado esperado: `git version 2.43.x` (se aparecer `command not found`, instale com `sudo apt install -y git`).

O Git assina cada commit com seu nome. Configure uma vez só:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
git config --global init.defaultBranch main
```

> 💡 O e-mail fica gravado em cada commit e será **público** quando o projeto for para o GitHub (Aula 09). Se preferir não expor o seu, o GitHub oferece um endereço *noreply* em *Settings → Emails* — dá para trocar depois com o mesmo comando.

## Passo 2 — Nasce um repositório

```bash
cd ~/meu-projeto-devops
git init
ls -la
```

Resultado esperado: `Initialized empty Git repository...` e, no `ls -la`, a pasta oculta `.git` — o cofre do histórico.

## Passo 3 — Status, o seu melhor amigo

```bash
git status
```

Resultado esperado: arquivos em vermelho como *untracked* — o Git os vê, mas ainda não os protege.

## Passo 4 — Primeiro commit! 🎉

Antes, duas arrumações que todo profissional faz: o arquivo vazio `scripts/teste.sh` (Aula 03) não precisa entrar no histórico, e arquivos **gerados** — logs, relatórios, a página que o build cria — não se versionam; versiona-se o *código que os gera*. O `.gitignore` é a lista do que o Git deve ignorar:

```bash
rm scripts/teste.sh
nano .gitignore
```

Conteúdo:

```text
# arquivos gerados - nao versionar
*.log
relatorio.txt
app/index.html
```

Rode `git status` de novo: o `healthcheck.log`, o `relatorio.txt` e o `app/index.html` sumiram da lista. Agora sim:

```bash
git add .
git commit -m "primeiro commit: scripts de healthcheck e pipeline"
git status
git log
```

Resultado esperado: `nothing to commit, working tree clean` e um `git log` com seu nome, data e mensagem. **Essa versão agora existe para sempre.**

## Passo 5 — Mude algo e veja o Git perceber

```bash
echo "Projeto versionado com Git!" >> README.txt
git status
git diff
```

O `git diff` mostra exatamente **a linha** que mudou. Agora sele a mudança:

```bash
git add README.txt
git commit -m "atualiza README com nota sobre versionamento"
git log --oneline
```

Resultado esperado: duas linhas no log — sua linha do tempo cresceu.

## Passo 6 — Branch: experimente sem medo

```bash
git checkout -b melhoria-healthcheck
```

Edite o script e adicione, no final (antes da última linha `echo`), há quanto tempo a máquina está ligada:

```bash
vi scripts/healthcheck.sh
```

```bash
echo "[OK] Tempo ligado: $(uptime -p)"
```

Commit na branch:

```bash
git add scripts/healthcheck.sh
git commit -m "adiciona tempo ligado ao healthcheck"
```

## Passo 7 — Compare os universos paralelos

```bash
git checkout main
cat scripts/healthcheck.sh | tail -3
```

Repare: na `main`, sua mudança **não existe**! Ela vive só na branch. Agora o merge:

```bash
git merge melhoria-healthcheck
cat scripts/healthcheck.sh | tail -3
git log --oneline
```

Resultado esperado: a mudança chegou à `main`. Ideia testada, aprovada e integrada — em miniatura, é assim que times inteiros trabalham.

## Desafio bônus 🏆

Crie uma branch `experimento`, faça um commit **quebrando** o healthcheck de propósito, volte para a `main`... e simplesmente **apague a branch** (`git branch -D experimento`). Sinta o poder: o erro nunca tocou a linha oficial.

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `Please tell me who you are` | Faltou o `git config` do Passo 1 |
| `not a git repository` | Você não está dentro de `~/meu-projeto-devops` |
| `nothing to commit` | Faltou o `git add` antes do commit, ou nada mudou |
| Abriu um editor estranho no merge/commit | É o editor de mensagem; salve e saia (`Ctrl+X` no nano; `Esc :wq` no vim) |
| `git log` abriu uma tela que não sai | É o visualizador de páginas: navegue com as setas e saia com `q` |

## Missão até a próxima aula 📌

1. Faça pelo menos **dois commits reais** até a próxima aula: melhore um comentário num script, acrescente uma linha ao `README.txt`, ajuste o health check. Mensagens que dizem *o que* e *por quê*.
2. Antes de cada commit, rode `git status` e `git diff` — e só depois `git add`. Esse ritual é o que separa quem usa Git de quem sofre com Git.
3. Veja sua história crescer: `git log --oneline`.
