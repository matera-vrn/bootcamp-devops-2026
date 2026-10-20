# Prática 09 — Publicando seu projeto no GitHub ☁️

**Objetivo:** criar sua conta e repositório no GitHub, enviar o `meu-projeto-devops` para a nuvem e abrir seu primeiro Pull Request.

**Onde:** navegador do **seu computador** + terminal conectado à VM **via SSH** — obrigatório hoje: você vai precisar colar um token longo (veja o [setup](../../setup/instalacao-ubuntu-vm.md), passo 7).

## Passo 1 — Conta no GitHub pronta?

Você criou a conta na missão da Aula 08? Então siga para o Passo 2. 😉

Ainda não? Crie agora em **https://github.com/signup** (nome de usuário profissional — ele aparecerá no seu portfólio — e confirme o e-mail). Se o cadastro pedir alguma verificação, chame um monitor para não perder o ritmo.

## Passo 2 — Crie o repositório

No GitHub: botão **New** (ou https://github.com/new):

| Campo | Valor |
|-------|-------|
| Repository name | `meu-projeto-devops` |
| Description | Projeto do Bootcamp DevOps Matera 2026 |
| Choose visibility | **Public** (é portfólio!) |
| Add README | **Off** |
| Add .gitignore | **No .gitignore** |
| Add license | **No license** |


> Click no botão **"Create repository"**

## Passo 3 — Crie um token de acesso (PAT)

1. GitHub → seu avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
2. Token Name: `bootcamp-matera` · Description: `Token bootcamp-matera` · Resource owner: `Seu username` · Expiration: `30 dias` · *Repository access*: **Only select repositories** → `meu-projeto-devops` · *Permissions*: **+ Add permissions** · **Contents: Read and write** e **Workflows: Read and write** (a segunda é obrigatória na Aula 10, quando você enviará a pipeline).
3. **Copie o token** (ele aparece uma única vez!).

> 🔐 O token é sua senha para esta VM. **Não** o salve em arquivos do projeto, **não** poste print dele no chat.

## Passo 4 — Conecte o repositório local ao remoto

No terminal da VM (troque `SEU-USUARIO` pelo seu usuário do GitHub):

```bash
cd ~/meu-projeto-devops
git remote add origin https://github.com/SEU-USUARIO/meu-projeto-devops.git
git remote -v
```

## Passo 5 — O primeiro push! 🚀

```bash
git push -u origin main
```

Quando pedir usuário: seu usuário do GitHub. Quando pedir senha: **cole o token** (nada aparece na tela — é normal; dê Enter).

Resultado esperado: várias linhas, entre elas `main -> main` e, por último, `branch 'main' set up to track 'origin/main'`. Atualize a página do repositório no navegador: **seu projeto está na nuvem!** Scripts, Dockerfile, compose, histórico — tudo lá. 🎉

> 💡 Para não colar o token a cada push: `git config credential.helper store`.
>
> ⚠️ Isso grava o token **em texto puro** no arquivo `~/.git-credentials` da VM. Aceitável aqui — é uma VM de estudo e o token vale 30 dias para um único repositório. Num computador de trabalho, prefira `git config --global credential.helper 'cache --timeout=7200'` (guarda só na memória, por 2 horas). E, ao fim do bootcamp, **revogue o token** em *Developer settings*.

## Passo 6 — Seu primeiro Pull Request

Vamos fazer uma melhoria pelo fluxo profissional completo. O GitHub mostra automaticamente, na página do repositório, um arquivo chamado `README.md` — então vamos renomear o `README.txt` da Aula 02 (`git mv` renomeia e já avisa o Git) e reescrevê-lo:

```bash
git checkout -b docs-readme
git mv README.txt README.md
vi README.md
```

Apague o que estava lá e escreva um README caprichado em **markdown** — a linguagem de formatação do GitHub, em que `#` vira título e `-` vira lista. Por exemplo:

```markdown
# Meu Projeto DevOps

Projeto construído no Bootcamp DevOps Matera 2026.

## O que tem aqui
- `scripts/` — health check e pipeline (build, test, deploy)
- `Dockerfile` — imagem da aplicação
- `compose.yaml` — app + Redis com docker compose

## Como rodar
docker compose up -d
```

Commit e push da branch:

```bash
git add README.md
git commit -m "adiciona README do projeto"
git push -u origin docs-readme
```

## Passo 7 — Abra e integre o PR

1. No navegador, o GitHub mostra por alguns minutos um aviso amarelo **Compare & pull request** — clique. (Sumiu? Aba **Pull requests** → **New pull request** → em *compare*, escolha `docs-readme`.)
2. Título: `Adiciona README do projeto`. Descreva **o que** e **por quê**.
3. **Create pull request**.
4. Explore a aba **Files changed** — é assim que um colega revisaria seu código.
5. **Merge pull request** → **Confirm merge**.

De volta à VM, sincronize:

```bash
git checkout main
git pull
```

Resultado esperado: o README integrado chegou à sua `main` local. Ciclo completo: branch → push → PR → review → merge → pull. **Esse é o fluxo de trabalho de milhões de devs, e agora é o seu.**

## Desafio bônus 🏆

Capriche no seu **perfil** do GitHub: foto, bio ("Estudante de DevOps — Bootcamp Matera 2026") e fixe (*pin*) o repositório `meu-projeto-devops` na página inicial do perfil.

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `Authentication failed` | Token colado errado/expirado, ou usou a senha da conta — gere/cole o PAT |
| `remote origin already exists` | `git remote remove origin` e refaça o Passo 4 |
| `error: src refspec main does not match any` | Sua branch se chama `master` (faltou o `init.defaultBranch` da Aula 06). Renomeie com `git branch -M main` e repita o push |
| Colei o token e nada apareceu | Normal: senhas não aparecem. Dê Enter |
| `error: failed to push some refs` | O repositório remoto foi criado com README — rode `git pull origin main --allow-unrelated-histories` (salve a mensagem com `Ctrl+X`) e repita o push |
| `Repository not found` | URL com typo no usuário ou nome do repositório — confira com `git remote -v` |

## Missão até a próxima aula 📌

1. Faça o desafio bônus (perfil + repositório fixado): é a sua vitrine a partir de agora.
2. Abra um **segundo Pull Request** sozinho(a): corrija ou melhore qualquer coisa no `README.md` pelo fluxo completo — branch → commit → push → PR → merge → `git pull`. Na próxima aula, a pipeline vai rodar dentro desse mesmo fluxo.
