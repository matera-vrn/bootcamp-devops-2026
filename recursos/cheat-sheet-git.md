# Cola do Git 🌳

Uma página para imprimir ou deixar aberta ao lado. Tudo aqui é o Git básico do bootcamp (Aulas 06 e 09).

## 🧠 O mapa mental: três áreas

```text
 📂 pasta de trabalho  ──git add──▶  📦 staging  ──git commit──▶  🗄️ repositório (.git)
   (onde você edita)                (o que vai na                 (histórico permanente)
                                     próxima foto)
          ◀────────── git restore ──────────      ◀── git restore --staged ──
```

| Área | O que é | Comando para olhar |
|------|---------|--------------------|
| 📂 Pasta de trabalho | Os arquivos como estão agora no disco | `git status` · `git diff` |
| 📦 Staging | O "carrinho" do próximo commit | `git diff --staged` |
| 🗄️ Repositório | As fotos (commits) já gravadas | `git log --oneline` |

## 📖 Commit, branch e HEAD: as definições

| Termo | Definição | No livro | Onde mora |
|-------|-----------|----------|-----------|
| **Commit** (`e0b70f5`) | Registro **permanente** do estado de todos os arquivos acompanhados, com hash único, autor, data, mensagem e o commit anterior (o *pai*) | Uma **página** escrita | `.git/objects/` |
| **Branch** (`main`) | **Nome que aponta para um commit**, o mais recente da linha. Não é cópia de arquivos: avança sozinho a cada commit feito nela | Um **marcador** com nome | `.git/refs/heads/` |
| **HEAD** | Indica **onde você está**: aponta para a branch em uso, define os arquivos da pasta e qual branch avança no próximo commit | O seu **dedo** | `.git/HEAD` |
| **Merge** | Traz o histórico de outra branch para a branch atual (a do HEAD) | Juntar capítulos | — |

> **Commit é a página. Branch é o marcador. HEAD é o dedo.**
> Ao commitar, só o marcador que está no seu dedo anda.

## 🗺️ Branches em desenho

Cada letra é um commit, o tempo corre para a direita e `<-` mostra para onde cada nome aponta.

```text
① git switch -c ideia       ② commit na ideia           ③ merge: fast-forward
                                                           (main não tinha andado)
A---B   <- main              A---B   <- main              A---B---C   <- main <- HEAD
        <- ideia <- HEAD          \                                   <- ideia
                                   C   <- ideia <- HEAD

④ as duas andaram           ⑤ merge commit (M tem dois pais: D e C)
A---B---D   <- main <- HEAD  A---B---D---M   <- main <- HEAD
     \                            \     /
      C     <- ideia               C---'     <- ideia
```

No terminal, o Git desenha na vertical, com o mais novo no topo: `git log --oneline --graph --all`.

Como ler o `git log --oneline --decorate`:

| Você vê | Significa |
|---------|-----------|
| `(HEAD -> main)` | Você está na `main`, e ela aponta para este commit |
| `(HEAD -> melhoria, main)` | Você está na `melhoria`; as duas apontam para o mesmo commit |
| `(main)` sem `HEAD` | A `main` está aqui, mas você está em outra branch |
| `(origin/main)` | Onde está a `main` do GitHub (desde o último `fetch`/`pull`) |
| `(HEAD)` sozinho | *Detached HEAD*: dedo numa página, sem marcador — volte com `git switch main` |

## ⚙️ Configurar (uma vez por máquina)

| Comando | Faz |
|---------|-----|
| `git config --global user.name "Seu Nome"` | Nome que assina os commits |
| `git config --global user.email "voce@exemplo.com"` | E-mail dos commits (fica **público** no GitHub; há a opção *noreply*) |
| `git config --global init.defaultBranch main` | Repositórios novos nascem com `main` |
| `git config --global --list` | Mostra o que está configurado |

## 🚀 Começar

| Comando | Faz |
|---------|-----|
| `git init` | Transforma a pasta atual em repositório (cria o `.git`) |
| `git clone URL` | Baixa um repositório existente, com todo o histórico |
| `vi .gitignore` | Lista do que **não** versionar: `*.log`, arquivos gerados, `.env`, chaves |

## 🔁 O dia a dia: o ritual

```text
git status  ➜  git diff  ➜  git add arquivo  ➜  git commit -m "msg"  ➜  git log --oneline
   olhe          confira        escolha              grave                  admire
```

| Comando | Faz |
|---------|-----|
| `git status` | **O mais importante.** Onde estou e o que mudou |
| `git diff` · `git diff --staged` | Linhas mudadas fora do staging · dentro do staging |
| `git add arquivo` · `git add .` | Coloca no staging um arquivo · tudo da pasta |
| `git commit -m "mensagem"` | Grava a foto |
| `git commit -am "mensagem"` | `add` + `commit` de arquivos **já** acompanhados (novos não entram) |
| `git log --oneline` | Histórico resumido (`q` sai) |
| `git log --oneline --graph --all --decorate` | Histórico em árvore, com branches e HEAD |
| `git show hash` | O que um commit mudou |

