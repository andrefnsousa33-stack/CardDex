listac = {}
listae = {}

decisao = input("Queres criar uma lista(W), adicionar uma carta a uma lista existente(A) ou ver uma lista(R): ")
if decisao.lower() == "w":
    nomelistac_entry = input("Qual o nome da lista que queres criar: ").strip().lower()
    while True:
       nomecc_entry = input("Nome da carta(escreve sair quando acabares): ").strip().lower()
       if nomecc_entry == "sair":
          break
       else:
          tipocc_entry = input(f"Qual o tipo de {nomecc_entry.capitalize()}: ").strip().lower()
          listac[nomecc_entry] = tipocc_entry
    with open(f"{nomelistac_entry}.txt", "w", encoding="utf-8") as fileuser:
       fileuser.write("Lista de Cartas:\n")
       for nome, tipo in listac.items():
          fileuser.write(f"- {nome}: {tipo}\n")
       print("Ficheiro criado com sucesso!")

elif decisao.lower() == "a":
    nomelistae_entry = input("Qual a lista que queres editar: ").strip().lower()
    try:
         with open(f"{nomelistae_entry}.txt", "r", encoding="utf-8") as fileuser:
            pass
         while True:
            nomece_entry = input("Nome da carta(escreve sair quando acabares): ").strip().lower()
            if nomece_entry.lower() == "sair":
               break
            else:
               tipoce_entry = input(f"Qual o tipo de {nomece_entry.capitalize()}: ").strip().lower()
               listae[nomece_entry] = tipoce_entry
         with open(f"{nomelistae_entry}.txt", "a", encoding="utf-8") as fileuser:
            for nome, tipo in listae.items():
               fileuser.write(f"- {nome}: {tipo}\n")
            print("Cartas adicionadas com sucesso!")
        
    except FileNotFoundError:
        print("A lista ainda não existe.")

elif decisao.lower() == "r":
    nomelistav_entry = input("Qual o nome da lista que queres ver: ").strip().lower()
    try:
       with open(f"{nomelistav_entry}.txt", "r", encoding="utf-8") as fileuser:
        conteudo = fileuser.read()
        print("--- Conteúdo do Ficheiro ---")
        print(conteudo)
    except FileNotFoundError:
        print("A lista ainda não existe.")

elif decisao.lower() == "sair":
   exit()

else:
   print("Comando não válido!")