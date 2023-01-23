


#FUNÇÕES
def cadastrar():
    nome = input('Digite o nome de usuário: ').strip()
    senha = input('Digite sua senha: ').strip()

    if nome == senha:
        print('Sua senha não pode ser igual ao login!')
    else:
        fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'r')
        var = fixario.readlines()


        for i in range(len(var)):
            num = var[i].split(',')[0]  #ser criado uma lista no indice i, com dois elementos
            if nome == num:
                print('Esse número de login já existe!')
                break
            else:
                fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'a')
                fixario.write(nome + ',' + senha + '\n')
                print('Login realizado com sucesso!')
                break
                





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




def sair():
    print("Te vejo na próxima!")


def lista():
    senha = input('Digite a senha do ADMINISTRADOR: ')
    senhaADM = 'tuamae'
    if senha == senhaADM:
        fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'r')
        print('\n')
        print('-='*45)
        print("LISTA DE CADASTRO")
        print('-='*45 + '\n')
        print(fixario.read())
        print('-='*45)
    else:
        print('EROUUU')



#MENU
while True:
    print('''
    -=-=[MENU]=-=-
    1 - CADASTRAR
    2 - LOGIN
    3 - SAIR
    4 - MOSTRAR LISTA\n''')

    escolha = input("Escolha: ")

    if escolha not in "1234" or escolha == '':
        print('Digite algo válido!\n\n')
    else:
        if escolha in "1":
            cadastrar()
        elif escolha in "2":
            login()
        elif escolha in "3":
            sair()
            break
        elif escolha in "4":
            lista()
        else: 
            print('Digite algo que seja valido')

