from datetime import datetime


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def mes_cadastro(self):
        meses_do_ano = ["janeiro", "fevereiro", "março", "abril",
                        "maio", "junho", "julho", "agosto",
                        "setembro", "outubro", "novembro", "dezembro"]
        mes_cadastro = self.momento_cadastro.month -1 # para correção, month possui range de 1 a 12 
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = ["segunda", "terça", "quarta",
                            "quinta", "sexta", "sábado", "domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
