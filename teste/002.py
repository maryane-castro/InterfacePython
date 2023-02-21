meuarquivo = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/teste/uir.txt', 'a')

#nome = input('nome: ').strip()
#senha = input('senha: ').strip()

#meuarquivo.write(nome + ',' + senha +  '\n')

#meuarquivo = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/teste/uir.txt', 'r')




nome = input('Digite o nome de usuário: ').strip()
senha = input('Digite sua senha: ').strip()


if nome == senha:
    print('Sua senha não pode ser igual ao login!')
else:
    fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/teste/uir.txt', 'r')
    var = fixario.readlines()


    for i in range(len(var)):
        num = var[i].split(',')[0]  #ser criado uma lista no indice i, com dois elementos
        if nome == num:
            print('Esse número de login já existe!')
        else:
            fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/teste/uir.txt', 'a')
            fixario.write('\n' + nome + ',' + senha)
            print('Login realizado com sucesso!')
            break
            

/
nome = input('Digite o nome de usuário: ').strip()
    senha = input('Digite sua senha: ').strip()

    fixario = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/cadastrosLogin/cadastros.txt', 'r')
    var = fixario.readlines()


    for i in range(len(var)):
        num = var[i].split(',')[0]  #ser criado uma lista no indice i, com dois elementos
        if nome == num:
            print('Login realizado!')
            break
        print('Login errado')
        break
/



















'''var = meuarquivo.readlines()
print(var)
num = var[0].split(',')[0]
print(num)

nome = 'maryane'


for i in range(len(var)):
    num = var[i].split(',')[0]
    print(num)
    if num == nome:
        print('iguais')
    else:
        print('diferente')'''













'''aux = 'tutu'
for nomes in range(len(nome)):
    if aux == nome[nomes]:
        print('são iguais')
    else:
        print('são diferentes')
        meuarquivo = open('C:/Users/kookp/OneDrive/Documentos/vscode/InterfacePython/teste/uir.txt', 'a')
        meuarquivo.write(aux + '\n')
        print(meuarquivo)'''
