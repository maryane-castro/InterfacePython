import PySimpleGUI as sg

sg.theme('Lightblue')

tela = [    [sg.Text('BEM VINDO(A)')],
            [sg.Text('Digite seu LOGIN: ')],
            [sg.Input(key='-INPUT-')], #entrada da informação
            [sg.Text(key='-OUTPUT-')], #saida da informação "print na interface"
            [sg.Button('Criar'), sg.Button('Logar')]
]


window = sg.Window('Sistema Teste de Login', tela)
while True:
    event, values = window.read()
    if event == "Criar":
        window['-OUTPUT-'].update('Hello ' + values['-INPUT-'])
    if event == sg.WINDOW_CLOSED: #se eu apertar o X da guia ele quebra o laço e fecha a janela
        break
    
    
window.close()