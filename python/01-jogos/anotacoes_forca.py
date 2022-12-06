import random as rd


# iterando strings
arquivo = open('frutas.txt', 'w', encoding='utf-8')   # cria um arquivo de texto
arquivo.write(      # adiciona itens ao arquivo, pulando linha
    'banana\n'\
    'maça\n' \
    'melancia\n' \
    'manga\n'
)
arquivo.close()     # fecha o arquivo 

palavras = []
arquivo = open('frutas.txt', 'r')                       # abre o arquivo em modo de leitura
for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)
arquivo.close()

numero = rd.randrange(0, len(palavras))                 # cria um número aleatório entre 0 e (qtd de itens da lista)
palavra = palavras[numero].upper()                      # atribui uma palavra da lista a variável, usando o número aleatório gerado como índice 



palavra, chute, posicao = 'python', 'p', 0
palavra_oculta = []
for letra in palavra:
    palavra_oculta.append('_')                          # atribui '_' para cada letra em 'palavra'
# outra forma de fazer usando list comprehension:                          
palavra_oculta = ['_' for letra in palavra]             # usando o 'for' dentro da atribuição da lista

palavra_completa = '_' not in palavra_oculta            # retorna True quando não houver mais '_' em 'palavra_oculta'
for letra in palavra: 
    if chute.upper() == letra.upper():                  # comparando sem diferenças de maíusculo e minúsculo
        print(f'letra {letra} na posição {posicao}')    # resultado: 'letra p na posição 0'
        palavra_oculta[posicao] = letra                 # sobrescreve letra informada dentro da lista, na 'posição' indicada
    posicao =+ 1                                        # somando 1 em 'posicao' para iniciar o laço novamente
    if (palavra_completa):
        break                                           # se True, sai do laço
print(palavra_oculta)                                   # 'P', '_', '_', '_', '_', '_'
letras_restantes = str(palavra_oculta.count('_'))       # '5'
print(f'ainda faltam {letras_restantes} letras')        # 'ainda faltam 5 letras'
