from PySimpleGUI import PySimpleGUI as sg

# Criar janelas e estilos (layout)
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input('')],
        [sg.Button('Continuar')],
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Peperoni', key='pizza1'), sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)

# Criar janelas iniciais
janela1, janela2 = janela_login(), None

# Criar loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()

    # Quando janela for fechada
    if (window == janela1 or window == janela2) and event == sg.WIN_CLOSED:
        break

    # Quando quer ir para próxima janela
    if window == janela1 and event == 'Continuar':
        janela1.hide()
        janela2 = janela_pedido()

    # Quando quer voltar para janela anterior
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

# Lógica de o que deve acontecer ao clicar os botões
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitadas uma Pizza Pepperoni e uma Pizza Frango c/ Catupiry')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitada uma Pizza Pepperoni')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitada uma Pizza Frango c/ Catupiry')
        else:
            sg.popup('Selecione no mínimo uma opção')
