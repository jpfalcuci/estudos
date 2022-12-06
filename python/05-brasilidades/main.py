### documentos ###
from cpf_cnpj import Documento
cpf = Documento.cria_documento('15316264754')
cnpj = Documento.cria_documento('35379838000112')
print(f'CPF = {cpf}, CNPJ = {cnpj}')
# CPF = 153.162.647-54, CNPJ = 35.379.838/0001-12


### telefones ###
from TelefonesBr import TelefonesBr
telefone = TelefonesBr('5516912345678')
print(telefone) # '+55(16)91234-5678'


### datas ###
from datas_br import DatasBr
cadastro = DatasBr()
print(cadastro)                     # '19/06/2022 15:20'
print(cadastro.tempo_cadastro())    # '0:01:44.536879'


### cep ###
from acesso_cep import BuscarEndereco
cep = BuscarEndereco("01001000")
bairro, cidade, uf = cep.acessa_via_cep()
print(cep)                  # '01001-000'
print(bairro, cidade, uf)   # 'Sé São Paulo SP' 
