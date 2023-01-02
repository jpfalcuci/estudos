# $ sudo apt-get install ruby-full
# $ irb

regex = /(\d\d)(\w)/
alvo = "12a34b56c"

resultado = regex.match(alvo)   # => #<MatchData "12a" 1:"12" 2:"a">

resultado[0]    # => 12a
resultado[1]    # => 12

resultado.begin 0   # => 0 (inicio do match inteiro)
resultado.begin 1   # => 0 (inicio do grupo)
resultado.end 0     # => 3 (fim do match inteiro)
resultado.end 1     # => 2 (fim do grupo)

resultados = alvo.scan regex    # => [["12", "a"], ["34", "b"], ["56", "c"]]
resultados[2]       # => ["56", "c"]
resultados[2][1]    # => "c"
