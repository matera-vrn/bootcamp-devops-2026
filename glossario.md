# Glossário 📖

Os termos do bootcamp explicados em uma linha, em ordem alfabética. Não decore: volte aqui sempre que uma palavra aparecer e você não lembrar.

| Termo | Em uma linha |
|-------|--------------|
| **amd64 / arm64** | Tipos de processador. amd64 = Intel/AMD (a maioria dos PCs); arm64 = chips Apple M e similares. Cada um precisa da sua versão de sistema |
| **apt** | O "instalador de programas" do Ubuntu: `sudo apt install nome` busca o programa nos repositórios oficiais |
| **bash** | O *shell* padrão do Ubuntu — o programa que lê o que você digita no terminal e executa |
| **binário** | Um programa já pronto para rodar (compilado), em oposição ao código-fonte |
| **blameless** | Cultura de analisar incidentes sem procurar culpados: a pergunta é "o que no processo permitiu o erro?" |
| **branch** | Uma "linha do tempo" paralela no Git para trabalhar sem mexer na versão oficial (`main`) |
| **build** | Montar/empacotar o programa a partir do código: compilar, gerar arquivos, criar a imagem |
| **CI / CD** | Integração Contínua (integrar e testar o código automaticamente a cada mudança) / Entrega Contínua (deixar cada versão pronta para produção) |
| **commit** | Uma "foto" do projeto gravada no histórico do Git, com autor, data e mensagem |
| **container** | Um programa empacotado com tudo que precisa, rodando isolado — como um "apartamento" dentro do sistema |
| **cron** | O "despertador" do Linux: executa comandos em horários agendados |
| **deploy** | Colocar uma versão do sistema no ar (em produção) |
| **/dev/null** | O "buraco negro" do Linux: tudo que é enviado para lá some. Usado para descartar a saída de um comando |
| **DevSecOps** | DevOps com segurança desde o início: verificações de segurança fazem parte da esteira |
| **diretório** | O mesmo que pasta |
| **distribuição (distro)** | Um "pacote completo" de Linux: o kernel mais as ferramentas. Ubuntu, Debian, Fedora são distribuições |
| **DNS** | A "agenda de contatos" da internet: traduz nomes (`matera.com`) em endereços IP |
| **Docker Hub** | O "mercado público" de imagens Docker prontas (`ubuntu`, `nginx`, `redis`...) |
| **Dockerfile** | A receita, em texto, para construir uma imagem Docker |
| **esteira** | O mesmo que *pipeline*: a sequência automática de etapas que o código percorre até produção |
| **GitHub Actions** | O serviço de CI/CD embutido no GitHub: executa a pipeline descrita em um arquivo YAML dentro do repositório |
| **hash (SHA256)** | A "impressão digital" de um arquivo: um código que muda se um único byte mudar. Serve para conferir downloads |
| **hostname** | O nome da máquina na rede (na VM do bootcamp: `bootcamp`) |
| **HTTP / HTTPS** | O "idioma" da web, usado entre navegador e servidor. O S é a versão criptografada |
| **imagem (Docker)** | O pacote pronto e imutável gerado pelo Dockerfile; um container é uma imagem em execução |
| **indentação** | Os espaços no início de uma linha. Em YAML, dizem "isto está dentro daquilo" |
| **IP** | O endereço de uma máquina na rede (ex.: `10.0.2.15`) |
| **ISO** | Um "DVD de instalação" em forma de arquivo (`.iso`) |
| **kernel** | O núcleo do sistema operacional: conversa com o hardware e gerencia tudo. O Linux, a rigor, é o kernel |
| **localhost** | O endereço da própria máquina (`127.0.0.1`): falar com `localhost` é falar consigo mesmo |
| **log** | O "diário de bordo" de um programa ou do sistema: registro do que aconteceu, com horário. Vivem em `/var/log` |
| **LTS** | *Long Term Support*: versão com suporte longo (5 anos no Ubuntu), a preferida em empresas |
| **markdown** | Linguagem simples de formatação de texto usada em READMEs: `#` vira título, `-` vira lista |
| **merge** | Juntar uma branch em outra (ex.: integrar sua branch na `main`) |
| **NAT** | Modo de rede em que a VM fica "escondida" atrás do seu computador, usando a internet dele |
| **nginx** | Um servidor web muito usado: entrega páginas HTML para quem acessa |
| **PAT (token)** | *Personal Access Token*: uma "senha de aplicativo" do GitHub, com validade e permissões limitadas |
| **PID** | O número de identificação de um processo em execução |
| **pipe (`\|`)** | Liga a saída de um comando à entrada do próximo: `ps aux \| grep bash` |
| **pipeline** | Veja *esteira* |
| **porta** | A "porta da casa" por onde um serviço atende: web na 80/443, SSH na 22 |
| **post-mortem** | A análise feita depois de um incidente, para aprender e evitar que se repita |
| **processo** | Um programa em execução |
| **prompt** | A linha do terminal que fica esperando seu comando (`aluno@bootcamp:~$`) |
| **Pull Request (PR)** | O pedido para revisarem e integrarem sua branch na `main`, feito no GitHub |
| **push / pull** | Enviar seus commits para o GitHub / trazer os commits novos de lá |
| **Redis** | Um banco de dados em memória, rápido, muito usado para contadores e cache |
| **registry** | Um "depósito" de imagens Docker (o Docker Hub é o mais conhecido) |
| **repositório** | A pasta do projeto com o histórico do Git dentro (`.git`) |
| **root** | O superusuário do Linux: pode tudo. `sudo` executa um único comando como root |
| **runner** | A máquina que executa a pipeline no GitHub Actions |
| **script** | Um arquivo de texto com comandos que o shell executa em sequência |
| **shebang** | A primeira linha de um script (`#!/bin/bash`), que diz qual programa deve executá-lo |
| **shell** | O programa que interpreta seus comandos no terminal (no Ubuntu, o *bash*) |
| **SSH** | Forma segura de usar o terminal de outra máquina a partir da sua |
| **stage** | Uma etapa da esteira (build, teste, deploy) |
| **sudo** | "Super user do": executa o comando seguinte com poderes de root |
| **systemctl / systemd** | O gerenciador de serviços do Linux; `systemctl` liga, desliga e consulta serviços (ssh, docker, cron...) |
| **terminal** | A janela onde você digita comandos para o shell |
| **variável** | Um nome que guarda um valor: `NOME="Matera"`, lido com `$NOME` |
| **vi (Vim)** | O editor de texto presente em todo Linux. É *modal*: `i` para escrever, `Esc` para voltar aos comandos, `:wq` salva e sai, `:q!` sai sem salvar |
| **VM (máquina virtual)** | Um computador completo simulado por software dentro do seu — a VM Ubuntu do bootcamp roda no VirtualBox |
| **volume** | Um espaço de armazenamento que sobrevive à destruição de um container |
| **workflow** | A pipeline, no vocabulário do GitHub Actions |
| **WSL** | *Windows Subsystem for Linux*: roda um Ubuntu de verdade dentro do Windows, sem VM |
| **YAML** | Formato de texto para configurações (usado no compose e no GitHub Actions), sensível à indentação |
