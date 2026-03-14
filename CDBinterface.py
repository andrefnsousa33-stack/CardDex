import customtkinter
import CDBlogic
import frames


class AppCDB(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("CardDex Beta v1.1.1 stable")
        self.gestor = None

        self.paginas = {
            "menu": frames.MenuFrame,
            "ver": frames.VerFrame,
            "adc": frames.AdcFrame,
            "adcex": frames.AdcexFrame,
            "adcexinf": frames.AdcexinfFrame,
            "adcnw": frames.AdcnwFrame,
            "adcnwinf": frames.AdcnwinfFrame,
            "remov": frames.RemovFrame,
            "removlist": frames.RemovlistFrame,
            "removct": frames.RemovctFrame,
            "removctinf": frames.RemovctinfFrame,
        }

        self.container_frame = customtkinter.CTkFrame(self)
        self.container_frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.frame_atual = None
        self.trocar_frame("menu")

    def configurar_gestor(self, nome_lista):
        self.gestor = CDBlogic.GestorTabelas(nome_lista)
        print(f"--- DEBUG: A ACEDER AO FICHEIRO: {nome_lista}.db ---")

    def trocar_frame(self, nome_do_frame):
        if self.frame_atual is not None:
            self.frame_atual.destroy()
        classe_frame = self.paginas.get(nome_do_frame)
        if classe_frame:
            self.frame_atual = classe_frame(self.container_frame, self)
            self.frame_atual.pack(fill="both", expand=True)

    def verif_file_trocar_frame(self, label_resver, entryfi, nextframe, acaobool):
        nome_fich = entryfi.get().strip()
        if not nome_fich:
            label_resver.configure(text="Escreve um nome!", text_color="red")
            return
        self.configurar_gestor(nome_fich)
        conteudo = self.gestor.verificar_existencia()
        if conteudo == True and acaobool == True:
            self.trocar_frame(nextframe)
            self.msn_file = nome_fich
        elif conteudo == True and acaobool == False:
            self.trocar_frame(nextframe)
            self.msn_file = nome_fich
        else:
            label_resver.configure(text=f"O ficheiro {nome_fich} nao existe!", text_color="white")

    def mostrar_menu(self):
        self.trocar_frame("menu")

    def executar_leitura(self, label_res, entry):
        nome_fich = entry.get().strip()
        if not nome_fich:
            label_res.configure(text="Escreve um nome!", text_color="red")
            return
        label_res.configure(text="") 
        self.configurar_gestor(nome_fich)
        if self.gestor.verificar_existencia():
            conteudo = self.gestor.ler_tudo()
            label_res.configure(text=conteudo, text_color="white")
        else:
            label_res.configure(text=f"O ficheiro {nome_fich} não existe", text_color="red")

    def adicionar_card(self, filetoedit, name, tel, label_res):
        fileedit = filetoedit.strip() if isinstance(filetoedit, str) else filetoedit.get().strip()
        newname = name.get().strip()
        newtel = tel.get().strip()
        if not newname and not newtel:
            label_res.configure(text="Escreve um nome e um ID!", text_color="red")
        elif not newname:
            label_res.configure(text="Escreve um nome!", text_color="red")
        elif not newtel:
            label_res.configure(text="Escreve um ID!", text_color="red")
        else:
            self.configurar_gestor(fileedit)
            self.gestor.adicionar_carta(newname, newtel)
            label_res.configure(text="Carta adicionada!", text_color="green")
            name.delete(0, 'end')
            tel.delete(0, 'end')

    def criar_file(self, listacriar, nextframe, lblres):
        lista = listacriar.strip()if isinstance(listacriar, str) else listacriar.get().strip()
        self.configurar_gestor(lista)
        existe = self.gestor.verificar_existencia()
        if existe == True:
            lblres.configure(text="Ficheiro já existe!", text_color="red")
        else:
            self.gestor.criar_tabela()
            self.msn_file = lista
            self.trocar_frame(nextframe)

    def remov_lista(self, listaremov, label_res):
        lista = listaremov.get().strip()
        if not lista:
            label_res.configure(text="Escreve o nome da lista!", text_color="yellow")
            return
        self.configurar_gestor(lista)
        if self.gestor.eliminar_ficheiro_lista(): 
            label_res.configure(text="Tabela eliminada!", text_color="green")
        else:
            label_res.configure(text="Erro ao eliminar!", text_color="red")

    def remov_card(self, filetoedit, name, tel, label_res):
        fileedit = filetoedit.strip() if isinstance(filetoedit, str) else filetoedit.get().strip()
        newname = name.get().strip()
        newtel = tel.get().strip()
        if not newname and not newtel:
            label_res.configure(text="Escreve um nome ou um ID!", text_color="red")
        else:
            self.configurar_gestor(fileedit)
            conteudo = self.gestor.remover_carta(newname, newtel)
            label_res.configure(text=conteudo, text_color="red")
            name.delete(0, 'end')
            tel.delete(0, 'end')