# Prática 03 — Permissões, processos, pacotes e rede 🔧

**Objetivo:** usar comandos intermediários para investigar o sistema, controlar permissões e falar com a internet — tudo dentro do `meu-projeto-devops`.

**Onde:** no terminal conectado à VM via SSH (como no [setup](../../setup/instalacao-ubuntu-vm.md)). A janela do VirtualBox também serve, mas sem copiar e colar.

## Passo 1 — Instale sua primeira ferramenta

```bash
sudo apt update
sudo apt install -y btop
btop
```

Explore o `btop` (um `top` turbinado e colorido): veja CPU, memória, rede e processos. Saia com `q`.

## Passo 2 — Investigue processos com pipes

```bash
ps aux | grep systemd | head -5
```

Resultado esperado: as 5 primeiras linhas de processos que contêm "systemd". Você acabou de encadear **três** comandos!

Quantos processos estão rodando agora?

```bash
ps aux | wc -l
```

## Passo 3 — Permissões na prática

```bash
cd ~/meu-projeto-devops/scripts
touch teste.sh
ls -l teste.sh
```

Repare: sem `x` nas permissões. Agora:

```bash
chmod +x teste.sh
ls -l teste.sh
```

Resultado esperado: as permissões mudaram de `-rw-rw-r--` para `-rwxrwxr-x`. Esse `x` é o que permitirá **executar** scripts na próxima aula.

## Passo 4 — Descubra seu endereço na rede

```bash
ip a | grep inet
```

Resultado esperado: entre as linhas, algo como `inet 10.0.2.15/24` — o IP da sua VM na rede NAT do VirtualBox.

## Passo 5 — Converse com a internet

O servidor da Matera responde?

```bash
ping -c 3 matera.com
```

Agora uma requisição HTTP de verdade, vendo só os cabeçalhos:

```bash
curl -IL https://www.matera.com | grep HTTP
```

Resultado esperado: algumas linhas de status, a última com `200` (o famoso "OK" do HTTP):

```text
HTTP/2 302
HTTP/2 307
HTTP/2 200
```

O site da Matera responde primeiro com `302` e `307` — códigos que significam *"vá para outro endereço"* (redirecionamento) — e o `-L` do `curl` segue o caminho até chegar ao `200`. O número de linhas pode variar; o que importa é a última. Repare no `https` — conversa criptografada.

## Passo 6 — Grave um relatório do sistema

Combine tudo e gere um arquivo de "diagnóstico" no seu projeto:

```bash
cd ~/meu-projeto-devops
echo "=== Relatorio do sistema ===" > relatorio.txt
date >> relatorio.txt
uptime >> relatorio.txt
df -h / | grep -v Filesystem >> relatorio.txt
cat relatorio.txt
```

Resultado esperado: um arquivo com data, tempo ligado e uso de disco. **Guarde esse encadeamento na memória — ele vira um script na próxima aula!**

## Desafio bônus 🏆

Usando pipes, conte quantos arquivos de configuração `.conf` existem em `/etc`. (Dica: `ls /etc | grep ... | wc -l`). Poste o número no chat!

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `Unable to locate package` | Rode `sudo apt update` antes do `install` |
| `Permission denied` no `apt` | Faltou o `sudo` |
| `ping: Name or service not known` | VM sem internet — confira o adaptador NAT e rode o [roteiro de testes](../../setup/roteiro-de-testes.md) |
| `curl: command not found` | Instale com `sudo apt install -y curl` |

## Missão até a próxima aula 📌

1. Abra o `btop` amanhã e descubra qual processo mais consome memória na sua VM. Depois feche-o com `q`.
2. Investigue com `grep`: quantas linhas do arquivo `/etc/passwd` contêm a palavra `nologin`? (Dica: `grep -c`.)
3. Rode `ls -l /etc | head -20` e tente ler as permissões de três arquivos em voz alta: "dono pode ler e escrever, grupo pode ler...".
