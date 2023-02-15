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
    [sg.Button('Confirmar'), sg.Button('Sair'), sg.Button('Voltar')]                           
    ]

    window = sg.Window('Sistema Teste de Login', telaCadastro)
    while True:
        event, values = window.read()
        if event == "Confirmar":
            nome = values['cadastro']
            senha = values['senha']

            if nome == senha:
                window['saida'].update('Sua senha não pode ser igual ao login!')
                
            else:
                fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'r')
                var = fixario.readlines()

                for i in range(len(var)):
                    num = var[i].split(',')[0]  #ser criado uma lista no indice i, com dois elementos
                    if nome == num:
                        window['saida'].update('Esse número de loogin já existe')
                        break
                    else:
                        fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'a')
                        fixario.write(nome + ',' + senha + '\n')
                        fixario.close()
                        window['saida'].update('Cadastro realizado com sucesso!')
                        break

        if event == 'Voltar':
            window.close()
            menu()
                           
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
    [sg.Text('Login:')],
    [sg.Input(key='login')],
    [sg.Text('Senha:')],
    [sg.Input(key='senha')],
    [sg.Text(key='saida')], #saida da informação "print na interface"
    [sg.Button('Confirmar'), sg.Button('Sair'), sg.Button('Voltar')]                           
    ]

    window = sg.Window('Sistema Teste de Login', telaLogin)
    while True:
        event, values = window.read()
        if event == "Confirmar":
            nome = values['login']
            senha = values['senha']

            fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'r')
            var = fixario.readlines()
            booleano = bool
            for i in range(len(var)):
                num = var[i].split(',')

                if num[0] == nome and num[1].split('\n')[0] == senha :
                    booleano = True
                    if booleano == True:
                        window['saida'].update('Login realizado com sucesso')
                    break
                        
        
            else:
                window['saida'].update('Esse usuário não existe ou você errou a senha!\nTente novamente')
            


        if event == 'Voltar':
            window.close()
            menu()
            
        if event == sg.WINDOW_CLOSED or event == 'Sair': #se eu apertar o X da guia ele quebra o laço e fecha a janela
            break    
        
    window.close()




#---------TELA INICIAL----------
def menu():
    sg.theme('Darkblue')
    tela = [    #oq vai ser mostrado na tela
        [sg.Text('BEM VINDO(A)')],
        [sg.Text('1-Cadastrar\n2-Login\n')],
        [sg.Input(key='entrada')], #entrada da informação
        [sg.Button('Cadastro'), sg.Button('Login')]                           
    ]


    window = sg.Window('Sistema Teste de Login', tela)
    while True:
        event, values = window.read()
        if event == "Cadastro":
            entrada = values['entrada']  #variavel recebe os valores do input
            window.close()
            telaCadastro()       
        elif event == "Login":
            entrada = values['entrada']  #variavel recebe os valores do input
            window.close()
            telaLogin()


        if event == sg.WINDOW_CLOSED or event == 'Sair': #se eu apertar o X da guia ele quebra o laço e fecha a janela
            break
    window.close()
menu()


















