# parâmetros em páginas da internet

'https://www.dominio.com/search?parametros_da_url'  # parâmetros são como variáveis passados para o programa
'q=query_busca''&(E_comercial serve para separar parâmetros)''src=source_origem'

url = 'www.alura.com/search?query1=python&query2=sql&query3=php'
# sanitização de dados
if type(url) == str:
    url = url.strip()
# validação de dados
if url == '':
    raise ValueError('URL não pode ser vazia')  # 'raise' para retornar um erro ao usuário
    # 'ValueError' é uma classe do python que indica que aconteceu um 'erro de valor'

inter = url.find('?')           # retorna a posição de índice de '?'
url_base = url[0:inter]         # retorna 'www.alura.com/search'
url_param = url[inter+1:]       # retorna 'query1=python&query2=sql&query3=php'
parametro = 'query1'
indice1 = url_param.find(parametro)
i_valor = indice1 + len(parametro) + 1
eh_comercial = url_param.find('&', i_valor) # busca pelo '&', iniciando a busca a partir do índice 'i_valor'

if eh_comercial == -1:                      # se for '-1' significa que o '&' não foi encontrado
    valor = url_param[i_valor:]             # se True, fatia string até o final
else:
    valor = url_param[i_valor:eh_comercial] # se False, fatia string até o '&'

'se o "parametro" for "query1", retorna "python"; "query2":"sql", "query3":"php"'