""" estruturas de dados (coleções) são estruturas que permitem guardar diversos valores ('sequence types' na documentação) """


##### LISTAS #####
# estrutura iterável que pode ter seus valores alterados e podem receber objetos com tipos diferentes (não recomendado)

list()                  # recebe um iterável e converte itens em uma lista; cria uma lista vazia
list('321')             # ['3', '2', '1']
lista = [0, 1, 2, 3, 4] # cria uma lista e atribui a uma variável

# funções de listas
1 in lista              # retorna True se encontrar o valor dentro da lista
len(lista)              # 5; retorna o comprimento/quantidade de itens da lista
max(lista)              # 4; retorna o maior valor da lista
min(lista)              # 0; retorna o menor valor da lista
lista.count(2)          # 1; retorna o número de ocorrências de um valor dentro da lista
lista.append(5)         # [..., 3, 4, 5]; acrescenta o item informado ao final da lista
lista.insert(0, 8)      # [8, 0, 1 ... 5]; insere um item na lista na posição informada (index, item)
lista.extend([7, 9])    # [..., 4, 5, 7, 9]; adiciona multiplos elementos a lista a partir de outro iterável
lista.pop()             # 9; devolve e remove o último item da lista ou o item informado (i)
lista.remove(5)         # [..., 3, 4, 7]; remove da lista a primeira ocorrência encontradado do item informado
lista.index(4)          # 5; retorna o índice da primeira ocorrência de (i)
lista[2]                # 1; retorna o valor da lista no íncide [i]
lista[-1]               # 7; retorna o último valor da lista; [-2], [-3]
lista += [6, 9]         # [..., 4, 7, 6, 9]; concatena as duas listas em uma nova lista
lista[1:5]              # [0, 1, 2, 3]; retorna elementos do intervalo de índices [inclusivo:exclusivo]
lista[5:]               # [4, 7, 6, 9]; retorna elementos do índice [i:] até o final
lista[:3]               # [8, 0, 1]; retorna elementos do início até o índice [:i] (exclusivo)
lista.reverse()         # [9, 6, ..., 0, 8]; inverte os itens da lista
lista.sort()            # [0, 1, ..., 8, 9]; ordena a lista em ordem crescente; reverse=True para decrescente
lista += [['a', 'b']]   # [..., 8, 9, ['a', 'b']]; concatena uma lista com outra lista
lista[-1][0]            # 'a'; acessa o índice [0] do último elemento [-1]
copia = lista.copy()    # cria uma 'cópia rasa' da lista (faz referência aos objetos) em uma nova lista
copia = lista[:]        # mesmo efeito de lista.copy()
lista.clear()           # []; remove todos os itens da lista
del lista[:]            # mesmo efeito de lista.clear()
palavra = 'Hello world'
palavra.split()         # ['Hello', 'world']; retorna uma lista com as palavras separadas

# ordenação básica
# sorted() e reversed() não alteram a lista original, (p/ alterar a lista, usar o .sort())
id = [15, 87, 32, 65, 56, 32, 49, 37]
sorted(id)                  # [15, 32, 32, 37, 49, 56, 65, 87]; retorna os itens de forma ordenada
sorted(id, reverse=True)    # [87, 65, 56, 49, 37, 32, 32, 15]
list(reversed(id))          # [37, 49, 32, 56, 65, 32, 87, 15]; retorna os itens ordenados ao contrário da lista original

### list comprehension ###

lista = [1, 2, 3, 4, 5]
i_lista = [i+1 for i in lista]                  # [2, 3, 4, 5, 6]; aplica uma função (i+1) para cada item (i) da lista
j_lista = [j for j in i_lista if j > 3]         # [4, 5, 6]; nova lista apenas com elementos da condição (j>3)

inteiros = [1,3,4,5,7,8]
quadrados = [n*n for n in inteiros]             # [1, 9, 16, 25, 49, 64]; cria uma nova lista contendo o quadrado dos itens de 'inteiros'
pares = [n for n in inteiros if n % 2 == 0]     # [4, 8]; adiciona os números pares a lista, verificando se o resto da divisão de cada um é '0'

