# Prática 05 — Montando uma pipeline manual 🏭

**Objetivo:** construir uma esteira com 3 stages — **build**, **teste** e **deploy** — onde cada stage é um script e a esteira **para no primeiro erro**. É exatamente assim que uma pipeline de verdade funciona; a diferença é que na Aula 10 quem vai apertar o botão é o GitHub.

**Onde:** dentro da VM Ubuntu, no `~/meu-projeto-devops`.

## O cenário

Nossa "aplicação" é simples de propósito: uma página `index.html`. A esteira vai **montá-la** (build), **verificá-la** (teste) e **publicá-la** (deploy) em uma pasta que simula o servidor de produção.

> ⌨️ Os quatro scripts usam só caracteres do teclado (sem emoji nem acento). Digite com calma ou, se estiver via SSH, cole bloco a bloco.

## Passo 1 — Stage de build

```bash
cd ~/meu-projeto-devops/scripts
nano build.sh
```

Conteúdo:

```bash
#!/bin/bash
set -e
echo "[BUILD] Montando a aplicacao..."

mkdir -p ~/meu-projeto-devops/app
cat > ~/meu-projeto-devops/app/index.html <<EOF
<html>
  <body>
    <h1>Bootcamp DevOps Matera 2026</h1>
    <p>Build feito em: $(date '+%d/%m/%Y %H:%M:%S')</p>
  </body>
</html>
EOF

echo "[BUILD] OK - app/index.html gerado."
```

## Passo 2 — Stage de teste

```bash
nano test.sh
```

Conteúdo:

```bash
#!/bin/bash
set -e
echo "[TEST] Verificando a aplicacao..."

ARQUIVO=~/meu-projeto-devops/app/index.html

# Teste 1: o arquivo existe?
if [ ! -f "$ARQUIVO" ]; then
    echo "[TEST] FALHOU: index.html nao existe!"
    exit 1
fi

# Teste 2: o conteudo esperado esta la?
if ! grep -q "Bootcamp DevOps" "$ARQUIVO"; then
    echo "[TEST] FALHOU: conteudo esperado nao encontrado!"
    exit 1
fi

echo "[TEST] OK - 2 de 2 testes passaram."
```

## Passo 3 — Stage de deploy

```bash
nano deploy.sh
```

Conteúdo:

```bash
#!/bin/bash
set -e
echo "[DEPLOY] Publicando em 'producao'..."

mkdir -p ~/producao
cp ~/meu-projeto-devops/app/index.html ~/producao/
echo "[DEPLOY] OK - publicado em ~/producao/index.html"
```

## Passo 4 — A esteira que liga tudo

```bash
nano pipeline.sh
```

Conteúdo:

```bash
#!/bin/bash
set -e
echo "===== PIPELINE INICIADA - $(date '+%H:%M:%S') ====="

./build.sh
./test.sh
./deploy.sh

echo "===== PIPELINE VERDE - aplicacao em producao! ====="
```

## Passo 5 — Execute a esteira!

```bash
chmod +x build.sh test.sh deploy.sh pipeline.sh
./pipeline.sh
```

Resultado esperado: os três stages em sequência e a mensagem final de pipeline verde:

```text
===== PIPELINE INICIADA - 20:50:12 =====
[BUILD] Montando a aplicacao...
[BUILD] OK - app/index.html gerado.
[TEST] Verificando a aplicacao...
[TEST] OK - 2 de 2 testes passaram.
[DEPLOY] Publicando em 'producao'...
[DEPLOY] OK - publicado em ~/producao/index.html
===== PIPELINE VERDE - aplicacao em producao! =====
```

Confira a "produção":

```bash
cat ~/producao/index.html
```

## Passo 6 — Quebre a pipeline (de propósito!) 💥

Cultura blameless na prática: vamos provocar uma falha e ver a esteira nos proteger. Edite o `build.sh` e troque a frase `Bootcamp DevOps Matera 2026` por `Ola mundo`. Rode de novo:

```bash
./pipeline.sh
```

Resultado esperado: o **[TEST] FALHOU** e — aqui está a mágica — o **deploy nunca executou**. A versão quebrada **não chegou em produção**. Isso é qualidade antes de ir para o ar!

> 🔎 Confirme: `cat ~/producao/index.html` ainda mostra a versão boa anterior.

Agora desfaça a mudança no `build.sh` e deixe a pipeline verde de novo. 💚

## Desafio bônus 🏆

Adicione um 4º stage à pipeline: o `healthcheck.sh` da Aula 04 rodando **depois** do deploy (na vida real isso se chama *smoke test* — checar se produção continua saudável após a mudança).

## Deu errado? 😥

| Problema | Causa provável |
|----------|----------------|
| `Permission denied` | Faltou `chmod +x` em algum dos 4 scripts |
| `No such file or directory` | Rode a pipeline de dentro da pasta `scripts` (`cd ~/meu-projeto-devops/scripts`) |
| Pipeline não para no erro | Confira o `set -e` no topo do `pipeline.sh` e os `exit 1` no `test.sh` |
| `EOF` dá erro de sintaxe | O `EOF` final precisa estar sozinho na linha, sem espaços antes |

## Missão até a próxima aula 📌

1. Rode a pipeline mais duas vezes esta semana e provoque uma falha **diferente** da aula: apague o `app/index.html` antes de rodar só o `./test.sh` e veja qual dos dois testes pega o problema.
2. Faça o desafio bônus (health check como 4º stage) — na próxima aula você vai versionar tudo isso, e é bom que esteja do seu jeito.
