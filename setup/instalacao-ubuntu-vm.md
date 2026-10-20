# Criando a máquina virtual Ubuntu

Com o VirtualBox instalado, agora vamos criar a VM com **Ubuntu Server 24.04 LTS** — a distribuição Linux que usaremos em todas as práticas.

> 💡 Usamos a versão **Server** porque ela é leve (não tem interface gráfica) e porque o terminal é exatamente o ambiente que um profissional DevOps usa no dia a dia. Sem medo da tela preta — ela vai virar sua melhor amiga. 🖥️

⏱️ **Reserve cerca de 1 hora** para este guia (o download da imagem tem ~4 GB). Faça com calma, de preferência com alguns dias de folga antes da Aula 01.

**Palavras novas que aparecem neste guia:**

| Termo | O que significa |
|-------|-----------------|
| **ISO** (`.iso`) | Um "DVD de instalação" em forma de arquivo. É o que a VM vai usar para instalar o Ubuntu |
| **LTS** | *Long Term Support*: versão com suporte longo (5 anos). É a que empresas usam |
| **amd64 / arm64** | O tipo de processador. **amd64** = Intel ou AMD (quase todos os PCs e Macs antigos). **arm64** = chips Apple M1/M2/M3/M4 |
| **Hash / SHA256** | A "impressão digital" de um arquivo. Serve para conferir se o download não veio corrompido nem alterado |
| **SSH** | Forma de usar o terminal de outra máquina a partir da sua. Vamos usar para controlar a VM pelo terminal do seu próprio computador |

## 1. Baixe a imagem oficial do Ubuntu (.iso)

Baixe **somente dos espelhos oficiais do Ubuntu**. Qual arquivo baixar depende do processador do **seu computador**:

| Seu computador | Arquivo | Onde baixar (oficial) |
|----------------|---------|-----------------------|
| **Windows** (qualquer) | `ubuntu-24.04.x-live-server-amd64.iso` | https://releases.ubuntu.com/24.04/ |
| **Linux** (qualquer) | `ubuntu-24.04.x-live-server-amd64.iso` | https://releases.ubuntu.com/24.04/ |
| **Mac com processador Intel** | `ubuntu-24.04.x-live-server-amd64.iso` | https://releases.ubuntu.com/24.04/ |
| **Mac com chip Apple M** (M1, M2, M3, M4...) | `ubuntu-24.04.x-live-server-arm64.iso` | https://cdimage.ubuntu.com/releases/24.04/release/ |

> 🍎 **Qual Mac é o meu?** Menu Apple → *Sobre este Mac*. Se aparecer **"Chip: Apple M…"**, baixe a versão **arm64**. Se aparecer **"Processador: Intel…"**, baixe a **amd64**. A ISO errada simplesmente não inicia (tela preta).

Na página, baixe o arquivo cujo nome termina em `-live-server-amd64.iso` (ou `-arm64.iso`), com o maior número de versão (ex.: `ubuntu-24.04.5-live-server-amd64.iso`). O download tem **cerca de 4 GB**.

### Verifique a integridade do arquivo (recomendado)

Na mesma página há um arquivo `SHA256SUMS` com a "impressão digital" oficial de cada ISO. Compare com a do arquivo que você baixou:

- **Windows (PowerShell):** `Get-FileHash .\ubuntu-24.04.5-live-server-amd64.iso -Algorithm SHA256`
- **Linux:** `sha256sum ubuntu-24.04.5-live-server-amd64.iso`
- **macOS:** `shasum -a 256 ubuntu-24.04.5-live-server-arm64.iso`

Se o código for igual ao da linha correspondente do `SHA256SUMS`, o download está íntegro. Guia oficial: https://ubuntu.com/tutorials/how-to-verify-ubuntu

## 2. Crie a VM no VirtualBox

Abra o VirtualBox e clique em **Nova** (*New*). Dependendo da versão, as opções aparecem em páginas sucessivas ou todas numa única janela — os campos são os mesmos:

1. **Nome e sistema operacional**
   - **Nome** (*Name*): `bootcamp-devops`
   - **Pasta** (*Folder*): deixe o padrão sugerido
   - **Imagem ISO** (*ISO Image*): selecione o arquivo `.iso` que você baixou
   - ✅ **Marque "Pular instalação desassistida"** (*Skip Unattended Installation*). Vamos instalar manualmente — é rápido e você já começa a aprender.