frutas = ["maçã", "banana", "laranja", "melancia"]
f_lista = [fruta.upper() for fruta in frutas]   # ['MAÇÃ', 'BANANA', ...]; cria uma nova lista com todos os itens em letras maiusculas



##### TUPLAS #####
# tuplas são similares as listas, porém são imutáveis
# geralmente as funções que retornam mais de um valor usam tuplas
# podem receber objetos de tipos diferentes, e a posição [indice] é importante

tuple()                 # recebe um iterável e converte itens em uma tupla; cria uma tupla vazia
tuple('321')            # ('3', '2', '1')
tupla = (0, 1, 2, 3, 4) # cria uma tupla e atribui a uma variável

# funções de tuplas
len(tupla)              # 5; retorna o comprimento/quantidade de itens da tupla
max(tupla)              # 4; retorna o maior valor da tupla
min(tupla)              # 0; retorna o menor valor da tupla
tupla[3]                # 3; retorna o valor da tupla no íncide [i]
tupla.count(2)          # 1; retorna o número de ocorrências de um valor dentro da tupla

# listas e tuplas podem ser usadas em conjunto; existem listas de tuplas, e tuplas de listas
t1, t2 = ('str1', 1), ('str2', 2)
lista = [t1, t2]               # [('str1', 1), ('str2', 2)]; lista com tuplas 
lista[0]                       # ('str1', 1)
lista[0][1]                    # 1

### desempacotamento de tupla ###

tupla = (1, 2, 3)
var1, var2, var3 = tupla    # 1, 2, 3; variáveis recebendo itens da tupla, sequencialmente
_, var2, var3 = tupla       # 2, 3; atribui variáveis ignorando alguns valores usando o underscore '_'
var1, *_ = tupla            # 1; atribui o valor e ignora todos os restantes usando '*_'

for i, valor in enumerate(tupla):
    print(i, 'x', valor)    # 0 x 1/ 1 x 2/ 2 x 3; imprime numeração e itens, sem lista nem tupla

lista = [('ab', 18, 28), ('cd', 38, 48), ('ef', 58, 68)]
for user, _, _ in lista:    # desempacotando e ignorando outros valores usando o "_"
    print(user)             # ab/ cd/ ef



##### CONJUNTOS #####
# são similares as listas, mas não permitem elementos duplicados, repetidos
# não possui índice, portanto não é uma sequência nem é ordenado, exibe elementos na ordem de inserção
# recomenda-se usar quando a posição dos elementos não é importante

set()                       # recebe um iterável e converte itens em um set; cria um set vazio
set = {'cpf1', 'cpf2'}

# funções de sets
set.add('cpf3')             # {'cpf1', 'cpf2', 'cpf3'}; adiciona um item ao set (apenas se não existir)
len(set)                    # 3; retorna o comprimento/quantidade de itens do set
max(set)                    # 'cpf3'; retorna o maior valor do set
min(set)                    # 'cpf1'; retorna o menor valor do set
novo_set = frozenset(set)   # retorna um novo set, porém imutável

""" operações com sets
    união           =>  set1 | set2
    intersecção     =>  set1 & set2
    exclusão        =>  set1 - set2
    ou exclusivo    =>  set1 ^ set2 (um ou outro, mas não nos dois) """

lista = [1, 2, 3, 3, 4, 5, 2, 4, 3] # lista com elementos duplicados
nova_lista = list(set(lista))       # [1, 2, 3, 4, 5]; nova lista sem elementos duplicados

lista = [[1, 2, 3], [3, 4, 5], [2, 4, 3]]   # lista de listas com elementos duplicados
nova_lista = list(set([i for item in lista for i in item])) # [1, 2, 3, 4, 5]



##### DICIONÁRIOS #####
# estrutura para armazenar pares de valores, no formato '{key : value}'

