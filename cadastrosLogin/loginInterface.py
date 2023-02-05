import PySimpleGUI as sg

sg.theme('Lightblue')

tela = [    #oq vai ser mostrado na tela

    [sg.Text('BEM VINDO(A)')],
    [sg.Text('Digite seu LOGIN: ')],
    [sg.Input(key='entrada')], #entrada da informação
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Criar'), sg.Button('Logar')]
                                   
]


window = sg.Window('Sistema Teste de Login', tela)


while True:
    event, values = window.read()
    if event == "Criar":
        window['saida'].update('Hello ' + values['entrada'])
        
    if event == sg.WINDOW_CLOSED: #se eu apertar o X da guia ele quebra o laço e fecha a janela
        break
    
    
window.close()