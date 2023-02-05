import PySimpleGUI as sg











sg.theme('Lightblue')
tela = [    #oq vai ser mostrado na tela
    [sg.Text('BEM VINDO(A)')],
    [sg.Text('1-Cadastrar\n2-Login\n')],
    [sg.Input(key='entrada')], #entrada da informação
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Confirmar'), sg.Button('Sair')]                           
]


window = sg.Window('Sistema Teste de Login', tela)
while True:
    event, values = window.read()
    if event == "1":
        pass #cadastrar
    elif event == "1":
        pass #login


    if event == sg.WINDOW_CLOSED: #se eu apertar o X da guia ele quebra o laço e fecha a janela
        break
    
    
window.close()