import customtkinter
import os

def criar_file(usercname, frameante, frameno, lbltit):
    user = usercname.get()
    lbltit.configure(text=f"Adicionar cartas a {user}")
    with open(f"{user}.txt", "w", encoding="utf-8") as fileuser:
        
        fileuser.write("Cartas:\n")
        print(f"A criar: {usercname}.txt")
    frameante.pack_forget()
    frameno.pack(pady=20, fill="both", expand=True)



def mostrar_ver(frameant, framenova):
    # Esconde o frame de ver e mostra o de criar
    frameant.pack_forget()
    framenova.pack(pady=20, fill="both", expand=True)



def ver_file(filenam, labelresultado):
    # 1. Pega no texto da caixa de entrada
    file = filenam.get()
    while True:
        try:
            with open(f"{file}.txt", "r", encoding="utf-8") as filee:
                conteudo = filee.read()
                print("--- Conteúdo do Ficheiro ---")
                print(conteudo)
                labelresultado.configure(text=f"Conteudo do ficheiro:\n{conteudo}", text_color="green")
        except FileNotFoundError:
            print("O ficheiro ainda não existe.")
            print(f"A criar: {file}.txt")
            labelresultado.configure(text="Ficheiro não existe!", text_color="red")
        break



def add_nomesetipo(filetoedit, nome, tipo):
    fich = filetoedit.get()
    nnome = nome.get()
    ttipo = tipo.get()
    listateluser = {}
    listateluser[nnome] = ttipo
    with open(f"{fich}.txt", "a", encoding="utf-8") as ficheiro:
        for nomeca, tipoca in listateluser.items():
            ficheiro.write(f"- {nomeca}: {tipoca}\n")
        print("Cartas adicionadas com sucesso!")



def verif_file(filetoverif, labelres, framant, framnov, labeltit):
    supfile = filetoverif.get()
    try:
        with open(f"{supfile}.txt", "r", encoding="utf-8") as ficheiro:
            labeltit.configure(text=f"Adicionar cartas a {supfile}")
            content = ficheiro.read()
            framant.pack_forget()
            framnov.pack(pady=20, fill="both", expand=True)
    except FileNotFoundError:
        labelres.configure(text="Ficheiro não existe!", text_color="red")


def elim_file(fileee, labres):
    userename = fileee.get()
    if os.path.exists(f"{userename}.txt"):
        os.remove(f"{userename}.txt")
        print(f"O ficheiro {userename} foi eliminado!")
        labres.configure(text=f"{userename}.txt eliminado")
    else:
        print("O ficheiro não foi encontrado.") 
        labres.configure(text=f"O ficheiro {userename}.txt nao foi encontrado")


def remover_carta(ficheironome, nomearem):
    ficheiro_nome = ficheironome.get()
    nomearemover = nomearem.get()
    linhas_vivas = []
    encontrado = False

    with open(f"{ficheiro_nome}.txt", "r", encoding="utf-8") as f:
        for linha in f:
            # Se o nome NÃO estiver na linha, guardamos a linha
            if nomearemover.lower() not in linha.lower():
                linhas_vivas.append(linha)
            else:
                encontrado = True
        
     # Reescrever o ficheiro apenas com as linhas que restaram
    with open(f"{ficheiro_nome}.txt", "w", encoding="utf-8") as f:
        f.writelines(linhas_vivas)
            
    if encontrado:
        print(f"A carta {nomearemover} foi removida.")
    else:
        print("Nome não encontrado.")