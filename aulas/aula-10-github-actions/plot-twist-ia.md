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

```text
Crie um projeto chamado meu-projeto-devops com:

1. Uma pagina index.html gerada por um script scripts/build.sh (com a data do build);
2. Um script scripts/test.sh que valida a existencia e o conteudo da pagina,
   retornando codigo de saida diferente de zero em caso de falha;
3. Um script scripts/deploy.sh que copia a pagina para ~/producao;
4. Um script scripts/pipeline.sh que encadeia build, teste e deploy e para no primeiro erro;
5. Um script scripts/healthcheck.sh que verifica internet, uso de disco e memoria disponivel;
6. Um Dockerfile servindo a pagina com nginx:alpine;
7. Um compose.yaml com o site (porta 8080) e um redis chamado "visitas";
8. Um workflow .github/workflows/ci.yml que roda build e teste a cada push e pull request;
9. Um README.md explicando o projeto.

Depois inicialize o repositorio git, faca o commit inicial e execute a pipeline local
para provar que esta tudo verde.
```

## Checklist de riscos

- [ ] Internet do estúdio testada (a demo baixa imagens Docker).
- [ ] Imagens `nginx:alpine` e `redis:alpine` já baixadas na máquina da demo (cache).
- [ ] Vídeo de backup gravado do fluxo completo.
- [ ] Nenhum token/segredo visível na tela durante a demo (usar conta de demonstração!).
- [ ] Combinar quem narra e quem digita (dupla funciona melhor).
