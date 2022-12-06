import PySimpleGUI as sg
from cotacao import pegar_cotacoes

sg.theme('DarkAmber')

layout = [
    [sg.Text('Pegar Cotação da Moeda')],
    [sg.InputText(key='nome_cotacao')], # USD, EUR, BTC
    [sg.Button('Pegar Cotação'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')]
]

janela = sg.Window('Cotação', layout)

while True:
    evento, valores = janela.read()
    
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    
    if evento == 'Pegar Cotação':
        codigo_cotacao = valores['nome_cotacao']
        cotacao = pegar_cotacoes(codigo_cotacao)

        if cotacao == None:
            janela['texto_cotacao'].update(f'Código de Moeda Inválido')
        else:
            janela['texto_cotacao'].update(f'A cotação do {codigo_cotacao} é de R${cotacao}')

janela.close()
