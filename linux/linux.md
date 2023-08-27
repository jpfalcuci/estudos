# Guia de Linux

## História do Linux

O Linux é um sistema operacional de código aberto do tipo Unix, que teve origem a partir do sistema operacional Unix da empresa de telecomunicações AT&T. A AT&T licenciou o código-fonte do Unix para universidades por um valor simbólico.

Em 1984, Richard M. Stallman iniciou o projeto GNU com o objetivo de reescrever o Unix. No entanto, ainda faltava o kernel para completar o sistema operacional. Nesse contexto, surgiu a licença GPL (GNU Public License), que possui algumas características importantes:
- Softwares produzidos sob essa licença devem ser distribuídos livremente.
- Pessoas com acesso ao código podem utilizar, editar e criar softwares a partir dele.
- Softwares criados podem ser revendidos, mas devem permanecer como software livre.

Em 1991, Linus Torvalds começou a desenvolver seu próprio kernel. Seu objetivo era usar em casa o mesmo sistema operacional que ele usava na universidade (Unix). Esse kernel era o que faltava para criar um sistema operacional tipo Unix com licença GPL.

A partir do kernel Linux, diversas distribuições de Linux foram criadas, como Red Hat, Debian, Suse, entre outras. Algumas distribuições referem-se ao kernel como "GNU/Linux".

## Kernel do Linux

O kernel é o núcleo de um sistema operacional e é responsável por intermediar a comunicação entre hardware e software. A combinação do kernel com outros softwares forma o sistema operacional.

O Linux utiliza um kernel monolítico, que gerencia a CPU, memória, IPC, drivers e sistema de arquivos. Existem outros tipos de kernels, como microkernel e kernel híbrido.

## Módulos do Kernel

Os módulos do kernel são responsáveis por gerenciar os drivers utilizados para a comunicação com o hardware. Você pode listar os módulos com o comando `lsmod`.

## Estrutura de Diretórios

- **/bin**: Arquivos binários do Linux.
- **/boot**: Arquivos de configuração de boot da máquina.
- **/dev**: Diretório de montagem de dispositivos.
- **/etc**: Arquivos de configuração do sistema e de softwares.
- **/home**: Diretório dos usuários.
- **/lib**: Bibliotecas do sistema.
- **/media**: Usado para montar mídias removíveis como CDs e pendrives.
- **/mnt**: Usado para montar temporariamente outros sistemas de arquivos.
- **/opt**: Softwares instalados, complementares.
- **/proc**: Informações do hardware da máquina.
- **/root**: Diretório do usuário root.
- **/sbin**: Comandos que exigem privilégios de administrador.
- **/srv**: Dados específicos de serviços.
- **/tmp**: Diretório temporário.
- **/usr**: Contém subdiretórios com programas, bibliotecas, documentação e mais.
- **/var**: Arquivos variáveis e dinâmicos, incluindo logs.

## Comandos Essenciais

- `man`: Mostra o manual de um comando.
- `pwd`: Mostra o diretório atual.
- `cd`: Acessa um diretório.
- `ls`: Lista o conteúdo de um diretório.
- `mkdir`: Cria um diretório.
- `touch`: Altera a data de criação de um arquivo.
- `rm`: Apaga arquivos.
- `mv`: Move e renomeia.
- `cp`: Copia arquivos.
- `find`: Procura arquivos no Linux.
- `clear`: Limpa a tela.
- Gerenciamento de pacotes:
  - `yum` | `dnf` | `apt`: Instala pacotes no Linux.
- `service`: Gerencia serviços (start, stop, status).
- Visualização de arquivos:
  - `tail`: Exibe as últimas linhas de um arquivo.
  - `cat`: Visualiza um arquivo.
- Uso de espaço em disco:
  - `du`: Mostra o tamanho da pasta.
  - `df`: Mostra a utilização da pasta.
- Gerenciamento de usuários:
  - `useradd`: Cria um usuário.
  - `passwd`: Altera a senha de um usuário.
- Elevação de privilégios:
  - `sudo`: Executa um comando com privilégios de administrador.
- Gerenciamento de discos:
  - `fdisk`: Gerencia discos e partições.
  - `mkfs`: Formata partições.
  - `mount`: Monta uma partição.
  - `umount`: Desmonta uma partição.
  
## Criação de Scripts

Um script é uma sequência de comandos executados de forma ordenada.

Exemplo de um script básico:

```bash
#!/bin/bash

mkdir directory
cd directory
mkdir dir1 dir2 dir3
cd dir1
touch file1 file2
cd ../dir2
touch file3 file4
```

## Instalação de Pacotes (Ubuntu)

Atualize os repositórios:

```bash
sudo apt update
```

Instale pacotes:

```bash
sudo apt install pacote
```

## Gerenciamento de Logs

Os logs são armazenados em `/var/log/`. Você pode visualizá-los com o comando `cat` ou monitorar em tempo real com o `tail -f`. Para filtrar logs, use `grep`.

## Gerenciamento de Permissões

As permissões são definidas como r, w e x, correspondendo a read, write e execution. O formato de permissões é rwx rwx rwx (objeto | dono | grupo | outros). Use o comando `chmod` para alterar permissões.

## Criação de Usuários

Use comandos como `useradd`, `passwd`, `su` e `sudo` para gerenciar usuários e permissões.

## Gerenciamento de Discos

Use o comando `fdisk` para gerenciar discos e partições. Formate partições com `mkfs` e monte-as com `mount`. Desmonte com `umount`.
