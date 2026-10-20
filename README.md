# Bootcamp DevOps 2026 — Instituto Matera

Bem-vindo(a) ao repositório oficial do **Bootcamp DevOps 2026**! 🚀

Aqui você encontra todo o material do bootcamp: o conteúdo de cada aula, as práticas passo a passo e os guias de preparação do ambiente. Este repositório é a **fonte única da verdade** do bootcamp — exatamente como o Git deve ser no dia a dia de um profissional DevOps.

## 🎯 Objetivo

Levar você **do zero ao primeiro deploy automatizado**: ao final das 10 aulas, você terá construído um mini-projeto completo com Linux, Shell Script, Git, Docker, GitHub e uma pipeline de CI com GitHub Actions — tudo publicado no seu próprio GitHub, pronto para virar portfólio.

## 📅 Grade das aulas

> As aulas acontecem em **novembro de 2026**, de 3 a 18/11, sempre ao vivo das **19:30 às 21:45**.

| Aula | Data | Tema | Parte 1 (conceitos) | Parte 2 (prática) |
|------|------|------|---------------------|-------------------|
| [01](aulas/aula-01-devops-overview/) | 03/11 (ter) | DevOps: Overview + Comunidades | O que é DevOps, cultura, ciclo de vida | Boas-vindas + apoio à configuração do ambiente |
| [02](aulas/aula-02-linux-basico/) | 04/11 (qua) | Linux 1: História + Comandos básicos | Por que o Linux domina o DevOps | Primeiros comandos no terminal |
| [03](aulas/aula-03-linux-intermediario/) | 05/11 (qui) | Linux 2: Comandos intermediários | Permissões, processos, pacotes e redes | `grep`, pipes, `apt`, `curl` e companhia |
| [04](aulas/aula-04-linux-shell-script/) | 06/11 (sex) | Linux 3: Shell Script | Automatizando tarefas com scripts | Seu primeiro script de health check |
| [05](aulas/aula-05-devops-pipelines/) | 10/11 (ter) | DevOps: Esteiras e Pipelines | O que é CI/CD e por que ele existe | Dinâmica: montando uma pipeline "manual" |
| [06](aulas/aula-06-git/) | 11/11 (qua) | Git | Controle de versão e fonte única da verdade | `init`, `commit`, `branch` e `merge` |
| [07](aulas/aula-07-docker/) | 12/11 (qui) | Docker 1: Overview + Comandos | Containers vs. VMs | `docker run` e seu primeiro `Dockerfile` |
| [08](aulas/aula-08-docker-compose/) | 13/11 (sex) | Docker 2: Docker Compose | Orquestrando múltiplos containers | Subindo app + serviço com `docker compose` |
| [09](aulas/aula-09-github/) | 17/11 (ter) | GitHub | Remotos, colaboração e portfólio | Publicando seu projeto + primeiro Pull Request |
| [10](aulas/aula-10-github-actions/) | 18/11 (qua) | GitHub Actions + Encerramento | CI na prática, DevSecOps e próximos passos | Sua primeira pipeline no GitHub + surpresa final 🎁 |

## 🕒 Formato das aulas

| Horário | Atividade |
|---------|-----------|
| 19:30 – 19:35 | Abertura, boas-vindas e avisos ("Energia Matera") |
| 19:35 – 20:20 | **Parte 1** — Conceitos e analogias |
| 20:20 – 20:35 | Intervalo ☕ |
| 20:35 – 21:20 | **Parte 2** — Mão na massa |
| 21:20 – 21:45 | Perguntas & Respostas |
| 21:45 | Encerramento pontual |

A partir da Aula 02, cada aula começa com uma **revisão rápida da aula anterior**, conectando o que você já aprendeu com o conteúdo do dia.

## 🖥️ Antes de começar: prepare seu ambiente

Todas as práticas rodam em uma **máquina virtual Ubuntu no VirtualBox**, para que todo mundo — Windows, Linux ou macOS — tenha exatamente o mesmo ambiente.

👉 **Siga o guia em [`setup/`](setup/) antes da primeira aula.** Uma semana antes do início enviaremos um formulário para confirmar que seu ambiente está pronto. Na Aula 01 haverá um momento dedicado a ajudar quem tiver dificuldades.

## 📂 Como usar este repositório

- [`aulas/`](aulas/) — uma pasta por aula, com o resumo do conteúdo (`README.md`) e a prática passo a passo (`pratica.md`).
- [`organizacao/`](organizacao/) — materiais de organização do bootcamp (formato das lives, checklist, certificado).
- [`glossario.md`](glossario.md) — os termos do bootcamp explicados em uma linha. Apareceu uma palavra estranha? Comece por aqui.
- [`recursos/`](recursos/) — a [cola de comandos do terminal](recursos/cheat-sheet-terminal.md) para imprimir e o guia [continuando com Linux](recursos/continuando-com-linux.md) para manter o hábito depois do bootcamp, e a [micro aula de vi](recursos/micro-aula-vi.md), o editor usado em todas as práticas.

## 🏅 Certificado

Para receber o certificado do Instituto Matera, ao final do bootcamp você deverá **publicar no LinkedIn o projeto prático** que desenvolveu ao longo das aulas, marcando a **@Matera**. Detalhes em [`organizacao/certificado.md`](organizacao/certificado.md).

## 🤝 Comunidade

Você não está sozinho(a): teremos canais de comunidade com monitores voluntários da Matera para tirar dúvidas entre as aulas. Participe, pergunte e compartilhe — **não existe pergunta boba**. Errar faz parte do aprendizado (é a cultura *blameless* que você vai conhecer na Aula 01 😉).
