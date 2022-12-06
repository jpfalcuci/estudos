# pandas é um pacote de manipulação de dados de alto nível, construído com base no pacote numpy
# instalar com 'pip install pandas'
# principal estrutura de dados do pandas é o DataFrame
# pandas classifica string como 'object'
# ao contrário do array numpy, o DataFrame permite dados diferentes
import pandas as pd
pd.set_option('display.max_rows', 100)      # para definir a qtd de linhas a mostrar
pd.set_option('display.max_columns', 100)   # para definir a qtd de colunas a mostrar
pd.__version__  # verifica a versão do pandas

# Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado
# os rótulos das linhas são chamados de index
# basicamente é uma tabela de uma coluna
s = pd.Series('dados', index = 'index')
# 'dados' podem ser dict, list, arrayNP ou uma constante
# index= recebe rótulos para os índices

# DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linhas e colunas, também armazenam qualquer tipo de dado
# basicamente, é uma tabela normal, com várias colunas; conjunto de Series
df = pd.DataFrame('dados', index = 'index', columns = 'columns', index_col = 0)
# dados podem ser dict, list, arrayNP, series ou outro DataFrame
# columns= para rotular colunas; index= para rotular índices; index_col atribui coluna como índice
# DataFrame ou Series gerados com dicionário, vão usar as chaves como rótulos das colunas

# importando e exportando arquivos
s = s + 2   # realiza operação em todos os itens da Series (ou NaN)
json = pd.read_json('file.json')
txt = pd.read_table('file.txt')
xlsx = pd.read_excel('file.xlsx')
import html5lib
html = pd.read_html('file.html')    # pode receber uma url; retorna uma lista de DF, com conteúdo da(s) tabela(s); usar 'html[0]' para visualizar como DF
df = pd.read_csv('file.csv', sep=';')
df.to_csv('caminho/file.csv', sep=';', index=False) # index=False para index não ser exportado como nova coluna
df.to_excel('caminho/file.csv', index=False)
df.to_json()
df.to_html()

s.unique()                  # retorna os elementos únicos em um array, sem repetição
s.value_counts()            # retorna a contagem de elementos únicos
df.head()                   # mostra as 5 primeiras linhas do DF, ou a quantidade informada em '( )'
df.sample()                 # retorna um registro aleatóriamente, ou a quantidade informada em '( )'
df.dtypes                   # retorna os tipos de dados de cada coluna
df.info()                   # informações resumidas do DataFrame
df.shape                    # retorna uma tupla com o tamanho do DF (linhas, colunas) ou (registros, variaveis)
df.shape[0]                 # 0 retorna a qtd de linhas, 1 retorna a qtd de colunas
df.columns.name = 'Indice'  # rotula a coluna dos índices
df.index = range(1,(len(df)+1))         # define um novo índice começando de 1
df.index = range(1,(df.shape[0]+1))     # outra forma com o mesmo resultado
df.coluna1                  # forma de consultar valores da coluna (só funciona se o nome não tiver espaços)
df['Coluna1']               # retorna os valores da coluna e o índice, em formato Series
df[['Coluna1']]             # retorna os valores da coluna e o índice, em formato DataFrame
df[['Col1', 'Col2']].describe()         # gera um DF com um conjunto de estatísticas descritivas da coluna informada
                                        # count, mean, std, min, 25%, 50%, 75%, max
df['Col1'].aggregate(['min', 'sum'])    # gera um DF com um conjunto de estatísticas solicitadas
df['Col1'].aggregate(['min', 'sum']).rename(columns = {'min':'Minimo', 'sum':'Soma'})
df[['Coluna2', 'Coluna1']]  # altera a ordem de visualização do DataFrame (não altera o objeto)
df[0:3]                     # retorna as linhas 0, 1 e 2 (selecionadas no slice)
df[0:3][['Col1', 'Col2']]   # retorna seleção de linhas e colunas
df['Nova Col'] = 'Valor'    # cria uma nova variável no DF
df['Nova Col'] = df.C1.str.cat(df.C2).str.lower()   # cria uma nova variável no DF concatenando (str.cat) as strings de C1 com C2 e transformando em minúsculas
df = df.rename(columns={'Col1':'Col1.1'})   # renomear colunas
df['new'] = df['col'].diff()                # cria uma nova coluna com a diferença entre valores da coluna informada
df = pd.DataFrame.from_dict('dict', orient='index').T   # cria DF através de um dicionário, orientando pelo index; .T para transpor linhas para colunas

