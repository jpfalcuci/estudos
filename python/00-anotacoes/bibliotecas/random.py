# módulo random
import random # importa o módulo no início do arquivo

random.random() # retorna um número float aleatório entre 0.0 e 1.0, (16 casas após o ponto)  

# pseudo-random
""" a função random() não gera um número verdadeiramente aleatório, e usa como base uma entrada (seed) para gerar o número; por padrão, o seed usado é a hora (milissegundos)"""
random.seed(10) # define o seed usado para gerar o número aleatório
                # um mesmo seed sempre resulta num mesmo número

n = random.random() * 100   # returna um número aleatório entre 0 e 100
int(n)                      # returna um número inteiro, sem arredondar
round(n)                    # returna um número inteiro, arredondado

random.randrange(10)    # returna um número inteiro entre 0 e 9
random.randrange(0, 11) # returna um número inteiro entre 0 e 10

# preenchendo uma lista com números aleatórios
vetor = []
for i in range(10):
    numero_aleatorio = random.randint(0,50) # criando números aleatórios de 0 a 50
    vetor.append(numero_aleatorio)          # adicionando 10 números aleatórios a lista

# escolher número aleatório a partir de uma lista
vetor = [3, 22, 17, 28, 31, 31, 26, 45, 40, 31]
random.choice(vetor)
