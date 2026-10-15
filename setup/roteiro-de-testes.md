# Roteiro de testes do ambiente ✅

Execute este checklist **depois de instalar a VM** e traga o resultado para a Aula 01. Cada teste valida algo que usaremos durante o bootcamp.

Faça login na VM e digite os comandos abaixo, um por vez. Não se preocupe em entender cada comando agora — é exatamente isso que vamos aprender nas aulas de Linux! 😉

## Teste 1 — A VM liga e o login funciona

Você consegue fazer login e ver o *prompt*?

```text
aluno@bootcamp:~$
```

- [ ] Sim, estou logado(a)!

## Teste 2 — O sistema é o Ubuntu esperado

```bash
lsb_release -a
```

Resultado esperado: uma linha `Description: Ubuntu 24.04.x LTS` (ou a versão LTS que você instalou).

- [ ] Versão confirmada

## Teste 3 — Acesso à internet

```bash
ping -c 4 google.com
```

Resultado esperado: 4 linhas de resposta e, no final, `4 received, 0% packet loss`.

- [ ] Internet funcionando

## Teste 4 — Resolução de nomes (DNS) e HTTPS

```bash
curl -I https://www.google.com
```

Resultado esperado: a primeira linha contém `HTTP/2 200` (ou `HTTP/1.1 200 OK`).

- [ ] DNS e HTTPS funcionando

## Teste 5 — Instalação de pacotes

```bash
sudo apt update
```

Digite sua senha quando pedir. Resultado esperado: várias linhas terminando **sem mensagens de erro** (avisos em amarelo são OK).

- [ ] `apt` funcionando

## Teste 6 — Espaço em disco

```bash
df -h /
```

Resultado esperado: a coluna `Avail` mostra **pelo menos 20G** disponíveis.

- [ ] Espaço suficiente

---

## Deu tudo certo? 🎉

Seu ambiente está pronto para o bootcamp! Responda o formulário de confirmação (enviado uma semana antes do início) dizendo que está tudo OK.

## Algo falhou? 😥

Sem pânico — isso também é DevOps! Anote **qual teste falhou** e **a mensagem de erro exata** (foto ou print ajuda muito) e:

1. Consulte a seção *Problemas comuns* dos guias de [instalação do VirtualBox](instalacao-virtualbox.md) e da [VM Ubuntu](instalacao-ubuntu-vm.md).
2. Poste nos canais da comunidade para receber ajuda dos monitores.
3. Informe no formulário de confirmação que precisa de apoio — reservamos um tempo na Aula 01 exatamente para isso.
