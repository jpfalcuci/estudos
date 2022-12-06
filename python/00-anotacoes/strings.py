##### STRINGS #####

""" strings são sequências de caractéres
    podem usas aspas 'simples' ou "duplas" (por convenção, mais comum usar aspas simples)
    strings com mais de uma linha usam 3 aspas
    strings são sequências iteráveis e são imutáveis """


# localizar substring dentro da string (retorna posição apenas da primeira correspondência, ou '-1' se não existir)
exemplo = 'Esta é uma string'
exemplo.find('string')      # 11; (índice)


# índice (posição)
exemplo[5]          # 'é'
exemplo[5:10]       # 'é uma'


# transforma em maíusculo apenas a primeira letra da string (sem alterar a variável)
palavra = 'banana'
palavra.capitalize()    # 'Banana'


# transforma em maíusculo a primeira letra de cada palavra da string (sem alterar a variável)
nome = 'nome composto'
nome.title()    # 'Nome Composto'


# verifica se começa com o prefixo / termina com o sufixo
palavra.startswith('ba')    # True
palavra.endswith('na')      # True


# retorna a string sem espaços em branco do início e do fim (sem alterar a variável); também remove '\n'
string_com_espacos = '   string   '
string_com_espacos.strip()      # 'string'
string_com_espacos.lstrip()     # 'string   '
string_com_espacos.rstrip()     # '   string'


# retorna a quantidade de caracteres da string
len(palavra)    # 6


# retorna a maior / menos letra alfabeticamente da string
min(palavra)    # 'a'
max(palavra)    # 'n'


# substitui caractere na string
valor = 12.46
str(valor).replace('.', ',')    # '12,46'


# usando mais de uma função
nome = '  nomE compOSto   '
nome.strip().title()    # 'Nome Composto'


# verifica se todo os caracteres da string são letras do alfabeto (a-z)
palavra.isalpha()   # True
nome.isalpha()      # False


# transforma toda string em maiúscula / minúscula (sem alterar a variável)
nome = 'João Paulo'
nome.lower()    # 'joão paulo'
nome.upper()    # 'JOÃO PAULO'



### interpolação de strigs ###

# função format recebe conteúdos a inserir na string
texto_1, texto_2 = 'formatação', 'strings'
'exemplo de {} de {}'.format(texto_1, texto_2)  # 'exemplo de formatação de strings'

# invertendo parâmetros usando índices
'tentativa {} de {}'.format(2, 5)       # 'tentativa 2 de 5'
'tentativa {1} de {0}'.format(2, 5)     # 'tentativa 5 de 2'

# função f-string
f'exemplo de {texto_1} de {texto_2}'    # 'exemplo de formatação de strings'
f'meu nome é {nome}'                    # 'meu nome é João Paulo'



### formatação de valores ###

# formatação de valores
'R$ {}'.format(1.59)        # 'R$ 1.59'
'R$ {:f}'.format(1.59)      # 'R$ 1.590000'; f para float
'R$ {:.2f}'.format(1.5)     # 'R$ 1.50'
'R$ {:7.2f}'.format(4.5)    # 'R$    4.50'
f'R$ {4.5:07.2f}'           # 'R$ 0004.50'
f'R$ {4.5:08.3f}'           # 'R$ 0004.500'
f'R$ {10.16:5.1f}'          # 'R$  10.2'
f'R$ {4:07d}'               # 'R$ 0000004'; d para inteiro
f'R$ {46:7d}'               # 'R$      46'
f'data {9:2d}/{4:2d}'       # 'data  9/ 4'
f'data {9:02d}/{4:02d}'     # 'data 09/04'
f'data {19:02d}/{11:02d}'   # 'data 19/11'
a, b = 10, 4
f'resultado de {a}/{b} é {(a/b):7.3f}'    # 'resultado de 10/4 é   2.500'


# 'escape character'
a = 'string, código, '\
    'continuação'           # permite continuar em outra linha de código
b = 'string \tcontinuação'  # cria um espaço
c = 'string \ncontinuação'  # pula uma linha
