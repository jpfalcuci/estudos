class Data:
    def __init__(self, dia, mes, ano):
        self.dia, self.mes, self.ano = dia, mes, ano
    def formatada(self):
        print(f'{self.dia:02}/{self.mes:02}/{self.ano}')

d = Data(18,9,1992)
d.formatada()   # retorna '18/09/1992'