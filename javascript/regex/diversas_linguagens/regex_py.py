import re

alvo = '11a22b33c'
regexp = r'(\d\d)\w'
resultado = re.search(regexp,alvo)

resultado.group()   # '11a'
resultado.group(1)  # '11'
resultado.start()   # 0
resultado.end()     # 3


resultados = re.finditer(regexp,alvo)
for resultado in resultados:
    print ("%s com grupo %s [%s,%s]" % (resultado.group(), resultado.group(1),resultado.start(), resultado.end()))
# 11a com grupo 11 [0,3]
# 22b com grupo 22 [3,6]
# 33c com grupo 33 [6,9]


# p/ melhorar o desempenho, o python possui uma forma de compilar a regex antes de usá-la:
regex = re.compile(regexp)
resultados = regex.finditer(alvo)
# mesmo resultado
