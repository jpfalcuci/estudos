# contar palavras em um texto

texto = 'Este é um exemplo de texto'
texto = texto.lower()
aparicoes = {}
for palavra in texto.split():   # quebrando palavras do texto em itens separados
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
aparicoes   # {'este': 1, 'é': 1, 'um': 1, 'exemplo': 1, 'de': 1, 'texto': 1}

# versão usando defaultdict
# usado quando precisa trabalhar com valores padrão em dicionários
from collections import defaultdict
aparicoes = defaultdict(int)        # função que será chamada sempre que não tiver valor, e é necessário valor /tipo 'int' devolve 0
for palavra in texto.split():       # quebrando palavras do texto em itens separados
    aparicoes[palavra] += 1
aparicoes   # defaultdict(int, {'este': 1, 'é': 1, 'um': 1, 'exemplo': 1, 'de': 1, 'texto': 1})
# 'defauldict' também é comumente usado para atribuir valor padrão para atribuição de objetos, caso não sejam passados os valores de Classe

from collections import Counter
# método Counter, contador que por padrão já tem valor '0'
aparicoes = Counter(texto.split())
aparicoes   # Counter({'este': 1, 'é': 1, 'um': 1, 'exemplo': 1, 'de': 1, 'texto': 1})

# exemplo de uso: contar letras em um texto
txt1 = 'Este é um exemplo que representa um texto longo'
Counter(txt1.lower())       # retorna a qtd de aparições de cada caractere
# Counter({'e': 9, 's': 2, 't': 4, ' ': 8, 'é': 1, 'u': 3, 'm': 3, 'x': 2, 'p': 2, 'l': 2, 'o': 4, 'q': 1, 'r': 2, 'n': 2, 'a': 1, 'g': 1})
sum(aparicoes.values())     # retorna a soma dos valores, '47'
txt2 = 'Este também é um exemplo de texto longo, diferente do texto anterior'

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]    # criando uma lista 
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)    # seleciona os 10 mais comuns
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao * 100:05.2f}%')
analisa_frequencia_de_letras(txt1)  # e => 19.15% /  => 17.02% /t => 08.51% /o => 08.51% /u => 06.38% /m => 06.38% /s => 04.26% /x => 04.26% /p => 04.26% /l => 04.26%
analisa_frequencia_de_letras(txt2)  # e => 16.18% /  => 16.18% /t => 11.76% /o => 10.29% /m => 05.88% /x => 04.41% /d => 04.41% /n => 04.41% /r => 04.41% /a => 02.94%
