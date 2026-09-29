# Aula 06 — Git: onde o código vive

> **Objetivo:** entender o que é controle de versão, por que o Git é a **fonte única da verdade** do DevOps e dominar o fluxo básico: `init`, `add`, `commit`, `branch`, `merge`.

## 🔁 Revisão da Aula 05 (5 min)

- CI = integrar pouco e sempre; CD = toda versão pronta (ou indo) para produção.
- Vocês montaram uma pipeline com stages de build → teste → deploy que **para no primeiro erro** — e viram um teste barrar uma versão quebrada.
- **Gancho:** mas a esteira roda em cima de *qual* versão do código? Se dois colegas mudam o mesmo arquivo, quem vence? Hoje conhecemos a fonte única da verdade: o **Git**.

---

## Parte 1 — Controle de versão e a fonte única da verdade

### 1. A dor que o Git cura

> `sistema_final.zip`, `sistema_final_v2.zip`, `sistema_final_AGORA_VAI.zip` 😅

Sem controle de versão: ninguém sabe qual é a versão atual, quem mudou o quê, nem como voltar atrás. Em equipe, vira caos multiplicado.

### 2. O que é o Git

Criado em 2005 por Linus Torvalds (o mesmo do Linux!) para organizar o desenvolvimento do kernel. O Git registra **cada mudança**, de **cada arquivo**, feita por **cada pessoa**, para sempre:

- **Histórico completo:** quem, quando, o quê e por quê (a mensagem de commit!).
- **Volta no tempo:** qualquer versão pode ser restaurada.
- **Trabalho em paralelo:** cada um na sua linha do tempo (*branch*), juntando depois (*merge*).

### 3. Git como fonte única da verdade no DevOps

No DevOps, o repositório Git não guarda só código da aplicação:

- Scripts de automação ✔ (os seus da Aula 04–05!)
- Definição da pipeline ✔ (Aula 10)
- Infraestrutura como código ✔
- Documentação ✔

**Se não está no Git, não existe.** É do Git que a esteira parte; é o Git que conta a história do sistema. Este próprio bootcamp vive em um repositório!

### 4. Os três estados de um arquivo

```text
[ Working Directory ] --git add--> [ Staging Area ] --git commit--> [ Repositório ]
   (sua bancada)                    (a caixa a enviar)                (o cofre com histórico)
```

| Comando | O que faz |
|---------|-----------|
| `git init` | Transforma uma pasta em repositório |
| `git status` | O comando que você mais vai usar: o que mudou? |
| `git add arquivo` | Coloca a mudança na "caixa" (staging) |
| `git commit -m "mensagem"` | Sela a caixa no histórico, com autor e data |
| `git log` | Mostra a linha do tempo |

> 🧠 **Boas mensagens de commit** dizem o *o quê* e o *porquê*: `"adiciona teste de disco ao healthcheck"` ✔ · `"ajustes"` ✖

### 5. Branches: universos paralelos

- `main` — a linha do tempo oficial, sempre funcional.
- `git branch minha-ideia` + `git checkout minha-ideia` (ou `git checkout -b minha-ideia`) — experimente sem medo, longe da `main`.
- `git merge minha-ideia` — ideia aprovada? Junta na linha oficial.

> 💬 **Interação:** "Aquele `ls -la` da Aula 02 que mostrou arquivos ocultos... rodem na pasta do projeto depois do `git init` e me digam o que apareceu!" (resposta: a pasta `.git`, onde o histórico mora)

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: o `meu-projeto-devops` vira um repositório Git de verdade, com histórico, branch e merge.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 07:** "Seu projeto agora tem histórico e versão. Mas quando ele rodar na máquina de outra pessoa... será que funciona? Amanhã atacamos a frase mais famosa do software: **'na minha máquina funciona'** — com containers e Docker. 🐳"
