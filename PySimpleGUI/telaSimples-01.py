import PySimpleGUI as sg

layout = [
    [sg.Text('Qual seu nome?')],
    [sg.Input()],
    [sg.Button('Ok'), sg.Button('Sair')]
]

window = sg.Window('Janela de teste', layout)

event, values = window.read()

while True:
    if event == 'Ok':
        print('Olá', values[0], '!')
        break
    if event == 'Sair' or event == sg.WINDOW_CLOSED:
        break
