# Roteiro de testes do ambiente ✅

Execute este checklist **depois de instalar a VM** e traga o resultado para a Aula 01. Cada teste valida algo que usaremos durante o bootcamp.

Não se preocupe em entender cada comando agora — é exatamente isso que vamos aprender nas aulas de Linux! 😉 Digite um comando por vez e dê Enter.

## Teste 1 — A VM liga e o login funciona

Na janela do VirtualBox, faça login com o usuário `aluno` e sua senha (lembre: **a senha não aparece enquanto você digita**). Você vê o *prompt* abaixo?

```text
aluno@bootcamp:~$
```

- [ ] Sim, estou logado(a)!

## Teste 2 — O teclado está certo

Os caracteres especiais do terminal precisam sair corretos. Digite exatamente (lembre: `~` é tecla morta no ABNT2 — aperte `~` e depois **Espaço**; `|` é Shift + `\`):

```bash
echo "teclado: ~ | / > ç"
```

Resultado esperado: a linha `teclado: ~ | / > ç` repetida na tela, com todos os símbolos iguais.

- [ ] Todos os símbolos saíram certos

> Saiu trocado? O layout do teclado ficou errado na instalação. Corrija com `sudo dpkg-reconfigure keyboard-configuration` (escolha *Generic 105-key*, *Portuguese (Brazil)*) e reinicie com `sudo reboot`.

## Teste 3 — O sistema é o Ubuntu esperado

```bash
lsb_release -a
```

Resultado esperado: uma linha `Description: Ubuntu 24.04.x LTS`.

- [ ] Versão confirmada

## Teste 4 — Acesso à internet

```bash
ping -c 4 google.com
```

Resultado esperado: 4 linhas de resposta e, no final, `4 received, 0% packet loss`.

- [ ] Internet funcionando

## Teste 5 — Resolução de nomes (DNS) e HTTPS

```bash
curl -I https://www.google.com
```

Resultado esperado: a primeira linha contém `HTTP/2 200` (ou `HTTP/1.1 200 OK`).

- [ ] DNS e HTTPS funcionando

## Teste 6 — Instalação de pacotes

```bash
sudo apt update
```

Digite sua senha quando pedir (de novo: ela não aparece). Resultado esperado: várias linhas terminando **sem mensagens de erro** (avisos em amarelo são OK).

- [ ] `apt` funcionando

## Teste 7 — Espaço em disco

```bash
df -h /
```

Resultado esperado: a coluna `Avail` mostra **pelo menos 15G** disponíveis.

- [ ] Espaço suficiente

> Menos que isso? Veja a última linha de *Problemas comuns* do [guia da VM](instalacao-ubuntu-vm.md).

## Teste 8 — Conexão por SSH a partir do seu computador

Este é o jeito como você vai usar a VM em todas as aulas. Abra o terminal **do seu computador** (Terminal/PowerShell no Windows, Terminal no macOS/Linux) e digite:

```bash
ssh aluno@localhost -p 2222
```

Resultado esperado: depois de `yes` (só na primeira vez) e da senha, o mesmo prompt `aluno@bootcamp:~$` aparece **na janela do seu terminal**. Teste colar algo (Ctrl+V no Windows, Cmd+V no Mac, Ctrl+Shift+V no Linux) e depois saia com `exit`.

- [ ] SSH funcionando e consigo colar

---

## Deu tudo certo? 🎉

Seu ambiente está pronto para o bootcamp! Responda o formulário de confirmação (enviado uma semana antes do início) dizendo que está tudo OK.

## Algo falhou? 😥

Sem pânico — isso também é DevOps! Anote **qual teste falhou** e **a mensagem de erro exata** (foto ou print ajuda muito) e:

1. Consulte a seção *Problemas comuns* dos guias de [instalação do VirtualBox](instalacao-virtualbox.md) e da [VM Ubuntu](instalacao-ubuntu-vm.md).
2. Poste nos canais da comunidade para receber ajuda dos monitores.
3. Informe no formulário de confirmação que precisa de apoio — reservamos um tempo na Aula 01 exatamente para isso.
