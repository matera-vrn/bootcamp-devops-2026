# Instalação do VirtualBox

O **VirtualBox** é um software gratuito e de código aberto que permite rodar uma "máquina dentro da máquina": a chamada **máquina virtual (VM)**. É nele que rodará o Ubuntu usado em todas as práticas do bootcamp.

> ✅ Utilize **sempre os guias e downloads oficiais** listados abaixo, mantidos pela equipe do VirtualBox. Não baixe o VirtualBox de outros sites.

## 1. Baixe o instalador

Acesse a página oficial de downloads e escolha o pacote do **seu sistema operacional**:

👉 **https://www.virtualbox.org/wiki/Downloads**

- **Windows**: "Windows hosts"
- **macOS**: "macOS / Intel hosts" ou "macOS / Apple Silicon hosts" (conforme seu processador)
- **Linux**: "Linux distributions" → veja a página específica: https://www.virtualbox.org/wiki/Linux_Downloads

## 2. Siga o guia oficial de instalação

O manual oficial do VirtualBox tem um capítulo de instalação com instruções detalhadas para cada sistema:

👉 **https://www.virtualbox.org/manual/ch02.html**

- **Windows**: seção *Installing on Windows Hosts* — basicamente "avançar, avançar, concluir". Se o Windows pedir permissão para instalar drivers de rede, aceite.
- **macOS**: seção *Installing on macOS Hosts* — após a instalação, pode ser necessário autorizar a extensão do sistema em *Ajustes → Privacidade e Segurança*.
- **Linux (Ubuntu)**: seção *Installing on Linux Hosts* — você pode instalar pelo pacote `.deb` baixado no site oficial ou pelo repositório oficial da Oracle descrito no guia.

## 3. Confirme que funcionou

Abra o VirtualBox. Se a tela inicial do **Oracle VirtualBox Manager** aparecer, a instalação deu certo. 🎉

Próximo passo: **[criar a máquina virtual Ubuntu](instalacao-ubuntu-vm.md)**.

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| "VT-x is not available" / "AMD-V is disabled" | Habilite a virtualização na BIOS/UEFI do computador (procure por *Virtualization Technology*, *Intel VT-x* ou *SVM Mode*). |
| Erro de instalação no Windows | Verifique se você tem permissão de administrador e se o Hyper-V não está conflitando (o guia oficial acima orienta sobre isso). |
| macOS bloqueou a extensão | Vá em *Ajustes → Privacidade e Segurança* e clique em **Permitir** para a Oracle. |

Se travar em qualquer passo, poste a mensagem de erro nos canais da comunidade — os monitores vão te ajudar!
