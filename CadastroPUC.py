import json

def Criar_Arquivo(lista, arquivo_info):
    with open(arquivo_info, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent = 4)

def Ler_Arquivo(arquivo_info):
    try:    
        with open(arquivo_info, 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)

        return lista
    except:
        return []


def Cadastro_verificar(lista, codigo):
    for i in lista:
        if i["codigo"] == codigo:
            return True
    return False    
        


def Menu_de_Principal():
    print("----- MENU PRINCIPAL -----")
    print("")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.")
    print("")

    return input("Informe a opção desejada:")

def Menu_de_Operacoes():
    print("")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.") 
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.")

    return input("Informe a ação desejada:")

def Incluir_alu_prof(arquivo_info): #Inclui alunos ou professores
    cadastro_alu_prof = Ler_Arquivo(arquivo_info)
    print("===== INCLUIR =====")
    while True:
        try:
            codigo = int(input("Digite o código: "))
            break
        except ValueError:
            print("Digite um número!")

    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")

    info_alu_prof = {
        "codigo": codigo,
        "nome" : nome,
        "cpf": cpf,
    }

    cadastro_alu_prof.append(info_alu_prof)
    Criar_Arquivo(cadastro_alu_prof, arquivo_info)
    return None

def Incluir_disciplinas(arquivo_info): #Inclui disciplinas
    cadastro_disciplinas = Ler_Arquivo(arquivo_info)
    print("===== INCLUIR =====")
    while True:
        try:
            codigo = int(input("Digite o código da disciplina: "))
            break
        except ValueError:
            print("Digite um número!")

    nome = input("Digite o nome da disciplina: ")

    info_disciplinas = {
        "codigo": codigo,
        "nome da disciplina" : nome
    }

    cadastro_disciplinas.append(info_disciplinas)
    Criar_Arquivo(cadastro_disciplinas, arquivo_info)
    return None

def Incluir_turmas(arquivo_info):
    cadastro_turmas = Ler_Arquivo(arquivo_info)
    print("===== INCLUIR =====")
    while True:
        try:
            codigo_turma = int(input("Digite o codigo da turma: "))
            if Cadastro_verificar(cadastro_turmas, codigo_turma):
                print("Código já existente!")
                continue
            codigo_prof = int(input("Digite o codigo do professor: "))
            codigo_disciplina = int(input("Digite o codigo da disciplina: "))
            break
        except ValueError:
            print("Digite um número!")

    info_turmas = {
        "codigo": codigo_turma,
        "codigo do professor" : codigo_prof,
        "codigo da disciplina": codigo_disciplina,
    }

    cadastro_turmas.append(info_turmas)
    Criar_Arquivo(cadastro_turmas, arquivo_info)
    return None

def Incluir_matriculas(arquivo_info):
    cadastro_matriculas = Ler_Arquivo(arquivo_info)
    print("===== INCLUIR =====")
    while True:
        try:
            codigo_turma = int(input("Digite o codigo da turma: "))
            if Cadastro_verificar(cadastro_matriculas, codigo_turma):
                print("Código já existente!")
                continue
            codigo_aluno = int(input("Digite o codigo do aluno: "))
            break
        except ValueError:
            print("Digite um número!")

    info_matricula = {
        "codigo": codigo_turma,
        "codigo do aluno": codigo_aluno
    }

    cadastro_matriculas.append(info_matricula)
    Criar_Arquivo(cadastro_matriculas, arquivo_info)
    return None

def Listar(arquivo_info):
    cadastro = Ler_Arquivo(arquivo_info)
    if cadastro:
        print("===== LISTAR =====")
        for i in cadastro:
            print(f"- {i}")
    else:
        print("Sem cadastros!")
    return None

