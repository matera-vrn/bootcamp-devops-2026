# Prática 08 — Um sistema inteiro com docker compose 🧩

**Objetivo:** declarar um sistema com **dois serviços** — a página do seu projeto + um banco Redis de apoio — e subir tudo com um único comando.

**Onde:** no terminal conectado à VM via SSH (como no [setup](../../setup/instalacao-ubuntu-vm.md)). A janela do VirtualBox também serve, mas sem copiar e colar.

## Passo 1 — Instale o plugin do Compose

```bash
sudo apt update
sudo apt install -y docker-compose-v2
docker compose version
```

Resultado esperado: `Docker Compose version 2.x...`.

## Passo 2 — Declare o sistema

```bash
cd ~/meu-projeto-devops
vi compose.yaml
```

Conteúdo (atenção à indentação — 2 espaços, nunca Tab!):

```yaml
services:
  site:
    build: .
    ports:
      - "8080:80"
    depends_on:
      - visitas

  visitas:
    image: redis:alpine
```

Traduzindo: o serviço `site` é construído do seu `Dockerfile` (Aula 07) e publica a porta 8080; o serviço `visitas` usa a imagem oficial do Redis; o `site` só sobe depois do `visitas`.

## Passo 3 — Suba o sistema inteiro 🚀

```bash
docker compose up -d
docker compose ps
```

Resultado esperado: dois serviços com status `Up`/`running`. Teste a página:

```bash
curl http://localhost:8080
```

E no navegador do seu computador: **http://localhost:8080**.

## Passo 4 — Espie os bastidores

Logs de cada serviço:

```bash
docker compose logs visitas | grep Ready
```

Resultado esperado: a linha `Ready to accept connections tcp` do log do Redis. (Quer ver o log inteiro? `docker compose logs visitas` — o aviso `WARNING Memory overcommit must be enabled!` é inofensivo aqui.)

## Passo 5 — A mágica da rede interna

Os serviços se enxergam **pelo nome**. Prove, entrando no container do site e chamando o `visitas` pelo hostname:

```bash
docker compose exec site ping -c 2 visitas
```

Resultado esperado: o `visitas` responde! O Compose criou uma rede privada com DNS automático — nenhum IP decorado (Aula 03 mandou lembranças 📡).

Grave uma "visita" no Redis, direto pelo serviço:

```bash
docker compose exec visitas redis-cli INCR visitas_do_site
docker compose exec visitas redis-cli GET visitas_do_site
```

Resultado esperado: `(integer) 1` e, no `GET`, `"1"`. Rode o `INCR` mais vezes e veja o contador subir — dados vivendo em um serviço, consultados de fora dele.

## Passo 6 — Derrube tudo (e suba de novo, só para sentir o poder)

```bash
docker compose down
docker compose ps
docker compose up -d
```

Um comando derruba o sistema; outro o recria. **Esse é o superpoder do declarativo**: o arquivo é a verdade, o ambiente é descartável.

E o contador? Confira:

```bash
docker compose exec visitas redis-cli GET visitas_do_site
```

Resultado esperado: `(nil)` — o contador **sumiu**. Não é bug: o container do Redis foi destruído e recriado do zero, e os dados viviam dentro dele. Ambiente descartável, dados descartados. Para dados sobreviverem, usa-se um **volume** — um tema para você explorar depois do bootcamp.

## Passo 7 — Versione a infraestrutura

```bash
git add compose.yaml
git commit -m "adiciona compose.yaml com site e redis"
git log --oneline
```

Seu repositório agora conta a história completa: app, scripts, receita da imagem e a definição do sistema. 📜

## Desafio bônus 🏆

Adicione um terceiro serviço ao `compose.yaml` usando a imagem `traefik/whoami` na porta `8081:80`. Suba com `docker compose up -d` (só o novo serviço será criado!) e teste com `curl http://localhost:8081`.

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `yaml: line X: ...` | Indentação errada — use 2 espaços, remova Tabs |
| `port is already allocated` | Sobrou um container da Aula 07 na 8080: `docker ps` + `docker stop <nome>` |
| `permission denied ... docker.sock` | Sessão sem o grupo docker — saia (`exit`) e conecte de novo por SSH |
| `no configuration file provided: not found` | Rode os comandos de dentro de `~/meu-projeto-devops`, onde está o `compose.yaml` |
| `'compose' is not a docker command` | O plugin não foi instalado — refaça o Passo 1 |
| `pull access denied` | Erro de digitação no nome da imagem (`redis:alpine`) |

## Missão até a próxima aula 📌

Na Aula 09 o seu projeto vai para o GitHub — e criar a conta no meio da aula consome tempo precioso (confirmação de e-mail, verificações). Faça antes:

1. Crie sua conta em **https://github.com/signup** — escolha um nome de usuário profissional: ele aparecerá no seu portfólio.
2. Confirme o e-mail.
3. Recomendado: ative a verificação em duas etapas em *Settings → Password and authentication*.

Já tem conta? Missão cumprida. 😉
