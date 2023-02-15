import PySimpleGUI as sg
 


def telaCadastro():
    print('tela cadastro')

def telaLogin():
    print('tela Login')








sg.theme('Lightblue')
tela = [    #oq vai ser mostrado na tela
    [sg.Text('BEM VINDO(A)')],
    [sg.Text('1-Cadastrar\n2-Login\n')],
    [sg.Input(key='entrada')], #entrada da informação
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('1'), sg.Button('2'), sg.Button('teste')]                           
]


window = sg.Window('Sistema Teste de Login', tela)


while True:
    event, values = window.read()
    if event == "1":
        entrada = values['entrada']  #variavel recebe os valores do input
        print(entrada)
        telaCadastro()
    elif event == "2":
        telaLogin()


    if event == sg.WINDOW_CLOSED: #se eu apertar o X da guia ele quebra o laço e fecha a janela
        break
    
    
window.close()































'''telaCadastro = [    #oq vai ser mostrado na tela
    [sg.Text('BEM VINDO(A)')],
    [sg.Text('1-Cadastrar\n2-Login\n')],
    [sg.Input(key='entrada')], #entrada da informação
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Confirmar'), sg.Button('Sair')]                           
]




telaLogin = [    #oq vai ser mostrado na tela
    [sg.Text('BEM VINDO(A)')],
    [sg.Text('1-Cadastrar\n2-Login\n')],
    [sg.Input(key='entrada')], #entrada da informação
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Confirmar'), sg.Button('Sair')]                           
]'''