# Micro aula: o editor `vi` ✏️

> Roteiro de **10 minutos** (5 de conceito + 5 de exercício guiado), apresentado na Aula 03 e usado em todas as práticas a partir da Aula 04. Serve de texto-base para os slides e de referência para consultar depois.

## Por que o `vi`?

Porque ele está em **todo** Linux — do servidor da Matera ao roteador da sua casa, inclusive em máquinas onde não existe mais nada instalado. Quem sabe o básico do `vi` consegue editar um arquivo de configuração em qualquer lugar do mundo. É uma habilidade de carreira, não só do bootcamp.

No Ubuntu, o comando `vi` abre o **Vim** ("vi melhorado"), que já vem instalado no Ubuntu Server. Existe também o `nano`, mais simples — mas nem sempre está lá. Por isso, aprendemos o `vi`.

## A ideia que muda tudo: o `vi` tem modos

Num editor comum, tudo que você digita vira texto. No `vi`, **depende do modo em que ele está**:

| Modo | Analogia | O que as teclas fazem |
|------|----------|-----------------------|
| **Normal** (é assim que ele abre) | Controle remoto 🎮 | Cada tecla é um **comando**: mover, apagar, copiar, desfazer |
| **Inserção** | Máquina de escrever ⌨️ | As teclas **viram texto** — é onde você digita o conteúdo |
| **Linha de comando** (`:`) | Menu 📋 | Comandos "grandes": salvar, sair, procurar e substituir |

Como saber onde você está: no modo de inserção aparece **`-- INSERT --`** no canto inferior esquerdo. Se não aparece, você está no modo normal.

**O ciclo de vida de toda edição:**

```text
vi arquivo  →  [modo normal]  → i →  [modo inserção: digite]  → Esc →  [modo normal]  → :wq → Enter
```

## Os comandos que resolvem 95% do dia a dia

| Tecla / comando | Modo | Faz |
|-----------------|------|-----|
| `vi arquivo` | terminal | Abre o arquivo (cria, se não existir) |
| `i` | normal → inserção | Começa a **inserir** texto onde o cursor está |
| `o` | normal → inserção | Abre uma **linha nova abaixo** e já entra em inserção |
| `Esc` | inserção → normal | Volta ao modo normal (aperte sem medo, quantas vezes quiser) |
| `:w` + Enter | normal | **Salva** (*write*) |
| `:q` + Enter | normal | **Sai** (*quit*) — só se não houver mudança pendente |
| `:wq` + Enter | normal | Salva **e** sai — o que você mais vai usar |
| `:q!` + Enter | normal | Sai **sem salvar** (descarta tudo) — a saída de emergência |
| setas | qualquer | Movem o cursor (no modo normal, `h` `j` `k` `l` fazem o mesmo) |
| `x` | normal | Apaga o caractere sob o cursor |
| `dd` | normal | Apaga a **linha** inteira |
| `u` | normal | **Desfaz** (*undo*) — sua melhor amiga |
| `yy` depois `p` | normal | Copia a linha (*yank*) e cola abaixo (*paste*) |
| `/texto` + Enter | normal | Procura `texto` (`n` vai para a próxima ocorrência) |
| `gg` · `G` | normal | Vai para o início · para o fim do arquivo |

> 🚪 **Como sair do `vi`** (a pergunta mais famosa da internet): aperte `Esc` (uma ou duas vezes), digite `:q!` e dê Enter. Pronto, você está fora — sem salvar nada. Para sair salvando: `Esc`, `:wq`, Enter.

## Exercício guiado (5 min)

1. Abra um arquivo novo:
   ```bash
   vi ~/rascunho.txt
   ```
2. Aperte `i` — repare no `-- INSERT --` lá embaixo. Digite três linhas (Enter entre elas):
   ```text
   primeira linha
   segunda linha
   terceira linha
   ```
3. Aperte `Esc`. O `-- INSERT --` sumiu: você está no modo normal.
4. Com as setas, vá até a **segunda linha** e aperte `dd`. Ela sumiu.
5. Arrependeu? `u`. Ela voltou. Aperte `dd` de novo para apagá-la mesmo.
6. Salve e saia: digite `:wq` (aparece no rodapé) e Enter.
7. Confira no terminal:
   ```bash
   cat ~/rascunho.txt
   ```
   Resultado esperado: `primeira linha` e `terceira linha`.
8. Bônus: abra de novo (`vi ~/rascunho.txt`), aperte `o`, escreva `quarta linha`, `Esc`, `:wq`. Depois teste a saída de emergência: abra, digite qualquer coisa em modo de inserção, `Esc`, `:q!` — nada mudou.

## Pegadinhas (todo mundo cai; o segredo é reconhecer)

| O que aconteceu | O que foi | Como sair |
|-----------------|-----------|-----------|
| Digitei e apareceram coisas estranhas, linhas sumiram | Você digitou no **modo normal**: as letras viraram comandos | `Esc`, depois `u` várias vezes até voltar ao normal; aí `i` para escrever |
| Apareceu `recording @a` (ou outra letra) no rodapé | Apertou `q` + uma letra no modo normal (gravação de macro) | Aperte `q` de novo |
| Digito `:wq` e as letras aparecem no texto | Estava no modo de inserção | `Esc` primeiro, depois `:wq` |
| `E37: No write since last change` | Tentou sair com `:q` com mudanças pendentes | `:wq` para salvar, ou `:q!` para descartar |
| As letras saem maiúsculas e os comandos não funcionam | Caps Lock ligado (`I`, `U`, `X` são comandos diferentes!) | Desligue o Caps Lock, `Esc`, `u` |
| Colei um bloco pelo SSH e as linhas ficaram "escadinha" | O Vim indentou automaticamente o que foi colado | Antes de colar: `Esc`, `:set paste`, Enter, `i`, cole. (Ou `u` e cole de novo com `:set paste`) |
| A tela ficou "presa" sem responder | Apertou `Ctrl + S` (pausa o terminal) | `Ctrl + Q` |

## Para colar código pelo SSH (o caso mais comum no bootcamp)

1. `vi arquivo.sh`
2. `:set paste` + Enter (evita a indentação automática)
3. `i`
4. Cole (`Ctrl + V` no Windows, `Cmd + V` no Mac, `Ctrl + Shift + V` no Linux)
5. `Esc`, `:wq`, Enter

## Quer ir além?

Dentro do próprio terminal, o Vim traz um tutorial interativo de 30 minutos: digite `vimtutor` (se não estiver instalado, `sudo apt install -y vim`). É a melhor forma de passar do "sobrevivo no vi" para o "gosto do vi".
