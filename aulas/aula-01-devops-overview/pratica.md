# Prática 01 — Validando seu laboratório 🧪

**Objetivo:** garantir que sua VM Ubuntu está pronta para o bootcamp e dar seus primeiros passos no terminal.

**Pré-requisito:** ter seguido os guias de [`setup/`](../../setup/). Se você travou em algum passo, este é o momento de pedir ajuda — os monitores estão de plantão!

## Passo 1 — Ligue a VM e faça login

Abra o VirtualBox, selecione a VM `bootcamp-devops` e clique em **Iniciar**. Faça login com o usuário `aluno` e sua senha (ela não aparece enquanto você digita).

Resultado esperado:

```text
aluno@bootcamp:~$
```

Agora conecte-se do jeito que usaremos em todas as aulas: abra o terminal **do seu computador** (Terminal/PowerShell no Windows, Terminal no macOS/Linux) e digite:

```bash
ssh aluno@localhost -p 2222
```

O mesmo prompt deve aparecer na sua janela — com copiar e colar funcionando. Dúvidas? Passo 6 do [guia da VM](../../setup/instalacao-ubuntu-vm.md).

## Passo 2 — Execute o roteiro de testes

Siga o **[roteiro de testes](../../setup/roteiro-de-testes.md)** completo (8 testes: login, SSH, teclado, versão do Ubuntu, internet, DNS/HTTPS, `apt` e disco).

## Passo 3 — Deixe sua marca 🖋️

Agora um gostinho do que vem por aí. Digite:

```bash
echo "Meu primeiro comando no bootcamp DevOps!"
```

O terminal repete a frase de volta. Você acabou de usar o `echo` — o comando que "fala" no terminal.

Que tal saber quem você é para o sistema?

```bash
whoami
```

E há quanto tempo a máquina está ligada?

```bash
uptime
```

## Passo 4 — Compartilhe a vitória 🎉

Digite o comando abaixo, tire um print do resultado e poste no chat/comunidade:

```bash
echo "Ambiente pronto! $(whoami) reportando da VM $(hostname)"
```

(`hostname` mostra o nome da máquina e `whoami`, o seu usuário — o terminal montou a frase para você.)

## Deu errado? 😥

| Problema | Caminho |
|----------|---------|
| VM não liga / erro de virtualização | Seção *Problemas comuns* do [guia do VirtualBox](../../setup/instalacao-virtualbox.md) |
| Login não funciona | Confira usuário/senha; se esqueceu a senha, veja o [guia da VM](../../setup/instalacao-ubuntu-vm.md) |
| Algum teste do roteiro falhou | Anote a mensagem de erro e chame um monitor no canal `#setup-ambiente` |
| Nada resolveu | Sinalize para a equipe — a partir da Aula 02 existe uma imagem backup para casos extremos |

## Missão da semana 📌

Antes da Aula 02: se ainda não respondeu, preencha o formulário de confirmação do ambiente. E brinque com o terminal sem medo — **dentro da VM você não quebra nada do seu computador**. Se a VM "quebrar de vez", é só criar outra. Esse é o superpoder das máquinas virtuais!
