"""
Universidade Federal de Pernambuco - UFPE
Centro de Informática (CIn) 
Bacharelado em Sistemas de Informação
IF968 - Programação 1

Autor: Pedro Augusto de Almeida Falcão (paaf2) 
Email: paaf2@cin.ufpe.br
Data: 2018-10-16
"""

def cadastraUsuarios(usuario, usuarios, lista, log):
    '''
    A função cadastraUsuarios vai receber dois parâmetros, um nome de usuário e um arquivo, e será responsável por, como o próprio nome sugere, cadastrar usuários ao banco de usuários encontrados no arquivo em questão
    Exemplo 1: Se você digitar um usuário "adm", ele vai pedir para você digitar novamente, pois o usuário já existe no banco de usuários;
    Exemplo 2: Se você digitar um usuário "fernando", ele vai pedir uma senha para o usuário e vai adicioná-lo ao banco de usuários, pois o usuário desejado não existe no banco de usuários
    '''
    
    cadastrando = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                cadastrando += elemento
                
    arq = open(usuarios, "r")
    lerArq = arq.readlines()
    arq.close()
    aux = True

    while(aux == True):
        if((usuario+"\n") in lerArq):
            print("Usuário existente, tente novamente!")
            usuario = input("Digite o usuário a ser cadastrado: ")
        else:
            aux = False
            
    senha = input("Digite uma senha para o usuário: ")
    arq = open(usuarios, "a")
    arq.write(usuario)
    arq.write("\n")
    arq.write(senha)
    arq.write("\n")
    arq.write("1")
    arq.write("\n\n")
    arq.close()

    dataAtual = datetime.now()
    arq = open(log, "a")
    adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + cadastrando + " cadastrou " + usuario + "\n"
    arq.write(adicionar)
    arq.close()
    
    return usuarios 

def removeUsuarios(usuario, usuarios, lista, log):
    '''
    A função removeUsuarios vai, também, receber um usuário e um arquivo como parâmetro, e será utilizada a fim de remover um usuário existente no banco de arquivos
    Exemplo 1: Se você tentar remover "fernando", ele vai imprimir que o usuário não foi encontrado
    Exemplo 2: Se você tentar remover "adm", ele vai imprimir que o usuário foi removido
    '''
    
    removendo = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                removendo += elemento
    
    arq = open(usuarios, "r")
    lerArq = arq.readlines()
    arq.close()
    users = {}
    lista = []
    achei=False
    
    for linha in lerArq:
        if(linha != "\n"):
            lista.append(linha)
        else:
            if(lista[0] == usuario+"\n"):
                print("Usuário removido!")
                lista = []
                achei=True
            else:
                nome = lista[0]
                senha = lista[1]
                hierarquia = lista[2]
                user = (senha, hierarquia)
                users[nome] = user
                lista = []
                
    if(achei): 
        arq = open(usuarios, "w")
        for key in users.keys():
            arq.write(key)
            arq.write(users[key][0])
            arq.write(users[key][1])
            arq.write("\n")
        arq.close()

        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + removendo + " removeu " + usuario + "\n"
        arq.write(adicionar)
        arq.close()

    else:
        print("O usuário não foi encontrado!")

        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + removendo + " tentou remover o usuário inexistente " + usuario + "\n"
        arq.write(adicionar)
        arq.close()
        
    return usuarios 

