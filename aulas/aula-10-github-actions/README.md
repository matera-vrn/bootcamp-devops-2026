# Aula 10 — GitHub Actions + Encerramento 🏁

> **Objetivo:** fechar o ciclo: a pipeline manual da Aula 05 vira uma pipeline **de verdade**, executada automaticamente pelo GitHub a cada push. E encerrar o bootcamp olhando para frente: DevSecOps, Kubernetes, carreira — e uma surpresa. 🎁

## 🔁 Revisão da Aula 09 (5 min)

- Git local + GitHub remoto: `push`, `pull`, e o fluxo profissional branch → PR → review → merge.
- O `meu-projeto-devops` está público, com README — portfólio no ar.
- **Gancho:** lembra da pipeline manual da Aula 05, em que **você** era o robô? Hoje o robô assume. A cada push, o GitHub builda e testa **sozinho**.

---

## Parte 1 — GitHub Actions: a esteira dentro do repositório

### 1. O que é o GitHub Actions

O serviço de **CI/CD embutido no GitHub**: você descreve a pipeline em um arquivo YAML **dentro do próprio repositório** e o GitHub executa em máquinas dele (os *runners*), de graça para repositórios públicos.

> 💡 A pipeline versionada junto com o código = **a fonte única da verdade da Aula 06 valendo também para a automação**.

### 2. Anatomia de um workflow

O arquivo mora em `.github/workflows/ci.yml`:

```yaml
name: CI                       # nome da pipeline

on:                            # QUANDO rodar (o gatilho)
  push:
    branches: [main]
  pull_request:

jobs:                          # O QUE rodar
  build-e-teste:
    runs-on: ubuntu-latest     # em qual máquina (olha o Linux aí! 🐧)
    steps:                     # os passos, em ordem
      - uses: actions/checkout@v4      # 1) baixa o código do repo
      - name: Build
        run: ./scripts/build.sh        # 2) roda SEU script de build
      - name: Teste
        run: ./scripts/test.sh         # 3) roda SEU script de teste
```

Traduzindo o vocabulário:

| Termo | Significado | Equivalente da Aula 05 |
|-------|-------------|------------------------|
| **workflow** | A pipeline inteira | `pipeline.sh` |
| **trigger (`on`)** | O evento que dispara | você digitando `./pipeline.sh` |
| **job** | Grupo de passos numa máquina | — |
| **step** | Um passo (comando ou action pronta) | `build.sh`, `test.sh` |
| **runner** | A máquina que executa | sua VM |

### 3. O ciclo completo (o que você construiu em 10 aulas!)

```text
git push → GitHub Actions acorda → checkout → build → testes
   → ✅ verde: badge verde no repo, PR liberado para merge
   → ❌ vermelho: e-mail na hora, merge bloqueado, produção protegida
```

Cada peça dessa frase você aprendeu numa aula: Linux (02–04), pipeline (05), Git (06), containers (07–08), GitHub (09). **Hoje tudo se conecta.**

### 4. Segredos na pipeline (DevSecOps na prática)

E quando a pipeline precisa de uma senha (registry, nuvem)? **Nunca no YAML!** O GitHub tem um cofre: *Settings → Secrets and variables → Actions*. No workflow, usa-se `${{ secrets.MINHA_SENHA }}` — o valor nunca aparece nos logs.

### 5. Próximos passos da jornada

- **Kubernetes (K8s):** o compose "adulto" — orquestra containers em **muitas máquinas**, com auto-recuperação e escala automática. É o padrão da indústria (e o dia a dia na Matera).
- **DevSecOps:** segurança desde o dia zero — scanners de vulnerabilidade e de segredos **como stages da pipeline**.
- **Infraestrutura como Código (Terraform), observabilidade (métricas, logs, traces), nuvem (AWS/Azure/GCP)** — cada um dá um bootcamp inteiro.

### 6. Carreira e comunidade

- Seu diferencial ao final de hoje: um repositório público com **projeto funcional e pipeline verde** — mais do que muito candidato júnior tem.
- Poste no LinkedIn marcando a **@Matera** (#BootcampDevOpsMatera) — é o critério do [certificado](../../organizacao/certificado.md) e o começo da sua rede.
- Continuem nos canais da comunidade; as portas do Instituto Matera seguem abertas.

---

## Parte 2 — Mão na massa (a última!)

👉 Siga o **[pratica.md](pratica.md)**: criar o workflow, ver a primeira pipeline verde, quebrar e consertar (blameless até o fim!).

E no encerramento... **[a surpresa final](plot-twist-ia.md)**. 🤖🎁

---

## O que levamos daqui para a vida 🔗

> "Vocês chegaram sem saber o que era um terminal. Saem com Linux, scripts, Git, Docker, GitHub e uma esteira de CI rodando num projeto público de vocês. O loop do DevOps não termina — ele recomeça: **planejem** o próximo aprendizado, **codem**, **testem**, **monitorem** a evolução de vocês. A comunidade fica. Obrigado, e até a próxima! 💙"