# tratamento de dados
df['Col'].isna()                            # retorna uma Series booleana, True onde houver valor nulo
df.isnull()                                 # retorna um DF booleano, True onde houver valor nulo
df.notnull()                                # retorna um DF booleano, True onde não houver valor nulo
df['Col'].mean()                            # retorna um DF com valores médios da(s) coluna(s) informadas
df[df.coluna1.isna()]                       # retorna um DF apenas com os itens que contém valor nulo na coluna selecionada
df.fillna(0, inplace=True)                  # substitui os valores nulos por 0, alterando o DF
df = df.fillna({'col1':0, 'col2':0})        # substitui os valores nulos por 0, alterando o DF
df.fillna(method='ffill')                   # substitui os valores nulos copiando o último valor válido (de cima pra baixo)
df.fillna(method='bfill', limit=1)          # mesom efeito, porém de baixo pra cima; limit= para definir limite das cópias
df.fillna(df.mean())                        # substitui os valores nulos usando a média de todos valores não nulos
df.dropna(subset=['coluna2'], inplace=True) # remove todos os itens que contiverem valores nulos na coluna indicada, alterando o DF
df['Col'].drop_duplicates(inplace=True)     # retorna uma Series com elementos únicos
df.astype(float)                            # altera o tipo de valor do DF ou Series
df.set_index('Col1')                        # define uma variável (coluna) como index
df.sort_index(inplace = True)               # ordena dados do DF pela ordem das linhas
df.sort_index(inplace = True, axis = 1)     # ordena dados do DF pela ordem das colunas
df.sort_values(by = ['C1', 'C2'], inplace = True)   # ordena dados do DF pela ordem de valores de uma ou mais colunas
df.sort_values(by = 'R1', axis = 1, inplace = True) # ordena dados do DF pela ordem de valores de uma ou mais linhas
filtro = ['valor1', 'valor2']
sel = df['Col'].isin(filtro)                # retorna uma Series booleana, True onde encontrar valor do 'filtro'
novo_df = df[sel]                           # cria um novo DF, apenas com os valores True da seleção 'sel'
novo_df = df[~sel]                          # cria um novo DF, invertendo (~) a seleção 'sel'
del df['Coluna']                            # exclui a variável do DF
df.pop('Coluna')                            # exclui a variável do DF
df.drop(['C1', 'C2'], axis=1, inplace=True) # exclui mais de uma variável do DF, axis=1 para colunas, 0 para linhas
df['col'] = pd.to_datetime(df['col'])       # converte os valores da coluna em datetime
df['col'].rolling(21).mean()                # acrescenta uma coluna com a "média móvel" dos últimos 21 dados
df['Col'] = df['Col'].apply(lambda x: x.title())    # aplica a função
df = df[['Col1', 'Col2']]                   # reposicionando colunas
df = df.reindex(['index1', 'index2'])       # redefine a ordem dos index

# .loc => seleciona um grupo de linhas e colunas segundo os rótulos ou uma matriz booleana
df.loc['linha']         # retorna uma Series com as informações da linha selecionada
df.loc['l1', 'col2']    # retorna o valor da 'linha 1' na 'coluna 2'
df.loc[['l1', 'l2']]    # retorna um DataFrame com o conteúdo das linhas selecionadas
df.loc[['l1', 'l2'], ['col1', 'col2']]  # retorna um DataFrame com o conteúdo das linhas e colunas selecionadas
df.loc[:, ['col1', 'col2']]     # retorna um DataFrame com todas as linhas e com seleção de colunas

