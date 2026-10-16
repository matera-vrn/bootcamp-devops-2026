# Aula 01 — DevOps: Overview + Comunidades

> **Objetivo:** nivelar todos os participantes. Explicar por que o DevOps nasceu, a dor que ele cura e por que o mercado paga tão bem por isso. Garantir que todos saiam com o ambiente funcionando.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).

## Agenda

| Horário | Atividade |
|---------|-----------|
| 19:30 | Abertura, boas-vindas e "Energia Matera" |
| 19:35 | Parte 1 — O Mindset DevOps |
| 20:20 | Intervalo |
| 20:35 | Parte 2 — Apoio à configuração do ambiente + roteiro de testes |
| 21:20 | Perguntas & Respostas |
| 21:45 | Encerramento |

---

## Parte 1 — O Mindset DevOps: muito além das ferramentas

### 1. A história de uma rivalidade

Era uma vez duas equipes na mesma empresa:

- **Desenvolvimento (Dev):** quer entregar funcionalidades novas, rápido. Mudança é o seu trabalho.
- **Operações (Ops):** quer o sistema estável, no ar, sem sustos. Mudança é o seu maior risco.

Resultado: o Dev "joga o código por cima do muro" e o Ops segura o deploy com medo de quebrar tudo. Cada incidente vira caça ao culpado. Entregas que deveriam levar dias levam meses.

> 💬 **Interação:** "Quem aqui já ouviu (ou disse) *'no meu ambiente funciona, o problema é do servidor'*?"

### 2. O que é DevOps, afinal?

**DevOps não é um cargo, nem uma ferramenta — é uma cultura.** É a decisão de derrubar o muro entre Dev e Ops e fazer as duas pontas trabalharem como **um time só**, responsáveis juntas pelo produto: do código à produção.

Os pilares:

- **Cultura e comunicação:** todos falam a mesma língua e olham para o mesmo objetivo.
- **Empatia e quebra de silos:** o Dev entende a dor de operar; o Ops entende a dor de entregar.
- **Automação:** tudo que é repetitivo e manual vira código (spoiler das próximas aulas!).
- **Cultura blameless:** quando algo quebra, a pergunta é *"o que no processo permitiu esse erro?"* — nunca *"quem errou?"*. Post-mortem (a análise feita depois de um incidente) sem culpados.

### 3. O ciclo de vida DevOps ♾️

O famoso "loop infinito":

**Planejar → Codificar → Buildar → Testar → Liberar → Implantar → Operar → Monitorar** → (e volta ao planejar)

Desmistificando os termos que você vai ouvir o bootcamp inteiro:

| Termo | Tradução para humanos |
|-------|-----------------------|
| **CI** (Integração Contínua) | Integrar e testar o código várias vezes ao dia, automaticamente |
| **CD** (Entrega Contínua) | Deixar cada versão pronta para ir ao ar com um clique (ou nenhum) |
| **Pipeline / Esteira** | A sequência automatizada de etapas que o código percorre até produção |
| **Build** | Montar/empacotar o programa a partir do código |
| **Deploy** | Colocar uma versão do sistema no ar |

### 4. Por que o mercado paga tão bem?

Empresas que dominam DevOps entregam **mais rápido, com menos erro e mais segurança**. Na Matera, sistemas financeiros processam milhões de transações — sem automação, cultura e monitoramento, isso simplesmente não funciona em escala. Profissionais que sabem construir e operar essas esteiras são disputados.

### 5. Comunidades: ninguém aprende DevOps sozinho

- O ecossistema é gigante e muda rápido — comunidade é como você se mantém atualizado.
- Onde participar: comunidades locais e online de DevOps e Cloud, eventos e meetups, os canais deste bootcamp.
- **Nosso combinado:** usem os canais do bootcamp! Pergunta boba não existe; quem pergunta aprende e ajuda os outros a aprender.

---

## Parte 2 — Ambiente funcionando é a primeira entrega!

Na prática de hoje, vamos garantir que **todo mundo** saia com a VM Ubuntu validada — nosso laboratório para as próximas 9 aulas.

👉 Siga o passo a passo em **[pratica.md](pratica.md)**.

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 02:** "Hoje vocês viram que DevOps é cultura + automação. Mas toda automação roda em cima de um sistema operacional — e em 9 de cada 10 servidores do mundo, esse sistema é o **Linux**. Amanhã a tela preta deixa de ser assustadora e vira sua ferramenta de trabalho."
