# Continuando com Linux depois do bootcamp 🐧

O bootcamp acaba; o hábito, não. Terminal é como idioma: quem não usa, esquece. Este guia mostra **como manter o Linux na sua rotina** a partir de amanhã, em qualquer computador.

## Escolha o seu caminho (pode ser mais de um)

### 1. Continue usando a sua VM — ela é sua

A VM `bootcamp-devops` não some com o fim do curso. É o seu laboratório: pode quebrar à vontade e, no pior caso, reinstalar em 20 minutos pelo [guia do setup](../setup/instalacao-ubuntu-vm.md).

- Rotina: ligar sem janela (*Headless Start*), `ssh aluno@localhost -p 2222`, trabalhar, `sudo poweroff`.
- Dica: antes de um experimento arriscado, tire um **snapshot** no VirtualBox (*Máquina → Ferramentas → Snapshots*). Deu errado? Volte ao snapshot.

### 2. Windows: Linux dentro do Windows com WSL2

O **WSL2** (*Windows Subsystem for Linux*) roda um Ubuntu de verdade integrado ao Windows — sem VM, abrindo em 2 segundos, com acesso às suas pastas. É o que a maioria dos profissionais que usam Windows faz hoje.

- Instalação oficial (um comando no PowerShell como administrador: `wsl --install`): https://learn.microsoft.com/windows/wsl/install
- Depois, abra "Ubuntu" no menu Iniciar: o mesmo `bash`, o mesmo `apt`, os mesmos comandos do bootcamp. Suas pastas do Windows ficam em `/mnt/c/`.
- Para uma experiência melhor, use o **Windows Terminal**: https://learn.microsoft.com/windows/terminal/install
- ⚠️ Se você **desativou o Hyper-V** para o VirtualBox rodar mais rápido (veja o setup), o WSL2 precisa dele ligado de novo. Os dois convivem, mas o VirtualBox fica mais lento com o Hyper-V ativo. Escolha o que vai usar mais.

### 3. macOS: o terminal já é Unix

O macOS descende do Unix, "primo" do Linux: abra o **Terminal** e quase tudo do bootcamp funciona igual (`ls`, `cd`, `grep`, `ssh`, scripts em bash/zsh).

- Para instalar programas como no `apt`, use o **Homebrew**: https://brew.sh/ (`brew install btop`).
- Para um Linux "puro" quando precisar, mantenha a VM (caminho 1).

### 4. Linux de verdade no computador

Tem um PC antigo parado? Instale o **Ubuntu Desktop** nele — Linux revive máquinas antigas, e nada ensina mais do que usar como sistema principal. Guia oficial: https://ubuntu.com/tutorials/install-ubuntu-desktop

(Dá para testar sem instalar, pelo pendrive, no modo *Try Ubuntu* do próprio instalador.)

## O desafio dos 30 dias

Hábito se constrói com frequência, não com intensidade. Por 30 dias, **10 minutos de terminal por dia**:

| Semana | Faça |
|--------|------|
| 1 | Navegue pelas suas pastas só com `cd`, `ls`, `pwd`. Crie, copie e mova arquivos de verdade pelo terminal |
| 2 | Use `grep` para achar coisas em arquivos seus; leia logs em `/var/log`; `btop` aberto enquanto trabalha |
| 3 | Escreva um script que automatize algo seu (renomear fotos, fazer backup de uma pasta, limpar downloads) |
| 4 | Versione um projeto pessoal com Git e publique no GitHub; coloque um container para rodar algo útil |

Regra de ouro: **sempre que for fazer algo no computador, pergunte "dá para fazer pelo terminal?"** — e tente.

## Use a IA como tutora (do jeito certo)

Assistentes de IA são ótimos professores de Linux quando você pergunta **"explique este comando"** ou **"por que deu este erro?"** antes de rodar. O que o bootcamp te deu é a capacidade de **julgar** a resposta. Dois cuidados:

- Nunca rode um comando com `sudo` ou `rm -rf` que você não entende — peça a explicação linha a linha primeiro.
- A IA erra com confiança. Se o comando parece fazer mais do que você pediu, desconfie.

## Onde continuar estudando

- **Linha de comando para iniciantes** (tutorial oficial do Ubuntu, em inglês): https://ubuntu.com/tutorials/command-line-for-beginners
- **Linux Journey** (trilha gratuita, do básico ao avançado): https://linuxjourney.com/
- **Guia Foca Linux** (clássico em português, gratuito): https://www.guiafoca.org/
- **Shell Script — um guia básico** (em português): https://diegomariano.com/shell-script-um-guia-basico/
- **Pro Git** (o livro oficial do Git, em português): https://git-scm.com/book/pt-br/v2
- **Docker — Get started** (documentação oficial): https://docs.docker.com/get-started/
- A [cola de comandos](cheat-sheet-terminal.md) e o [glossário](../glossario.md) deste repositório.

## E a comunidade

Os canais do bootcamp continuam: compartilhe o que automatizou, pergunte o que travou, ajude quem está começando. Ensinar é a forma mais rápida de consolidar o que você aprendeu. 💙
