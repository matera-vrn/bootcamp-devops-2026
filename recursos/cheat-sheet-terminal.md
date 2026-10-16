# Cola do terminal Linux 📝

Uma página para imprimir ou deixar aberta ao lado. Tudo aqui foi visto no bootcamp.

## Teclas que salvam sua vida

| Tecla | Faz |
|-------|-----|
| `Tab` | Autocompleta nomes de arquivos, pastas e comandos (aperte 2x para ver as opções) |
| `↑` `↓` | Navega pelos comandos anteriores |
| `Ctrl + C` | Cancela o comando atual (o terminal "travou"? é isto) |
| `Ctrl + L` ou `clear` | Limpa a tela |
| `q` | Sai de telas de leitura (`man`, `less`, `git log`) |
| `Ctrl + R` | Busca no histórico: digite parte do comando |
| `Ctrl + D` ou `exit` | Encerra a sessão |
| `comando --help` · `man comando` | Ajuda rápida · manual completo |

Apareceu um `>` sozinho? Você abriu aspas e não fechou: `Ctrl + C` e digite de novo.

## Teclado ABNT2

`~` e `^` são teclas mortas: aperte e depois **Espaço**. `|` é `Shift + \` (tecla ao lado do `Z`). `/` fica ao lado do `Shift` direito.

## Navegar

| Comando | Faz |
|---------|-----|
| `pwd` | Onde estou? |
| `ls` · `ls -la` | Lista · lista com detalhes e ocultos |
| `cd pasta` · `cd ..` · `cd ~` · `cd /` | Entra · sobe um nível · vai para casa · vai para a raiz |

Caminho **absoluto** começa em `/` (`/var/log`); **relativo** parte de onde você está (`scripts/`).

## Arquivos e pastas

| Comando | Faz |
|---------|-----|
| `mkdir pasta` · `mkdir -p a/b/c` | Cria pasta · cria a árvore inteira |
| `touch arquivo` | Cria arquivo vazio |
| `cp origem destino` · `cp -r pasta destino` | Copia · copia pasta |
| `mv origem destino` | Move ou renomeia |
| `rm arquivo` · `rm -r pasta` | Apaga (sem lixeira!) · apaga pasta |
| `nano arquivo` | Edita |

## Ver conteúdo

| Comando | Faz |
|---------|-----|
| `cat arquivo` | Mostra tudo |
| `head -5 arquivo` · `tail -5 arquivo` | Primeiras · últimas 5 linhas |
| `tail -f arquivo.log` | Acompanha o arquivo crescendo (`Ctrl + C` para sair) |
| `less arquivo` | Lê com rolagem (`q` para sair) |
| `wc -l arquivo` | Conta linhas |

## Buscar e combinar

| Comando | Faz |
|---------|-----|
| `grep "texto" arquivo` · `grep -i` · `grep -v` | Procura · ignora maiúsculas · inverte (mostra o que NÃO tem) |
| `comando \| grep x` | Filtra a saída de um comando |
| `comando > arquivo` · `comando >> arquivo` | Grava a saída (substitui) · acrescenta no final |
| `echo "texto"` | Imprime texto (ou grava, com `>`) |
| `find . -name "*.sh"` | Procura arquivos pelo nome |

## Permissões e usuários

| Comando | Faz |
|---------|-----|
| `ls -l` | Mostra permissões: `-rwxr-xr--` = dono / grupo / outros |
| `chmod +x script.sh` | Torna executável |
| `sudo comando` | Executa como root (cuidado!) |
| `whoami` · `groups` | Quem sou · meus grupos |

## Processos e sistema

| Comando | Faz |
|---------|-----|
| `ps aux` · `btop` | Lista processos · monitor ao vivo (`q` sai) |
| `kill PID` | Encerra um processo |
| `df -h` · `free -m` · `uptime` | Disco · memória · tempo ligado |
| `systemctl status nome` | Situação de um serviço (`ssh`, `docker`) |
| `sudo poweroff` · `sudo reboot` | Desliga · reinicia |

## Pacotes e rede

| Comando | Faz |
|---------|-----|
| `sudo apt update` · `sudo apt install -y nome` | Atualiza o catálogo · instala |
| `ping -c 3 site.com` | O servidor responde? |
| `curl -I https://site.com` · `curl -IL` | Cabeçalhos HTTP · seguindo redirecionamentos |
| `ip a` | Meu IP |
| `ssh usuario@maquina -p porta` | Conecta em outra máquina |

## Scripts (bash)

```bash
#!/bin/bash
set -e                      # para no primeiro erro
NOME="Matera"               # variavel (sem espacos em volta do =)
DATA=$(date +%d/%m/%Y)      # saida de um comando em variavel
if ping -c 1 google.com > /dev/null 2>&1; then
    echo "[OK] $NOME online em $DATA"
else
    echo "[FALHA] sem internet"
fi
for X in a b c; do echo "$X"; done
echo "primeiro parametro: $1"
```

`chmod +x script.sh` e depois `./script.sh`. Código de saída: `0` = deu certo; qualquer outro = falhou.

## nano em 30 segundos

`Ctrl + O` + `Enter` salva · `Ctrl + X` sai (responda `Y` se perguntar) · `Ctrl + K` recorta a linha · `Ctrl + U` cola · `Ctrl + W` procura · `Alt + U` desfaz. O `^` na barra de baixo significa `Ctrl`. O mouse não funciona: use as setas.

## Git essencial

| Comando | Faz |
|---------|-----|
| `git status` · `git log --oneline` | O que mudou · histórico resumido |
| `git add arquivo` · `git add .` | Prepara para o commit |
| `git commit -m "mensagem"` | Grava no histórico |
| `git checkout -b nome` · `git checkout main` | Cria e entra na branch · volta para a main |
| `git merge nome` | Junta a branch na atual |
| `git push` · `git pull` | Envia · traz do GitHub |

## Docker essencial

| Comando | Faz |
|---------|-----|
| `docker run -d --name x -p 8080:80 imagem` | Roda em segundo plano, publicando a porta |
| `docker ps` · `docker ps -a` | Rodando · todos |
| `docker stop x` · `docker rm x` | Para · remove |
| `docker build -t nome:1.0 .` · `docker images` | Constrói a imagem · lista imagens |
| `docker compose up -d` · `docker compose down` | Sobe · derruba o sistema do `compose.yaml` |
| `docker compose logs servico` · `docker compose exec servico comando` | Logs · roda comando dentro do serviço |
