import os

class GestorFile:
    def __init__(self, nomearquivo):
        self.nomecompleto = f"{nomearquivo}.txt"

    def ler_tudo(self):
        try:
            with open(self.nomecompleto, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Erro: Ficheiro não encontrado."
        
    def verif(self):
        try:
            with open(self.nomecompleto, "r", encoding="utf-8") as f:
                return True
        except FileNotFoundError:
            return False
        
    def adicionar(self, nome, telefone):
        with open(self.nomecompleto, "a", encoding="utf-8") as f:
            f.write(f"- {nome}: {telefone}\n")
        print(f"{nome} adicionado com sucesso!")

    def criar(self):
        with open(self.nomecompleto, "w", encoding="utf-8") as f:
            f.write("Lista de Cartas:\n")
        print(f"Ficheiro {self.nomecompleto} criado!")

    def eliminar_arquivo(self):
        if os.path.exists(self.nomecompleto):
            os.remove(self.nomecompleto)
            return True
        return False
    
    def remover_car(self, nome):
        linhas_vivas = []
        encontrado = False
        with open(self.nomecompleto, "r", encoding="utf-8") as f:
            for linha in f:
                if nome.lower() not in linha.lower():
                    linhas_vivas.append(linha)
                else:
                    encontrado = True
        
        with open(self.nomecompleto, "w", encoding="utf-8") as f:
            f.writelines(linhas_vivas)
            
            if encontrado:
                print(f"A carta {nome} foi removida.")
            else:
                print("Nome não encontrado.")