def login(lista):
    '''
    A função login vai ser responsável por executar o menu, conforme as especificações do usuário, dependendo dele ser um usuário comum, um estagiário ou um gerente
    Exemplo 1: Se você digitar a senha "adm123" para o usuário adm, ele vai dar que a senha está incorreta e vai pedir para que você tente novamente, chamando a função novamente
    Exemplo 2: Se você digitar a senha "adm" para o usuário adm, ele vai concluir o login, levando ao seu menu de opções, conforme sua hierarquia
    '''
    
    user = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                user+= elemento
    senha = input("Digite a sua senha: ")
    if(lista[1] == senha+"\n"):
        print("--------------------")

        dataAtual = datetime.now()
        arq = open("log.txt", "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " se logou\n"
        arq.write(adicionar)
        arq.close()
        
        if(lista[2] == "3\n"):
            menuGerencial("usuarios.txt", "livros.txt", lista, "log.txt")
        elif(lista[2] == "2\n"):
            menuEstagiario("usuarios.txt", "livros.txt", lista, "log.txt")
        else:
            menu("livros.txt", lista, "log.txt")
            
    else:
        print("Senha incorreta, tente novamente!")
        login(lista)

def livrosExistentes(isbn, livros):
    '''
    A função livrosExistentes vai varrer o arquivo livros e vai buscar um livro desejado pelo usuário comum
    Exemplo 1: Se você digitar o ISBN "1", ele vai dizer que o livro não foi encontrado
    Exemplo 2: Se você digitar o ISBN "8574060321", ele vai retornar todas as especificações do livro "Robinson Crusoe"
    '''
    
    banco = {}
    lista = []
    achei = False
    arq = open(livros, "r")
    lerArq = arq.readlines()
    arq.close()

    for linha in lerArq:
        if(linha != "\n" and achei == False):
            lista.append(linha)
        elif(linha == "\n" and achei == False):
            if(lista[0] == isbn+"\n"):
                achei=True
            else:
                lista=[]
    if(achei):
        print("--------------------")
        print("O nome é:", lista[1])
        print("O autor é:",lista[2])
        print("A editora do livro é:", lista[3])
        print("O livro tem:",lista[4])
        print("O ano da edição é:",lista[5])
        if(lista[6] == "A\n"):
            print("O tipo é: Fábula, contos de fada ou folclore")
        elif(lista[6] == "B\n"):
            print("O tipo é: Conto")
        elif(lista[6] == "C\n"):
            print("O tipo é: Romance")
        elif(lista[6] == "D\n"):
            print("O tipo é: Poesia")
        elif(lista[6] == "E\n"):
            print("O tipo é: Ilustrado")
    else:
        print("O livro não foi encontrado!")
        

def buscaGerencial(isbn, livros, lista, log):
    '''
    A função buscaGerencial vai varrer todo o banco de livros contidos no arquivo e vai procurar o ISBN do livro desejado que, caso esteja na lista, será especificado ao usuário e, em seguida, vai fazer as devidas alterações, caso o usuário deseje.
    Essa função vai ser parecida com a função livrosExistentes, entretanto, ela vai ser feita por alguém de hierarquia 2 ou 3, e não mais 1. Ela difere-se da função livrosExistentes pois, além de especificar os livros, ela vai ser capaz de alterar as informações do livro
    '''
    
    usuario = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                usuario+= elemento                
    banco = {}
    lista = []
    dados = []
    achei = False
    arq = open(livros, "r")
    lerArq = arq.readlines()
    arq.close()

    for linha in lerArq:
        if(linha != "\n" and achei == False):
            lista.append(linha)
        elif(linha == "\n" and achei == False):
            if(lista[0] == isbn+"\n"):
                achei=True
            else:
                lista=[]
    if(achei):
        print("--------------------")
        print("O nome é:", lista[1])
        print("O autor é:",lista[2])
        print("A editora do livro é:", lista[3])
        print("O livro tem:",lista[4])
        print("O ano da edição é:",lista[5])
        if(lista[6] == "A\n"):
            print("O tipo é: Fábula, contos de fada ou folclore")
        elif(lista[6] == "B\n"):
            print("O tipo é: Conto")
        elif(lista[6] == "C\n"):
            print("O tipo é: Romance")
        elif(lista[6] == "D\n"):
            print("O tipo é: Poesia")
        elif(lista[6] == "E\n"):
            print("O tipo é: Ilustrado")

        print("--------------------")
        mudar = int(input("Você deseja atualizar a informação desse livro?\n1 - ISBN\n2 - Nome\n3 - Autor\n4 - Editora\n5 - Número de páginas\n6 - Edição\n7 - Tipo\n8 - Alterar tudo\n9 - Não desejo alterar\nDigite a opção desejada: "))
        while(mudar <1 or mudar > 9):
            print("A opção inexiste, tente novamente!")
            mudar = int(input("Digite a opção desejada: "))
        if(mudar >= 1 and mudar<=8):
            for linha in lerArq:
                if(linha != "\n"):
                    dados.append(linha)
                else:
                    isbn = dados[0]
                    nome = dados[1]
                    autor = dados[2]
                    editora = dados[3]
                    paginas = dados[4]
                    edicao = dados[5]
                    tipo = dados[6]
                    tuplaDados = (nome, autor, editora, paginas, edicao, tipo)
                    banco[isbn] = tuplaDados
                    dados = [] 
            if(mudar == 1): #caso ele deseje mudar o isbn
                banco.pop(lista[0])
                isbn = input("Digite o novo isbn: ")
                isbn+= "\n"
                while(isbn in lerArq):
                    print("O ISBN desejado já existe, tente novamente: ")
                    isbn = input("Digite o novo isbn: ")
                    isbn+= "\n"
                banco[isbn]= (lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])

                listando = ""
                for elemento in lista[0]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou o isbn de " + listando + " para " + isbn
                arq.write(adicionar)
                arq.close()
                
            elif(mudar == 2): #caso ele deseje mudar o nome do livro
                nome = input("Digite o novo nome do livro: ")
                nome += "\n"
                banco[lista[0]] = (nome, lista[2], lista[3], lista[4], lista[5], lista[6])
                
                listando = ""
                for elemento in lista[1]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou o nome do livro de " + listando + " para " + nome
                arq.write(adicionar)
                arq.close()
                
            elif(mudar == 3): #caso ele deseje mudar o nome do autor
                autor = input("Digite o novo autor: ")
                autor += "\n"
                banco[lista[0]] = (lista[1], autor, lista[3], lista[4], lista[5], lista[6])

                listando = ""
                for elemento in lista[2]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou o autor de " + listando + " para " + autor
                arq.write(adicionar)
                arq.close()
                
            elif(mudar == 4): #caso ele deseje mudar o nome da editora
                editora = input("Digite a nova editora: ")
                editora += "\n"
                banco[lista[0]] = (lista[1], lista[2], editora, lista[4], lista[5], lista[6])

                listando = ""
                for elemento in lista[3]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou a editora de " + listando + " para " + editora
                arq.write(adicionar)
                arq.close()
                
            elif(mudar == 5): #caso ele deseje mudar o número de páginas
                paginas = input("Digite o novo número de páginas: ")
                paginas += "\n"
                banco[lista[0]] = (lista[1], lista[2], lista[3], paginas, lista[5], lista[6])

                listando = ""
                for elemento in lista[4]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou o número de páginas de " + listando + " para " + paginas
                arq.write(adicionar)
                arq.close()
                
            elif(mudar == 6): #caso ele deseje mudar a data da edição
                edicao = input("Digite a nova data de edição: ")
                edicao += "\n"
                banco[lista[0]] = (lista[1], lista[2], lista[3], lista[4], edicao, lista[6])
                
                listando = ""
                for elemento in lista[5]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou a edição de " + listando + "para " + edicao
                arq.write(adicionar)
                arq.close()
                
            elif(mudar == 7): #caso deseje mudar o tipo do livro
                tipo = input("OPÇÕES:\nA- Fábulas, Contos de Fadas e Folclore\nB- Contos\nC- Romance\nD- Poesia\nE- Ilustrados\nDigite o novo tipo: ")
                while(tipo != "A" and tipo != "B" and tipo != "C" and tipo != "D" and tipo != "E"):
                    print("O tipo desejado não existe, tente novamente!")
                    tipo = input("Digite o novo tipo: ")
                tipo+= "\n"
                banco[lista[0]] = (lista[1], lista[2], lista[3], lista[4], lista[5], tipo)

                listando = ""
                for elemento in lista[6]:
                    if(elemento != "\n"):
                        listando += elemento
                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou o tipo de " + listando + " para " + tipo
                arq.write(adicionar)
                arq.close()
                
            else: #caso deseje mudar tudo
                banco.pop(lista[0])
                isbn = input("Digite o novo isbn: ")
                isbn += "\n"
                while(isbn in lerArq):
                    print("O ISBN desejado já existe, tente novamente: ")
                    isbn = input("Digite o novo isbn: ")
                    isbn+= "\n"
                nome = input("Digite o novo nome do livro: ")
                nome += "\n"
                autor = input("Digite o novo autor: ")
                autor += "\n"
                editora = input("Digite a nova editora: ")
                editora += "\n"
                paginas = input("Digite o novo número de páginas: ")
                paginas += "\n"
                edicao = input("Digite a nova data de edição: ")
                edicao += "\n"
                tipo = input("OPÇÕES:\nA- Fábulas, Contos de Fadas e Folclore\nB- Contos\nC- Romance\nD- Poesia\nE- Ilustrados\nDigite o novo tipo: ")
                while(tipo != "A" and tipo != "B" and tipo != "C" and tipo != "D" and tipo != "E"):
                    print("O tipo desejado não existe, tente novamente!")
                    tipo = input("Digite o novo tipo: ")
                tipo+= "\n"
                banco[isbn] = (nome, autor, editora, paginas, edicao, tipo)

                listando = ""
                for elemento in lista[0]:
                    if(elemento != "\n"):
                        listando += elemento

                dataAtual = datetime.now()
                arq = open(log, "a")
                adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " mudou toda a especificação do livro de anterior isbn " + listando + " e atual isbn " + isbn
                arq.write(adicionar)
                arq.close()
                
            arq = open(livros, "w")
            for key in banco.keys():
                arq.write(key)
                arq.write(banco[key][0])
                arq.write(banco[key][1])
                arq.write(banco[key][2])
                arq.write(banco[key][3])
                arq.write(banco[key][4])
                arq.write(banco[key][5])
                arq.write("\n")
            arq.close()
                
            
    else:
        print("O livro não foi encontrado!")
    return livros


