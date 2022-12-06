import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip() #tira espaços em branco da URL
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca) # busca a posicao de indice do parametro
        indice_valor = indice_parametro + len(parametro_busca) + 1 # define a quantidade de indices que o parametro ocupa + 1 para ser exclusivo
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor) # busca por um '&' começando a partir do indice_valor
        if indice_e_comercial == -1: # se não encontrar um '&' na frente do parametro
            valor = self.get_url_parametros()[indice_valor:] # imprime do parametro pra frente
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial] # imprime do parametro até o &
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url


url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)

# Verifica que duas instâncias com a mesma URL são iguais
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url2)

print("O tamanho da URL:", len(extrator_url))
print("URL completa: ", extrator_url)

# Busca o valor do parâmetro quantidade
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)


### DESAFIO ###
# Conversão de dólar para real
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
