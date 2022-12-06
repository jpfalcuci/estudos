# módulo locale
# módulo dedicado a serviços de internacionalização
# permite lidar facilmente com problemas culturais em uma aplicação

import locale       # importa o módulo 'locale' no início do arquivo
locale.setlocale()  # recebe 'category' e 'locale'
""" categorias:
    locale.LC_CTYPE       - Funções relacionadas a caracteres
    locale.LC_COLLATE     - Ordenação de strings
    locale.LC_TIME        - Formatação de tempo
    locale.LC_MONETARY    - Formatação de valores monetários
    locale.LC_MESSAGES    - Exibição de mensagens
    locale.LC_NUMERIC     - Formatação de números
    locale.LC_ALL         - Combinação de todas as categorias """
    # as strings aceitas dependem do sistema em que o código está rodando
    # em sistemas unix, pode consultar a lista através de 'locale -a' no terminal
    # 'pt_BR.utf8', 'en_US.utf8'
    # a consulta de locale no windows é mais complicada

locale.setlocale(locale.LC_MONETARY, 'en_US.utf8')
locale.currency(12.4593681)                 # retorna '$12.46'
locale.currency(15000)                      # retorna '$15000.00'
locale.currency(15000)                      # retorna '$15000.00'
# 'symbol' para usar ou não o símbolo da moeda
locale.currency(15000, symbol=False)        # retorna '15000.00'
# 'grouping' para agrupar os milhares
locale.currency(15000, grouping=True)       # retorna '$15,000.00'
# 'international' para símbolo internacional da moeda
locale.currency(15000, international=True)  # retorna 'USD15000.00'

locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')
locale.currency(12.4593681)                 # retorna 'R$ 12,46'
locale.currency(15000)                      # retorna 'R$ 15000,00'
locale.currency(15000, symbol=False)        # retorna '15000,00'
locale.currency(15000, grouping=True)       # retorna 'R$ 15.000,00'
locale.currency(15000, international=True)  # retorna 'BRL 15000,00'