def adicionaLivros(isbn, nome, autor, editora, paginas, edicao, tipo, livros):
    '''
    A função adicionaLivros vai receber do usuário algumas strings e vai adicionar ao banco de livros, no arquivo, as especificações atribuídas
    '''
    arq = open(livros, "a")
    arq.write(isbn)
    arq.write("\n")
    arq.write(nome)
    arq.write("\n")
    arq.write(autor)
    arq.write("\n")
    arq.write(editora)
    arq.write("\n")
    arq.write(paginas)
    arq.write("\n")
    arq.write(edicao)
    arq.write("\n")
    arq.write(tipo)
    arq.write("\n\n")
    arq.close()
    print("O livro foi adicionado!")
    return livros


def removeLivros(isbn, livros, lista, log):
    '''
    A função removeLivros vai basicamente varrer o banco de livros, no arquivo, em busca de um isbn passado pelo usuário e, caso ache, irá remover o livro do arquivo em questão
    Exemplo 1: Se você digitar o ISBN "1", ele vai informar que o livro não foi encontrado
    Exemplo 2: Se você digitar o ISBN "8574060321", ele vai remover esse livro do banco de livros
    '''
    
    usuario = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                usuario+= elemento                
    banco= {}
    lista2=[]
    arq = open(livros, "r")
    lerArq = arq.readlines()
    achei=False

    for linha in lerArq:
        if(linha != "\n"):
            lista2.append(linha)
        else:
            if(lista2[0] == isbn+"\n"):
                print("Livro removido!")
                lista2 = []
                achei = True
            else:
                codigo = lista2[0]
                nome = lista2[1]
                autor = lista2[2]
                editora = lista2[3]
                paginas = lista2[4]
                edicao = lista2[5]
                tipo = lista2[6]
                dados = (nome, autor, editora, paginas, edicao, tipo)
                banco[codigo] = dados
                lista2 = []
    if(achei):
        arq = open(livros, "w")
        for key in banco.keys():
            arq.write(key)
            arq.write(banco[key][0])
            arq.write(banco[key][1])
            arq.write(banco[key][2])
            arq.write(banco[key][3])
            arq.write(banco[key][4])
            arq.write(banco[key][5])
            arq.write("\n")
        arq.close()

        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " removeu o livro de ISBN " + isbn + "\n"
        arq.write(adicionar)
        arq.close()

    else:
        print("O livro não foi encontrado")

        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " tentou remover o livro de ISBN " + isbn + "\n"
        arq.write(adicionar)
        arq.close()

    return livros


