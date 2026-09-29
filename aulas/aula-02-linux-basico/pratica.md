# Prática 02 — Primeiros passos no terminal 🐧

**Objetivo:** usar os comandos básicos para criar a estrutura do **seu projeto do bootcamp** — a pasta que vamos evoluir até a última aula.

**Onde:** dentro da VM Ubuntu.

## Passo 1 — Onde estou?

```bash
pwd
```

Resultado esperado: `/home/aluno` (com o seu usuário). Essa é a sua casa, o `~`.

## Passo 2 — Crie a pasta do projeto

```bash
mkdir meu-projeto-devops
cd meu-projeto-devops
pwd
```

Resultado esperado: `/home/aluno/meu-projeto-devops`.

## Passo 3 — Crie a estrutura interna

```bash
mkdir scripts app
touch README.txt
ls
```

Resultado esperado:

```text
app  README.txt  scripts
```

## Passo 4 — Escreva e leia um arquivo

```bash
echo "Projeto do Bootcamp DevOps Matera 2026" > README.txt
cat README.txt
```

Resultado esperado: o terminal mostra a frase que você gravou. O `>` "despeja" a saída do comando para dentro do arquivo.

## Passo 5 — Copie, renomeie, mova

```bash
cp README.txt README-backup.txt
mv README-backup.txt app/
ls app/
```

Resultado esperado: `README-backup.txt` agora está dentro de `app/`.

## Passo 6 — Remova com cuidado

```bash
rm app/README-backup.txt
ls app/
```

Resultado esperado: `app/` vazio de novo.

> ⚠️ **No Linux não existe lixeira no terminal.** `rm` apaga de verdade. Antes de remover, respire e confira o caminho — principalmente se um dia você tiver `sudo` na frente. 😄

## Passo 7 — Explore o manual

```bash
man ls
```

Navegue com as setas e saia com a tecla `q`. Descubra: o que faz a opção `-a`? Teste:

```bash
ls -la
```

Viu arquivos começando com `.`? São os arquivos ocultos — eles vão reaparecer na aula de Git!

## Desafio bônus 🏆

Sem olhar as respostas acima, crie dentro de `meu-projeto-devops` uma pasta `docs` contendo um arquivo `notas.txt` com a frase "Linux dominado!" — e mostre o conteúdo na tela. Poste o print no chat!

## Deu errado? 😥

| Mensagem | Causa provável |
|----------|----------------|
| `No such file or directory` | Você não está na pasta que imagina — rode `pwd` e `ls` para se localizar |
| `Permission denied` | Você tentou mexer fora da sua pasta pessoal — por enquanto, fique dentro de `~` (permissões são o tema da próxima aula!) |
| `command not found` | Erro de digitação no comando — o terminal é implacável com typos |
