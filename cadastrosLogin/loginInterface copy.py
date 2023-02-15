import PySimpleGUI as sg




#---------TELA CADASTRO----------
def telaCadastro():
    print('tela cadastro')

    sg.theme('Darkblue')
    telaCadastro = [    #oq vai ser mostrado na tela
    [sg.Text('CADASTRO')],
    [sg.Text('Digite um nome para cadastrar:')],
    [sg.Input(key='cadastro')],
    [sg.Text('Digite uma senha:')],
    [sg.Input(key='senha')],
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Confirmar'), sg.Button('Sair')]                           
    ]

    window = sg.Window('Sistema Teste de Login', telaCadastro)
    while True:
        event, values = window.read()
        if event == "Confirmar":
            print('cadastro show')


        if event == sg.WINDOW_CLOSED or event == 'Sair': #se eu apertar o X da guia ele quebra o laço e fecha a janela
            break    
        
    window.close()








#---------TELA LOGIN----------
def telaLogin():
    print('tela login')

    sg.theme('Darkblue')
    telaLogin = [    #oq vai ser mostrado na tela
    [sg.Text('LOGIN')],
    [sg.Text('Digite seu login e senha\n')],
    [sg.Text('Login')],
    [sg.Input(key='login')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Confirmar'), sg.Button('Sair')]                           
    ]

    window = sg.Window('Sistema Teste de Login', telaLogin)
    while True:
        event, values = window.read()
        if event == "Confirmar":
            print('login show')
            window['saida'].update('Login: ' + values['login'] + '\nSenha: ' + values['senha'])


        if event == sg.WINDOW_CLOSED or event == 'Sair': #se eu apertar o X da guia ele quebra o laço e fecha a janela
            break    
        
    window.close()








#---------TELA INICIAL----------

sg.theme('Darkblue')
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
        window.close()
        telaCadastro()       
    elif event == "2":
        entrada = values['entrada']  #variavel recebe os valores do input
        print(entrada)
        window.close()
        telaLogin()


    if event == sg.WINDOW_CLOSED or event == 'Sair': #se eu apertar o X da guia ele quebra o laço e fecha a janela
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