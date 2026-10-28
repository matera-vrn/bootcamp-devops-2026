# Preparação do ambiente 🛠️

Para que **todo mundo tenha exatamente o mesmo ambiente** — não importa se seu computador é Windows, Linux ou macOS — as práticas do bootcamp rodam dentro de uma **máquina virtual (VM) Ubuntu**, executada pelo **VirtualBox**.

> 💡 **Por quê?** Essa é, inclusive, sua primeira lição de DevOps: ambientes padronizados eliminam o famoso *"na minha máquina funciona"*. Você vai ouvir muito essa frase na Aula 07. 😄

## Passo a passo

Siga os guias **nesta ordem**, antes da primeira aula:

1. **[Instalar o VirtualBox](instalacao-virtualbox.md)** no seu computador (Windows, Linux ou macOS).
2. **[Criar a máquina virtual Ubuntu](instalacao-ubuntu-vm.md)** dentro do VirtualBox — inclui a instalação automática do Ubuntu (tudo preenchido numa tela do VirtualBox), a **instalação do servidor SSH** na VM e a conexão por **SSH**, o jeito como você vai usar a VM nas aulas.
3. **[Executar o roteiro de testes](roteiro-de-testes.md)** para confirmar que está tudo funcionando.

⏱️ **Reserve cerca de 2 horas** para tudo (o download da imagem do Ubuntu tem ~4 GB) e faça **pelo menos uma semana antes** da Aula 01, para dar tempo de pedir ajuda se algo travar.

**O que esperar:** você preenche **uma única tela** no VirtualBox (nome, usuário, senha, memória e disco) e o Ubuntu Server se instala **sozinho**, sem perguntar nada, em 10–20 minutos. Depois disso, você vai usar a VM pelo terminal do seu próprio computador (SSH), com copiar e colar funcionando. O sistema pode ficar em português ou em inglês, conforme o idioma do seu computador — os comandos são os mesmos.

## Requisitos mínimos do computador

| Recurso | Mínimo recomendado |
|---------|--------------------|
| Memória RAM | 8 GB (a VM usará 2–4 GB) |
| Espaço em disco livre | 30 GB (a VM usa até 25 GB; a imagem de instalação, 4 GB) |
| Processador | Com suporte a virtualização (VT-x/AMD-V) habilitado na BIOS/UEFI |
| Internet | Necessária durante as aulas para baixar pacotes |

> ⚠️ **Virtualização desabilitada?** Se o VirtualBox reclamar que a virtualização não está disponível, será preciso habilitar **VT-x** (Intel) ou **AMD-V** (AMD) na BIOS/UEFI do computador. O passo a passo (inclusive como conferir pelo Gerenciador de Tarefas no Windows) está em *Problemas comuns* do [guia do VirtualBox](instalacao-virtualbox.md). Em caso de dúvida, chame a gente nos canais da comunidade!

> 🍎 **Mac com chip Apple M (M1, M2, M3, M4)?** Funciona, mas atenção: baixe o VirtualBox para **Apple Silicon** e a imagem do Ubuntu **arm64** — os guias indicam qual.

## E se eu não conseguir?

- **Uma semana antes do bootcamp** enviaremos um formulário para você nos contar como foi a configuração. Responda com sinceridade — é assim que saberemos quem precisa de ajuda!
- **Na Aula 01** teremos um momento dedicado (até 1 hora) para apoiar quem tiver dificuldades com o ambiente.
- Em casos extremos, a partir da Aula 02 disponibilizaremos uma **imagem de VM pré-configurada** com tudo instalado. Mas tente fazer a instalação você mesmo(a) primeiro — o aprendizado começa aqui! 💪
