# pip install PySimpleGUI

from logging import PlaceHolder
from PySimpleGUI import PySimpleGUI as sg

### VERSÃO 01 ###

# Layout
# sg.theme('Reddit')
# layout = [
#     [sg.Text('Usuário', size=(15,1)), sg.Input(key='usuario', size=(20,1))],
#     [sg.Text('Senha', size=(15,1)), sg.Input(key='senha', password_char='*', size=(20,1))],
#     [sg.Checkbox('Salvar o login?')],
#     [sg.Button('Entrar')]
# ]

# # Janela
# janela = sg.Window('Tela de Login', layout)

# # Ler os eventos
# while True:
#     eventos, valores = janela.read()
#     if eventos == sg.WIN_CLOSED:
#         break
#     if eventos == 'Entrar':
#         if valores['usuario'] == 'joao' and valores['senha'] == '1234':
#             print('Acessou')
#         else:
#             print('Errou')

### VERSÃO 02 ###

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='user', size=(25,1))],
    [sg.Text('Senha')],
    [sg.Input(key='password', password_char='*', size=(25,1))],
    [sg.Button('LogIn')],
    [sg.Text('', key='message')],
]

window = sg.Window('LogIn', layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'LogIn':
        senha_correta = '1234'
        usuario_correto = 'joao'
        usuario = values['user']
        senha = values['password']
        if senha == senha_correta and usuario == usuario_correto:
            window['message'].update('LogIn feito com sucesso')
        else:
            window['message'].update('Usuário ou senha inválidos')
