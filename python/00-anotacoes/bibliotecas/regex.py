# expressões regulares
# servem para encontrar padrões bem definidos dentro de uma cadeia de caracteres em um texto ou str maiores

""" biblioteca re
    []  define um range ou um grupo de caracteres
    *   marca nenhuma, uma ou mais ocorrências
    {}  qtd de repetições de uma ocorrência definida
    \d  qualquer número de 0 até 9
    \w  qualquer número de 0 até 9, letra de a até z ou o _
    |   um ou outro
    ()  captura e agrupa """

# método compile recebe uma string e retorna o objeto 'pattern', ou 'padrão'
# cada caractere é representado por [abcd] [0123] (pode conter qualquer um dos valores informados)
# para definir intervalo de valores: [0-9] [a-z] (pode conter qualquer valor de x a y)
# '?' após [] para representar caractere opcional, pode aparecer uma ou nenhuma vez
# quantificador {} após o [] para a representar a qtd de vezes que aquele conjunto deve aparecer
# {} também pode receber intervalo para definir limite, usando vírgula: {0,2} (pode aparecer de 0 a 2 vezes)

import re # 'regular expression' ou 'regex'
endereco = 'Rua Fulano de Tal, 1020, apartamento 37, BairroX, São Paulo, SP, 54321-666'
padrao_cep = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca_cep = padrao_cep.search(endereco) # o objeto 'pattern' tem o método 'search', que recebe uma string
                                        # busca padrão dentro da string
                                        # retorna o objeto 'match' se encontrar a combinação, ou 'None'
busca_cep.group()                       # retorna a string encontrada naquele padrão, '54321-666'

url = 'https://www.site.com.br/pagina'
# para definir uma sequência exata de caracteres, usa-se ()
padrao_url = re.compile('(http(s)?://)?(www.)?site.com(.br)?/pagina')   # o 's' de 'https://' é opcional
match = padrao_url.match(url)       # assim como 'search', 'match' é um método de 'pattern'
                                    # verifica se a string inteira bate com o padrão
                                    # retorna o objeto 'match' se encontrar, ou 'None'
if not match:
    raise ValueError('A URL não é válida')

# padrão para celulares brasileiros
padrao = "(55)?([0-9]{2})([0-9]{4,5})([0-9]{4})"
r = re.search(padrao, '5516912345678')
numero = f"+{r.group(1)}({r.group(2)}){r.group(3)}-{r.group(4)}"
numero  # '+55(16)91234-5678'
