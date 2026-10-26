# Aula 05 — DevOps: Esteiras e Pipelines

> **Objetivo:** entender de verdade o que é CI/CD e o conceito de esteira (pipeline) — e sentir na pele, montando uma pipeline "manual" com os scripts que vocês já sabem escrever.
>
> 📖 Apareceu uma palavra nova? Consulte o [glossário](../../glossario.md).
>
> 📽️ Slides desta aula: [`slides/aula-05.odp`](slides/aula-05.odp) (roteiro editável em [`slides/aula-05.json`](slides/aula-05.json) — veja [tools/slides](../../tools/slides/README.md)).

## 🔁 Revisão da Aula 04 (5 min)

- Comandos viraram **scripts**: shebang, variáveis, `if`, `for`, códigos de saída.
- O `healthcheck.sh` verifica a VM em segundos e guarda histórico em log.
- `set -e`: em automação, **falhar rápido é uma virtude**.
- **Gancho:** um script automatiza uma tarefa. Uma **esteira** automatiza o caminho inteiro do código até produção. Hoje entramos no coração do DevOps.

---

## Parte 1 — A esteira que mudou a indústria de software

### 1. A dor: o "dia do deploy"

Antes do CI/CD: meses de código acumulado, integração na véspera, deploy de madrugada, todo mundo rezando. Quando quebrava (e quebrava), começava a caça ao culpado.

> 💬 **Interação:** "O que pode dar errado quando 10 pessoas juntam 3 meses de código de uma vez só? Joga no chat!"

### 2. CI — Integração Contínua

**Integrar pouco, integrar sempre.** Cada mudança de código entra no repositório várias vezes ao dia e, a cada entrada, um robô:

1. Pega o código
2. **Builda** (compila/empacota)
3. **Testa** automaticamente
4. Avisa imediatamente se algo quebrou

Erro descoberto em 5 minutos custa quase nada. O mesmo erro descoberto em produção custa caro — em dinheiro e em sono. 😴

### 3. CD — Entrega/Implantação Contínua

- **Entrega Contínua (Continuous Delivery):** toda versão que passa na esteira fica **pronta para produção** — o deploy é uma decisão de negócio, a um clique.
- **Implantação Contínua (Continuous Deployment):** nem clique precisa — passou nos testes, vai pro ar.

### 4. A analogia da esteira de fábrica 🏭

Uma fábrica moderna não monta um carro inteiro e só no final verifica se ele liga. Cada estação da esteira **verifica e agrega valor**; se algo está errado, a esteira **para na hora** (o *andon* da Toyota — que inspirou o DevOps!).

No software, a esteira (pipeline) tem estações chamadas **stages**:

```text
[ Código ] → [ Build ] → [ Testes ] → [ Qualidade/Segurança ] → [ Deploy ]
```

- Cada stage só roda se o anterior **passou** (lembra dos códigos de saída da Aula 04? São eles que decidem!).
- Pipeline **verde** ✅ = pode confiar. Pipeline **vermelha** ❌ = pare e conserte antes de seguir.

### 5. Qualidade antes de ir para o ar

O que uma esteira verifica na vida real:

| Verificação | Pergunta que responde |
|-------------|----------------------|
| Build | O código sequer compila/empacota? |
| Testes automatizados | O que funcionava continua funcionando? |
| Análise estática (lint) | O código segue os padrões? |
| Segurança (DevSecOps) | Há dependências vulneráveis? Segredos vazados no código? |

### 6. Ferramentas de mercado

Jenkins, GitHub Actions, GitLab CI, Tekton, CircleCI... **Os conceitos são os mesmos em todas.** No bootcamp usaremos o **GitHub Actions** (Aula 10) — gratuito e acessível. Aprenda o conceito e você troca de ferramenta em uma semana.

---

## Parte 2 — Dinâmica: a pipeline manual

👉 Siga o **[pratica.md](pratica.md)**: vamos construir uma esteira de verdade — build, teste e deploy — onde **cada stage é um script** e a esteira para se algum falhar. Hoje o robô é você. Na Aula 10, o GitHub assume. 🤖

---

## O que levamos para a próxima aula 🔗

> **Gancho para a Aula 06:** "Nossa esteira já funciona... mas ela roda em cima de **qual versão do código**? Se dois colegas mudarem o mesmo arquivo, quem vence? Sem controle de versão não existe CI/CD. Na próxima aula: **Git**, a fonte única da verdade."