✍️ **Mensagem boa:** imperativo, diz *o quê* e *por quê* — `adiciona checagem de memoria ao healthcheck`. Evite `ajustes`, `update`, `teste`.

## 🌿 Branches e merge

| Comando | Faz |
|---------|-----|
| `git branch` | Lista as branches (`*` = onde está o HEAD) |
| `git switch -c nome` · `git checkout -b nome` | Cria a branch e entra nela (forma nova · forma clássica) |
| `git switch nome` · `git checkout nome` | Muda de branch (o Git reescreve os arquivos da pasta) |
| `git merge nome` | Traz a branch `nome` para a branch **atual** |
| `git branch -d nome` | Apaga a branch já integrada (seguro) |
| `git branch -D nome` | Apaga **à força**, mesmo sem merge |

| Tipo de merge | Quando acontece | O que você vê |
|---------------|-----------------|---------------|
| **Fast-forward** | A `main` não andou desde que a branch nasceu | `Fast-forward` — o marcador `main` só avança |
| **Merge commit** | As duas andaram, em linhas diferentes | Abre o `vi` pedindo a mensagem (`Esc`, `:wq`) |
| **Conflito** | As duas mexeram na **mesma linha** | `CONFLICT` — você decide (veja *Socorro*) |

## ☁️ Com o GitHub (Aula 09)

| Comando | Faz |
|---------|-----|
| `git remote add origin URL` · `git remote -v` | Liga o repositório ao GitHub · mostra a ligação |
| `git push -u origin main` | Primeiro envio (depois, só `git push`) |
| `git push -u origin nome` | Envia uma branch nova (para abrir um Pull Request) |
| `git pull` | Traz e integra as novidades do GitHub |
| `git fetch` | Só traz as novidades, sem mexer nos seus arquivos |

> No GitHub, a `main` costuma ser **protegida**: nada de commit direto — tudo chega por branch + Pull Request.

## ↩️ Desfazer

| Situação | Comando | Perde algo? |
|----------|---------|-------------|
| Descartar alteração ainda não adicionada | `git restore arquivo` | ⚠️ Sim, a alteração |
| Tirar do staging, mantendo a alteração | `git restore --staged arquivo` | ✅ Não |
| Corrigir a mensagem do **último** commit (não enviado) | `git commit --amend -m "nova"` | ✅ Não |
| Desfazer um commit criando o "contrário" dele | `git revert hash` | ✅ Não — seguro mesmo após `push` |
| Guardar alterações de lado para trocar de branch | `git stash` · depois `git stash pop` | ✅ Não |
| "Onde eu estava?" — todo movimento do HEAD | `git reflog` | ✅ Não — é a sua rede de segurança |

> 🛑 Commit que **já foi para o GitHub** não se reescreve (`--amend`, `reset`): use `git revert`.

## 🆘 Socorro

| Mensagem ou situação | O que fazer |
|----------------------|-------------|
| `Please tell me who you are` | Faltou o `git config` de nome e e-mail |
| `not a git repository` | Entre na pasta do projeto (`cd ~/meu-projeto-devops`) |
| `nothing to commit` | Faltou o `git add`, ou nada mudou |
| Branch se chama `master` | `git branch -m master main` (e configure o `init.defaultBranch`) |
| `Your local changes would be overwritten` | Faça commit, `git stash` ou `git restore` antes de trocar de branch |
| `CONFLICT (content)` | Abra o arquivo, escolha o que fica, apague `<<<<<<<` `=======` `>>>>>>>`, `git add` e `git commit` |
| `rejected ... fetch first` no `push` | Alguém enviou antes: `git pull` e depois `git push` |
| Abriu o `vi` no commit ou merge | `Esc`, `:wq`, Enter |
| `git log` abriu tela que não sai | `q` |
| Commitei uma senha 😱 | Troque a senha **já** — apagar o arquivo não a tira do histórico |

## 🏁 Fluxo completo, em 7 linhas

```bash
git switch -c minha-melhoria          # 1. cria a branch (dedo no marcador novo)
vi scripts/healthcheck.sh             # 2. edita
git status && git diff                # 3. confere
git add scripts/healthcheck.sh        # 4. prepara
git commit -m "adiciona X porque Y"   # 5. grava (so a minha-melhoria anda)
git switch main                       # 6. volta para a linha oficial
git merge minha-melhoria              # 7. integra (no GitHub: Pull Request)
```

Veja também: [cola do terminal](cheat-sheet-terminal.md) · [glossário](../glossario.md).
