##### ESTRUTURAS DE LAÇO #####


# executa o código 'enquanto' condição for verdadeira
i, n, s = 1, 10, 0
while (i <= n):
    s += i  # códigos do loop (pode receber 'if')
    i += 1  # incrementa contador
else:
    print(f'A soma é {s}')  # A soma é 55


# executa o código 'para cada' item de um iterável
list = []
for i in range(1, 6):
    list.append(i)  # códigos do loop (pode receber 'if')
print(list)         # [1, 2, 3, 4, 5]


genre = ['blues', 'rock']
for i in range(len(genre)):
    print(f'I like {genre[i]}')
else:
    print('No items left')
# I like blues / I like rock / No items left


for number in range(5):
    if number == 2:
        break    # interrompe o loop
    print(f'Número {str(number)}')
print('Fora do loop')   # Número 0 / Número 1 / Fora do loop

for number in range(5):
    if number == 2:
        continue    # recomeça o loop; ignora códigos abaixo
    print(f'Número {str(number)}')
print('Fora do loop')   # Número 0 / Número 1 / Número 3 / Número 4 / Fora do loop


# loop dentro de loop
lista = [[1, 2, 3], [3, 4, 5], [2, 4, 3]]
nova_lista = []
for item in lista:
    for i in item:
        nova_lista.append(i)
nova_lista  # [1, 2, 3, 3, 4, 5, 2, 4, 3]

# usando list comprehensions
nova_lista = list(set([i for item in lista for i in item]))
nova_lista # [1, 2, 3, 4, 5] => set para remover itens duplicados



# função enumerate (numera os itens de um iterável e retorna objeto 'enumarate')
inteiros = [1,3,4,5,7,8]
lista_num = list(enumerate(inteiros))           # [(0, 1), (1, 3), (2, 4), (3, 5), (4, 7), (5, 8)]


# função map (aplica função para cada item de um iterável e retorna objeto 'map')
valor_dobrado = list(map(lambda x : x*2, inteiros))     # [2, 6, 8, 10, 14, 16]
valor_float = list(map(float, valor_dobrado))           # [2.0, 6.0, 8.0, 10.0, 14.0, 16.0]


# função reduce (aplica função para cada par de itens de um iterável, usando o resultado para o par seguinte)
from functools import reduce
valor_somado = reduce(lambda x, y: x + y , inteiros)    # 28


# função filter (retorna um objeto 'filter' apenas com os objetos de um iterável que atendem a condição)
frutas = ["maçã", "banana", "laranja", "melancia"]
frutas_m = list(filter(lambda i: i[0] == "m", frutas))  # ['maçã', 'melancia']


# função zip (une itens de listas com os mesmos índices, em tuplas)
l1, l2, l3 = [1, 2, 3], ['a', 'b', 'c'], ['$1', '$2', '$3']
list(zip(l1, l2, l3))   # [(1, 'a', '$1'), (2, 'b', '$2'), (3, 'c', '$3')]
for i, j, k in zip(l1, l2, l3):
    print(i, j, k)      # 1 a $1 \ 2 b $2 \ 3 c $3 (desempacotamento de tuplas)

a, b = ['a', 'b', 'c'], [10, 20, 30]
dict(zip(a, b))     # {'a': 10, 'b': 20, 'c': 30}


# ignorando valores em uma iteração
lista = [('ab', 18, 28), ('cd', 38, 48), ('ef', 58, 68)]
for user, _, _ in lista:    # desempacotando tuplas e ignorando outros valores usando o "_"
    print(user)             # ab/ cd/ ef
    # o uso do "_" deve ser avaliado em cada caso
    # pode ser útil para a legibilidade do código, deixar explícito quais outros valores estão na lista, mas não estão sendo utilizados
