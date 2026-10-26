# Slides do bootcamp 📽️

Os decks de cada aula são gerados a partir de um **roteiro em JSON** (`aulas/aula-XX-*/slides/aula-XX.json`) usando o template oficial do Instituto Matera (`template.odp`). O arquivo `.odp` resultante fica ao lado do JSON e abre no LibreOffice Impress, no Google Slides (importar) e no PowerPoint.

## Por que JSON + gerador?

- O roteiro fica **versionado e legível** no Git (diff de texto, revisão por PR), e o deck é reproduzível.
- O visual é sempre o do template: fundos, fontes (Poppins), posições e os quatro tipos de página (capa, conteúdo, seção, encerramento).
- Cada slide carrega **notas do apresentador** com o tempo previsto (`⏱ N min`) — o roteiro falado da live.

## Regenerar um deck

```bash
python3 tools/slides/gerar_slides.py aulas/aula-03-linux-intermediario/slides/aula-03.json
```

Para conferir visualmente (gera PDF e PNGs numa pasta `render/` ao lado — não versionar):

```bash
tools/slides/renderizar.sh aulas/aula-03-linux-intermediario/slides/aula-03.json
```

Requisitos: Python 3 (só biblioteca padrão); para renderizar, LibreOffice (`soffice`) e `pdftoppm` (poppler-utils). Para ver as fontes corretas, instale a **Poppins** (Google Fonts) — sem ela o LibreOffice substitui por outra fonte e as quebras de linha mudam um pouco.

## Formato do roteiro

```json
{"aula": 3, "slides": [
  {"tipo": "capa", "bloco": "abertura", "titulo": "Aula 03", "subtitulo": "Linux 2: Comandos intermediários", "notas": "⏱ 0 min — ...", "minutos": 0},
  {"tipo": "conteudo", "bloco": "parte1", "titulo": "Usuários, root e sudo", "paragrafos": ["..."], "bullets": ["`sudo` executa **um** comando como root"], "destaque": "💬 Interação: ...", "codigo": "ls -l\n", "rodape": "Resultado esperado: ...", "notas": "⏱ 3 min — ...", "minutos": 3},
  {"tipo": "secao", "bloco": "intervalo", "titulo": "INTERVALO", "subtitulo": "Voltamos às 20:35", "notas": "⏱ 15 min", "minutos": 15},
  {"tipo": "encerramento", "bloco": "fechamento", "notas": "", "minutos": 0}
]}
```

- `tipo`: `capa` · `conteudo` · `secao` · `encerramento`.
- `conteudo` aceita `titulo`, `paragrafos` (lista), `bullets` (lista), `destaque` (frase em azul negrito), `codigo` (bloco monoespaçado com fundo cinza) e `rodape` (texto pequeno). Nos textos, `**negrito**` e `` `código` `` viram formatação.
- O gerador avisa (`[AVISO]`) quando estima que um slide ultrapassa a área útil — divida o slide em dois.
- Limites que cabem bem: título até ~34 caracteres; até 6 bullets de até ~90 caracteres; código até 9 linhas de até 70 caracteres; no total ~12 linhas por slide.

## Tempos de cada aula (como os roteiros foram montados)

| Bloco | Minutos |
|-------|---------|
| Abertura + agenda | 5 |
| Revisão da aula anterior (aulas 02–10) | 5 |
| Parte 1 — conceitos | 40 (45 na Aula 01) |
| Intervalo | 15 |
| Parte 2 — prática | 45 |
| Perguntas & Respostas (Aula 10: a surpresa final) | 25 |
