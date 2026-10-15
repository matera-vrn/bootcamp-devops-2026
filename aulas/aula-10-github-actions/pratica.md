# Prática 10 — Sua primeira pipeline no GitHub Actions 🤖

**Objetivo:** fazer o GitHub buildar e testar seu projeto **automaticamente a cada push** — a pipeline da Aula 05, agora executada por um robô de verdade.

**Onde:** terminal da VM + navegador (GitHub).

## Passo 1 — Crie o arquivo do workflow

O caminho é sagrado: `.github/workflows/` (com ponto, no plural!):

```bash
cd ~/meu-projeto-devops
mkdir -p .github/workflows
nano .github/workflows/ci.yml
```

Conteúdo (indentação com 2 espaços!):

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build-e-teste:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build
        run: ./scripts/build.sh

      - name: Teste
        run: ./scripts/test.sh
```

> 💡 Repare: a pipeline reutiliza **os scripts que você escreveu na Aula 05**. O runner é um Ubuntu — os mesmos comandos da sua VM funcionam lá.

## Passo 2 — Commit e push

```bash
git add .github/workflows/ci.yml
git commit -m "adiciona pipeline de CI com GitHub Actions"
git push
```

## Passo 3 — Veja o robô trabalhar 🍿

No navegador: seu repositório → aba **Actions**. Você verá o workflow `CI` rodando (bolinha amarela). Clique nele → clique no job `build-e-teste` → expanda os steps **Build** e **Teste**.

Resultado esperado: ✅ verde, com os mesmos `[BUILD] OK` e `[TEST] OK` que você via na VM — só que executados numa máquina do GitHub, disparados pelo seu push. **Essa é a Integração Contínua.**

## Passo 4 — O selo de qualidade no README (se der tempo; senão, missão de casa)

Na página do workflow: botão `···` → **Create status badge** → copie o markdown. Na VM:

```bash
nano README.md    # cole o badge na primeira linha
git add README.md
git commit -m "adiciona badge de status da CI"
git push
```

Atualize a página do repositório: um selo **passing** no topo. Portfólio com prova de qualidade automática. 😎

## Passo 5 — Veja a pipeline te proteger num PR 💥

O gran finale: vamos tentar integrar um código quebrado — pelo fluxo da Aula 09 — e ver a esteira barrar.

```bash
git checkout -b quebra-proposital
nano scripts/build.sh
```

Troque `Bootcamp DevOps Matera 2026` por `Ola mundo` (o teste vai reprovar, lembra?).

```bash
git add scripts/build.sh
git commit -m "altera titulo da pagina"
git push -u origin quebra-proposital
```

No navegador, abra o **Pull Request** dessa branch. Aguarde alguns segundos e observe: o check **CI / build-e-teste** fica ❌ **vermelho, dentro do PR**. O GitHub avisa que o merge não é seguro — **antes** de o erro chegar à main (o botão de merge continua ativo: aqui é você quem decide não clicar; em projetos reais, uma regra de proteção da branch bloqueia o botão). Clique em **Details** e encontre a linha exata do `[TEST] FALHOU`.

## Passo 6 — Conserte e veja o PR ficar verde

```bash
nano scripts/build.sh     # desfaça a mudança
git add scripts/build.sh
git commit -m "corrige titulo da pagina"
git push
```

O PR reexecuta a pipeline sozinho → ✅ verde → **Merge pull request**. Na VM: `git checkout main && git pull`.

**Ciclo DevOps completo, de ponta a ponta, no seu projeto.** 🏆

## Passo 7 — O post do certificado 🏅

Tire prints do repositório com o badge verde e da aba Actions, e prepare seu post no LinkedIn marcando a **@Matera** com **#BootcampDevOpsMatera** — critérios no [certificado.md](../../organizacao/certificado.md).

## Deu errado? 😥

| Problema | Causa provável |
|----------|----------------|
| A aba Actions não mostra nada | O arquivo não está em `.github/workflows/ci.yml` exato — confira com `ls -la .github/workflows/` |
| `Permission denied` no step Build | Os scripts perderam o `+x`? Rode `git update-index --chmod=+x scripts/*.sh`, commit e push |
| Erro de YAML no workflow | Indentação — compare com o modelo; 2 espaços, sem Tab |
| Pipeline verde mas badge não aparece | O markdown do badge aponta para a branch certa? Regenere pelo botão *Create status badge* |
| `refusing to allow a Personal Access Token to create or update workflow` no push | O token não tem a permissão **Workflows**. Edite-o em *Settings → Developer settings → Fine-grained tokens* (ou gere outro com *Contents* + *Workflows: Read and write*) e repita o `git push`. Se o Git guardou o token antigo, apague a linha dele em `~/.git-credentials` com o `nano` para ele pedir o novo |
