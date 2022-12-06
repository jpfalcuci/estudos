import PySimpleGUI as sg

# Criando o layout
def criar_janela_inicial():
    sg.theme('DarkBlue4')

    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True) # Finalize é necessário quando se cria janelas através de funções

# Criar a janela
janela = criar_janela_inicial()

# Criar as regras da janela
while True:
    event, values = janela.read() # Lê eventos e valores vindos da janela
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        # Adiciona novos elementos dentro de outro elemento
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