def Atualizar_alu_prof(arquivo_info):
    cadastro_alu_prof = Ler_Arquivo(arquivo_info)
    print("===== ATUALIZAR =====")
    while True:
        try:
            codigo_atualizar = int(input("Digite o codigo: "))
            break
        except ValueError:
            print("Digite um número!")
    cadastro_atualizar = None
    for i in cadastro_alu_prof:
        if i["codigo"] == codigo_atualizar:
            cadastro_atualizar = i
            break
    if cadastro_atualizar is None:
        print("Não encontrado!")
    else:
        while True:
            try:
                cadastro_atualizar["codigo"] = int(input("Digite o código novo: "))
                break
            except ValueError:
                print("Digite um número!")
                
        cadastro_atualizar["nome"] = input("Digite o nome novo: ")
        cadastro_atualizar["cpf"] = input("Digite o cpf novo: ")

    Criar_Arquivo(cadastro_alu_prof, arquivo_info)
    return None

def Atualizar_disciplinas(arquivo_info):
    cadastro_disciplinas = Ler_Arquivo(arquivo_info)
    print("===== ATUALIZAR =====")
    while True:
        try:
            codigo_atualizar = int(input("Digite o codigo da turma: "))
            break
        except ValueError:
            print("Digite um número!")
    cadastro_atualizar = None
    for i in cadastro_disciplinas:
        if i["codigo"] == codigo_atualizar:
            cadastro_atualizar = i
            break
    if cadastro_atualizar is None:
        print("Não encontrado!")
    else:
        while True:
            try:
                cadastro_atualizar["codigo"] = int(input("Digite o código novo: "))
                break
            except ValueError:
                print("Digite um número!")
                
        cadastro_atualizar["nome da disciplina"] = input("Digite o novo nome da disciplina: ")

    Criar_Arquivo(cadastro_disciplinas, arquivo_info)
    return None

def Atualizar_turmas(arquivo_info):
    cadastro_turmas = Ler_Arquivo(arquivo_info)
    print("===== ATUALIZAR =====")
    while True:
        try:
            codigo_atualizar = int(input("Digite o codigo da turma: "))
            break
        except ValueError:
            print("Digite um número!")
    cadastro_atualizar = None
    for i in cadastro_turmas:
        if i["codigo"] == codigo_atualizar:
            cadastro_atualizar = i
            break
    if cadastro_atualizar is None:
        print("Não encontrado!")
    else:
        while True:
            try:
                cadastro_atualizar["codigo"] = int(input("Digite o novo código da turma: "))
                cadastro_atualizar["codigo do professor"] = int(input("Digite o novo código do professor: "))
                cadastro_atualizar["codigo da disciplina"] = int(input("Digite o novo código da disciplina: "))
                break
            except ValueError:
                print("Digite um número!")

    Criar_Arquivo(cadastro_turmas, arquivo_info)
    return None

def Atualizar_matriculas(arquivo_info):
    cadastro_matriculas = Ler_Arquivo(arquivo_info)
    print("===== ATUALIZAR =====")
    while True:
        try:
            codigo_atualizar = int(input("Digite o codigo da turma: "))
            break
        except ValueError:
            print("Digite um número!")
    cadastro_atualizar = None
    for i in cadastro_matriculas:
        if i["codigo"] == codigo_atualizar:
            cadastro_atualizar = i
            break
    if cadastro_atualizar is None:
        print("Não encontrado!")
    else:
        while True:
            try:
                cadastro_atualizar["codigo"] = int(input("Digite o novo código da turma: "))
                cadastro_atualizar["codigo do aluno"] = int(input("Digite o novo código do aluno: "))
                break
            except ValueError:
                print("Digite um número!")

    Criar_Arquivo(cadastro_matriculas, arquivo_info)
    return None


def Excluir(arquivo_info):
    cadastro = Ler_Arquivo(arquivo_info)
    print("===== EXCLUIR =====")
    while True:
        try:
            codigo_excluir = int(input("Digite o codigo: "))
            break
        except ValueError:
            print("Digite um número!")
    cadastro_remover = None
    for i in cadastro:
        if i["codigo"] == codigo_excluir:
            cadastro_remover = i
            break
    if cadastro_remover is None:
        print("Não encontrado!")
    else:
        cadastro.remove(cadastro_remover)
    Criar_Arquivo(cadastro, arquivo_info)
    return None

arquivo_alunos = "alunos.json"
arquivo_professores = "professores.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"