2. **Instalação desassistida / Usuário e senha**: fica desabilitada por causa do item anterior. Usuário e senha serão definidos pelo instalador do Ubuntu, no passo 3.
3. **Hardware**
   - **Memória base**: `2048` MB (ou `4096` MB se seu computador tiver 16 GB de RAM ou mais)
   - **Processadores**: `2`
4. **Disco rígido virtual**
   - **Tamanho**: `40` GB. Não se assuste: é "alocado dinamicamente" — só ocupa no seu computador o que a VM realmente usar (uns 10–15 GB ao final do bootcamp).
5. Clique em **Finalizar** (*Finish*).

## 3. Instale o Ubuntu — tela a tela

Selecione a VM `bootcamp-devops` e clique em **Iniciar** (*Start*). Vai abrir uma janela com o instalador do Ubuntu em **modo texto**.

> ⌨️ **Como navegar no instalador:** o mouse não funciona aqui. Use as **setas** para mover, **Tab** para pular entre campos, **Espaço** para marcar/desmarcar caixas e **Enter** para confirmar. Para avançar, selecione **[ Done ]** no fim da tela e dê Enter.
>
> 🖱️ Ao clicar dentro da janela da VM, ela "captura" seu mouse e teclado. Para devolvê-los ao seu computador, aperte a **tecla Host**: `Ctrl` **da direita** (Windows/Linux) ou `⌘` **da esquerda** (Mac). Ela aparece no canto inferior direito da janela.

Siga as telas nesta ordem (os nomes estão em inglês, como aparecem na tela):

| # | Tela | O que escolher |
|---|------|----------------|
| 1 | Menu inicial (*GRUB*) | **Try or Install Ubuntu Server** → Enter (ou só aguarde) |
| 2 | *Welcome!* (idioma) | **English**. As mensagens de erro do material e as respostas que você vai achar na internet estão em inglês — e o teclado continua em português, tranquilo |
| 3 | *Installer update available* (pode não aparecer) | **Continue without updating** |
| 4 | *Keyboard configuration* | Veja o box de teclado logo abaixo. Para notebooks e teclados brasileiros: *Layout* **Portuguese (Brazil)**, *Variant* **Portuguese (Brazil)** → Done |
| 5 | *Choose the type of installation* | **Ubuntu Server** (já selecionado). Não marque *Search for third-party drivers* → Done |
| 6 | *Network configuration* | Deixe como está (vai aparecer `DHCPv4 10.0.2.15/24`) → Done |
| 7 | *Proxy configuration* | Deixe em branco → Done |
| 8 | *Ubuntu archive mirror configuration* | Deixe o padrão; aguarde a mensagem *This mirror location passed tests* → Done |
| 9 | *Guided storage configuration* | **Use an entire disk** (já selecionado). **Desmarque a caixa *Set up this disk as an LVM group*** (desça até ela com a seta e aperte Espaço) → Done |
| 10 | *Storage configuration* (resumo) | Done |
| 11 | *Confirm destructive action* | **Continue**. Pode confirmar sem medo: o "disco" aqui é o arquivo virtual de 40 GB que você criou no passo 2 — seu Windows/Mac e seus arquivos não são tocados |
| 12 | *Profile configuration* | *Your name*: seu nome · *Your servers name*: **`bootcamp`** · *Pick a username*: **`aluno`** · *Choose a password*: uma senha simples que você **vai lembrar** (anote! ela será pedida em todas as aulas) → Done |
| 13 | *Upgrade to Ubuntu Pro* | **Skip for now** → Continue |
| 14 | *SSH configuration* | ✅ **Marque *Install OpenSSH server*** (Espaço). *Import SSH key*: **No** → Done |
| 15 | *Featured server snaps* | Não marque nada → Done |
| 16 | *Installing system* | Aguarde (5–15 min). Quando aparecer **Install complete!**, selecione **Reboot Now** → Enter |
| 17 | *Please remove the installation medium, then press ENTER* | Só aperte **Enter** (o VirtualBox já ejeta a ISO sozinho) |