dicionario = {'chave1' : 10, 'chave2' : 20}
dict_alt = dict(cão = 1, gato = 2)      # {'cão': 1, 'gato': 2}; outra forma de inicializar um dicionário, menos usual

# funções de dicts
'chave1' in dicionario                  # True ou False
dicionario['chave1']                    # 10; retorna o valor armazenado na chave
dicionario.get('chave1', 'not found')   # 10; retorna o valor armazenado na chave, ou o segundo parametro se a chave não existir
dicionario['chave3'] = 30               # cria uma chave e adiciona o valor
len(dicionario)                         # 3; retorna o comprimento/quantidade de itens do dicionário
del dicionario['chave3']                # remove chave e o valor
dicionario.pop('chave3', 'not found')   # remove a chave, ou retorna o segundo parametro se a chave não existir
dicionario.update({'chave4' : 40})      # atualiza valor do dicionário, ou cria chave e valor se não existirem
dicionario.update(dict_alt)             # {'chave1': 10, 'chave2': 20, 'chave4': 40, 'cão': 1, 'gato': 2}; une os dois dicionários
dict_copy = dicionario.copy()           # copia o conteúdo do dicionário pra um novo dicionário, independente da origem
dict_copy.clear()                       # apaga todo conteúdo do dicionário
dicionario.keys()                       # ['chave1', 'chave2', 'chave4', 'cão', 'gato']; retorna uma lista com todas as chaves do dicionário
dict_alt.items()                        # retorna uma lista com o conteúdo do dicionário em tuplas => [('cão', 1), ('gato', 2)]
sum(dict_alt.values())                  # 3; retorna a soma dos valores do dicionário
list(dict_alt.values())                 # [1, 2]; retorna uma lista com os valores do dicionário

# list comprehension e iteração em dicionários

[i for i in dict_alt]                       # ['cão', 'gato']
[i for i in dict_alt.keys()]                # ['cão', 'gato']
[f'palavra {i}' for i in dict_alt.keys()]   # ['palavra cão', 'palavra gato']
[dict_alt[i] for i in dict_alt.keys()]      # [1, 2]
[i for i in dict_alt.values()]              # [1, 2]
[i for i in dict_alt.items()]               # [('cão', 1), ('gato', 2)]
for i, j in dict_alt.items():
    print(i, '=', j)                        # cão = 1 / gato = 2; desempacotamento de tuplas

contatos = {'Ana': '8765-4321', 'Luiza': '4567-7654'}
contatos_novo = {nome: '9' + contatos[nome] for nome in contatos}   # {'Ana': '98765-4321', 'Luiza': '94567-7654'}



##### ARRAYS #####
# o módulo array tenta armazenar os valores de uma maneira eficiente, para otimizar os processamentos em cima desses valores
# este módulo array é nativo do python, mas deve ser importado (recomenda-se evitar usar)
import array as arr
arr.array('d', [1, 3.5])    # instanciando um array, recebe(tipo de array, lista com elementos)

""" tipos de arrays
b   signed char         int
B   unsigned char       int
u   wchar_t             Unicode character
h   signed short        int
H   unsigned short      int
i   signed int          int
I   unsigned int        int
l   signed long         int
L   unsigned long       int
q   signed long long    int
Q   unsigned long long  int
f   float               float
d   double              float
- é mais comum usar apenas listas, e para conjuntos pequenos de tipos diferentes com posições específicas, as tuplas
- quando é importante o alto desempenho em funções matemáticas, é comum usar a biblioteca numpy """


### exemplo de problema da mutabilidade de objetos de coleção ###

def problema(lista = []):   # a criação da nova lista é feita apenas na primeira vez que o a função for executada, e o resultado é guardado na memória
    lista.append(1)         # por outro lado, o código da função será executado todas as vezes que a função for executada
                            # neste caso, a lista será vazia na primeira execução, e a cada execução, o '1' será adicionado
  
def solucao(lista = None):  # a verificação será feita uma única vez, mas sempre será 'None'
    if lista == None:       # sempre será 'True'
        lista = list()      # a cada execução, criará uma nova lista vazia
