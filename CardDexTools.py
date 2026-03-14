import os

def remover_carta(ficheiro_nome, carta_a_remover):
    linhas_vivas = []
    encontrado = False

    with open(f"{ficheiro_nome}.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if carta_a_remover not in linha:
                linhas_vivas.append(linha)
            else:
                encontrado = True
        
    with open(f"{ficheiro_nome}.txt", "w", encoding="utf-8") as f:
        f.writelines(linhas_vivas)
            
    if encontrado:
        print(f"A carta {carta_a_remover.capitalize()} foi removida.")
    else:
        print("Carta não encontrada.")


def ver_ficheiro(filetosee):
    try:
       with open(f"{filetosee}.txt", "r", encoding="utf-8") as file:
        conteudo = file.read()
        print("--- Conteúdo do Ficheiro ---")
        print(conteudo)
    except FileNotFoundError:
        print("A lista ainda não existe.")


def verif_file(filetoverif):
    try:
        with open(f"{filetoverif}.txt", "r", encoding="utf-8") as ficheiro:
           content = ficheiro.read()
    except FileNotFoundError:
        print("A lista ainda não existe.")


def add_nomes(filetoedit):
    listateluser = {}
    while True:
        carta = input("Nome da carta(ou escreve sair quando acabares): ").strip().lower()
        if carta == "sair":
            break
        else:
            ctipo= input(f"Tipo de {carta.capitalize()}: ").strip().lower()
            listateluser[carta] = ctipo
    with open(f"{filetoedit}.txt", "a", encoding="utf-8") as ficheiro:
        for nome, tipo in listateluser.items():
            ficheiro.write(f"- {nome}: {tipo}\n")
        print("Carta/s adicionada/s com sucesso!")


def elim_file():
    userename = input("Qual o nome da lista que queres eliminar: ").strip().lower()
    if os.path.exists(f"{userename}.txt"):
        os.remove(f"{userename}.txt")
        print(f"A lista {userename} foi eliminada!")
    else:
        print("A lista não foi encontrado.")  


def criar_file():
    listatel = {}
    usercname = input("Qual o nome do ficheiro que queres criar: ").strip().lower()
    while True:
        nomec = input("Nome da carta(ou escreve sair quando acabares): ").strip().lower()
        if nomec == "sair":
            break
        else:
            tipoc = input(f"Tipo de {nomec.capitalize()}: ").strip().lower()
            listatel[nomec] = tipoc
    with open(f"{usercname}.txt", "w", encoding="utf-8") as fileuser:
        fileuser.write("Lista de Amigos:\n")
        for nome, tipo in listatel.items():
            fileuser.write(f"- {nome}: {tipo}\n")
        print("Lista criada com sucesso!")  