def mudaHierarquia(usuario, usuarios, lista, log):
    '''
    A função mudaHierarquia vai basicamente fazer a ateração da hierarquia do usuário, podendo ser alternadas entre 1, 2 ou 3 (comum, estagiário ou gerente, respectivamente)
    Exemplo 1: Se você digitar o usuário "fernando", ele vai informar que o usuário não foi encontrado
    Exemplo 2: Se você digitar o usuário "adm", ele vai perguntar qual a opção hierárquica que você deseja dá-lo
    '''
    
    user = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                user+= elemento                
    banco = {}
    lista2 = []
    achei = False
    arq = open(usuarios, "r")
    lerArq = arq.readlines()
    arq.close()

    for linha in lerArq:
        if(linha != "\n"):
            lista2.append(linha)
        else:
            nome= lista2[0]
            senha = lista2[1]
            hierarquia = lista2[2]
            tupla = (senha, hierarquia)
            banco[nome] = tupla
            lista2 = []

    arq = open(usuarios, "w")
    for key in banco.keys():
        if(usuario+"\n" == key):
            achei = True
            hierarquia= input("Digite a opção hierárquica desejada: ")
            while(int(hierarquia)<1 or int(hierarquia)>3):
                print("Hierarquia inexistente, tente novamente!")
                hierarquia = input("Digite a opção hierárquica desejada: ")
            print("Hierarquia alterada!")
            arq.write(key)
            arq.write(banco[key][0])
            arq.write(hierarquia)
            arq.write("\n\n")
        else:
            arq.write(key)
            arq.write(banco[key][0])
            arq.write(banco[key][1])
            arq.write("\n")
    arq.close()

    if(achei):
        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " mudou a hierarquia de " + usuario + "\n"
        arq.write(adicionar)
        arq.close()

    else:
        print("O usuário não foi encontrado!")
        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " tentou mudar a hierarquia de " + usuario + "\n"
        arq.write(adicionar)
        arq.close()
        
    return usuarios


