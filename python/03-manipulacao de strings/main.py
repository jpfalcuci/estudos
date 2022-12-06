# ExtratorURL no arquivo extrator_url.py
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# sanitização da URL
url = url.strip() # tira espaços em branco da URL

# validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca) # busca a posicao de indice do parametro
indice_valor = indice_parametro + len(parametro_busca) + 1 # define a quantidade de indices que o parametro ocupa + 1 para ser exclusivo
indice_e_comercial = url_parametros.find('&', indice_valor) # busca por um '&' começando a partir do indice_valor
if indice_e_comercial == -1: # se não encontrar um '&' na frente do parametro
    valor=url_parametros[indice_valor:] # imprime do parametro pra frente
else:
    valor=url_parametros[indice_valor:indice_e_comercial] # imprime do parametro até o &

print(valor)
