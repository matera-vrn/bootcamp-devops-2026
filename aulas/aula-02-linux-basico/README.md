# Aula 02 — Linux 1: História + Comandos básicos

> **Objetivo:** perder o medo da tela preta. Entender por que o Linux domina o mundo DevOps e sair navegando pelo terminal com confiança.

## 🔁 Revisão da Aula 01 (5 min)

- DevOps é **cultura**: Dev + Ops como um time só, com automação e cultura blameless.
- O ciclo de vida DevOps é um loop: planejar → codificar → buildar → testar → liberar → implantar → operar → monitorar.
- Todos validaram o ambiente: a VM Ubuntu é nosso laboratório.
- **Gancho:** toda essa automação roda em cima de um sistema operacional. Hoje conhecemos o rei deles: o **Linux**. 🐧

---

## Parte 1 — Por que o Linux domina o DevOps?

### 1. Um pouco de história

- **1991:** Linus Torvalds, um estudante finlandês, publica um kernel "de hobby" na internet e convida o mundo a colaborar.
- O Linux cresce como **software livre e de código aberto**: qualquer pessoa pode ler, modificar e distribuir.
- Hoje: roda na **imensa maioria dos servidores do mundo**, em todos os supercomputadores do TOP500, em todo Android, nos carros, roteadores... e em toda a nuvem.

> 💬 **Interação:** "Quantos dispositivos com Linux você acha que tem na sua casa? Chuta aí no chat!"

### 2. Distribuições: o mesmo coração, várias roupas

O **kernel** é o núcleo; as **distribuições** (distros) empacotam kernel + ferramentas: Ubuntu, Debian, Fedora, Alpine... Usamos o **Ubuntu**, uma das mais populares em servidores e a mais amigável para começar.

### 3. Por que DevOps = Linux?

- Os servidores onde os sistemas rodam são Linux — quem opera precisa falar a língua deles.
- Containers (Aula 07!) **são** tecnologia do kernel Linux.
- Automação nasce no **terminal**: scripts, pipelines e ferramentas de infra assumem um shell Linux.

### 4. Anatomia do terminal

```text
aluno@bootcamp:~$ ls -l /home
```

| Pedaço | Significado |
|--------|-------------|
| `aluno` | usuário logado |
| `bootcamp` | nome da máquina |
| `~` | diretório atual (`~` = sua pasta pessoal) |
| `$` | usuário comum (`#` seria o superusuário root) |
| `ls` | o **comando** |
| `-l` | uma **opção** (modifica o comportamento) |
| `/home` | o **argumento** (em quem o comando age) |

### 5. O sistema de arquivos é uma árvore

Tudo começa na raiz `/`:

```text
/
├── home/    ← pastas dos usuários (a sua: /home/aluno)
├── etc/     ← arquivos de configuração
├── var/     ← dados variáveis (logs vivem em /var/log!)
├── tmp/     ← arquivos temporários
└── usr/     ← programas
```

Caminho **absoluto** começa da raiz (`/home/aluno/projetos`); caminho **relativo** parte de onde você está (`projetos`).

### 6. Os comandos de hoje

| Comando | O que faz | Mnemônico |
|---------|-----------|-----------|
| `pwd` | Mostra onde você está | *print working directory* |
| `ls` | Lista arquivos e pastas | *list* |
| `cd` | Muda de pasta | *change directory* |
| `mkdir` | Cria pasta | *make directory* |
| `touch` | Cria arquivo vazio | — |
| `cat` | Mostra o conteúdo de um arquivo | *concatenate* |
| `cp` | Copia | *copy* |
| `mv` | Move ou renomeia | *move* |
| `rm` | Remove (⚠️ sem lixeira!) | *remove* |
| `man` | Abre o manual de qualquer comando | *manual* |

> 🧠 **Regra de ouro:** na dúvida, `man comando`. O terminal vem com a documentação embutida.

---

## Parte 2 — Mão na massa

👉 Siga o passo a passo em **[pratica.md](pratica.md)**: você vai criar a estrutura de pastas do seu projeto do bootcamp usando só o terminal.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 03:** "Hoje você aprendeu a andar pela casa. Na próxima aula, você vira o síndico: permissões, processos, instalação de programas e os primeiros comandos de rede — o dia a dia de quem administra servidores de verdade."
