# Aula 08 — Docker 2: Docker Compose

> **Objetivo:** sair de "um container" para "um sistema": orquestrar múltiplos containers com um único arquivo declarativo, o `compose.yaml`.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).
>
> 📽️ Slides desta aula: [`slides/aula-08.odp`](slides/aula-08.odp) (roteiro editável em [`slides/aula-08.json`](slides/aula-08.json) — veja [tools/slides](../../tools/slides/README.md)).

## 🔁 Revisão da Aula 07 (5 min)

- Container = a carga na caixa padronizada: roda igual em qualquer lugar.
- Receita (**Dockerfile**) → bolo (**imagem**) → fatia servida (**container**).
- Vocês containerizaram a página do projeto e a serviram com `docker run -p 8080:80`.
- **Gancho:** foi só **um** container. Sistemas de verdade têm app + banco + cache... Subir cada um na mão, com os parâmetros certos, na ordem certa? Hoje um único arquivo faz isso por nós.

---

## Parte 1 — Orquestrando containers

### 1. A dor: o comando que não acaba mais

Imagine subir um sistema com 3 serviços na mão:

```bash
docker run -d --name banco -e SENHA=... -v dados:/var/lib/... rede...
docker run -d --name api -p 3000:3000 --link banco ...
docker run -d --name site -p 8080:80 ...
```

Três comandos gigantes, ordem certa, parâmetros decorados. E amanhã, tudo de novo. 😫

### 2. A solução: declarar em vez de digitar

O **Docker Compose** lê um arquivo `compose.yaml` que **declara** o sistema inteiro — quais serviços, portas, volumes e dependências — e o materializa com um comando:

```bash
docker compose up -d
```

> 💡 **Conceito-chave do DevOps: declarativo vs. imperativo.** Em vez de ditar os passos (imperativo), você descreve **o estado desejado** (declarativo) e a ferramenta faz acontecer. Guarde essa ideia: é a base da Infraestrutura como Código e do Kubernetes.

### 3. Anatomia de um compose.yaml

```yaml
services:            # a lista de containers do sistema
  site:              # nome do serviço (você escolhe)
    build: .         # construa a partir do Dockerfile desta pasta
    ports:
      - "8080:80"    # VM:container — igual ao -p!

  visitas:
    image: redis:alpine   # ou use uma imagem pronta do Hub (Redis: banco de dados em memoria)
```

- **YAML**: formato de texto sensível a **indentação** — os espaços no início de cada linha, que dizem "isto está dentro daquilo" (2 espaços por nível, nunca Tab!).
- Cada serviço = um container. O Compose cria automaticamente uma **rede interna** onde os serviços se enxergam **pelo nome** (`site` acessa `visitas` pelo hostname `visitas` — DNS da Aula 03 em ação!).

### 4. Comandos do dia a dia

| Comando | O que faz |
|---------|-----------|
| `docker compose up -d` | Sobe o sistema inteiro (constrói o que precisar) |
| `docker compose ps` | Situação dos serviços |
| `docker compose logs -f site` | Acompanha os logs de um serviço |
| `docker compose down` | Derruba tudo, limpo |

### 5. Onde isso te leva

- Ambiente de desenvolvimento de um time inteiro: `git clone` + `docker compose up`. Fim do "configura aí que na sexta eu te ajudo".
- O `compose.yaml` vive no Git — **infraestrutura versionada** junto com o código.
- Em produção, essa ideia cresce e vira **Kubernetes** (spoiler da Aula 10!).

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: o projeto ganha um `compose.yaml` com **dois serviços** — sua página e um serviço de apoio — subindo juntos com um comando.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 09:** "Seu projeto tem código, scripts, Dockerfile, compose... tudo commitado. Mas tudo **preso na sua VM**. Se ela morrer, morre junto. E o recrutador, como vê seu trabalho? Na próxima aula seu repositório vai para a nuvem: **GitHub**."
