# Prática 07 — Primeiro container e primeira imagem 🐳

**Objetivo:** instalar o Docker na VM, rodar o primeiro container, e containerizar a página do seu projeto com um `Dockerfile`.

**Onde:** no terminal conectado à VM via SSH (como no [setup](../../setup/instalacao-ubuntu-vm.md)). A janela do VirtualBox também serve, mas sem copiar e colar.

## Passo 1 — Instale o Docker

Vamos instalar do repositório oficial do Ubuntu (simples e confiável):

```bash
sudo apt update
sudo apt install -y docker.io docker-buildx
docker --version
```

Resultado esperado: `Docker version 2x.x.x, build ...`.

Para usar o Docker sem `sudo`, adicione seu usuário ao grupo `docker` e **saia e entre de novo** para a mudança valer:

```bash
sudo usermod -aG docker $USER
exit
```

Conecte-se novamente por SSH (`ssh aluno@localhost -p 2222`) e confira:

```bash
groups
```

Resultado esperado: a palavra `docker` aparece na lista.

> 🔐 Quem está no grupo `docker` pode fazer na máquina quase tudo que o root faz. Na VM de estudo, tudo bem — num servidor real, isso é uma decisão de segurança.

## Passo 2 — O "hello world" dos containers

```bash
docker run hello-world
```

Resultado esperado: `Hello from Docker!` — o Docker **baixou** a imagem do Docker Hub e **executou** um container que imprimiu a mensagem e terminou.

Veja o container (já finalizado):

```bash
docker ps -a
```

## Passo 3 — Um servidor web em UM comando

```bash
docker run -d --name meu-nginx -p 8080:80 nginx:alpine
```

Traduzindo: rode em segundo plano (`-d`), com nome `meu-nginx`, ligando a porta **8080 da VM** à porta **80 do container**, usando a imagem oficial `nginx:alpine`.

Teste (lembra do `curl` da Aula 03?):

```bash
curl http://localhost:8080
```

Resultado esperado: o HTML de boas-vindas do nginx. **Você subiu um servidor web em segundos, sem instalar nginx na VM!**

Agora pare e remova:

```bash
docker stop meu-nginx
docker rm meu-nginx
```

## Passo 4 — A receita: seu primeiro Dockerfile

Vamos containerizar a página que a sua pipeline da Aula 05 gera:

```bash
cd ~/meu-projeto-devops
./scripts/build.sh        # garante que app/index.html existe
vi Dockerfile
```

Conteúdo (repare: o nome é `Dockerfile`, com D maiúsculo e sem extensão):

```dockerfile
FROM nginx:alpine
COPY app/index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

## Passo 5 — Construa a imagem

```bash
docker build -t meu-projeto:1.0 .
docker images
```

Resultado esperado: a imagem `meu-projeto` com tag `1.0` na lista. (O `.` final diz "a receita está nesta pasta".)

## Passo 6 — Rode a SUA aplicação em container 🚀

```bash
docker run -d --name meu-projeto -p 8080:80 meu-projeto:1.0
curl http://localhost:8080
```

Resultado esperado: a **sua página** — `Bootcamp DevOps Matera 2026` com a data do build.

Agora o momento **uau**: abra **http://localhost:8080** no navegador do **seu computador**. A página que você gerou com um script, empacotou num container e serviu com nginx — na sua tela (é a regra `WEB` de redirecionamento de porta do setup em ação). Print no chat! 🎉

## Passo 7 — Versione a receita

O Dockerfile é código — e código vive no Git (Aula 06!):

```bash
git add Dockerfile
git commit -m "adiciona Dockerfile da aplicacao"
```

## Passo 8 — Arrume a casa 🧹

Pare e remova o container antes de encerrar — a porta 8080 precisa estar livre na próxima aula:

```bash
docker stop meu-projeto
docker rm meu-projeto
docker ps -a
```

Resultado esperado: lista vazia. A imagem `meu-projeto:1.0` continua guardada (veja com `docker images`) — é o bolo no congelador, pronto para novas fatias.

## Desafio bônus 🏆

Rode um **segundo** container da mesma imagem na porta 8081 (`--name meu-projeto-2 -p 8081:80`). Confirme com `docker ps` e `curl`: duas fatias do mesmo bolo, isoladas, em segundos. Depois limpe tudo (`docker stop` + `docker rm`).

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `permission denied ... docker.sock` | Faltou o `usermod` do Passo 1, ou você ainda não saiu e entrou de novo no SSH (ou use `sudo docker`) |
| `DEPRECATED: The legacy builder is deprecated` | Só um aviso — o build funciona. Ele some instalando o `docker-buildx` (Passo 1) |
| `port is already allocated` | Já existe container na 8080 — `docker ps` e pare o antigo |
| `COPY failed: ... not found` | Rode o `docker build` de dentro de `~/meu-projeto-devops` e gere o `app/index.html` antes (`./scripts/build.sh`) |
| `Unable to find image` demorando | É o download da imagem — normal na primeira vez |

## Missão até a próxima aula 📌

1. Suba o container do projeto de novo (`docker run -d --name meu-projeto -p 8080:80 meu-projeto:1.0`), abra no navegador, e derrube (`docker stop` + `docker rm`). Repita até fazer sem olhar.
2. Explore um Linux dentro do Linux: `docker run --rm -it alpine sh` abre um terminal **dentro** de um container Alpine (uma distribuição minúscula). Rode `ls /` e `cat /etc/os-release` lá dentro e saia com `exit`. Tudo que você aprendeu nas aulas de Linux vale ali também.
