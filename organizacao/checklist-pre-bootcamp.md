# Checklist pré-bootcamp 📋

Documento de organização da equipe: tudo que precisa estar pronto **antes da Aula 01**.

## T-2 semanas

- [x] Datas das 10 aulas confirmadas e atualizadas no [README](../README.md): 3, 4, 5, 6, 10, 11, 12, 13, 17 e 18 de novembro de 2026.
- [ ] Repositório público revisado.
- [ ] Guia de setup **testado de ponta a ponta** por alguém da equipe em: Windows com teclado ABNT2 (instalador tela a tela, SSH pelo PowerShell), macOS com chip Apple M (VirtualBox Apple Silicon + ISO arm64) e Linux. Anotar o tempo gasto e ajustar o guia.
- [ ] Canais de comunidade criados (Discord ou Slack), com canal por tema: `#setup-ambiente`, `#duvidas-gerais`, `#aula-do-dia`.
- [ ] Monitores voluntários da Matera confirmados e com acesso aos canais.
- [ ] **Imagem backup da VM** montada e testada: Ubuntu com **todos os binários usados no curso** já instalados (git, docker, docker compose, curl, btop, vim), hostname `bootcamp`, usuário `aluno`, OpenSSH ativo. Publicar em local de download controlado pela equipe.
- [ ] Versão **arm64** da imagem backup (exportada de um Mac com chip M) — sem ela, alunos de Mac M não têm plano B.

## T-1 semana — Prévia da configuração do ambiente

- [ ] Enviar **formulário de validação do ambiente** para todos os inscritos.
- [ ] Acompanhar as respostas diariamente para "medir a temperatura": se muitos não conseguiram configurar, reforçar apoio nos canais antes da Aula 01.

### Perguntas sugeridas para o formulário

1. Qual o sistema operacional do seu computador? (Windows / Linux / macOS)
2. Conseguiu instalar o VirtualBox? (Sim / Não / Tive problemas — descreva)
3. Conseguiu criar a VM Ubuntu e fazer login? (Sim / Não / Tive problemas — descreva)
4. Executou o [roteiro de testes](../setup/roteiro-de-testes.md)? Todos passaram? (Sim / Alguns falharam — quais? / Ainda não executei)
5. Quanto de memória RAM tem seu computador?
6. De 0 a 5, qual seu nível de familiaridade com terminal/linha de comando?

## Aula 01 (dia D)

- [ ] Reservar **até 1 hora** após as apresentações e boas-vindas para **apoio à configuração do ambiente** (guiado pelo [roteiro de testes](../setup/roteiro-de-testes.md)).
- [ ] Monitores de plantão no chat para atendimentos individuais.

## Política da imagem backup ⚠️

A imagem backup **só é liberada a partir da Aula 02**, e **somente para quem tiver problema** que não foi possível resolver com apoio dos monitores. O objetivo é evitar que a turma fique parada muito tempo por causa de um único ambiente — mas a instalação manual é parte do aprendizado, então ela é o último recurso, não o atalho.

## Durante o bootcamp

- [ ] Após cada aula: publicar/atualizar no repositório o material apresentado e o código usado na Parte 2.
- [ ] Início de cada aula (02+): revisão do dia anterior com gancho (ver [formato-da-live.md](formato-da-live.md)).
- [ ] Monitorar os canais da comunidade entre as aulas.
