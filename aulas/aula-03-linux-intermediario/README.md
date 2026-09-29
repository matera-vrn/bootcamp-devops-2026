# Aula 03 — Linux 2: Comandos intermediários

> **Objetivo:** dar o próximo passo: permissões, processos, instalação de pacotes, filtros com pipes e os conceitos de rede que todo profissional DevOps precisa dominar (IP, portas, DNS, HTTP).

## 🔁 Revisão da Aula 02 (5 min)

- O Linux domina os servidores do mundo — e o terminal é a língua nativa dele.
- Vocês navegaram (`pwd`, `cd`, `ls`), criaram (`mkdir`, `touch`, `echo >`), leram (`cat`) e organizaram (`cp`, `mv`, `rm`) arquivos.
- Nasceu o `meu-projeto-devops` — ele cresce a cada aula.
- **Gancho:** vocês já sabem andar pela casa. Hoje recebem as **chaves do prédio**: permissões, processos, instalação de programas e rede.

---

## Parte 1 — Virando o síndico do servidor

### 1. Usuários, root e o poderoso `sudo`

- Todo arquivo e processo pertence a um **usuário**.
- O **root** é o superusuário: pode tudo (inclusive destruir tudo).
- `sudo` = *"super user do"*: executa **um** comando como root. Com grandes poderes... você já sabe. 🕷️

### 2. Permissões: quem pode fazer o quê

```text
-rwxr-xr--  1 aluno aluno  120 nov 10 19:40 script.sh
```

| Trecho | Significado |
|--------|-------------|
| `rwx` | o **dono** pode ler (r), escrever (w) e executar (x) |
| `r-x` | o **grupo** pode ler e executar |
| `r--` | os **outros** só podem ler |

- `chmod` muda permissões (ex.: `chmod +x script.sh` torna executável — essencial para a próxima aula!).
- `chown` muda o dono.

> 💬 **Interação:** "Por que será que um arquivo de senha não deve ter `r` para 'outros'?"

### 3. Processos: o que está rodando agora?

- `ps aux` — fotografia de todos os processos.
- `top` — monitor ao vivo (CPU, memória). Sai com `q`.
- `kill <PID>` — encerra um processo pelo número dele.

### 4. Instalando programas com `apt`

No Ubuntu, programas vêm de **repositórios oficiais** via `apt`:

```bash
sudo apt update        # atualiza o catálogo
sudo apt install htop  # instala um pacote
```

> 🔐 **Segurança desde o dia zero:** instalar de repositórios oficiais (em vez de baixar binários de sites aleatórios) é a primeira prática de DevSecOps que você aprende — origem confiável e versões auditadas.

### 5. Superpoderes: pipes e filtros

O `|` (pipe) conecta a saída de um comando à entrada do próximo — é LEGO de comandos:

```bash
ps aux | grep bash          # filtra só o que contém "bash"
cat arquivo | wc -l          # conta linhas
ls -la | grep ".txt"        # só os .txt
```

- `grep` — procura texto (o comando mais usado da sua carreira!)
- `>` grava em arquivo, `>>` acrescenta ao final.

### 6. Redes para DevOps em 4 conceitos

| Conceito | Analogia |
|----------|----------|
| **IP** | O endereço da casa (ex.: `192.168.0.10`) |
| **Porta** | A porta da casa: cada serviço atende em uma (web: 80/443, SSH: 22) |
| **DNS** | A agenda de contatos: traduz `matera.com` em IP |
| **HTTP/HTTPS** | O idioma da conversa web (o S = conversa criptografada 🔒) |

Comandos: `ping` (o servidor responde?), `curl` (faz requisições HTTP), `ip a` (qual meu IP?).

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: investigar o sistema com pipes, ajustar permissões e conversar com a internet via `curl`.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 04:** "Vocês já executam comandos como profissionais. Mas profissional de DevOps de verdade não digita a mesma sequência duas vezes — ele **automatiza**. Na próxima aula, seus comandos viram **scripts**: o primeiro passo da automação."