def ordenar(livros):
    '''
    A função ordenar vai ser responsável por imprimir ao usuário os livros ordenados do mais recente ao mais antigo
    '''
    
    arq = open(livros, "r")
    lerArq = arq.readlines()
    lista = []
    banco = {}
    anos = []
    ano = ""
    cont = 1
    for linha in lerArq:
        if(linha != "\n"):
            lista.append(linha)
        else:
            isbn = lista[0]
            nome = lista[1]
            autor = lista[2]
            editora = lista[3]
            paginas = lista[4]
            edicao = lista[5]
            tipo = lista[6]
            dados = (nome, autor, editora, paginas, edicao, tipo)
            banco[isbn] = dados
            lista = []
            
    indices = list(banco.keys())
    indices = reversed(indices)
    
    for key in indices:
        print("--------------------\n")
        print("LIVRO",cont,":\n")
        print("ISBN:",key,"\nNome:",banco[key][0],"\nAutor:",banco[key][1],"\nEditora:",banco[key][2],"\nPaginas:",banco[key][3],"\nEdição:",banco[key][4],"\nTipo:", banco[key][5])
        cont+=1
        

def sair(usuarios, livros, lista, log):
    '''
    A função sair vai ser executada apenas quando o usuário não desejar continuar e será uma função que não estará disponível em nenhum menu, quando ela for executada, significa que o programa será encerrado e, para isso, ela criptografa os livros e usuários
    '''
    
    print("Programa encerrado!")

    usuario = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                usuario+= elemento
                
    dataAtual = datetime.now() 
    arq = open(log, "a")
    adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " encerrou o programa\n"
    arq.write(adicionar)
    arq.close()

    arq = open(usuarios, "r")
    lerArq = arq.readlines()
    arq.close()
    
    arq2 = open("chavePublica.txt", "r")
    lerArq2 = arq2.readlines()
    arq2.close()
    
    string = ""
    criptografado = ""
    descriptografado = ""
    lista = []

    for linha in lerArq2:
        for caractere in linha:
            if(caractere != "\n"):
              string+= caractere  
    chaves = string.split(" ")

    for linha in lerArq:
        for caractere in linha:
            if(caractere != "\n"):
                criptografado+= str(ord(caractere)**int(chaves[0]) % int(chaves[1]))
                lista.append(criptografado)
                criptografado = ""
            else:
                lista.append("\n")


    arq = open("usuariosCriptografados.txt", "w", encoding = "utf-8")
    for usuario in lista:
        if(usuario != "\n"):
            arq.write(usuario+" ")
        else:
            arq.write("\n")
    arq.close()

    
    arq = open(livros, "r")
    lerArq = arq.readlines()
    arq.close()
    
    arq2 = open("chavePublica.txt", "r")
    lerArq2 = arq2.readlines()
    arq2.close()
    
    string = ""
    criptografado = ""
    descriptografado = ""
    lista = []

    for linha in lerArq2:
        for caractere in linha:
            if(caractere != "\n"):
              string+= caractere  
    chaves = string.split(" ")

    for linha in lerArq:
        for caractere in linha:
            if(caractere != "\n"):
                criptografado+= str(ord(caractere)**int(chaves[0]) % int(chaves[1]))
                lista.append(criptografado)
                criptografado = ""
            else:
                lista.append("\n")


    arq = open("livrosCriptografados.txt", "w", encoding = "utf-8")
    for usuario in lista:
        if(usuario != "\n"):
            arq.write(usuario+" ")
        else:
            arq.write("\n")
    arq.close()


    arq = open(livros, "r") 
    lerArq = arq.readlines()
    arq.close()
    arq2 = open("livrosSemCriptografia.txt", "w")
    cont = 0
    for linha in lerArq:
        if(linha == "\n"):
            arq2.write(linha)
            cont = 0
        elif(cont == 0):
            arq2.write("O isbn do livro é: " + linha)
            cont+=1
        elif(cont == 1):
            arq2.write("O nome do livro é: " + linha)
            cont+=1
        elif(cont == 2):
            arq2.write("O nome do autor é: " + linha)
            cont+=1
        elif(cont == 3):
            arq2.write("O nome da editora é: " + linha)
            cont+=1
        elif(cont == 4):
            arq2.write("O número de páginas é: " + linha)
            cont+=1
        elif(cont == 5):
            arq2.write("O ano da edição é: " + linha)
            cont+=1
        else:
            if(linha == "A\n"):
                arq2.write("O tipo do livro é: Fábulas, Contos de Fada e Folclore\n")
            elif(linha == "B\n"):
                arq2.write("O tipo do livro é: Contos\n")
            elif(linha == "C\n"):
                arq2.write("O tipo do livro é: Romance\n")
            elif(linha == "D\n"):
                arq2.write("O tipo do livro é: Poesia\n")
            else:
                arq2.write("O tipo do livro é: Ilustração\n")
    arq2.close()

    os.remove("usuarios.txt")
    os.remove("livros.txt")

    
