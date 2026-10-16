# Prática 09 — Publicando seu projeto no GitHub ☁️

**Objetivo:** criar sua conta e repositório no GitHub, enviar o `meu-projeto-devops` para a nuvem e abrir seu primeiro Pull Request.

**Onde:** navegador do **seu computador** + terminal conectado à VM **via SSH** — obrigatório hoje: você vai precisar colar um token longo (veja o [setup](../../setup/instalacao-ubuntu-vm.md), passo 6).

## Passo 1 — Crie sua conta no GitHub

No navegador: **https://github.com/signup**

- Escolha um nome de usuário profissional (ele aparecerá no seu portfólio!).
- Confirme o e-mail.

> Já tem conta? Pule para o Passo 2. 😉

## Passo 2 — Crie o repositório

No GitHub: botão **New repository** (ou https://github.com/new):

| Campo | Valor |
|-------|-------|
| Repository name | `meu-projeto-devops` |
| Description | Projeto do Bootcamp DevOps Matera 2026 |
| Visibilidade | **Public** (é portfólio!) |
| Initialize | **NÃO** marque nada (README, .gitignore etc.) — o projeto já existe na VM |

## Passo 3 — Crie um token de acesso (PAT)

1. GitHub → seu avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**.
2. Nome: `bootcamp-vm` · Expiração: 30 dias · Repositório: somente `meu-projeto-devops` · Permissão: **Contents: Read and write**.
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

Quando pedir usuário: seu usuário do GitHub. Quando pedir senha: **cole o token**.

Resultado esperado: várias linhas terminando com `main -> main`. Atualize a página do repositório no navegador: **seu projeto está na nuvem!** Scripts, Dockerfile, compose, histórico — tudo lá. 🎉

> 💡 Para não digitar o token a cada push: `git config credential.helper store` (o Git guarda a credencial dentro da VM).

## Passo 6 — Seu primeiro Pull Request

Vamos fazer uma melhoria pelo fluxo profissional completo:

```bash
git checkout -b docs-readme
nano README.md
```

Escreva um README caprichado (markdown!), por exemplo:

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

1. No navegador, o GitHub mostrará um aviso amarelo: **Compare & pull request** — clique.
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
| `error: failed to push some refs` | O repositório remoto foi criado com README — recrie **sem** inicializar, ou rode `git pull origin main --rebase` antes |
| `Repository not found` | URL com typo no usuário ou nome do repositório — confira com `git remote -v` |
