import CardDexTools

while True:
    decisao = input("Criar/Eliminar uma biblioteca (C)\nAdicionar/Remover amigos de uma biblioteca existente (A)\nVer uma biblioteca (V) \nSair (S)\n").strip().lower()
    if decisao.lower() == "c":
        decc = input("Criar (C)\nEliminar (E) ").strip().lower()
        if decc.lower() == "c":
             CardDexTools.criar_file()
        if decc.lower() == "e":
            CardDexTools.elim_file()

    elif decisao.lower() == "a":
        filetoedit = input("Qual o ficheiro que queres editar: ").strip().lower()
        CardDexTools.verif_file(filetoedit)
        deca = input("Adicionar (A)\nRemover (R) ").strip().lower()
        if deca.lower() == "a":
            CardDexTools.add_nomes(filetoedit)
        if deca.lower() == "r":
            carta = input("Qual o nome que queres eliminar: ").strip().lower()
            CardDexTools.remover_carta(filetoedit, carta)

    elif decisao.lower() == "v":
        filetosee = input("Qual o ficheiro que queres ver: ").strip().lower()
        CardDexTools.ver_ficheiro(filetosee)

    elif decisao.lower() == "s":
        print("Obrigado!")
        break

    else:
        print("Comando nao valido!")