def menu(livros, lista, log):
    '''
    A função menu será a mais básica função correspondente às hierarquias, e será responsável apenas por buscar livros e ordenar livros
    '''
    
    usuario = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                usuario+= elemento
    opcao = int(input("OPÇÕES:\n1 - Buscar livro\n2 - Ordenar livros\nDigite a opção desejada: "))
    
    while(opcao < 1 or opcao > 2):
        print("Opção não existente, tente novamente!")
        opcao = int(input("Digite a opção desejada: "))
        
    if(opcao == 1):
        isbn = input("Digite o ISBN a ser buscado: ")
        
        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " buscou o ISBN " + isbn + "\n"
        arq.write(adicionar)
        arq.close()
        
        livrosExistentes(isbn, livros)

    else:
        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + usuario + " ordenou os livros\n"
        arq.write(adicionar)
        arq.close()
        
        ordenar(livros)


def menuEstagiario(usuarios, livros, lista, log):
    '''
    A função menuEstagiario será a função mediana correspondente às hierarquias, tendo opções de: cadastro de usuários, busca de livros e adição de livros
    '''
    
    user = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                user+= elemento
                
    opcao = int(input("OPÇÕES:\n1 - Cadastro de Usuários\n2 - Busca de Livros\n3 - Adicionar livros\nDigite o código da opção desejada: "))
    
    while(opcao<1 or opcao>3):
        print("Opção não existente, tente novamente!")
        opcao = int(input("Digite o código da opção desejada: "))
        
    if(opcao == 1):
        usuario = input("Digite o nome de usuário a ser cadastrado: ")
        usuarios = cadastraUsuarios(usuario, usuarios, lista, log)
        
    elif(opcao == 2):
        isbn = input("Digite o ISBN a ser buscado: ")
        
        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " buscou o ISBN " + isbn + "\n"
        arq.write(adicionar)
        arq.close()
        
        livros = buscaGerencial(isbn, livros, lista, log)
        
    else:
        achei = False
        isbn = input("Digite o ISBN a ser adicionado: ")
        arq = open(livros, "r")
        lerArq = arq.readlines()
        for linha in lerArq:
            if(linha == isbn+"\n"):
                achei = True
                
        if(achei):
            print("O ISBN dado já existe no banco de livros!")

            dataAtual = datetime.now()
            arq = open(log, "a")
            adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " tentou adicionar o ISBN " + isbn + "\n"
            arq.write(adicionar)
            arq.close()
            
        else:     
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            editora = input("Digite  o nome da editora do livro: ")
            paginas = input("Digite o número de páginas do livro: ")
            edicao = input("Digite a data da edição do livro: ")
            tipo = input("OPÇÕES:\nA- Fábulas, contos de Fada e folclores\nB- Contos\nC - Romance\nD- Poesia\nE- Ilustrados\nDigite a opção correspondente: ")
            while(tipo != "A" and tipo != "B" and tipo != "C" and tipo != "D" and tipo != "E"):
                    print("O tipo desejado não existe, tente novamente!")
                    tipo = input("Digite o novo tipo: ")

            dataAtual = datetime.now()
            arq = open(log, "a")
            adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " adicionou o livro de ISBN " + isbn + "\n"
            arq.write(adicionar)
            arq.close()
            
            livros = adicionaLivros(isbn, nome, autor, editora, paginas, edicao, tipo, livros)


