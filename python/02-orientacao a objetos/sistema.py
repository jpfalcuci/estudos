class Sistema:
    def __init__(self):
        self.texto = ''         # inicializa o atributo 'texto'
    def le_entrada(self):
        self.texto = input()    # capta entrada e armazena em 'texto'
    def exibe_saida(self):
        print(self.texto)       # imprime texto armazenado