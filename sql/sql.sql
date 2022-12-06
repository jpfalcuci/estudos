-- ##### banco de dados sql #####

-- banco de dados é um conjunto de arquivos relacionados entre si com diversos registros de informação
-- armazenar dados de forma segura e com integridade, com integração com sistemas web

-- bd relacionais são informações em tabelas que se relacionam, tipo mais comum
-- bd não relacionais (nosql), mais performance(?)

-- sql = structured query language (linguagem de consulta estruturada)
-- bancos de dados possuem sistemas de gerenciamento (já que sql é a linguagem usada)
-- MySQL é um dos sistemas mais usados, se popularizou devido ao suporte a linguagem de programação web
-- phpMyAdmin é um app PHP p/ administração do MySQL pela internet
-- operações CRUD => Creat, Read, Update e Delete

-- banco de dados devem executar transações, e a integridade regida por 4 propriedades:
--     atomicidade: todas as ações devem ser concluídas com sucesso, ou se falha, desfazer (rollback)
--     consistência: deve=se obedecer regras e restrições definidas em um banco, ex: chaves estrangeiras, campos únicos
--     isolamento: cada transação deve ser independente de outras transações
--     durabilidade: os resultados de uma transação devem ser permanentes, exceto se desfeito por outra transação

-- quando se cria uma tabela em sql, é preciso definir quais tipos de dados a serem armazenados
--     char    varchar    int    float, double    date    not null    auto_increment   primary_key    foreign_key    text

-- comandos básicos
--     CREATE DATABASE NOME => criar bases de dados
--     CREATE TABLE NOME(COLUNAS TIPO) => criar tabelas
--     SELECT * FROM TABELA => selecionar dados
--     DELETE FROM TABELA => deletar dados de uma tabela
-- outros DROP, UPDATE, ALTER

-- sistemas famosos de gerenciamento de bancos de dados são MySQL, SQL Server, Maria DB, Cassandra, MongoDB, Voldemort