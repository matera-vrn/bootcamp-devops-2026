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

## 2. Crie a VM no VirtualBox — toda a configuração em uma só tela

Abra o VirtualBox e clique em **Nova** (*New*). A janela **New Virtual Machine** tem cinco seções que se abrem ao clicar na setinha (▶). Preencha **todas** antes de clicar em **Finish**:

**▶ Virtual machine name and operating system** (nome e sistema)
- **Name**: `bootcamp-devops`
- **Folder**: deixe o padrão sugerido
- **ISO Image**: selecione o arquivo `.iso` que você baixou. O VirtualBox reconhece o Ubuntu e preenche *Type* e *Version* sozinho.
- **Skip Unattended Installation**: deixe **desmarcado** — é justamente a instalação automática que vamos usar.

**▶ Set up unattended guest OS installation** (instalação automática — é aqui que você define usuário, senha e nome da máquina)
- **User Name**: `aluno`
- **Password** e **Confirm Password**: uma senha simples que você **vai lembrar** (anote! ela será pedida em todas as aulas). O aviso *Password must match* some quando as duas ficam iguais.
- **Product Key**: em branco (só serve para Windows)
- **Host Name**: `bootcamp` — é o nome que aparece no prompt (`aluno@bootcamp`)
- **Domain Name**: deixe o padrão (`myguest.virtualbox.org`)
- **Install in Background**: desmarcado (queremos ver a instalação acontecer)

**▶ Install Guest Additions**: deixe **desmarcado**.

**▶ Specify virtual hardware** (hardware)
- **Base Memory**: `2048` MB (ou `4096` MB se seu computador tiver 16 GB de RAM ou mais)
- **Processors**: `2`
- **Enable EFI**: deixe como está

**▶ Specify virtual hard disk** (disco)
- **Create a Virtual Hard Disk Now** (já selecionado)
- **Disk Size**: `25` GB. Não se assuste: é "alocado dinamicamente" — só ocupa no seu computador o que a VM realmente usar
- **Pre-allocate Full Size**: desmarcado

Confira o resumo e clique em **Finish**.

## 3. Aguarde a instalação automática (10–20 min)

A VM liga sozinha e o Ubuntu se instala **sem perguntar nada**: telas do instalador passam por conta própria, uma barra de progresso avança e, no fim, a máquina reinicia. **Não clique dentro da janela nem aperte teclas** durante esse tempo. (Clicou e o mouse "sumiu"? Aperte a **tecla Host**: `Ctrl` **da direita** no Windows/Linux, `⌘` **da esquerda** no Mac.)

O que a instalação automática configura, a partir do que você preencheu:

| Item | Como fica |
|------|-----------|
| Usuário | `aluno`, com poderes de administrador (`sudo`) e a senha que você escolheu |
| Nome da máquina | `bootcamp` |
| Disco | Os 25 GB inteiros para o sistema (sem partições extras) |
| Teclado **da janela da VM** | Inglês (US) — veja o box abaixo; pelo SSH isso não importa |
| Servidor SSH | **Não vem instalado** — instalamos no passo 6 |

Está pronto quando aparecer `bootcamp login:` na tela.

> ⌨️ **Teclado: por que a janela da VM fica "em inglês" e por que isso não importa.** A instalação automática não pergunta o layout e deixa o console com teclado **US**: num teclado ABNT2, `/`, `ç`, `;` e `~` saem trocados **dentro da janela do VirtualBox**. Por isso usamos a janela só para o login, o teste de internet e a instalação do SSH — comandos sem esses caracteres. Daí em diante, **pelo SSH o teclado é o do seu computador** e tudo funciona.
>
> Quer corrigir o console mesmo assim? Depois do login, rode `sudo dpkg-reconfigure keyboard-configuration` (escolha *Generic 105-key PC*, depois *Portuguese (Brazil)* duas vezes; nas outras telas, só Enter) e `sudo reboot`.
>
> No terminal do seu computador valem as pegadinhas do ABNT2: `~` e `^` são **teclas mortas** (aperte e depois **Espaço**; apertar duas vezes dá `~~`); `|` é **Shift + `\`**, a tecla ao lado do `Z`; `/` fica ao lado do Shift direito.

## 4. Primeiro login

Depois de reiniciar, a tela mostra várias mensagens e, no meio delas, `bootcamp login:`. **Aperte Enter** se o cursor ficar escondido atrás das mensagens.

Digite `aluno`, dê Enter, digite a senha e dê Enter — **a senha não aparece enquanto você digita, nem asteriscos. É normal!**

Se você está vendo isto, o Ubuntu está instalado:

```text
aluno@bootcamp:~$
```

## 5. Valide a conexão com a internet

Antes de seguir, confirme que a VM enxerga a internet — sem isso, nenhuma prática do bootcamp funciona (instalação de pacotes, Docker, GitHub...). Ainda na janela da VM, digite (este comando só usa letras, números, ponto e hífen — funciona mesmo com o teclado em US):

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

### 6.1 Instale o servidor SSH na VM

A instalação automática não traz o OpenSSH. Ainda na janela da VM (os comandos só usam letras e hífen):

```bash
sudo apt update
sudo apt install -y openssh-server
```

Em `[sudo] password for aluno:` digite sua senha (invisível) e Enter. Resultado esperado: várias linhas e, no fim, algo como `Setting up openssh-server` — sem mensagens de erro.

### 6.2 Abra uma "porta" entre o seu computador e a VM

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

### 6.3 Conecte-se

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
| A **instalação automática parou com erro** ou pediu para você escolher coisas | Confira se a ISO é a **Server** certa para o seu processador (passo 1) e se *Skip Unattended Installation* ficou **desmarcado**. Apague a VM (botão direito → **Remover** → **Apagar todos os arquivos**) e recrie pelo passo 2 |
| `ssh: connect to host localhost port 2222: Connection refused` | OpenSSH não instalado (passo 6.1), regra de redirecionamento não salva (passo 6.2) ou VM desligada |
| `Permission denied, please try again` no SSH | Senha errada (lembre: nada aparece ao digitar). Confira também se digitou `aluno` |
| `~` não aparece / sai `~~` | Tecla morta do ABNT2: aperte `~` e depois **Espaço** |
| Na janela da VM, `/`, `ç` ou `;` saem trocados | O console está com teclado US (instalação automática). Use o SSH — ou corrija com `sudo dpkg-reconfigure keyboard-configuration` (box do passo 3) |
| Esqueci a senha | Mais rápido: apague a VM (botão direito → **Remover** → **Apagar todos os arquivos**) e recrie pelo passo 2 (~20 min). Anote a nova senha! |
| Sem internet na VM | Adaptador de rede em modo **NAT** (padrão) e internet funcionando no seu computador |
| Teste 8 do roteiro: **menos de 10G livres** | A VM foi criada com um disco menor que 25 GB. Recrie-a pelo passo 2 com **25 GB** |
