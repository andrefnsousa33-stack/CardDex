import CardDexTools
import os


listac = {}
listae = {}

decisao = input("Criar/Eliminar uma lista (C)\nAdicionar/Remover cartas de uma lista existente (A)\nVer uma lista (V) \nEscreva algo sem ser as opçoes para sair:")
if decisao.lower() == "c":
   decc = input("Criar (C)\nEliminar (E) ").strip().lower()
   if decc.lower() == "c":
      usercname = input("Qual o nome da lista que queres criar: ").strip().lower()
      if os.path.exists(f"{usercname}.txt"):
         print("O ficheiro já existe!")
      else:
         while True:
            cartaum = input("Nome da carta:(ou escreve sair quando acabares): ").strip().lower()
            if cartaum == "sair":
               break
            else:
               tipoum = input(f"Tipo de {cartaum.capitalize()}: ").strip().lower()
               listac[cartaum] = tipoum
         with open(f"{usercname}.txt", "w", encoding="utf-8") as fileuser:
            fileuser.write(f"Lista {usercname.capitalize()}:\n")
            for nome, tipo in listac.items():
               fileuser.write(f"- {nome}: {tipo}\n")
            print("Lista criada com sucesso!")

   elif decc.lower() == "e":
      userename = input("Qual o nome do ficheiro que queres eliminar: ").strip().lower()
      if os.path.exists(f"{userename}.txt"):
         os.remove(f"{userename}.txt")
         print(f"O ficheiro {userename} foi eliminado!")
      else:
         print("O ficheiro não foi encontrado.")

elif decisao.lower() == "a":
   filetoedit = input("Qual a lista que queres editar: ").strip().lower()
   try:
      with open(f"{filetoedit}.txt", "r", encoding="utf-8") as fileuser:
         pass
      deca = input("Adicionar (A)\nRemover (R) ").strip().lower()
      if deca.lower() == "a":
         while True:
            cartadois = input("Nome da carta:(ou escreve sair quando acabares): ").strip().lower()
            if cartadois == "sair":
               break
            else:
               tipodois = input(f"Tipo de {cartadois.capitalize()}: ").strip().lower()
               listae[cartadois] = tipodois
         with open(f"{filetoedit}.txt", "a", encoding="utf-8") as fileuser:
            for nome, tipo in listae.items():
               fileuser.write(f"- {nome}: {tipo}\n")
            print("Nomes adicionados com sucesso!")
      if deca.lower() == "r":
         cartael = input("Qual o nome da carta que queres eliminar: ").strip().lower()
         CardDexTools.remover_carta(filetoedit, cartael)
   except FileNotFoundError:
      print("O ficheiro ainda não existe.")

elif decisao.lower() == "v":
   filetosee = input("Qual o nome da lista que queres ver: ").strip().lower()
   try:
      with open(f"{filetosee}.txt", "r", encoding="utf-8") as fileuser:
         conteudo = fileuser.read()
         print("--- Conteúdo do Ficheiro ---")
         print(conteudo)
   except FileNotFoundError:
      print("O ficheiro ainda não existe.")

else:
   print("Obrigado!")