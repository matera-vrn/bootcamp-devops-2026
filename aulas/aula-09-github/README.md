# Aula 09 — GitHub: seu código na nuvem, seu portfólio no mundo

> **Objetivo:** publicar o projeto no GitHub, entender remotos (`push`/`pull`), abrir o primeiro Pull Request e começar a construir o portfólio que recrutadores realmente olham.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).

## 🔁 Revisão da Aula 08 (5 min)

- `compose.yaml` declara o sistema inteiro; `docker compose up -d` materializa (declarativo > imperativo).
- Serviços se enxergam pelo nome na rede interna; a infraestrutura está **versionada no Git**.
- **Gancho:** mas todo esse trabalho está **preso na VM**. Hoje ele vai para a nuvem — e vira vitrine: **GitHub**.

---

## Parte 1 — Git ≠ GitHub (e por que você precisa dos dois)

### 1. Qual a diferença?

- **Git** = a ferramenta de controle de versão (roda na sua máquina — Aula 06).
- **GitHub** = a **plataforma na nuvem** que hospeda repositórios Git e adiciona colaboração: Pull Requests, revisão de código, issues, automação (Actions!) e... visibilidade.

Analogia: Git é o editor de texto; GitHub é a biblioteca pública onde a obra fica disponível, com histórico de edições e espaço para revisores.

### 2. Remotos: o elo entre local e nuvem

```text
[ Repositório local (VM) ]  --git push-->  [ Repositório remoto (GitHub) ]
                            <--git pull--
```

| Comando | O que faz |
|---------|-----------|
| `git remote add origin <url>` | Aponta o repositório local para o remoto |
| `git push` | Envia seus commits para o GitHub |
| `git pull` | Traz os commits novos do GitHub |
| `git clone <url>` | Baixa um repositório inteiro (qualquer um público!) |

### 3. Pull Request: a cerimônia mais importante do dia a dia

O **PR** é o pedido formal: *"revisem minha branch e, se estiver boa, integrem na main"*. É onde acontece:

- **Revisão de código** (outro par de olhos antes de integrar);
- **Discussão registrada** (o porquê das decisões fica documentado);
- **Verificações automáticas** — a pipeline roda **no PR**, antes do merge (amanhã você fará exatamente isso!).

> 💬 **Interação:** "Lembra da cultura blameless da Aula 01? O PR é ela em ação: crítica ao **código**, nunca à **pessoa**."

### 4. Autenticação segura

O GitHub não aceita senha em `git push` — usaremos um **Personal Access Token (PAT)** ou chave SSH.

> 🔐 **Regra de ouro (DevSecOps!):** token é **segredo**. Nunca commite um token, nunca cole em arquivo do projeto, nunca compartilhe print com token visível. Trate como escova de dentes: só sua e trocada com frequência. 🪥

### 5. GitHub como portfólio

Recrutadores de tecnologia **olham o GitHub**. Um perfil com projetos reais, commits com mensagens caprichadas e README bem escrito vale mais que dez cursos listados. O `meu-projeto-devops` que você constrói desde a Aula 02 vira hoje sua peça de portfólio.

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: criar a conta e o repositório, dar o primeiro `push`, e abrir (e integrar!) o seu primeiro Pull Request.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 10:** "Seu projeto está no GitHub, com PR e tudo. Falta a peça final: o **robô** que builda e testa a cada push — a pipeline da Aula 05, agora de verdade, com **GitHub Actions**. E teremos uma surpresa no encerramento... 🎁"
