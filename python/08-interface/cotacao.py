import requests

def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL')
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print('Código de Moeda Inválido')
        return None
