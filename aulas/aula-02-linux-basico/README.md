# Aula 02 — Linux 1: História + Comandos básicos

> **Objetivo:** perder o medo da tela preta. Entender por que o Linux domina o mundo DevOps e sair navegando pelo terminal com confiança.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).
>
> 📽️ Slides desta aula: [`slides/aula-02.odp`](slides/aula-02.odp) (roteiro editável em [`slides/aula-02.json`](slides/aula-02.json) — veja [tools/slides](../../tools/slides/README.md)).

## 🔁 Revisão da Aula 01 (5 min)

- DevOps é **cultura**: Dev + Ops como um time só, com automação e cultura blameless.
- O ciclo de vida DevOps é um loop: planejar → codificar → buildar → testar → liberar → implantar → operar → monitorar.
- Todos validaram o ambiente: a VM Ubuntu é nosso laboratório.
- **Gancho:** toda essa automação roda em cima de um sistema operacional. Hoje conhecemos o rei deles: o **Linux**. 🐧

---

## Parte 1 — Por que o Linux domina o DevOps?

### 1. Um pouco de história

- **1991:** Linus Torvalds, um estudante finlandês, publica um **kernel** (o núcleo de um sistema operacional) "de hobby" na internet e convida o mundo a colaborar.
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

A linha que fica esperando seus comandos chama-se **prompt**. O programa que lê e executa o que você digita é o **shell** — no Ubuntu, o **bash**. Veja um comando completo:

```text
aluno@bootcamp:~$ ls -l /home
```

| Pedaço | Significado |
|--------|-------------|
| `aluno` | usuário logado |
| `bootcamp-devops` | nome da máquina |
| `~` | diretório atual (`~` = sua pasta pessoal) |
| `$` | usuário comum (`#` seria o superusuário root) |
| `ls` | o **comando** |
| `-l` | uma **opção** (modifica o comportamento) |
| `/home` | o **argumento** (em quem o comando age) |

### 5. A estrutura de arquivos do Linux: tudo começa na raiz

> 💡 Quem vem do Windows está acostumado com `C:\`, `D:\` e pastas separadas por `\`. No Linux **não existem letras de unidade**: há **uma única árvore**, que começa na raiz `/`, e as pastas são separadas por `/`. Discos, pendrives e até dispositivos de hardware são "encaixados" (montados) em algum ponto dessa árvore. Outra diferença: o Linux **diferencia maiúsculas de minúsculas** — `Projeto` e `projeto` são pastas diferentes.

No Linux, **tudo é arquivo**: documentos, programas, configurações, logs, dispositivos. E tudo tem um lugar definido. Pense na árvore como um **prédio**, em que cada andar tem uma função:

```text
/                ← a raiz: o terreno onde o prédio está
├── home/        ← apartamentos dos moradores (a sua casa: /home/aluno)
├── root/        ← a cobertura: a casa do superusuário root
├── etc/         ← a administração: arquivos de configuração do sistema
├── bin/  sbin/  ← a caixa de ferramentas: programas essenciais (ls, cp, cat...)
├── usr/         ← a loja de departamentos: a maioria dos programas instalados
├── opt/         ← o depósito: softwares "opcionais" de terceiros
├── var/         ← o arquivo morto que não para de crescer: logs (/var/log), caches, bancos
├── tmp/         ← o lixão temporário: tudo aqui pode sumir ao reiniciar
├── dev/         ← a sala de máquinas: dispositivos (discos, terminais)
├── proc/  sys/  ← o painel de instrumentos: informações vivas do kernel
├── boot/        ← os alicerces: o que o sistema precisa para ligar
├── lib/         ← bibliotecas compartilhadas pelos programas
├── mnt/  media/ ← as portas de entrada: discos externos e pendrives
└── srv/         ← dados de serviços servidos pela máquina (sites, por exemplo)
```

Os que você mais vai visitar em DevOps:

| Pasta | Por que importa para você |
|-------|---------------------------|
| `/home/aluno` | Sua casa (`~`). É onde o projeto do bootcamp vai morar |
| `/etc` | Toda configuração de serviço (rede, usuários, SSH, Docker...) vive aqui |
| `/var/log` | Primeiro lugar para olhar quando algo quebra — os logs |
| `/usr/bin` | Onde os programas que você instala com `apt` ficam |
| `/tmp` | Rascunhos descartáveis — nunca guarde nada importante aqui |

**Caminhos: como dizer onde algo está**

- Caminho **absoluto** começa da raiz e funciona de qualquer lugar: `/home/aluno/meu-projeto-devops`.
- Caminho **relativo** parte de onde você está: se já estiver em `/home/aluno`, basta `meu-projeto-devops`.

Atalhos que você vai usar o tempo todo:

| Atalho | Significa |
|--------|-----------|
| `~` | sua pasta pessoal (`/home/aluno`) |
| `.` | a pasta atual |
| `..` | a pasta "pai" (um nível acima) — `cd ..` sobe um andar |
| `/` | a raiz — `cd /` leva ao térreo |

> 💬 **Interação:** "Se eu estou em `/var/log` e digito `cd ..`, onde fui parar? E com `cd ~`?"

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

### 7. Kit de sobrevivência do terminal

Oito teclas que resolvem 90% dos sustos de quem está começando:

| Tecla | Faz |
|-------|-----|
| `Tab` | **Autocompleta** nomes de arquivos, pastas e comandos. Digite `cd meu-` + `Tab` e veja a mágica (2x `Tab` mostra as opções) |
| `↑` `↓` | Navega pelos comandos que você já digitou — ninguém redigita comando |
| `Ctrl + C` | **Cancela** o comando atual. O terminal "travou"? É isto |
| `Ctrl + L` (ou `clear`) | Limpa a tela |
| `q` | Sai de telas de leitura (`man`, `less`, o histórico do Git). Entrou no editor `vi` sem querer? `Esc`, depois `:q!` e Enter |
| `Ctrl + R` | Busca no histórico: comece a digitar e ele encontra |
| `Ctrl + D` (ou `exit`) | Encerra a sessão |
| `comando --help` | Ajuda resumida, quando o `man` for longo demais |

Dois sustos clássicos:

- **Apareceu um `>` sozinho e nada acontece.** Você abriu aspas e não fechou — o shell está esperando o resto. `Ctrl + C` e digite de novo.
- **O `~` não aparece (ou sai `~~`).** No teclado ABNT2, `~` é tecla morta: aperte `~` e depois **Espaço**. E `|` é `Shift + \` (a tecla ao lado do `Z`). Veja o box de teclado no [setup](../../setup/instalacao-ubuntu-vm.md).

> 📝 Tudo isso está na [cola do terminal](../../recursos/cheat-sheet-terminal.md) — imprima e deixe ao lado.

---

## Parte 2 — Mão na massa

👉 Siga o passo a passo em **[pratica.md](pratica.md)**: você vai criar a estrutura de pastas do seu projeto do bootcamp usando só o terminal.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 03:** "Hoje você aprendeu a andar pela casa. Na próxima aula, você vira o síndico: permissões, processos, instalação de programas e os primeiros comandos de rede — o dia a dia de quem administra servidores de verdade."
