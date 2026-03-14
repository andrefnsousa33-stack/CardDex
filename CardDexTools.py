from CardDexClasses import GestorFile


def mostrar_ver(frameant, framenova):
    frameant.pack_forget()
    framenova.pack(pady=20, fill="both", expand=True)

def remover_carta(ficheironome, nomearem):
    ficheiro_nome = ficheironome.get()
    nomearemover = nomearem.get()
    gestor = GestorFile(ficheiro_nome)
    gestor.remover_car(nomearemover)

def acao_verif_lista(nomefile, labelres, framant, framnov, labeltit):
    namee = nomefile.get()
    gestora = GestorFile(namee)
    existe = gestora.verif()
    if existe:
        framant.pack_forget()
        framnov.pack(pady=20, fill="both", expand=True)
        labeltit.configure(text=f"Adicionar cartas a {namee}")
    else:
        labelres.configure(text="Ficheiro não existe!", text_color="red")   

def acao_ver_lista(ver_nome, label_resultadover):
    nome = ver_nome.get()
    gestor = GestorFile(nome)
    conteudo = gestor.ler_tudo()
    label_resultadover.configure(text=conteudo, text_color="white")

def acao_adicionar_existente(file_nam, newnome, newtef, label_res):
    nome_fich = file_nam.get()
    nome_amigo = newnome.get()
    tel_amigo = newtef.get()
    
    gestor = GestorFile(nome_fich)
    gestor.adicionar(nome_amigo, tel_amigo)
    label_res.configure(text=f"{nome_amigo} adicionado!", text_color="green")

def criar_file(usercname, frameante, frameno, lbltit, lblres):
    user = usercname.get()
    gestor = GestorFile(user)
    existe = gestor.verif()
    if existe:
        lblres.configure(text="Ficheiro já existe!", text_color="red")

    else:
        gestor.criar()
        frameante.pack_forget()
        frameno.pack(pady=20, fill="both", expand=True)
        lbltit.configure(text=f"Adicionar cartas a {user}")

def acao_eliminar_lista(newremovli, label_resultrem):
    nome = newremovli.get()
    gestor = GestorFile(nome)
    if gestor.eliminar_arquivo():
        label_resultrem.configure(text="Eliminado!", text_color="green")
    else:
        label_resultrem.configure(text="Não encontrado!", text_color="red")