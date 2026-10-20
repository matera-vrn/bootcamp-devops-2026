# Instalação do VirtualBox

O **VirtualBox** é um software gratuito e de código aberto que permite rodar uma "máquina dentro da máquina": a chamada **máquina virtual (VM)**. É nele que rodará o Ubuntu usado em todas as práticas do bootcamp.

> ✅ Utilize **sempre os guias e downloads oficiais** listados abaixo, mantidos pela equipe do VirtualBox. ⚠️ **Não baixe o VirtualBox de outros sites.**

## 1. Baixe o instalador

Baixe o instalador direto do servidor oficial do VirtualBox, conforme o **sistema operacional do seu computador** (o Ubuntu 24.04 citado na tabela é o caso de quem já usa Ubuntu no próprio computador):

| Seu computador | Download — VirtualBox 7.2.20 |
|----------------|------------------------------|
| **Windows** | [VirtualBox-7.2.22-175245-Win.exe](https://download.virtualbox.org/virtualbox/7.2.22/VirtualBox-7.2.22-175245-Win.exe) |
| **macOS — Intel** | [VirtualBox-7.2.22-175245-OSX.dmg](https://download.virtualbox.org/virtualbox/7.2.22/VirtualBox-7.2.22-175245-OSX.dmg) |
| **macOS — Apple Silicon (chip M)** | [VirtualBox-7.2.22-175245-macOSArm64.dmg](https://download.virtualbox.org/virtualbox/7.2.22/VirtualBox-7.2.22-175245-macOSArm64.dmg) |
| **Linux — Ubuntu 24.04 (homologado)** | [virtualbox-7.2_7.2.22-175245~Ubuntu~jammy_amd64.deb](https://download.virtualbox.org/virtualbox/7.2.22/virtualbox-7.2_7.2.22-175245~Ubuntu~jammy_amd64.deb) |
| **Outras distribuições Linux** | Página oficial de downloads: https://www.virtualbox.org/wiki/Linux_Downloads |

> 💡 **Qual Mac é o meu?** Se o seu Mac tem chip **Apple M** (M1, M2, M3...), baixe a versão **Apple Silicon**; caso contrário, use a **Intel**. Menu Apple → *Sobre este Mac* mostra "Chip: Apple M…" ou "Processador: Intel…". Atenção: o VirtualBox para Apple Silicon só roda sistemas **ARM** — por isso, no próximo guia, você baixará a ISO **arm64** do Ubuntu.

> 🐧 **Ubuntu 24.04 (host):** com o `.deb` baixado, instale com `sudo apt install ./virtualbox-7.2_7.2.20-175154~Ubuntu~noble_amd64.deb` — o `apt` resolve as dependências sozinho.

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
| "VT-x is not available" / "AMD-V is disabled" / "VERR_VMX_NO_VMX" | A virtualização está desligada no firmware do computador. **Como conferir (Windows):** Gerenciador de Tarefas → Desempenho → CPU → "Virtualização: Habilitado". **Como ligar:** reinicie e entre na BIOS/UEFI (tecla `F2`, `Del`, `F10` ou `Esc` logo ao ligar — varia por fabricante; no Windows 11 dá para ir por *Configurações → Sistema → Recuperação → Inicialização avançada → Reiniciar agora → Solucionar problemas → Opções avançadas → Configurações de firmware UEFI*). Procure *Virtualization Technology*, *Intel VT-x*, *SVM Mode* ou *AMD-V* e marque **Enabled**. Salve e reinicie. Na dúvida, mande foto da tela no `#setup-ambiente` |
| VM **muito lenta** ou ícone de **tartaruga verde** no rodapé da janela (Windows) | O Windows está rodando o Hyper-V "por baixo" e o VirtualBox perde desempenho. Para resolver: (1) *Painel de Controle → Programas → Ativar ou desativar recursos do Windows* → desmarque **Hyper-V**, **Plataforma de Máquina Virtual** e **Plataforma do Hipervisor do Windows**; (2) *Segurança do Windows → Segurança do dispositivo → Detalhes do isolamento de núcleo* → desligue **Integridade de memória**; (3) reinicie. ⚠️ Isso desativa o WSL2 e o Docker Desktop enquanto estiver assim (e a *Integridade de memória* é uma proteção do Windows): se você usa esses recursos, reative tudo ao final do bootcamp |
| Instalador reclama de **"Microsoft Visual C++ 2019 Redistributable"** (Windows) | Instale o pacote oficial da Microsoft e rode o instalador de novo: https://aka.ms/vs/17/release/vc_redist.x64.exe |
| Erro de instalação no Windows (outros) | Verifique se você tem permissão de administrador. Se o antivírus bloquear, autorize o instalador baixado do site oficial |
| macOS bloqueou a extensão | Vá em *Ajustes → Privacidade e Segurança* e clique em **Permitir** para a Oracle; depois reinicie o Mac |
| macOS com chip M: a VM não inicia | Confira se baixou o VirtualBox **Apple Silicon** e se a ISO do Ubuntu é a **arm64** (próximo guia) |

Se travar em qualquer passo, poste a mensagem de erro nos canais da comunidade — os monitores vão te ajudar!
