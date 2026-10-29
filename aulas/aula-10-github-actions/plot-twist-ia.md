# 🎁 A surpresa final: o plot twist da IA

> **Roteiro para os apresentadores** — conduzir ao vivo no **bloco final da Aula 10 (21:20–21:45)**, no lugar do Q&A de sempre. A prática (45 min) precisa terminar no horário: se atrasar, o badge (Passo 4 da prática) vira missão de casa.

## A ideia

Durante duas semanas, a turma construiu com as próprias mãos: estrutura de projeto, health check, pipeline de build/teste/deploy, Dockerfile, compose, repositório no GitHub e CI com Actions.

O plot twist: **mostrar, ao vivo, uma IA recriando tudo isso em poucos minutos, a partir de um único prompt.**

## O objetivo pedagógico (o mais importante!)

O impacto inicial é o "uau" (e um friozinho na barriga 😅). A mensagem final deve ser **energizante, não desanimadora**:

1. **A IA só fez em minutos porque VOCÊS agora sabem julgar o que ela fez.** Sem as 10 aulas, o resultado seria um bloco de texto indecifrável. Com elas, vocês leem cada arquivo e sabem exatamente o que é.
2. **O trabalho do profissional DevOps mudou de lugar:** sai do "digitar comandos" e vai para **entender, revisar, decidir e operar**. A IA escreve o script; quem responde pelo deploy em produção é você.
3. **Quem domina os fundamentos multiplica a própria produtividade com IA.** Quem não domina, apenas copia e cola — e não sabe consertar quando quebra (e sempre quebra!).

## Roteiro da demo (15–20 min)

1. **Setup prévio:** uma VM/máquina limpa com uma CLI de IA instalada e autenticada, e uma conta GitHub de demonstração. **Ensaiar antes** — demo ao vivo sem ensaio é roleta-russa. Ter um vídeo gravado de backup.
2. **A chamada:** "Vocês levaram 10 aulas para construir esse projeto. Alguém quer chutar quanto tempo uma IA levaria?" (enquete no chat!)
3. **Rodar o prompt** (abaixo) na frente de todos, narrando o que a IA vai fazendo — e conectando cada arquivo gerado à aula em que a turma o construiu ("olha o `set -e` da Aula 04!", "olha o `depends_on` da Aula 08!").
4. **Executar o resultado:** `./scripts/pipeline.sh` verde, `docker compose up -d`, `curl localhost:8080`, push e pipeline verde no Actions.
5. **A virada:** perguntar ao chat — "a IA errou algo? o que vocês fariam diferente?" — e deixar a turma **revisar a IA**. É o momento em que eles percebem que sabem.
6. Fechar com a mensagem pedagógica acima, o encerramento e o aviso de que o certificado será enviado pela organização.

## O prompt da demo

O prompt é uma **especificação fechada** do que a turma construiu — nomes de arquivos, mensagens, comportamentos e a prova de que funciona. Foi testado antes de entrar aqui: executado numa máquina limpa, gerou os 11 arquivos, pipeline verde, a quebra proposital barrando o deploy e o commit inicial em cerca de 1 minuto. Cole-o **inteiro** na CLI de IA (está também em [`prompt-demo.txt`](prompt-demo.txt), para copiar sem erro):