# Menu principal
while True:

    opcao = Menu_de_Principal()
      
    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        
        # Menu secundario
        while True:
            if opcao == "1": #ESTUDANTES
                print("***** [ESTUDANTES] Menu de operações *****")
                acao = Menu_de_Operacoes()
                if acao == "1" or acao == "2" or acao == "3" or acao == "4":
                    if acao == "1": #Incluir  
                        Incluir_alu_prof(arquivo_alunos)
                        
                    elif acao == "2": #Listar
                        Listar(arquivo_alunos)
                    
                    elif acao == "3": #Atualizar
                        Atualizar_alu_prof(arquivo_alunos)
                        
                    elif acao == "4": #Excluir
                        Excluir(arquivo_alunos)

                elif acao == "9":
                    print("Voltando ao menu principal")
                    break #volta pro menu principal
                else:
                    print("Insira uma ação válida")

            elif opcao == "2": #PROFESSORES
                print("***** [PROFESSORES] Menu de operações *****")
                acao = Menu_de_Operacoes()
                if acao == "1" or acao == "2" or acao == "3" or acao == "4":
                    if acao == "1": #Incluir  
                        Incluir_alu_prof(arquivo_professores)
                        
                    elif acao == "2": #Listar
                        Listar(arquivo_professores)
                    
                    elif acao == "3": #Atualizar
                        Atualizar_alu_prof(arquivo_professores)
                        
                    elif acao == "4": #Excluir
                        Excluir(arquivo_professores)

                elif acao == "9":
                    print("Voltando ao menu principal")
                    break #volta pro menu principal
                else:
                    print("Insira uma ação válida")

            elif opcao == "3": #DISCIPLINAS
                print("***** [DISCIPLINAS] Menu de operações *****")
                acao = Menu_de_Operacoes()
                if acao == "1" or acao == "2" or acao == "3" or acao == "4":
                    if acao == "1": #Incluir  
                        Incluir_disciplinas(arquivo_disciplinas)
                        
                    elif acao == "2": #Listar
                        Listar(arquivo_disciplinas)
                        
                    elif acao == "3": #Atualizar
                        Atualizar_disciplinas(arquivo_disciplinas)
                        
                    elif acao == "4": #Excluir
                        Excluir(arquivo_disciplinas)

                elif acao == "9":
                    print("Voltando ao menu principal")
                    break #volta pro menu principal
                else:
                    print("Insira uma ação válida")

            elif opcao == "4":#TURMAS
                print("***** [TURMAS] Menu de operações *****")
                acao = Menu_de_Operacoes()
                if acao == "1" or acao == "2" or acao == "3" or acao == "4":
                    if acao == "1": #Incluir  
                        Incluir_turmas(arquivo_turmas)
                        
                    elif acao == "2": #Listar
                        Listar(arquivo_turmas)
                    
                    elif acao == "3": #Atualizar
                        Atualizar_turmas(arquivo_turmas)
                        
                    elif acao == "4": #Excluir
                        Excluir(arquivo_turmas)

                elif acao == "9":
                    print("Voltando ao menu principal")
                    break #volta pro menu principal
                else:
                    print("Insira uma ação válida")
                
            elif opcao == "5": #MATRÍCULAS
                print("***** [MATRÍCULAS] Menu de operações *****")
                acao = Menu_de_Operacoes()
                if acao == "1" or acao == "2" or acao == "3" or acao == "4":
                    if acao == "1": #Incluir  
                        Incluir_matriculas(arquivo_matriculas)
                        
                    elif acao == "2": #Listar
                        Listar(arquivo_matriculas)
                    
                    elif acao == "3": #Atualizar
                        Atualizar_matriculas(arquivo_matriculas)
                        
                    elif acao == "4": #Excluir
                        Excluir(arquivo_matriculas)
                    
                elif acao == "9":
                    print("Voltando ao menu principal")
                    break #volta pro menu principal
                else:
                    print("Insira uma ação válida")

    elif opcao == "9":
        print("Finalizando aplicação")
        break#finaliza
    else:
        print("Insira uma opção válida")
