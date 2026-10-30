# Aula Extra — IA e DevOps: o que importa é saber o que pedir 🎁

> **Aula extra aninhada na Aula 10**, no bloco final (**18/11, 21:20–21:45**, no lugar do Q&A de sempre). Para a turma, é "a surpresa final": não anunciar o conteúdo antes. Para a equipe, é uma aula com roteiro, prompt e deck próprios.
>
> 📽️ Slides: [`slides/aula-extra.odp`](slides/aula-extra.odp) (roteiro editável em [`slides/aula-extra.json`](slides/aula-extra.json)). Prompts da demo: [`prompt-simples.txt`](prompt-simples.txt) e [`prompt-detalhado.txt`](prompt-detalhado.txt).
>
> ⏱ A prática da Aula 10 (45 min) precisa terminar no horário: se atrasar, o badge (Passo 4 da prática) vira missão de casa.

## Agenda (25 min)

| Horário | Bloco | Minutos |
|---------|-------|---------|
| 21:20 | A chamada + enquete no chat | 3 |
| 21:23 | Prompt 1, ao vivo: o pedido simples (9 linhas) | 7 |
| 21:30 | Funcionou… mas é o nosso projeto? Comparação lado a lado | 5 |
| 21:35 | Prompt 2: a especificação — o resultado igual ao da turma | 4 |
| 21:39 | A virada: a turma revisa a IA + mensagem pedagógica | 6 |
| 21:45 | Encerramento da Aula 10 (de volta ao deck da Aula 10) | — |

## A ideia

Durante duas semanas, a turma construiu com as próprias mãos: estrutura de projeto, health check, pipeline de build/teste/deploy, Dockerfile, compose, repositório no GitHub e CI com Actions.

O plot twist: **mostrar, ao vivo, uma IA recriando tudo isso em poucos minutos, a partir de um único prompt.**

E a lição por trás do truque: **o que importa agora é saber o que pedir — e como pedir.** Um pedido vago produz um projeto que *funciona*, mas não é o nosso; uma especificação precisa produz o projeto da turma. A diferença entre os dois prompts é exatamente o vocabulário que a turma aprendeu em 10 aulas.

## O objetivo pedagógico (o mais importante!)

O impacto inicial é o "uau" (e um friozinho na barriga 😅). A mensagem final deve ser **energizante, não desanimadora**:

1. **A IA só fez em minutos porque VOCÊS agora sabem julgar o que ela fez.** Sem as 10 aulas, o resultado seria um bloco de texto indecifrável. Com elas, vocês leem cada arquivo e sabem exatamente o que é.
2. **O trabalho do profissional DevOps mudou de lugar:** sai do "digitar comandos" e vai para **entender, revisar, decidir e operar**. A IA escreve o script; quem responde pelo deploy em produção é você.
3. **Quem domina os fundamentos multiplica a própria produtividade com IA.** Quem não domina, apenas copia e cola — e não sabe consertar quando quebra (e sempre quebra!).

## Dois prompts, um objetivo

| | Prompt 1 — o pedido simples | Prompt 2 — a especificação |
|---|---|---|
| Arquivo | [`prompt-simples.txt`](prompt-simples.txt) (9 linhas) | [`prompt-detalhado.txt`](prompt-detalhado.txt) (63 linhas) |
| O que diz | O que queremos, em linguagem natural, com o vocabulário do bootcamp (build, teste, deploy, pipeline, nginx, compose, redis, workflow) | Nomes de arquivos, caminhos, mensagens, comportamentos e a prova, item a item |
| Funciona? | **Sim**: pipeline verde, teste quebrado barra o deploy, commit — em ~1 min | **Sim**, igual |
| É o projeto da turma? | **Não.** No ensaio a IA decidiu sozinha: `dist/` em vez de `app/`; produção dentro do projeto em vez de `~/producao`; título "Meu Projeto DevOps"; mensagens `[build]`/`[test]` e 5 verificações no teste; `nginx:1.27-alpine`; serviço `redis` com volume e `restart`; workflow em qualquer push + upload de artefato; `set -euo pipefail`; `.gitignore` e README que ninguém pediu | **Sim.** 11 arquivos com os mesmos nomes, mensagens `[OK]`/`[FALHA]`/`[BUILD]`/`[TEST]`/`[DEPLOY]`, `nginx:alpine`, serviço `visitas`, `ci.yml` igual |