```text
Voce e um engenheiro DevOps. Crie, do zero, o projeto "meu-projeto-devops" na pasta ~/meu-projeto-devops,
exatamente com a estrutura e o comportamento abaixo. Use apenas bash puro (sem dependencias extras),
somente caracteres ASCII dentro dos scripts (sem acentos nem emojis), e deixe todos os .sh executaveis.

ESTRUTURA
~/meu-projeto-devops/
  README.md            (o que e o projeto, o que tem em cada pasta, como rodar:
                        ./scripts/build.sh e depois docker compose up -d)
  .gitignore           (ignorar: *.log, relatorio.txt e app/index.html - arquivos gerados nao se versionam)
  Dockerfile
  compose.yaml
  scripts/relatorio.sh
  scripts/healthcheck.sh
  scripts/build.sh
  scripts/test.sh
  scripts/deploy.sh
  scripts/pipeline.sh
  .github/workflows/ci.yml

SCRIPTS (todos comecam com #!/bin/bash; build.sh, test.sh, deploy.sh e pipeline.sh usam set -e;
relatorio.sh e healthcheck.sh NAO usam, pois precisam continuar mesmo se um comando falhar)
1. scripts/relatorio.sh: imprime "=== Relatorio do sistema ===", depois a saida de date, uptime e
   df -h / sem a linha de cabecalho (df -h / | grep -v Filesystem).
2. scripts/healthcheck.sh: imprime "=== Health Check - <hostname> - <dd/mm/aaaa HH:MM> ===";
   verifica internet com "ping -c 1 ubuntu.com" (saida descartada) e imprime "[OK] Internet" ou
   "[FALHA] Internet"; le o percentual de uso do disco raiz com
   df / --output=pcent | tail -1 | tr -d ' %' e imprime "[OK] Disco: N% usado" se N < 80 ou
   "[FALHA] Disco: N% usado (acima de 80%!)"; termina com "=== Fim do health check ===".
3. scripts/build.sh: imprime "[BUILD] Montando a aplicacao...", cria a pasta ~/meu-projeto-devops/app
   (mkdir -p) e grava em ~/meu-projeto-devops/app/index.html UMA linha:
   <h1>Bootcamp DevOps Matera 2026</h1><p>Build em dd/mm/aaaa HH:MM:SS</p> (data/hora atuais);
   imprime "[BUILD] OK - app/index.html gerado.".
4. scripts/test.sh: imprime "[TEST] Verificando a aplicacao..."; se
   grep -q "Bootcamp DevOps" ~/meu-projeto-devops/app/index.html der certo, imprime
   "[TEST] OK - conteudo esperado encontrado."; senao imprime
   "[TEST] FALHOU - conteudo esperado nao encontrado!" e termina com exit 1.
5. scripts/deploy.sh: imprime "[DEPLOY] Publicando em 'producao'...", cria ~/producao (mkdir -p),
   copia ~/meu-projeto-devops/app/index.html para la e imprime
   "[DEPLOY] OK - publicado em ~/producao/index.html".
6. scripts/pipeline.sh: imprime "===== PIPELINE INICIADA - HH:MM:SS =====", executa ./build.sh,
   ./test.sh e ./deploy.sh nesta ordem (ele e executado de dentro da pasta scripts) e, so se todos
   passarem, imprime "===== PIPELINE VERDE - aplicacao em producao! =====". Se um stage falhar,
   os seguintes nao rodam (set -e).

CONTAINERS
- Dockerfile: FROM nginx:alpine; COPY app/index.html /usr/share/nginx/html/index.html; EXPOSE 80.
- compose.yaml: servico "site" (build: . ; ports "8080:80"; depends_on visitas) e servico "visitas"
  com a imagem redis:alpine. Nada mais.

CI
- .github/workflows/ci.yml: name CI; dispara em push na branch main e em pull_request; um job
  "build-e-teste" em ubuntu-latest com os steps: actions/checkout@v4, "Build" (run: ./scripts/build.sh)
  e "Teste" (run: ./scripts/test.sh).

PROVA (execute e mostre a saida de cada comando)
1. cd ~/meu-projeto-devops/scripts && ./relatorio.sh && ./healthcheck.sh
2. ./pipeline.sh            -> deve terminar com PIPELINE VERDE; depois cat ~/producao/index.html
3. Troque, no build.sh, "Bootcamp DevOps Matera 2026" por "Ola mundo" e rode ./pipeline.sh de novo
   -> o TEST deve FALHAR e o deploy NAO deve executar; confirme com cat ~/producao/index.html
   (a versao boa continua la). Depois desfaca a troca e rode ./pipeline.sh ate ficar VERDE.
4. Se o Docker estiver disponivel: cd ~/meu-projeto-devops && docker compose up -d &&
   curl http://localhost:8080 && docker compose down.
5. cd ~/meu-projeto-devops && git init -b main && git add . && git commit -m "primeiro commit: projeto do bootcamp"
   && git log --oneline   (a branch precisa se chamar main, como o gatilho do ci.yml)
Nao crie nada alem do que foi pedido. Nao invente servicos, testes ou arquivos extras.
```

## Como conduzir a demo com esse prompt

1. **Antes de colar**, mostre na tela o repositório de um aluno (ou o seu) com os mesmos 11 arquivos: "foi isso que levamos 10 aulas para construir".
2. **Cole o prompt e narre** enquanto a IA cria os arquivos: "ela está escrevendo o `healthcheck.sh` — reparem no `[OK]`/`[FALHA]`, igual ao da Aula 04"; "olha o `set -e` da Aula 05"; "o `depends_on` da Aula 08".
3. **A prova** acontece sozinha (o prompt pede): pipeline verde → quebra proposital com o `[TEST] FALHOU` e o deploy que não roda → verde de novo → `docker compose` → `git log`. Dê zoom nessas saídas: são as mesmas que a turma viu.
4. **Comparação lado a lado** (o momento da virada): abra o `test.sh` da IA ao lado do `test.sh` da turma. São iguais? O que a IA decidiu sozinha? No teste de ensaio, ela: colocou `./scripts/build.sh` antes do `compose up` no README (porque o `index.html` está no `.gitignore`); escolheu a forma curta do `depends_on`; e **não** removeu o cabeçalho do `df` numa máquina em português (`grep -v Filesystem` só funciona com o sistema em inglês — a turma passou por isso). Pergunte ao chat: *"a IA errou algo? vocês fariam diferente?"* — e deixe a turma revisar.
5. Feche com a mensagem pedagógica: **a IA só fez em um minuto porque vocês, agora, sabem julgar o que ela fez.**

## Checklist de riscos

- [ ] **Ensaio com o prompt final** (`prompt-demo.txt`) na mesma CLI e na mesma máquina da live; anotar o tempo e as decisões que a IA tomou sozinha (viram perguntas para a turma).
- [ ] Internet do estúdio testada (a demo baixa imagens Docker).
- [ ] Imagens `nginx:alpine` e `redis:alpine` já baixadas na máquina da demo (cache).
- [ ] Vídeo de backup gravado do fluxo completo.
- [ ] Nenhum token/segredo visível na tela durante a demo (usar conta de demonstração!).
- [ ] Combinar quem narra e quem digita (dupla funciona melhor).
