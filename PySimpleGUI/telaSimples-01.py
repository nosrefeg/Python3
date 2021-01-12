import PySimpleGUI as sg

layout = [
    [sg.Text('Qual seu nome?')],
    [sg.Input()],
    [sg.Button('Ok')]
]

window = sg.Window('Janela de teste', layout)

event, values = window.read()

print('Olá', values[0], '!')

window.close()
