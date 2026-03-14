import CardDexTools

decisao = input("Criar/Eliminar uma lista (C)\nAdicionar/Remover cartas de uma lista existente (A)\nVer uma lista (V) \nEscreva algo sem ser as opçoes para sair:").strip().lower()
if decisao.lower() == "c":
    decc = input("Criar (C)\nEliminar (E) ").strip().lower()
    if decc.lower() == "c":
        CardDexTools.criar_file()
    if decc.lower() == "e":
        CardDexTools.elim_file()

elif decisao.lower() == "a":
    filetoedit = input("Qual a lista que queres editar: ").strip().lower()
    CardDexTools.verif_file(filetoedit)
    deca = input("Adicionar (A)\nRemover (R) ")
    if deca.lower() == "a":
       CardDexTools.add_nomes(filetoedit)
    if deca.lower() == "r":
       carta = input("Qual o nome da carta que queres eliminar: ").strip().lower()
       CardDexTools.remover_carta(filetoedit, carta)

elif decisao.lower() == "v":
    filetosee = input("Qual o nome da lista que queres ver: ").strip().lower()
    CardDexTools.ver_ficheiro(filetosee)

else:
    print("Obrigado!")