def menuGerencial(usuarios, livros, lista, log):
    '''
    A funçãomenuGerencial será a função mais abrangente correspondente às hierarquias, tendo como opção: cadastro de usuário, remoção de usuário, busca de livro, adição de livro, remoção de livro e mudança de hierarquia
    '''

    user = ""
    for elemento in lista[0]:
            if(elemento != "\n"):
                user+= elemento
                
    opcao = int(input("OPÇÕES:\n1 - Cadastro de Usuários\n2 - Remoção de Usuários\n3 - Busca de Livros\n4 - Adicionar livros\n5 - Remover livros\n6 - Mudar a hierarquia\nDigite o código da opção desejada: "))
    while(opcao<1 or opcao>6):
        print("Opção não existente, tente novamente!")
        opcao = int(input("Digite o código da opção desejada: "))
    if(opcao == 1):
        usuario = input("Digite o nome de usuário a ser cadastrado: ")
        usuarios = cadastraUsuarios(usuario, usuarios, lista, log)
        
    elif(opcao == 2):
        usuario= input("Digite o nome do usuário a ser removido: ")
        usuarios = removeUsuarios(usuario, usuarios, lista, log)
        
    elif(opcao == 3):
        isbn= input("Digite o ISBN a ser buscado: ")
        dataAtual = datetime.now()
        arq = open(log, "a")
        adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " buscou o ISBN " + isbn + "\n"
        arq.write(adicionar)
        arq.close()
        
        livros = buscaGerencial(isbn, livros, lista, log)
        
    elif(opcao == 4):
        achei = False
        isbn = input("Digite o ISBN a ser adicionado: ")
        arq = open(livros, "r")
        lerArq = arq.readlines()
        for linha in lerArq:
            if(linha == isbn+"\n"):
                achei = True
                
        if(achei):
            print("O ISBN dado já existe no banco de livros!")

            dataAtual = datetime.now()
            arq = open(log, "a")
            adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " tentou adicionar o ISBN " + isbn + "\n"
            arq.write(adicionar)
            arq.close()
            
        else:     
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            editora = input("Digite  o nome da editora do livro: ")
            paginas = input("Digite o número de páginas do livro: ")
            edicao = input("Digite a data da edição do livro: ")
            tipo = input("OPÇÕES:\nA- Fábulas, contos de Fada e folclores\nB- Contos\nC - Romance\nD- Poesia\nE- Ilustrados\nDigite a opção correspondente: ")
            while(tipo != "A" and tipo != "B" and tipo != "C" and tipo != "D" and tipo != "E"):
                    print("O tipo desejado não existe, tente novamente!")
                    tipo = input("Digite o novo tipo: ")

            dataAtual = datetime.now()
            arq = open(log, "a")
            adicionar = dataAtual.strftime("%d/%m/%Y %H:%M") + " - " + user + " adicionou o livro de ISBN " + isbn + "\n"
            arq.write(adicionar)
            arq.close()
            
            livros = adicionaLivros(isbn, nome, autor, editora, paginas, edicao, tipo, livros)
        
    elif(opcao == 5):
        livro = input("Digite o ISBN do livro a ser removido: ")
        livros = removeLivros(livro, livros, lista, log)
        
    else:
        usuario = input("Digite o usuário cuja hierarquia será mudada: ")
        usuarios = mudaHierarquia(usuario, usuarios, lista , log)

