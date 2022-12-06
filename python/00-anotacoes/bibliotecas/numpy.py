# módulo numpy (numerical python)
# biblioteca com conjunto de vários módulos, usada para alto desempenho em funções matemáticas
# muito usado para data science, preparado com otimizações e facilidades de código
# o numpy serve como base para a construção de outros pacotes, como o pandas
# numpy possui objeto array multidimensional com desempenho muito elevado, que permite a utilização de operações numéricas sem a necessidade de usar o formatação
# array tem desempenho melhor para operações matemáticas do que listas
# array não permite dados de tipos diferentes
# funções para trabalhar com array sem necessidade de laços 'for'
# instalar com 'pip install numpy' (usar '!' em jupyter notebooks)
import numpy as np

file1 = np.loadtxt('file.txt')              # carrega um arquivo txt para um dentro de um array numpy (numpy.ndarray)
file2 = np.loadtxt('file.txt', dtype = int) # dtype define o tipo dos valores da variável

# comparando com listas do python
# lista python   
py_list = list(range(10))
py_list = [x * 2 for x in py_list]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# mesmo efeito, usando array numpy (com melhor processamento)
np_array = np.arange(10)
np_array *= 2                       # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
type(np_array)  # numpy.ndarray

# arrays numpy permitem operações simples entre si
numeros = np.array([1, 3.5])    # cria um array numpy a partir de uma lista => array([1. , 3.5])
numeros + 3                     # realiza a operação aos itens do array => array([4. , 6.5])

km = np.array([44410., 37123., 0.])
anos = np.array([2003, 1990, 2019])
idade = 2019 - anos
idade   # array([16, 29,  0])
km_media = km / idade
km_media    # array([2775.625     , 1280.10344828,           nan])
# divisões por zero são substituídas por 'nan' (not a number)

dados = np.array([km, anos])    # cria um array de duas dimensões
dados       # array([[44410., 37123.,     0.] / [ 2003.,  1990.,  2019.]])
dados.shape # retorna uma tupla com o tamanho do array (linhas, colunas) => (2, 3)
dados.ndim  # retorna o número de dimensões do array => '2' (linhas e colunas)
dados.size  # retorna o número de elementos do array => '6'
dados.dtype # tipo de dados do array => dtype('float64')
dados.T             # retorna o array transposto, converte linhas em colunas e vice-versa
dados.transpose()   # equivalente ao .T
# array([[44410.,  2003.] / [37123.,  1990.] / [    0.,  2019.]])
dados[0]    # retorna a primeira 'linha' => array([44410., 37123.,     0.])
dados[1]    # array([2003., 1990., 2019.])
km_media = dados[0] / (2019 - dados[1])
km_media    # array([2775.625     , 1280.10344828,           nan])
# acessar valor dentro de um array
dados[1][2]     # [linha][coluna] => 2019
dados[1, 2]     # [linha, coluna] => 2019
dados.tolist()  # retorna o array numpy em uma lista do python => [[44410.0, 37123.0, 0.0], [2003.0, 1990.0, 2019.0]]
contador = np.arange(6)  # cria um array com o tamanho determinado, similar ao range(6)
contador    # array([0, 1, 2, 3, 4, 5])
contador.reshape((3, 2))    # retorna um array com os mesmos dados, em uma nova forma (colunas, linhas)
# array([[0, 1] / [2, 3] / [4, 5]])
contador.reshape((3, 2), order='C') # valor padrão
contador.reshape((3, 2), order='F') # array([[0, 3] / [1, 4] / [2, 5]])

info = [44410., 37123., 0.] + [2003, 1990, 2019]
info    # [44410.0, 37123.0, 0.0, 2003, 1990, 2019]
np.array(info).reshape((2, 3), order='F')  # array([[44410.,     0.,  1990.] / [37123.,  2003.,  2019.]])

# fatiamento
# array[i:j:k], onde o 'j' é exclusivo, e 'k' é o intervalo
contador = np.arange(10)    # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
contador[1:8:2] # array([1, 3, 5, 7]) vai do 1 ao 8, com intervalo de 2
contador[::2]   # array([0, 2, 4, 6, 8]) usa apenas o intervalo de 2
contador = np.arange(10)
contador[contador > 5]  # array([6, 7, 8, 9])

dados[:, 1:3]   # primeiro parâmetro selecionando todas as linhas, segundo parâmetro selecionando colunas
# array([[37123.,     0.], [ 1990.,  2019.]])
dados[:, 1:3][0]    # usa o fatiamento e seleciona a linha indice 0 => array([37123.,     0.])
km_media = dados[:, 1:3][0] / (2019 - dados[:, 1:3][1])
km_media    # array([1280.10344828,           nan])
dados[:, dados[1] > 2000]   # array([[44410.,     0.], [ 2003.,  2019.]])

ndados = dados.copy()
ndados.resize((3, 3), refcheck=False)   # altera a forma e o tamanho do array (refcheck=False para não checar referência do conteúdo copiado)
ndados  # array([[44410., 37123.,     0.] / [ 2003.,  1990.,  2019.] / [    0.,     0.,     0.]])
ndados[2] = ndados[0] / (2019 - ndados[1])
ndados  # array([[44410., 37123.,     0.] / [ 2003.,  1990.,  2019.] / [ 2775.625     ,  1280.10344828,            nan]])

valor = np.array([7283.21, 5644.52, 8807.86])
dataset = np.column_stack((km, anos, valor))    # transforma arrays unidimensionais em colunas de um array bidimensional
dataset # array([[44410.  ,  2003.  ,  7283.21] / [37123.  ,  1990.  ,  5644.52] / [    0.  ,  2019.  ,  8807.86]])
dataset.shape   # (3, 3)
np.mean(dataset, axis=0)    # retorna a média das colunas
# array([27177.66666667,  2004.        ,  7245.19666667])
np.mean(dataset, axis=1)    # retorna a média das linhas
# array([17898.73666667, 14919.17333333,  3608.95333333])
np.mean(dataset[:, 0])  # média da primeira coluna => 27177.666666666668
np.std(dataset[:, 2])   # calcula o desvio padrão => 1291.7078485564073
dataset.sum(axis=0)     # soma todas as colunas => array([81533.  ,  6012.  , 21735.59])
np.sum(dataset, axis=0) # mesmo efeito
dataset[:, 0].sum()     # soma a coluna 0 => 81533.0
np.sum(dataset[:, 0])   # mesmo efeito
np.random.rand(9)       # gera um número, dentro da quantidade informada
np.random.seed()        # gera um número aleatório
np.random.permutation() # distribui uma sequência de números de forma aleatória, pode receber um 'len'
np.random.choice()      # escolhe aleatoriamente elementos de uma lista, recebe '(lista, quantidade)'.
np.random.exponential() # recebe (scale= ,size= ) e retorna amostras aleatórias de distribuição exponencial
