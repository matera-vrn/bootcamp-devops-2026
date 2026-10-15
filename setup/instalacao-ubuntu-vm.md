# Criando a máquina virtual Ubuntu

Com o VirtualBox instalado, agora vamos criar a VM com **Ubuntu Server LTS** — a distribuição Linux que usaremos em todas as práticas.

> 💡 Usamos a versão **Server** porque ela é leve (não tem interface gráfica) e porque o terminal é exatamente o ambiente que um profissional DevOps usa no dia a dia. Sem medo da tela preta — ela vai virar sua melhor amiga. 🖥️

## 1. Baixe a imagem oficial do Ubuntu (.iso)

Baixe **somente do espelho oficial de downloads do Ubuntu**:

👉 **https://releases.ubuntu.com/**

1. Entre na pasta da versão **LTS mais recente** (ex.: `24.04`).
2. Baixe o arquivo **`ubuntu-24.04.x-live-server-amd64.iso`** (ex.: `ubuntu-24.04.5-live-server-amd64.iso`) (~3,2 GB).

> A página oficial de download do Ubuntu Server (https://ubuntu.com/download/server) leva para o mesmo arquivo.

### Verifique a integridade do arquivo (recomendado)

No mesmo diretório do espelho há um arquivo `SHA256SUMS`. Confira se o hash do arquivo baixado bate com o oficial — isso garante que o download não veio corrompido nem adulterado:

- **Windows (PowerShell):** `Get-FileHash .\ubuntu-24.04.x-live-server-amd64.iso -Algorithm SHA256`
- **Linux/macOS:** `sha256sum ubuntu-24.04.x-live-server-amd64.iso` (no macOS: `shasum -a 256`)

Compare o resultado com a linha correspondente do `SHA256SUMS`. Guia oficial de verificação: https://ubuntu.com/tutorials/how-to-verify-ubuntu

## 2. Crie a VM no VirtualBox

1. Abra o VirtualBox e clique em **Nova** (*New*).
2. **Preencha - Virtual machine name and operating systems**
   - **Nome:** (*VM Name*) `bootcamp-devops`
   - **Diretório:** (*VM Folder*) `/home/seu.usuario/VirtualBox VMs`
   - **ISO Image:** selecione o arquivo `.iso` baixado (ex.: `ubuntu-24.04.5-live-server-amd64.iso`)
   - Se aparecer a opção **Skip Unattended Installation**, **marque-a** (vamos instalar manualmente para aprender!)
3. **Usuário e Senha - Set up unattended guest OS installation**
   - User Name: **aluno**
   - Password: ************ (*Digite sua senha*)
   - Confirm Password: ************ (*Digite sua senha*)
4. **Hardware - Specify virtual hardware:**
   - Memória: **2048 MB** (ou 4096 MB se seu computador tiver 16 GB de RAM)
   - Processadores: **2 CPUs**
5. **Disco - Specify virtual Hard** 
   - Disk Size: **20 GB** (padrão, alocado dinamicamente).
6. Conclua e clique em **Finalizar** (*Finish*).
7. Selecione a opção:
   - `*Try or Install Ubuntu` e aguarde finalizar a instalação.

## 3. Primeiro login

Depois de reiniciar, aparecerá `bootcamp login:`. Digite seu usuário e senha (a senha não aparece enquanto você digita e é normal!).

Se você viu algo como:

```text
aluno@bootcamp-devops:~$
```

## 4. Acessar a VM via SSH pelo Terminal

A forma padrão de trabalhar com servidores ou VMs sem modo gráfico é conectar-se a eles pelo terminal da sua própria máquina usando SSH. Dessa forma, você usa o terminal nativo do seu sistema para copiar e colar livremente.

1. Instalar o serviço SSH na VM, no terminal da VM, rode:
```text
sudo apt update
[sudo] password for aluno: *************
sudo apt install openssh-server -y
```

**Configurar o Redirecionamento de Portas no VirtualBox**

2. No menu do VirtualBox, vá em Configurações da VM > Rede.
3. Com a placa configurada como **NAT**, clique no menu **Expert** > **Rede** (Network) > **Redirecionamento de Portas** (Port Forwarding).
4. Adicione uma regra com os valores:
- Nome: SSH
- Protocolo: TCP
- Porta do Hospedeiro (Host Port): 2222
- Porta do Convidado (Guest Port): 22
- Clique em OK para salvar.

5. Conectar pelo terminal da sua própria máquina.
- Abra o Terminal (Linux/Mac) ou o PowerShell/CMD (Windows) na sua máquina real e digite:
```text
$ ssh aluno@localhost -p 2222
The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is SHA256:aBcdeFghIjKLmNoPqRSTuvXwZabcDeFghijKLMNoPqRsT.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2222' (ED25519) to the list of known hosts.
aluno@localhost's password:
```
>🐧 A partir de agora, você estará controlando a VM diretamente da sua janela de terminal principal, podendo copiar e colar normalmente com Ctrl + Shift + V ou clicando com o botão direito.

**Parabéns, sua VM está pronta!** 🎉

## 5. Valide a conexão com a internet

Antes de seguir adiante, confirme que a VM enxerga a internet — sem isso, nenhuma prática do bootcamp funciona (instalação de pacotes, Docker, GitHub...). Ainda logado(a) na VM, digite:

```bash
ping -c 4 ubuntu.com
```

Resultado esperado: 4 respostas e, no final, `4 received, 0% packet loss`.

```text
64 bytes from ubuntu.com ...: icmp_seq=1 ttl=... time=...ms
...
4 packets transmitted, 4 received, 0% packet loss
```

- ✅ **Recebeu respostas?** Internet OK — siga para o roteiro de testes.
- ❌ **`Name or service not known` ou 100% packet loss?** A VM está sem rede. Desligue a VM, abra **Configurações → Rede** no VirtualBox e confirme que o adaptador está **habilitado** e em modo **NAT**. Ligue a VM e teste de novo. Se persistir, veja se o computador (host) está com internet e chame os monitores no canal `#setup-ambiente`.

Próximo passo: **[roteiro de testes](roteiro-de-testes.md)** para validar o ambiente completo.

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| VM muito lenta | Aumente memória/CPUs nas configurações da VM (com ela desligada). |
| Tela preta ao iniciar | Verifique se a virtualização (VT-x/AMD-V) está habilitada na BIOS/UEFI. |
| Esqueci a senha | Mais rápido: reinstalar a VM (leva ~15 min). Anote a nova senha! |
| Sem internet na VM | Confira se o adaptador de rede da VM está em modo **NAT** (padrão). |