# .iloc => seleciona com base nos índices, se baseia na posição das informações
df.iloc[1]      # retorna uma Series com as informações da linha selecionada
df.iloc[1, 2]   # retorna o valor da linha[1] na coluna[2]
df.iloc[[1]]    # retorna um DF com as informações da linha selecionada
df.iloc[1:4]    # retorna um DF com as informações das linhas selecionadas
df.iloc[1:4, [0, 5, 2]]     # retorna um DF com linhas e colunas selecionadas
df.iloc[[1, 22], [0, 2]]    # retorna um DF com linhas e colunas selecionadas
df.iloc[[1, 22], :]         # retorna um DF com linhas selecionadas e todas as colunas

# .at / .iat
""" PESQUISAR """

# queries
select = df['Col1'] == 'valor'  # retorna uma Series substituindo o valor da coluna1 por valores booleanos (True ou False)
df[select]                      # retorna um DF apenas com os elementos que contém 'valor' na 'coluna1'
df[df['Col1'] == 'valor']
df[(df.coluna1 == 'valorX') & (df.coluna2 == 'valorY')] # retorna um DF onde os valores das duas colunas sejam iguais as condições
df.query('coluna1 == "valorX" and coluna2 == valorY')   # mesmo resultado; 'df' pode ser uma variável que lê um sql

# iteração
list(df.iterrows()) # retorna uma lista com tuplas que contém o índice e uma Series com as informações ('index', Series)
for index, row in df.iterrows():    # passa linha por linha do DF
    if (100 - row['coluna1'] != 0):
        df.loc[index, 'nova_coluna'] = row['coluna1'] + row['coluna2']
    else:
        df.loc[index, 'nova_coluna'] = 0
df['NewCol'] = df['Col'].apply('função')        # aplica uma função para cada registro(linha) do DF (usando DF)
df['NewCol'] = df['Col'].transform('função')    # aplica uma função para cada registro(linha) do DF (usando Series)

# agrupamento
group = df.groupby('Col6')  # cria um objeto 'groupby' do pandas (mantém as informações do DF original, agora agrupando por ('Col6'))
group = df.groupby('Col6')['Col5']  # usando groupby apenas para os valores da 'Col5'
group.groups                # mostra o objeto 'groupby'; contém um dict que usa a chave como indexador ('Col6') e valor uma lista dos índices onde o indexador foi encontrado no DF
group['Col1'].mean()                # retorna a média dos valores de 'Col1'
group[['Col1', 'Col2']].describe()  # retorna um DF apenas com as colunas informadas

# função 'cut' para categorizar as classes, auxilia na criação de distribuição de frequencias
labels = ['1 e 2', '3 e 4', '5 e 6 ', '7 ou mais']
limites = [0, 2, 4, 6, 20]  # [valor min, 1º limite, 2º limite, ..., valor max]
selecao = pd.cut(df.Coluna, limites, labels = labels, include_lowest= True)
pd.value_counts(selecao)    # retorna uma Series somando os valores da coluna de acordo com os limites informados 

# concatenando DataFrames
df1, df2 = 'df1', 'df2'
df = pd.concat([df1, df2])              # une os dois DF em um só, agrupando por colunas (um em cima do outro)
df = pd.concat([df1, df2], axis=1)      # une os dois DF em um só, agrupando por linhas (um do lado do outro)
df = pd.concat([df1, df2])['Valor']     # une os dois DF em uma Series usando a variável 'Valor'
df = pd.concat([df1, df2])['Valor'].to_frame()  # une os dois DF em um outro DF, usando a variável 'Valor'

""" super colunas pandas:
 
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
 
    df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan],[19, 439, 6, 452, 226,232]],
                    index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'], name='Actual Label:'),
                    columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
    df.style """
