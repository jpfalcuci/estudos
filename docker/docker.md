# Docker

O Docker é uma plataforma de código aberto que permite desenvolver, empacotar e executar aplicativos em contêineres. Contêineres são ambientes isolados e portáteis que contêm tudo o que é necessário para executar um aplicativo, incluindo código, bibliotecas e dependências.

## Índice

1. [Introdução ao Docker](#1-introdução-ao-docker)
2. [Instalação](#2-instalação)
3. [Comandos Básicos](#3-comandos-básicos)
   - 3.1 [docker run](#31-docker-run)
   - 3.2 [docker ps](#32-docker-ps)
   - 3.3 [docker images](#33-docker-images)
   - 3.4 [docker build](#34-docker-build)
   - 3.5 [docker exec](#35-docker-exec)
4. [Gerenciamento de Contêineres](#4-gerenciamento-de-contêineres)
   - 4.1 [Iniciar e Parar Contêineres](#41-iniciar-e-parar-contêineres)
   - 4.2 [Remover Contêineres](#42-remover-contêineres)
   - 4.3 [Logs e Acompanhamento](#43-logs-e-acompanhamento)
5. [Criação de Imagens](#5-criação-de-imagens)
   - 5.1 [Dockerfile](#51-dockerfile)
   - 5.2 [Construindo Imagens](#52-construindo-imagens)
6. [Redes no Docker](#6-redes-no-docker)
   - 6.1 [Criar Rede](#61-criar-rede)
   - 6.2 [Conectar Contêineres à Rede](#62-conectar-contêineres-à-rede)
7. [Volumes](#7-volumes)
   - 7.1 [Montar Volumes](#71-montar-volumes)
   - 7.2 [Volumes de Bind](#72-volumes-de-bind)
8. [Docker Compose](#8-docker-compose)
9. [Boas Práticas de Uso](#9-boas-práticas-de-uso)
10. [Referências](#10-referências)

---

## 1. Introdução ao Docker

O Docker permite empacotar um aplicativo e suas dependências em um único contêiner, garantindo consistência e portabilidade em diferentes ambientes.

## 2. Instalação

Para instalar o Docker, siga as instruções fornecidas no [site oficial](https://docs.docker.com/get-docker/).

**Instalação no Ubuntu:**

- Atualizar o sistema
  ´´´shell
  sudo apt update
  ´´´
- Instalar pacotes de pré-requisitos para permitir o uso de pacotes seguros HTTPS
  ´´´shell
  sudo apt install apt-transport-https ca-certificates curl software-properties-common
  ´´´
- Baixar a chave GPG para garantir a validade dos pacotes do repositório do Docker
  ´´´shell
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  ´´´
- Adicionar o repositório Docker às fontes de pacotes do Ubuntu
  ´´´shell
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ´´´
- Atualizar novamente o sistema e instalar
  ´´´shell
  sudo apt update
  sudo apt install docker-ce
  ´´´
- Verificar a instalação
  ´´´shell
  sudo systemctl status docker
  docker --version
  ´´´
- Adicionar o usuário ao grupo 'docker'
  ´´´shell
  sudo usermod -aG docker ${USER}
  su - ${USER}
  ´´´

## 3. Comandos Básicos

### 3.1 docker run

O comando ´docker run´ cria e inicia um novo contêiner a partir de uma imagem.

Exemplo:

´´´shell
docker run -it ubuntu:latest /bin/bash
´´´

Este comando cria e executa um contêiner Ubuntu, iniciando um shell interativo (/bin/bash) dentro do contêiner.

### 3.2 docker ps

O comando ´docker ps´ lista os contêineres em execução, mostrando informações como ID, nome, imagem usada e status.

Exemplo:

´´´shell
docker ps
´´´

### 3.3 docker images

O comando ´docker images´ lista as imagens disponíveis no sistema, mostrando informações como nome, tag, ID da imagem e tamanho.

Exemplo:

´´´shell
docker images
´´´

### 3.4 docker build

O comando ´docker build´ cria uma nova imagem a partir de um Dockerfile.

Exemplo:

´´´shell
docker build -t my-app:latest .
´´´

Nesse exemplo, estamos construindo uma nova imagem chamada my-app com a tag latest a partir do contexto atual (o diretório atual contendo o Dockerfile).

### 3.5 docker exec

O comando ´docker exec´ permite executar comandos dentro de um contêiner em execução.

Exemplo:

´´´shell
docker exec -it meu-container /bin/bash
´´´

Este comando executa um shell interativo (/bin/bash) dentro do contêiner meu-container.

## 4. Gerenciamento de Contêineres

### 4.1 Iniciar e Parar Contêineres

- Iniciar um contêiner:
  ´´´shell
  docker start nome-do-container
  ´´´
- Parar um contêiner:
  ´´´shell
  docker stop nome-do-container
  ´´´

### 4.2 Remover Contêineres

O comando ´docker rm´ remove contêineres.

Exemplo:

´´´shell
docker rm nome-do-container
´´´

### 4.3 Logs e Acompanhamento

- Ver logs de um contêiner:
  ´´´shell
  docker logs nome-do-container
  ´´´
- Acompanhar logs em tempo real:
  ´´´shell
  docker logs -f nome-do-container
  ´´´

## 5. Criação de Imagens

### 5.1 Dockerfile

O Dockerfile é um arquivo de configuração que define como uma imagem é construída.

Exemplo:

´´´Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl
CMD ["curl", "https://www.example.com"]
´´´

### 5.2 Construindo Imagens

´´´shell
docker build -t nome-da-imagem .
´´´

## 6. Redes no Docker

### 6.1 Criar Rede

Criar uma nova rede Docker com o nome especificado.

´´´shell
docker network create nome-da-rede
´´´

### 6.2 Conectar Contêineres à Rede

Conecta um contêiner à rede especificada pelo nome.

´´´shell
docker network connect nome-da-rede nome-do-container
´´´

## 7. Volumes

### 7.1 Montar Volumes

Montar um volume dentro do contêiner, permitindo que dados sejam persistentes entre as execuções.

´´´shell
docker run -v /caminho/local:/caminho/contêiner ...
´´´

### 7.2 Volumes de Bind

Criar um volume de bind, que permite que um diretório no host seja compartilhado com o contêiner.

´´´shell
docker run -v /caminho/host:/caminho/contêiner ...
´´´

## 8. Docker Compose

O Docker Compose permite definir e executar aplicativos multicontêiner em um único arquivo de configuração.

Exemplo de ´docker-compose.yml´:

´´´yaml
version: '3'
services:
  web:
    image: nginx
  db:
    image: mysql
´´´

## 9. Boas Práticas de Uso

- Mantenha imagens leves e minimalistas.
- Use volumes para persistência de dados.
- Evite rodar processos em background nos contêineres.
- Use o Docker Hub para compartilhar imagens.

## 10. Referências

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
