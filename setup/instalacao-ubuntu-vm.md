# Criando a máquina virtual Ubuntu

Com o VirtualBox instalado, agora vamos criar a VM com **Ubuntu Server LTS** — a distribuição Linux que usaremos em todas as práticas.

> 💡 Usamos a versão **Server** porque ela é leve (não tem interface gráfica) e porque o terminal é exatamente o ambiente que um profissional DevOps usa no dia a dia. Sem medo da tela preta — ela vai virar sua melhor amiga. 🖥️

## 1. Baixe a imagem oficial do Ubuntu (.iso)

Baixe **somente do espelho oficial de downloads do Ubuntu**:

👉 **https://releases.ubuntu.com/**

1. Entre na pasta da versão **LTS mais recente** (ex.: `24.04`).
2. Baixe o arquivo **`ubuntu-24.04.x-live-server-amd64.iso`** (~2,5 GB).

> A página oficial de download do Ubuntu Server (https://ubuntu.com/download/server) leva para o mesmo arquivo.

### Verifique a integridade do arquivo (recomendado)

No mesmo diretório do espelho há um arquivo `SHA256SUMS`. Confira se o hash do arquivo baixado bate com o oficial — isso garante que o download não veio corrompido nem adulterado:

- **Windows (PowerShell):** `Get-FileHash .\ubuntu-24.04.x-live-server-amd64.iso -Algorithm SHA256`
- **Linux/macOS:** `sha256sum ubuntu-24.04.x-live-server-amd64.iso` (no macOS: `shasum -a 256`)

Compare o resultado com a linha correspondente do `SHA256SUMS`. Guia oficial de verificação: https://ubuntu.com/tutorials/how-to-verify-ubuntu

## 2. Crie a VM no VirtualBox

1. Abra o VirtualBox e clique em **Nova** (*New*).
2. Preencha:
   - **Nome:** `bootcamp-devops`
   - **ISO Image:** selecione o arquivo `.iso` baixado
   - Se aparecer a opção **Skip Unattended Installation**, **marque-a** (vamos instalar manualmente para aprender!)
3. **Hardware:**
   - Memória: **2048 MB** (ou 4096 MB se seu computador tiver 16 GB de RAM)
   - Processadores: **2 CPUs**
4. **Disco:** 20 GB (padrão, alocado dinamicamente).
5. Conclua e clique em **Iniciar** (*Start*).

## 3. Instale o Ubuntu

A instalação é guiada por um assistente em modo texto (use as setas, `Tab` e `Enter` para navegar). Guia oficial passo a passo:

👉 **https://ubuntu.com/tutorials/install-ubuntu-server**

Sugestões para o bootcamp:

| Tela | O que escolher |
|------|----------------|
| Idioma | English (evita problemas de codificação) ou Português |
| Teclado | Portuguese (Brazil) — teste as teclas `ç` e acentos |
| Tipo de instalação | Ubuntu Server (padrão) |
| Rede / Proxy / Espelho | Deixe o padrão |
| Disco | Use o disco inteiro (padrão) — é o disco *virtual*, seus arquivos estão seguros |
| Seu perfil | Nome: seu nome · Servidor: `bootcamp` · Usuário: escolha um simples (ex.: `aluno`) · **Senha: anote! Você vai usá-la em todas as aulas** |
| SSH | Marque **Install OpenSSH server** |
| Snaps adicionais | Não selecione nenhum |

Ao final, escolha **Reboot Now**. Se a tela pedir para remover a mídia de instalação, apenas pressione `Enter`.

## 4. Primeiro login

Depois de reiniciar, aparecerá `bootcamp login:`. Digite seu usuário e senha (a senha não aparece enquanto você digita — é normal!).

Se você viu algo como:

```text
aluno@bootcamp:~$
```

**Parabéns, sua VM está pronta!** 🎉

Próximo passo: **[roteiro de testes](roteiro-de-testes.md)** para validar o ambiente.

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| VM muito lenta | Aumente memória/CPUs nas configurações da VM (com ela desligada). |
| Tela preta ao iniciar | Verifique se a virtualização (VT-x/AMD-V) está habilitada na BIOS/UEFI. |
| Esqueci a senha | Mais rápido: reinstalar a VM (leva ~15 min). Anote a nova senha! |
| Sem internet na VM | Confira se o adaptador de rede da VM está em modo **NAT** (padrão). |
