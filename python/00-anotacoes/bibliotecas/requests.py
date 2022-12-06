# módulo requests
# permite o envio de solicitações http em python
# instalar com 'pip install requests'

import requests
cep = '01001000'
url = f"https://viacep.com.br/ws/{cep}/json/"
r = requests.get(url)
dados = r.json()
print(dados['bairro'], dados['localidade'], dados['uf'])

""" utilizando APIs:
API acessa o banco de dados e retorna uma resposta
get()       para pegar informação
post()      para criar
put()       para atualizar algo que já existe
delete()    para deletar """