> ⌨️ **Teclado ABNT2 (o padrão brasileiro) e os caracteres do terminal.** Se o layout escolhido na tela 4 estiver errado, teclas como `/`, `ç` e `~` saem trocadas. Com o layout certo, ainda há duas pegadinhas:
> - `~` e `^` são **teclas mortas**: aperte a tecla e depois **Espaço** para o símbolo aparecer (se apertar duas vezes, sai `~~`). Isso vale também no PowerShell do Windows.
> - `|` (a "barra em pé", que vamos usar muito) é **Shift + `\`**, a tecla entre o Shift esquerdo e o `Z`.
> - `/` fica ao lado do Shift direito (a mesma tecla do `?`) e também no `/` do teclado numérico.
>
> Teclados de Mac ou no padrão americano: escolha **English (US)** na tela 4.

## 4. Primeiro login

Depois de reiniciar, a tela mostra várias mensagens e, no meio delas, `bootcamp login:`. **Aperte Enter** se o cursor ficar escondido atrás das mensagens.

Digite `aluno`, dê Enter, digite a senha e dê Enter — **a senha não aparece enquanto você digita, nem asteriscos. É normal!**

Se você está vendo isto, o Ubuntu está instalado:

```text
aluno@bootcamp:~$
```

## 5. Valide a conexão com a internet

Antes de seguir, confirme que a VM enxerga a internet — sem isso, nenhuma prática do bootcamp funciona (instalação de pacotes, Docker, GitHub...). Ainda logado(a) na VM, digite:

```bash
ping -c 4 google.com
```

Resultado esperado: 4 respostas e, no final, `4 received, 0% packet loss`.

```text
64 bytes from ...: icmp_seq=1 ttl=... time=...ms
...
4 packets transmitted, 4 received, 0% packet loss
```

- ✅ **Recebeu respostas?** Internet OK — siga para o SSH.
- ❌ **`Name or service not known` ou `100% packet loss`?** A VM está sem rede. Desligue a VM (`sudo poweroff`), abra **Configurações → Rede** no VirtualBox e confirme que o adaptador está **habilitado** e em modo **NAT**. Ligue a VM e teste de novo. Se persistir, veja se o seu computador está com internet e chame os monitores no canal `#setup-ambiente`.

## 6. Conecte-se à VM pelo terminal do seu computador (SSH) — o jeito oficial do bootcamp

A janela do VirtualBox funciona, mas é desconfortável: a letra é pequena, não dá para rolar a tela nem **copiar e colar**. Profissionais não usam servidores por essa janela — eles se conectam por **SSH** a partir do próprio terminal. Vamos fazer igual.

### 6.1 Abra uma "porta" entre o seu computador e a VM

A VM está escondida atrás de uma rede interna (**NAT**). Vamos criar um redirecionamento: tudo que chegar na porta `2222` do seu computador vai para a porta `22` (SSH) da VM. Pode fazer com a VM ligada:

1. No VirtualBox, selecione a VM → **Configurações** (*Settings*) → **Rede** (*Network*).
2. No *Adaptador 1* (modo **NAT**), abra **Avançado** (*Advanced*) — em algumas versões é preciso ativar o modo **Expert** no alto da janela — e clique em **Redirecionamento de Portas** (*Port Forwarding*).
3. Clique no ícone **+** e preencha duas regras (deixe os campos de IP em branco):

   | Nome | Protocolo | Porta do hospedeiro (*Host Port*) | Porta do convidado (*Guest Port*) |
   |------|-----------|------------------------------------|-----------------------------------|
   | `SSH` | TCP | `2222` | `22` |
   | `WEB` | TCP | `8080` | `8080` |

   (A regra `WEB` será usada nas aulas de Docker, para abrir no navegador a página que você vai criar.)
4. **OK** e **OK**.

### 6.2 Conecte-se

Abra o terminal **do seu computador**:

- **Windows 10/11:** menu Iniciar → **Terminal** ou **PowerShell** (o comando `ssh` já vem instalado).
- **macOS:** *Terminal* (em *Aplicativos → Utilitários*, ou busque "Terminal" no Spotlight).
- **Linux:** o terminal da sua distribuição.

Digite (sem o `$`, se aparecer em algum exemplo):

```bash
ssh aluno@localhost -p 2222
```

- Na **primeira vez** aparece `Are you sure you want to continue connecting (yes/no/[fingerprint])?` — digite `yes` e Enter. (É o SSH memorizando a "identidade" da VM.)
- Em `aluno@localhost's password:` digite a senha da VM e Enter — **nada aparece na tela enquanto digita**, nem ao colar.

Se você vê o prompt `aluno@bootcamp:~$` **na janela do seu terminal**, pronto: você está controlando a VM de fora dela. 🎉

