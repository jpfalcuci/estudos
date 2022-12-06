# módulo sql alchemy
# biblioteca de mapeamento SQL
# instalar usando 'pip install sqlalchemy'
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect
df = 'DataFrame'
engine = create_engine('sqlite:///:memory:')    # sqlite é nativo do python, usando memória local
df.to_sql('nome_tabela', engine)
inspect(engine)                     # cria um inspector object
inspect(engine).get_table_names()   # exibe os nomes das tabelas contidas em 'engine'
query = 'select * from nome_tabela where condição'  # faz uma query no DB sql; * => todos
pd.read_sql(query, engine)          # lê sql usando a query
pd.read_sql_table('nome_tabela', engine, columns=['colunas'])
df2 = 'DF2'
df2.to_sql('outra_tabela', con=engine)                  # adiciona outra tabela em 'engine'
df.set_index('id').joindf2.set_index('id')[['coluna']]  # une os dois DFs comparando o id
