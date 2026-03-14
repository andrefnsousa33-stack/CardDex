import os

class GestorFicheiros:
    def __init__(self, nomearquivo):
        self.nomecompleto = f"{nomearquivo}.txt"

    def criar(self):
        with open(self.nomecompleto, "w", encoding="utf-8") as f:
            f.write("Lista de Cartas:\n")
        print(f"Ficheiro {self.nomecompleto} criado!")

    def adicionar(self, nome, telefone):
        with open(self.nomecompleto, "a", encoding="utf-8") as f:
            f.write(f"- {nome}: {telefone}\n")
        print(f"{nome} adicionado com sucesso!")

    def ler_tudo(self):
        try:
            with open(self.nomecompleto, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Erro: Ficheiro não encontrado."

    def eliminar_arquivo(self):
        if os.path.exists(self.nomecompleto):
            os.remove(self.nomecompleto)
            return True
        return False


def acao_ver_lista(ver_nome, label_resultadover):
    nome = ver_nome.get()
    gestor = GestorFicheiros(nome)
    conteudo = gestor.ler_tudo()
    label_resultadover.configure(text=conteudo, text_color="white")

def acao_adicionar_existente(ver_nomee, newnome, newtipo, label_resultadadcex):
    nome_fich = ver_nomee.get()
    nome_carta = newnome.get()
    tipo_carta = newtipo.get()
    
    gestor = GestorFicheiros(nome_fich)
    gestor.adicionar(nome_carta, tipo_carta)
    label_resultadadcex.configure(text=f"{nome_carta} adicionado!", text_color="green")

def acao_eliminar_lista(newremovli, label_resultrem):
    nome = newremovli.get()
    gestor = GestorFicheiros(nome)
    if gestor.eliminar_arquivo():
        label_resultrem.configure(text="Eliminado!", text_color="green")
    else:
        label_resultrem.configure(text="Não encontrado!", text_color="red")