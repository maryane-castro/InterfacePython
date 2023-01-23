import PySimpleGUI as sg

sg.theme('Lightblue')

tela = [    [sg.Text('BEM VINDO(A)')],
            [sg.Text('Digite seu LOGIN: ')],
            [sg.Input('')],
            [sg.Button('Criar'), sg.Button('Logar')]
]


window = sg.Window('Sistema Teste de Login', tela)

event, values = window.read()

if event == 'Criar':
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")