Os dois foram testados numa máquina limpa, sem acesso ao material. Nenhum dos dois está "errado": o primeiro mostra o que a IA faz quando a gente não sabe o que quer; o segundo mostra o que ela faz quando a gente sabe.

## Prompt 1 — o pedido simples (ao vivo)

```text
Crie um projeto chamado meu-projeto-devops com scripts em bash:
- um build que gera uma pagina index.html com a data do build;
- um teste que verifica a pagina e falha com codigo de saida diferente de zero se ela estiver errada;
- um deploy que copia a pagina para uma pasta de "producao";
- uma pipeline que roda build, teste e deploy nessa ordem e para no primeiro erro.
Inclua um Dockerfile com nginx para servir a pagina, um compose com o site e um redis,
e um workflow do GitHub Actions que roda build e teste a cada push.
Rode a pipeline para provar que funciona e depois quebre o teste de proposito
para mostrar que o deploy nao acontece. Por fim, inicie o repositorio git e faca o primeiro commit.
```

Narre enquanto a IA trabalha ("ela criou um `build.sh`… olha, decidiu chamar a pasta de `dist`") e deixe a prova rodar: pipeline verde, teste quebrado sem deploy, commit.

## Prompt 2 — a especificação (resultado ensaiado)

O [`prompt-detalhado.txt`](prompt-detalhado.txt) descreve o projeto da turma item a item. Rodá-lo ao vivo duplicaria o tempo; mostre o prompt na tela (dê zoom em 2 ou 3 trechos: as mensagens `[OK]`/`[FALHA]`, o `grep -q`, o serviço `visitas`) e, ao lado, o resultado **já ensaiado** — o `test.sh` da IA idêntico ao `test.sh` da turma. Se sobrar tempo, rode-o também.

## Roteiro da demo (25 min)

1. **Setup prévio:** máquina limpa com a CLI de IA autenticada e conta GitHub de demonstração; os dois prompts prontos para colar; o resultado do Prompt 2 já gerado (ou um vídeo); nenhum token visível. Dupla: um narra, outro digita.
2. **A chamada (3 min):** "Vocês levaram 10 aulas para construir esse projeto. Quanto tempo uma IA levaria?" — enquete no chat.
3. **Prompt 1 ao vivo (7 min):** cole o pedido simples e narre. Celebre o verde: *funcionou*.
4. **Comparação (5 min):** abra o projeto da IA ao lado do projeto de um aluno. Pergunte ao chat: "é o nosso projeto?" — e vá apontando as diferenças da tabela acima. A turma vai perceber que *sabe* ver a diferença.
5. **Prompt 2 (4 min):** mostre a especificação e o resultado ensaiado, idêntico ao da turma. A frase-chave: **"a diferença entre os dois prompts é o que vocês aprenderam aqui."**
6. **A virada (6 min):** "a IA errou algo? o que vocês fariam diferente?" — deixe a turma revisar a IA. Feche com a mensagem pedagógica acima, o encerramento e o aviso de que o certificado será enviado pela organização.

## Checklist de riscos

- [ ] **Ensaio com os dois prompts** (`prompt-simples.txt` e `prompt-detalhado.txt`) na mesma CLI e na mesma máquina da live; anotar o tempo e as decisões que a IA tomou sozinha no Prompt 1 (viram a tabela de comparação) e guardar o resultado do Prompt 2 para mostrar pronto.
- [ ] Internet do estúdio testada (a demo baixa imagens Docker).
- [ ] Imagens `nginx:alpine` e `redis:alpine` já baixadas na máquina da demo (cache).
- [ ] Vídeo de backup gravado do fluxo completo.
- [ ] Nenhum token/segredo visível na tela durante a demo (usar conta de demonstração!).
- [ ] Combinar quem narra e quem digita (dupla funciona melhor).