> 📋 **Copiar e colar no terminal** (o motivo de tudo isso):
>
> | Sistema | Colar no terminal |
> |---------|-------------------|
> | Windows (Terminal / PowerShell) | **Ctrl + V** ou **botão direito do mouse** |
> | macOS (Terminal) | **Cmd + V** |
> | Linux (terminal) | **Ctrl + Shift + V** |
>
> 🐧 **A partir de agora, use sempre o SSH nas aulas.** Deixe a janela do VirtualBox minimizada (ou inicie a VM sem janela, veja o passo 8). Para encerrar a sessão SSH, digite `exit`.

> ⚠️ **`ssh` não é reconhecido no Windows?** Em *Configurações → Aplicativos → Recursos opcionais → Adicionar um recurso*, instale **Cliente OpenSSH**. Guia oficial da Microsoft: https://learn.microsoft.com/windows-server/administration/openssh/openssh_install_firstuse

## 7. Sobrevivendo à janela do VirtualBox (quando precisar dela)

Você vai precisar da janela da VM só para ligar/desligar ou se o SSH falhar. Quatro dicas:

| Situação | O que fazer |
|----------|-------------|
| Letra minúscula | Menu **Visualizar → Tela virtual 1 → Escalar para 200%** (*View → Virtual Screen 1 → Scale*) |
| Mouse/teclado "presos" na VM | Aperte a **tecla Host** (`Ctrl` direito no Windows/Linux, `⌘` esquerdo no Mac) |
| A saída de um comando passou e sumiu (não há rolagem) | Rode `comando \| less` — navegue com as setas e saia com `q`. Ou limpe a tela com `clear` |
| Desligar a VM | Digite `sudo poweroff` no terminal, **ou** menu **Máquina → Desligamento por ACPI**. Se fechar a janela no X, escolha **Enviar sinal de desligamento** — nunca *Desligar a máquina*, que é como puxar o cabo da tomada |

## 8. Sua rotina em cada aula

1. Abra o VirtualBox, selecione `bootcamp-devops` e clique na setinha ao lado de **Iniciar** → **Início sem janela** (*Headless Start*). A VM liga "escondida".
2. Abra o terminal do seu computador e conecte: `ssh aluno@localhost -p 2222`.
3. Siga a prática da aula.
4. Ao terminar: `exit` (sai do SSH) e depois, no VirtualBox, **Máquina → Desligamento por ACPI** (ou conecte de novo e rode `sudo poweroff`).

**Parabéns, sua VM está pronta!** 🎉 Próximo passo: **[roteiro de testes](roteiro-de-testes.md)** para validar o ambiente completo.

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| **Tela preta** ao iniciar a VM | (1) Virtualização desligada na BIOS/UEFI — veja o [guia do VirtualBox](instalacao-virtualbox.md). (2) **Mac com chip Apple M usando a ISO `amd64`** — baixe a `arm64` (passo 1) |
| VM **muito lenta**, ícone de **tartaruga verde** no rodapé (Windows) | O Windows está com o Hyper-V ativo "por baixo". Veja *Problemas comuns* do [guia do VirtualBox](instalacao-virtualbox.md) |
| Depois do reboot, o **instalador apareceu de novo** | A ISO continuou "no drive". Desligue a VM, vá em **Configurações → Armazenamento**, clique no `.iso` e remova-o do drive virtual. Ligue de novo |
| `ssh: connect to host localhost port 2222: Connection refused` | Regra de redirecionamento não salva (passo 6.1), VM desligada, ou o OpenSSH não foi instalado — na janela da VM rode `sudo apt install -y openssh-server` |
| `Permission denied, please try again` no SSH | Senha errada (lembre: nada aparece ao digitar). Confira também se digitou `aluno` |
| `~` não aparece / sai `~~` | Tecla morta do ABNT2: aperte `~` e depois **Espaço** |
| `Esqueci a senha` | Mais rápido: reinstalar a VM (passo 2 em diante, ~20 min). Anote a nova senha! |
| Sem internet na VM | Adaptador de rede em modo **NAT** (padrão) e internet funcionando no seu computador |
| Teste 7 do roteiro: **menos de 15G livres** | Provavelmente a instalação ficou com LVM e disco pequeno. Rode: `sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv && sudo resize2fs /dev/ubuntu-vg/ubuntu-lv` e confira com `df -h /`. Se o disco tiver 20 GB, aumente para 40 GB nas configurações da VM (Armazenamento) ou reinstale |
