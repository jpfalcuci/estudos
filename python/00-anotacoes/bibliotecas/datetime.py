# módulo datetime
# biblioteca padrão para se trabalhar com datas

import datetime
hoje = datetime.datetime.now() 
print(str(hoje))    # 2022-06-19 11:30:46.893874
print(repr(hoje))   # datetime.datetime(2022, 6, 19, 11, 30, 46, 893874)

# método 'strftime' para formatar datetime em string, recebe uma string com o padrão a ser usado
data_e_hora_em_texto = hoje.strftime('%d/%m/%Y %H:%M')  # '19/06/2022 11:30'
type(data_e_hora_em_texto)  # 'str'

""" strftime
%A  dias da semana por extenso
%d  dias do mês
%m  meses em formato numérico
%y  ano em formato de 2 dígitos
%Y  ano em formato de 4 dígitos
%H  hora em formato decimal
%M  minuto em formato decimal
%S  segundo de forma decimal """

# método 'strptime' para formatar string em datetime, recebe string e o padrão dela
from datetime import datetime
data_em_str = '01/03/2018 12:30'
type(data_em_str)   # 'str'
str_em_datetime = datetime.strptime(data_em_str, '%d/%m/%Y %H:%M')
str_em_datetime         # 'datetime.datetime(2018, 3, 1, 12, 30)'
print(str_em_datetime)  # '2018-03-01 12:30:00'

# fuso horário com timezone
# classe timedelta tem a finalidade de representar uma duração, e permite realizar operações matemáticas com datas
from datetime import datetime, timezone, timedelta
data_e_hora_atuais = datetime.now() # '2022-06-19 12:00:23.394973'
diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)
print(fuso_horario) # 'UTC-03:00'
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario) # converte o tempo da máquina para o fuso_horario informado
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m %Y %H:%M')
print(data_e_hora_sao_paulo_em_texto)   # '19/06 2022 12:00'

# fuso horário com o módulo pytz
# instalar com 'pip install pytz'
from datetime import datetime
from pytz import timezone
data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_sao_paulo_em_texto)   # '19/06/2022 12:00'
# é possível ver a lista de fusos horários suportados pelo pytz iterando sobre o pytz.all_timezones
import pytz
for tz in pytz.all_timezones:
    print(tz)
