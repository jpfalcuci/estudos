# módulo validate_docbr
# pacote python para validação de documentos brasileiros
# instalar com 'pip install validate-docbr'

from validate_docbr import CPF, CNPJ
# método 'validate' recebe str para validar CPF e CNPJ
cpf = CPF()
cpf.validate('15316264754')     # True
cnpj = CNPJ()
cnpj.validate('35379838000112') # True

# validar diferentes documentos
import validate_docbr as docbr
docs = [(docbr.CPF, '90396100457'), (docbr.CNPJ, '49910753848365')]
docbr.validate_docs(docs)  # [True, False]

# máscara para documentos
from validate_docbr import CPF
CPF().mask('15316264754')   # retorna '153.162.647-54'