def descriptografiaDeLivros():
    '''
    A função descriptografiaDeLivros será executada no início do programa e será responsável por descriptografar o banco de livros
    '''
    
    arq = open("livrosCriptografados.txt", "r", encoding="utf-8")
    lerArq = arq.readlines()
    arq.close()

    arq = open("chavePrivada.txt", "r")
    lerArq2 = arq.readlines()
    arq.close()

    string = ""
    for linha in lerArq2:
        for caractere in linha:
            if(caractere != "\n"):
                string+= caractere
    chaves = string.split(" ")

    string = ""
    descriptografado = ""
    lista= []
    for linha in lerArq:
        if(linha != "\n"):
            for caractere in linha:
                if(caractere != " " and caractere != "\n"):
                    string+= caractere
                else:
                    if(string != ""):
                        string = int(string)
                        adicionar = string**int(chaves[0]) % int(chaves[1])
                        descriptografado+= chr(adicionar)
                    string = ""
            lista.append(descriptografado)
            descriptografado = ""

    cont = 0
    arq = open("livros.txt", "w", encoding="utf-8")
    for elemento in lista:
        if(cont<6):
            arq.write(elemento)
            arq.write("\n")
            cont+=1
        else:
            arq.write(elemento)
            arq.write("\n\n")
            cont = 0
    arq.close()

def descriptografiaDeUsuarios():
    '''
    A função descriptografiaDeUsuários será executada no início do programa, assim como a descriptografia de livros, e será responsável por descriptografar o banco de usuários
    '''
    
    arq = open("usuariosCriptografados.txt", "r", encoding="utf-8")
    lerArq = arq.readlines()
    arq.close()

    arq = open("chavePrivada.txt", "r")
    lerArq2 = arq.readlines()
    arq.close()

    string = ""
    for linha in lerArq2:
        for caractere in linha:
            if(caractere != "\n"):
                string+= caractere
    chaves = string.split(" ")

    string = ""
    descriptografado = ""
    lista= []
    for linha in lerArq:
        if(linha != "\n"):
            for caractere in linha:
                if(caractere != " " and caractere != "\n"):
                    string+= caractere
                else:
                    if(string != ""):
                        string = int(string)
                        adicionar = string**int(chaves[0]) % int(chaves[1])
                        descriptografado+= chr(adicionar)
                    string = ""
            lista.append(descriptografado)
            descriptografado = ""

    cont = 0
    arq = open("usuarios.txt", "w", encoding="utf-8")
    for elemento in lista:
        if(cont<2):
            arq.write(elemento)
            arq.write("\n")
            cont+=1
        else:
            arq.write(elemento)
            arq.write("\n\n")
            cont = 0
    arq.close()


descriptografiaDeLivros()
descriptografiaDeUsuarios()

import os
from datetime import datetime

lista = []
achei = False
aux = True

print("Olá, seja bem-vindo! Vamos efetuar o seu login?")
usuario = input("Digite o seu usuário: ")

arq = open("usuarios.txt", "r")
lerArq = arq.readlines()
arq.close()

for linha in lerArq:
    if(linha != "\n"):
        lista.append(linha)
    else:
        if(usuario+"\n" == lista[0]):
            achei = True
            hierarquia = lista[2]
        else:
            lista=[]
            
while(achei==False):
    print("Usuário inexiste, tente novamente!")
    usuario = input("Digite o seu usuário: ")
    for linha in lerArq:
        if(linha != "\n"):
            lista.append(linha)
        else:
            if(usuario+"\n" == lista[0]):
                achei = True
                hierarquia = lista[2]
            else:
                lista=[]
if(achei==True):
    login(lista)


 
while(aux):
    print("--------------------")
    continuar = int(input("OPÇÕES:\n1 - Continuar\n2 - Sair\nDigite a opção desejada: "))
    
    while(continuar<1 or continuar>2):
        print("Opção inexistente, tente novamente!")
        continuar= int(input("Digite a opção desejada: "))
        
    if(continuar == 1 and hierarquia == "1\n"):
        menu("livros.txt", lista, "log.txt")
        
    elif(continuar == 1 and hierarquia== "2\n"):
        menuEstagiario("usuarios.txt", "livros.txt", lista, "log.txt")
        
    elif (continuar == 1 and hierarquia=="3\n"):
        menuGerencial("usuarios.txt", "livros.txt", lista, "log.txt")
        
    else:
        aux = False
        sair("usuarios.txt", "livros.txt", lista, "log.txt")

'''
Enquanto a variável auxiliar for True, o programa permanece rodando. Quando o usuário optar por sair, a variável se torna False e a função sair, então, será executada
'''
