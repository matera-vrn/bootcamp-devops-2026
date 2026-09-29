# Preparação do ambiente 🛠️

Para que **todo mundo tenha exatamente o mesmo ambiente** — não importa se seu computador é Windows, Linux ou macOS — as práticas do bootcamp rodam dentro de uma **máquina virtual (VM) Ubuntu**, executada pelo **VirtualBox**.

> 💡 **Por quê?** Essa é, inclusive, sua primeira lição de DevOps: ambientes padronizados eliminam o famoso *"na minha máquina funciona"*. Você vai ouvir muito essa frase na Aula 07. 😄

## Passo a passo

Siga os guias **nesta ordem**, antes da primeira aula:

1. **[Instalar o VirtualBox](instalacao-virtualbox.md)** no seu computador (Windows, Linux ou macOS).
2. **[Criar a máquina virtual Ubuntu](instalacao-ubuntu-vm.md)** dentro do VirtualBox.
3. **[Executar o roteiro de testes](roteiro-de-testes.md)** para confirmar que está tudo funcionando.

## Requisitos mínimos do computador

| Recurso | Mínimo recomendado |
|---------|--------------------|
| Memória RAM | 8 GB (a VM usará 2–4 GB) |
| Espaço em disco livre | 30 GB |
| Processador | Com suporte a virtualização (VT-x/AMD-V) habilitado na BIOS/UEFI |
| Internet | Necessária durante as aulas para baixar pacotes |

> ⚠️ **Virtualização desabilitada?** Se o VirtualBox reclamar que a virtualização não está disponível, será preciso habilitar **VT-x** (Intel) ou **AMD-V** (AMD) na BIOS/UEFI do computador. Procure por "Virtualization Technology" nas configurações. Em caso de dúvida, chame a gente nos canais da comunidade!

## E se eu não conseguir?

- **Uma semana antes do bootcamp** enviaremos um formulário para você nos contar como foi a configuração. Responda com sinceridade — é assim que saberemos quem precisa de ajuda!
- **Na Aula 01** teremos um momento dedicado (até 1 hora) para apoiar quem tiver dificuldades com o ambiente.
- Em casos extremos, a partir da Aula 02 disponibilizaremos uma **imagem de VM pré-configurada** com tudo instalado. Mas tente fazer a instalação você mesmo(a) primeiro — o aprendizado começa aqui! 💪
