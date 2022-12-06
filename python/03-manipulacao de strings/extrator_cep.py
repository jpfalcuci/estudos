endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # regular expressions -- RegEx

# criando padrão para cep
# 5 dígitos de 0 a 9 + hífen opcional + 3 dígitos de 0 a
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) # match
if busca:
    cep = busca.group() # retorna string encontrada dentro do padrão
    print(cep)