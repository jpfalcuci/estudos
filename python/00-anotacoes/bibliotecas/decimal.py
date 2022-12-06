# módulo decimal

# na computação em geral, números de pontos flutuantes podem apresentar algums problemas
# os computadores não conseguem representar com precisão exata algumas frações
conta1 = 99.91 * 5      # retorna '499.54999999999995'
conta2 = 110.1 * 3      # retorna '330.29999999999995'
conta3 = 1.1 + 2.2      # retorna '3.3000000000000003'
# no geral é um erro pequeno para ser relevante, que pode ser resolvido com o round()

from decimal import Decimal     # importa o tipo 'Decimal' do módulo 'decimal', no início do arquivo
# usado quando precisa de precisão com números decimais
Decimal('99.91') * 5                # retorna '499.55'
Decimal('110.1') * 3                # retorna '330.3'
Decimal('1.1') + Decimal('2.2')     # retorna '3.3'
