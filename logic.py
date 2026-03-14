import os

class GestorFile:

    def __init__(self, nome_lista):
        self.caminho = f"{nome_lista}.txt"

    def criar(self):
        with open(self.caminho, "w", encoding="utf-8") as f:
            f.write("Lista de Cartas:\n")

    def verificar_existencia(self):
        return os.path.exists(self.caminho)

    def ler_conteudo(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Erro: Ficheiro não encontrado."

    def adicionar_contacto(self, nome, telefone):
        with open(self.caminho, "a", encoding="utf-8") as f:
            f.write(f"- {nome}: {telefone}\n")

    def eliminar_lista(self):
        if os.path.exists(self.caminho):
            os.remove(self.caminho)
            return True
        return False
    
    def remover_contact(self, nome, tel):
        linhas_vivas = []
        encontradonome = False
        encontradotel = False
        encontradoum = False
        with open(self.caminho, "r", encoding="utf-8") as f:
            for linha in f:
                if nome.lower() in linha.lower() and tel.lower() in linha.lower():
                    encontradoum = True
                elif nome.lower() in linha.lower() and tel.lower() not in linha.lower():
                    encontradonome = True
                elif nome.lower() not in linha.lower() and tel.lower() in linha.lower():
                    encontradotel = True
                else:
                    linhas_vivas.append(linha)
        with open(self.caminho, "w", encoding="utf-8") as f:
            f.writelines(linhas_vivas)
            if encontradoum:
                return f"A carta {nome} com o tipo {tel} foi removida."
            elif encontradonome and encontradotel:
                return f"A carta {nome} e a carta do tipo {tel} foram removidas"
            elif encontradonome and not encontradotel and not tel:
                return f"A carta {nome} foi removida"
            elif encontradonome and not encontradotel and tel:
                return f"A carta {nome} foi removida, mas a carta do tipo {tel} nao foi encontrada."
            elif not encontradonome and encontradotel and not nome:
                return f"A carta do tipo {tel} foi removida"
            elif not encontradonome and encontradotel and nome:
                return f"A carta {tel} foi removida, mas o a carta do tipo {nome} nao foi encontrada"
            elif not encontradonome and not encontradotel and nome and tel:
                return f"A carta {nome} e o carta do tipo {tel} nao foram encontrados"
            elif not encontradonome and not encontradotel and nome and not tel:
                return f"A carta {nome} nao foi encontrada"
            elif not encontradonome and not encontradotel and not nome and tel:
                return f"A carta do tipo {tel} nao foi encontrada"
            else:
                return "Erro!"