# SQL

## Instalação no Ubuntu

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ sudo mysql_secure_installation
$ sudo mysql
```

```sql
SELECT user,authentication_string,plugin,host FROM mysql.user;
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'P4ssw0rd';
-- ou
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'P4ssw0rd';
FLUSH PRIVILEGES;
exit;
```

Para alterar a senha do usuário root:

```bash
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyN3wP4ssw0rd';
FLUSH PRIVILEGES;
exit;
```

Para alterar a senha do usuário postgres:

```bash
sudo -u postgres psql
\password postgres
\q
```

## Docker

### MySQL

```bash
docker run --name mysql -e MYSQL_ROOT_PASSWORD=Password -d -p 3306:3306 --restart=always mysql
docker exec -it mysql bash
mysql -uroot -p Password
```

No DBeaver, altere `allowPublicKeyRetrieval` de `false` para `true` nas propriedades do driver.

### PostgreSQL

```bash
docker run --name postgres -e POSTGRES_PASSWORD=Password -d -p 5432:5432 --restart=always postgres
```

### SQL Server

```bash
docker run --name sqlserver -e ACCEPT_EULA=Y -e MSSQL_SA_PASSWORD=Password123 -p 1433:1433 -d --restart=always mcr.microsoft.com/mssql/server:2022-latest
```

## Banco de Dados SQL

Um banco de dados é um conjunto de arquivos relacionados entre si contendo diversos registros de informação. Eles armazenam dados de forma segura e com integridade, permitindo a integração com sistemas web.

Bancos de dados podem ser relacionais, com informações organizadas em tabelas que se relacionam entre si, ou não relacionais (NoSQL), que tendem a focar em performance.

SQL (Structured Query Language) é a linguagem utilizada para consultar bancos de dados. Cada banco de dados é gerenciado por um sistema de gerenciamento de banco de dados (DBMS). MySQL é um dos sistemas mais populares, com suporte à linguagem de programação web. O phpMyAdmin é uma ferramenta web para administrar bancos de dados MySQL.

As operações básicas em bancos de dados são CRUD: Create, Read, Update e Delete.

Transações em bancos de dados seguem quatro propriedades ACID:

- **Atomicidade**: Todas as ações devem ser concluídas com sucesso ou desfeitas em caso de falha.
- **Consistência**: Deve obedecer regras e restrições definidas no banco de dados.
- **Isolamento**: Cada transação deve ser independente das outras.
- **Durabilidade**: Os resultados de uma transação devem ser permanentes, a menos que desfeitos por outra transação.

Ao criar tabelas, é preciso definir os tipos de dados para armazenar informações:

- char, varchar, int, float, double, date, not null, auto_increment, primary_key, foreign_key, text.

Comandos básicos incluem:

- `CREATE DATABASE NOME`: Criar bases de dados.
- `CREATE TABLE NOME(COLUNAS TIPO)`: Criar tabelas.
- `SELECT * FROM TABELA`: Selecionar dados.
- `DELETE FROM TABELA`: Deletar dados de uma tabela.

Sistemas populares de gerenciamento de bancos de dados incluem MySQL, SQL Server, MariaDB, Cassandra, MongoDB e Voldemort.

## Anotações Adicionais

### Banco de Dados Relacionais

Bancos de dados relacionais organizam informações em tabelas com linhas (registros) e colunas (atributos). Tabelas relacionam-se entre si através de chaves primárias e estrangeiras.

### Banco de Dados Não Relacionais (NoSQL)

Bancos de dados NoSQL são mais flexíveis e escaláveis, ideais para lidar com grandes volumes de dados variáveis. Eles não seguem o modelo de tabela tradicional e podem usar estruturas como documentos, grafos ou colunas.

### Operações CRUD

- **Create**: Inserir novos dados na tabela.
- **Read**: Recuperar dados da tabela.
- **Update**: Atualizar dados existentes na tabela.
- **Delete**: Remover dados da tabela.

### Consultas SQL

Consultas SQL permitem buscar informações específicas de um banco de dados. Exemplo:

```sql
SELECT nome, idade FROM clientes WHERE cidade = 'São Paulo';
```

### JOINs

Os JOINs permitem combinar informações de diferentes tabelas em uma única consulta. Os tipos de JOIN mais comuns são INNER JOIN, LEFT JOIN e RIGHT JOIN.

### Índices

Índices melhoram a performance de consultas ao acelerar a busca de informações nas tabelas. Eles são criados em colunas específicas e facilitam o acesso aos dados.

### Transações

Transações garantem a integridade dos dados. Elas consistem em uma sequência de operações tratadas como uma única unidade. No SQL, transações são controladas pelos comandos BEGIN, COMMIT e ROLLBACK.

### Stored Procedures e Funções

Stored Procedures e Funções permitem criar blocos de código SQL que podem ser chamados como funções. Isso centraliza a lógica no banco de dados e melhora a segurança.

### Subconsultas

Subconsultas são consultas aninhadas dentro de outras consultas. Elas podem ser usadas em cláusulas WHERE, FROM e HAVING.

### Views

Views são consultas SQL predefinidas que podem ser tratadas como tabelas virtuais. Elas simplificam a complexidade das consultas e permitem reutilização de lógica.

### Triggers

Triggers são ações automáticas executadas quando um evento específico ocorre em uma tabela. Elas são úteis para manter a integridade dos dados.

### Noções Avançadas

- **Normalization (Normalização)**: Processo de organizar dados em tabelas para reduzir a redundância e melhorar a integridade.
- **ACID Transactions**: Propriedades que garantem a consistência e confiabilidade das transações.
- **Database Design**: Processo de modelagem de banco de dados para atender aos requisitos do sistema.
- **Performance Tuning**: Otimização de consultas e estruturas para melhorar a velocidade do banco de dados.
