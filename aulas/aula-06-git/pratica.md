# Prática 06 — Versionando o projeto com Git 🌳

**Objetivo:** transformar o `meu-projeto-devops` em um repositório Git, fazer os primeiros commits, criar uma branch, e fazer um merge.

**Onde:** dentro da VM Ubuntu.

## Passo 1 — Instale e apresente-se ao Git

```bash
sudo apt update && sudo apt install -y git
git --version
```

O Git assina cada commit com seu nome. Configure uma vez só:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
git config --global init.defaultBranch main
```

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

Edite o script e adicione a contagem de processos no final (antes da última linha `echo`):

```bash
nano scripts/healthcheck.sh
```

```bash
echo "✅ Processos ativos: $(ps aux | wc -l)"
```

Commit na branch:

```bash
git add scripts/healthcheck.sh
git commit -m "adiciona contagem de processos ao healthcheck"
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
