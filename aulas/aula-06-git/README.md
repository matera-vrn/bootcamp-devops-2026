# Aula 06 — Git: onde o código vive

> **Objetivo:** entender o que é controle de versão, por que o Git é a **fonte única da verdade** do DevOps e dominar o fluxo básico: `init`, `add`, `commit`, `branch`, `merge`.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).
>
> 📽️ Slides desta aula: [`slides/aula-06.odp`](slides/aula-06.odp) (roteiro editável em [`slides/aula-06.json`](slides/aula-06.json) — veja [tools/slides](../../tools/slides/README.md)).

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
| `git checkout` | Utilizado para alternar entre ramificações (branches) |
| `git merge` | Traz o conteúdo da branch informada para a branch atual |

> 🧠 **Boas mensagens de commit** dizem o *o quê* e o *porquê*: `"adiciona teste de disco ao healthcheck"` ✔ · `"ajustes"` ✖

### 5. Commit, branch e HEAD: as definições

Três palavras sustentam todo o resto do Git. Vale defini-las com precisão antes de desenhar.

**Commit** é um registro **permanente** do estado de todos os arquivos acompanhados pelo Git num certo momento, com:

- um **identificador único**, o *hash* (`e0b70f5`): uma impressão digital calculada a partir do conteúdo, que muda se qualquer detalhe mudar;
- **autor, data e mensagem**;
- uma referência ao **commit anterior** (o *pai*). É essa corrente de pais que forma a linha do tempo.

Um commit nunca é alterado depois de criado: "corrigir" é sempre fazer um commit novo.

**Branch** é um **nome que aponta para um commit**: o mais recente daquela linha de trabalho. Não é uma cópia da pasta nem dos arquivos; dentro do `.git` ela é só um arquivo de texto com um hash (`.git/refs/heads/main`). Duas consequências:

- criar uma branch é instantâneo e não ocupa espaço;
- ao fazer um commit **estando numa branch**, o nome dela avança sozinho para o commit novo.

O "histórico de uma branch" é o commit para onde ela aponta mais todos os antepassados dele, seguindo a corrente de pais.

**HEAD** é o indicador de **onde você está**. Normalmente ele aponta para uma branch (`HEAD -> main`) e define duas coisas:

- quais arquivos aparecem na pasta de trabalho (os do commit daquela branch);
- **qual branch avança** no próximo commit.

`git switch` (ou `git checkout`) é o comando que move o HEAD.

**Merge** integra o histórico de outra branch na branch **atual** (a do HEAD).

| Termo | Em uma frase | Analogia (livro) |
|-------|--------------|------------------|
| Commit | Registro permanente do projeto, com hash, autor, data, mensagem e pai | Uma página escrita |
| Branch | Nome que aponta para o commit mais recente de uma linha | Um marcador com nome |
| HEAD | Indica a branch em uso: define a pasta e quem avança no commit | O seu dedo |
| Merge | Traz o histórico de outra branch para a atual | Juntar dois capítulos |

### 6. Branches em desenho

Convenção dos desenhos: cada letra é um commit, o tempo corre da esquerda para a direita, `---` liga um commit ao seu pai e `<-` mostra para onde cada nome aponta.

**① Histórico linear: só a `main`.** Cada commit novo faz a `main` avançar.

```text
A---B                  <- main <- HEAD
```

**② `git switch -c ideia`: nasce uma branch.** Nenhum commit novo: só um nome a mais, no mesmo lugar. O HEAD passa para a `ideia`.

```text
A---B                  <- main
                       <- ideia <- HEAD
```

**③ Commit na branch: ela avança, a `main` fica parada.** Quem andou foi a branch do HEAD.

```text
A---B                  <- main
     \
      C                <- ideia <- HEAD
```

**④ `git switch main` e depois `git merge ideia`: fast-forward.** A `main` não andou desde que a `ideia` nasceu, então o Git só **avança o nome `main`** até o `C`. Nenhum commit novo é criado.

```text
A---B---C              <- main <- HEAD
                       <- ideia
```

**⑤ Quando as duas andam: merge commit.** Se a `main` ganhou o commit `D` enquanto a `ideia` ganhava o `C`, as histórias se separaram:

```text
A---B---D              <- main <- HEAD
     \
      C                <- ideia
```

O `git merge ideia` cria um commit novo, `M`, com **dois pais** (`D` e `C`), que junta as duas linhas:

```text
A---B---D---M          <- main <- HEAD
     \     /
      C---'            <- ideia
```

Se `C` e `D` mudaram **a mesma linha do mesmo arquivo**, o Git não sabe qual escolher: é um **conflito**. Você edita o arquivo, decide o que fica e conclui com `git add` e `git commit`.

> 🔎 Para ver esse desenho no seu repositório: `git log --oneline --graph --all`. O Git desenha na vertical, com o commit mais novo no topo e `*` no lugar das letras.

### 7. O fluxo de trabalho com branches

- `main` — a linha oficial, sempre funcional.
- `git switch -c minha-ideia` (ou `git checkout -b minha-ideia`) — cria a branch e move o HEAD para ela: experimente sem medo, longe da `main`.
- `git switch main` + `git merge minha-ideia` — ideia aprovada? Junta na linha oficial.

> 💬 **Interação:** "Aquele `ls -la` da Aula 02 que mostrou arquivos ocultos... rodem na pasta do projeto depois do `git init` e me digam o que apareceu!" (resposta: a pasta `.git`, onde o histórico mora)

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: o `meu-projeto-devops` vira um repositório Git de verdade, com histórico, branch e merge.

> 📝 Todos os comandos — e a explicação de commit, branch e HEAD — estão na [cola do Git](../../recursos/cheat-sheet-git.md). Imprima e deixe ao lado.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 07:** "Seu projeto agora tem histórico e versão. Mas quando ele rodar na máquina de outra pessoa... será que funciona? Amanhã atacamos a frase mais famosa do software: **'na minha máquina funciona'** — com containers e Docker. 🐳"
