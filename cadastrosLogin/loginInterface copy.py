import PySimpleGUI as sg


def login():
    nome = input('Digite o nome de login: ').strip()
    senha = input('Digite a senha de login: ').strip()

    fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'r')
    var = fixario.readlines()
    booleano = bool
    for i in range(len(var)):
        num = var[i].split(',')

        if num[0] == nome and num[1].split('\n')[0] :
            booleano = True
            if booleano == True:
                print('Login realizado com sucesso!')
            break

    
        
    else:
        print('Esse usuário não existe!')





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
        login()
        
    if event == sg.WINDOW_CLOSED: #se eu apertar o X da guia ele quebra o laço e fecha a janela
        break
    
    
window.close()