# Aula 07 — Docker 1: Overview + Comandos

> **Objetivo:** resolver o clássico *"na minha máquina funciona"*. Entender o que são containers, a diferença real entre container e máquina virtual, e rodar os primeiros containers com Docker.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).
>
> 📽️ Slides desta aula: [`slides/aula-07.odp`](slides/aula-07.odp) (roteiro editável em [`slides/aula-07.json`](slides/aula-07.json) — veja [tools/slides](../../tools/slides/README.md)).

## 🔁 Revisão da Aula 06 (5 min)

- Git = fonte única da verdade: `add` → `commit` → histórico para sempre; branches para experimentar, merge para integrar.
- O `meu-projeto-devops` agora tem linha do tempo própria.
- **Gancho:** o código está versionado... mas rodar na máquina do colega ainda é loteria: versão de sistema, bibliotecas, configurações. Hoje empacotamos **o ambiente inteiro junto com o código**: containers! 🐳

---

## Parte 1 — O poder dos containers

### 1. A dor: "na minha máquina funciona"

O app funciona na máquina do dev, quebra no servidor. Por quê? Porque o **ambiente** é diferente: outra versão de linguagem, outra biblioteca, outro sistema. O código viajou, mas o ambiente ficou para trás.

### 2. A analogia dos navios cargueiros 🚢

Antes dos anos 1950, cada carga era embarcada do seu jeito: sacas, barris, caixas — lento, caro, quebrava tudo. Aí veio o **contêiner padronizado**: não importa o que tem dentro, todo navio, trem, caminhão e guindaste do mundo sabe transportá-lo.

**Docker fez isso com software:** sua aplicação + todas as dependências dentro de uma "caixa padrão" que roda **igual** em qualquer lugar — na sua VM, no servidor da empresa, na nuvem.

### 3. Container vs. Máquina Virtual

| | Máquina Virtual | Container |
|---|---|---|
| O que carrega | Sistema operacional **inteiro** + app | Só o app + dependências |
| Tamanho | Gigabytes | Megabytes |
| Inicia em | Minutos | Segundos |
| Isolamento | Hardware virtual completo | Processos isolados pelo kernel |

- A **VM** é uma **casa completa**: fundação, encanamento, tudo próprio (vocês construíram uma no setup!).
- O **container** é um **apartamento**: isolado e com sua fechadura, mas compartilhando a estrutura do prédio (o kernel do Linux).

> 💡 Lembra da Aula 02? Containers **são tecnologia do kernel Linux** — por isso o Linux veio primeiro no bootcamp.

### 4. Os três conceitos do Docker

| Conceito | Analogia | Definição |
|----------|----------|-----------|
| **Dockerfile** | A receita 📝 | Texto com o passo a passo para montar o ambiente |
| **Imagem** | O bolo pronto congelado 🎂 | Pacote imutável construído a partir da receita |
| **Container** | A fatia servida 🍰 | Uma imagem em execução (pode haver várias ao mesmo tempo!) |

E o **Docker Hub** é a "padaria pública": um registro com milhares de imagens prontas (`ubuntu`, `nginx`, `python`...).

### 5. Anatomia de um Dockerfile

```dockerfile
FROM nginx:alpine                        # comece da imagem oficial do nginx (um servidor web)
COPY index.html /usr/share/nginx/html/   # copie meu app para dentro
EXPOSE 80                                # documente a porta usada
```

### 6. Comandos essenciais

| Comando | O que faz |
|---------|-----------|
| `docker run <imagem>` | Baixa (se preciso) e executa um container |
| `docker ps` / `docker ps -a` | Containers rodando / todos |
| `docker build -t nome .` | Constrói uma imagem a partir do Dockerfile |
| `docker stop` / `docker rm` | Para / remove um container |
| `docker images` | Lista as imagens locais |
| `-p 8080:80` | **Publica portas**: porta 8080 da VM → porta 80 do container |

> 🔢 Lembra de IP e portas da Aula 03? O `-p externa:interna` é a ponte entre o mundo e o container.

---

## Parte 2 — Mão na massa

👉 Siga o **[pratica.md](pratica.md)**: instalar o Docker na VM, rodar o primeiro container e **containerizar a página do seu projeto** com um Dockerfile.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 08:** "Um container, fácil. Mas sistemas reais têm vários: o app, o banco de dados, o cache... Subir cada um na mão, na ordem certa? Ninguém merece. Na próxima aula, um único arquivo orquestra tudo: **docker compose**."
