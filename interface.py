import customtkinter
from logic import GestorFile


class AppContactos(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("CardDex v1.1.1 stable")

        # Frames (Contentores)
        self.frame_atual = None
        self.frame_menu = customtkinter.CTkFrame(self)
        self.frame_ver = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_adc = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_adcex = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_adcexinf = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_adcnw = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_adcnwinf = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_remov = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_removlist = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_removcon = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_removconinf = customtkinter.CTkFrame(self, fg_color="transparent")

        self.desenhar_interface()
        self.abrir_menu()

    def desenhar_interface(self):
        # Menu
        customtkinter.CTkLabel(self.frame_menu, text="MENU", font=("Arial", 20)).pack(pady=10)
        customtkinter.CTkButton(self.frame_menu, text="Ver", command=lambda:self.trocar_frame(self.frame_ver)).pack(pady=5)
        customtkinter.CTkButton(self.frame_menu, text="Adicionar", command=lambda:self.trocar_frame(self.frame_adc)).pack(pady=5)
        customtkinter.CTkButton(self.frame_menu, text="Remover", command=lambda:self.trocar_frame(self.frame_remov)).pack(pady=5)
        
        # Ecrã Ver
        customtkinter.CTkLabel(self.frame_ver, text="VER CARTAS", font=("Arial", 18)).pack(pady=10)
        self.entry_ficheiro = customtkinter.CTkEntry(self.frame_ver, placeholder_text="Nome da lista...")
        self.entry_ficheiro.pack(pady=10)
        customtkinter.CTkButton(self.frame_ver, text="Carregar", command=lambda:self.executar_leitura(self.label_ver, self.entry_ficheiro)).pack(pady=5)
        customtkinter.CTkButton(self.frame_ver, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_ver = customtkinter.CTkLabel(self.frame_ver, text="")
        self.label_ver.pack(pady=20)

        # Ecrã Adicionar
        customtkinter.CTkLabel(self.frame_adc, text="ADICIONAR A LISTA", font=("Arial", 18)).pack(pady=10)
        customtkinter.CTkButton(self.frame_adc, text="Nova", command=lambda:self.trocar_frame(self.frame_adcnw)).pack(pady=5)
        customtkinter.CTkButton(self.frame_adc, text="Existente", command=lambda:self.trocar_frame(self.frame_adcex)).pack(pady=5)
        customtkinter.CTkButton(self.frame_adc, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)

        # Ecrã Adicionar a Existente
        customtkinter.CTkLabel(self.frame_adcex, text="ADICIONAR A LISTA", font=("Arial", 18)).pack(pady=10)
        self.entry_filetoadd = customtkinter.CTkEntry(self.frame_adcex, placeholder_text="Nome da lista...")
        self.entry_filetoadd.pack(pady=10)
        customtkinter.CTkButton(self.frame_adcex, text="Carregar", command=lambda:self.verif_file_trocar_frame(self.label_adcex, self.entry_filetoadd, self.frame_adcexinf, self.label_adctit, True)).pack(pady=5)
        customtkinter.CTkButton(self.frame_adcex, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_adcex = customtkinter.CTkLabel(self.frame_adcex, text="")
        self.label_adcex.pack(pady=20)

        # Ecrã Adicionar Nomes e Tipos a Existente
        self.label_adctit = customtkinter.CTkLabel(self.frame_adcexinf, text="")
        self.label_adctit.pack(pady=20)
        self.entry_name = customtkinter.CTkEntry(self.frame_adcexinf, placeholder_text="Nome...")
        self.entry_name.pack(pady=20)
        self.entry_tel = customtkinter.CTkEntry(self.frame_adcexinf, placeholder_text="Tipo")
        self.entry_tel.pack(pady=20)
        customtkinter.CTkButton(self.frame_adcexinf, text="Adicionar", command=lambda:self.adicionar_contact(self.entry_filetoadd, self.entry_name, self.entry_tel, self.label_resadc)).pack(pady=5)
        customtkinter.CTkButton(self.frame_adcexinf, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_resadc = customtkinter.CTkLabel(self.frame_adcexinf, text="")
        self.label_resadc.pack(pady=20)

        # Ecrã Adicionar a Lista Nova
        customtkinter.CTkLabel(self.frame_adcnw, text="ADICIONAR LISTA", font=("Arial", 18)).pack(pady=10)
        self.entry_listanova = customtkinter.CTkEntry(self.frame_adcnw, placeholder_text="Nome da lista...")
        self.entry_listanova.pack(pady=10)
        customtkinter.CTkButton(self.frame_adcnw, text="Criar lista", command=lambda:self.criar_file(self.entry_listanova, self.frame_adcnwinf, self.label_resadcnw, self.label_adcnwtit)).pack(pady=5)
        customtkinter.CTkButton(self.frame_adcnw, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_resadcnw = customtkinter.CTkLabel(self.frame_adcnw, text="")
        self.label_resadcnw.pack(pady=20)

        # Ecrã Adicionar Contactos a Lista Nova
        self.label_adcnwtit = customtkinter.CTkLabel(self.frame_adcnwinf, text="")
        self.label_adcnwtit.pack(pady=20)
        self.entry_nname = customtkinter.CTkEntry(self.frame_adcnwinf, placeholder_text="Nome...")
        self.entry_nname.pack(pady=20)
        self.entry_ntel = customtkinter.CTkEntry(self.frame_adcnwinf, placeholder_text="Tipo")
        self.entry_ntel.pack(pady=20)
        customtkinter.CTkButton(self.frame_adcnwinf, text="Adicionar", command=lambda:self.adicionar_contact(self.entry_listanova, self.entry_nname, self.entry_ntel, self.label_resadcnwinf)).pack(pady=5)
        customtkinter.CTkButton(self.frame_adcnwinf, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_resadcnwinf = customtkinter.CTkLabel(self.frame_adcnwinf, text="")
        self.label_resadcnwinf.pack(pady=20)

        # Ecrã Remover
        customtkinter.CTkLabel(self.frame_remov, text="REMOVER", font=("Arial", 18)).pack(pady=10)
        customtkinter.CTkButton(self.frame_remov, text="Lista", command=lambda:self.trocar_frame(self.frame_removlist)).pack(pady=5)
        customtkinter.CTkButton(self.frame_remov, text="Cartas", command=lambda:self.trocar_frame(self.frame_removcon)).pack(pady=5)
        customtkinter.CTkButton(self.frame_remov, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)

        # Ecrã Remover Lista
        customtkinter.CTkLabel(self.frame_removlist, text="REMOVER LISTA", font=("Arial", 18)).pack(pady=10)
        self.entry_listaremov = customtkinter.CTkEntry(self.frame_removlist, placeholder_text="Nome da lista...")
        self.entry_listaremov.pack(pady=10)
        customtkinter.CTkButton(self.frame_removlist, text="Remover lista", command=lambda:self.remov_lista(self.entry_listaremov, self.label_resrem)).pack(pady=5)
        customtkinter.CTkButton(self.frame_removlist, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_resrem = customtkinter.CTkLabel(self.frame_removlist, text="")
        self.label_resrem.pack(pady=20)

        # Ecrã Remover Contactos
        customtkinter.CTkLabel(self.frame_removcon, text="REMOVER CARTAS", font=("Arial", 18)).pack(pady=10)
        self.entry_lstrem = customtkinter.CTkEntry(self.frame_removcon, placeholder_text="Nome da lista...")
        self.entry_lstrem.pack(pady=10)
        customtkinter.CTkButton(self.frame_removcon, text="Selecionar lista", command=lambda:self.verif_file_trocar_frame(self.label_resr, self.entry_lstrem, self.frame_removconinf, self.label_remtit, False)).pack(pady=5)
        customtkinter.CTkButton(self.frame_removcon, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_resr = customtkinter.CTkLabel(self.frame_removcon, text="")
        self.label_resr.pack(pady=20)

        # Ecrã Remover Contactos a Existente
        self.label_remtit = customtkinter.CTkLabel(self.frame_removconinf, text="")
        customtkinter.CTkLabel(self.frame_removconinf, text="Insere um nome ou um tipo", font=("Arial", 18)).pack(pady=10)
        self.label_remtit.pack(pady=20)
        self.rem_name = customtkinter.CTkEntry(self.frame_removconinf, placeholder_text="Nome...")
        self.rem_name.pack(pady=20)
        self.rem_tel = customtkinter.CTkEntry(self.frame_removconinf, placeholder_text="Tipo")
        self.rem_tel.pack(pady=20)
        customtkinter.CTkButton(self.frame_removconinf, text="Remover", command=lambda:self.remov_contact(self.entry_lstrem, self.rem_name, self.rem_tel, self.label_resremfi)).pack(pady=5)
        customtkinter.CTkButton(self.frame_removconinf, text="Voltar", command=lambda:self.mostrar_menu()).pack(pady=5)
        self.label_resremfi = customtkinter.CTkLabel(self.frame_removconinf, text="")
        self.label_resremfi.pack(pady=20)

    def abrir_menu(self):
        self.frame_menu.pack(pady=20, padx=20, fill="both", expand=True)
        self.frame_atual = self.frame_menu

    def mostrar_menu(self):
        if self.frame_atual is not None:
            self.frame_atual.pack_forget()  
        self.frame_menu.pack(pady=20, padx=20, fill="both", expand=True)
        self.frame_atual = self.frame_menu

    def trocar_frame(self, novo_frame):
        if self.frame_atual is not None:
            self.frame_atual.pack_forget()  
        novo_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.frame_atual = novo_frame
    
    def remov_lista(self, listaremov, label_res):
        lista = listaremov.get().strip()
        gestor = GestorFile(lista)
        acao = gestor.eliminar_lista()
        if acao == True:
            label_res.configure(text="Ficheiro eliminado!", text_color="green")
        else:
            label_res.configure(text="Ficheiro nao existe!", text_color="red")

    def criar_file(self, listacriar, nextframe, lblres, titnxt):
        lista = listacriar.get().strip()
        gestor = GestorFile(lista)
        existe = gestor.verificar_existencia()
        if existe == True:
            lblres.configure(text="Ficheiro já existe!", text_color="red")
        else:
            gestor.criar()
            self.trocar_frame(nextframe)
            titnxt.configure(text=f"Adicionar cartas a {lista}")

    def remov_contact(self, filetoedit, name, tel, label_res):
        fileedit = filetoedit.get().strip()
        newname = name.get().strip()
        newtel = tel.get().strip()
        if not newname and not newtel:
            label_res.configure(text="Escreve um nome ou um tipo!", text_color="red")
        else:
            gestor = GestorFile(fileedit)
            conteudo = gestor.remover_contact(newname, newtel)
            label_res.configure(text=conteudo, text_color="red")
            name.delete(0, 'end')
            tel.delete(0, 'end')

    def adicionar_contact(self, filetoedit, name, tel, label_res):
        fileedit = filetoedit.get().strip()
        newname = name.get().strip()
        newtel = tel.get().strip()
        if not newname and not newtel:
            label_res.configure(text="Escreve o nome e o tipo!", text_color="red")
        elif not newname:
            label_res.configure(text="Escreve o nome!", text_color="red")
        elif not newtel:
            label_res.configure(text="Escreve o numero!", text_color="red")
        else:
            gestor = GestorFile(fileedit)
            gestor.adicionar_contacto(newname, newtel)
            label_res.configure(text="Carta adicionada!", text_color="green")
            name.delete(0, 'end')
            tel.delete(0, 'end')

    def verif_file_trocar_frame(self, label_resver, entryfi, nextframe, titnxframe, acaobool):
        nome_fich = entryfi.get().strip()
        if not nome_fich:
            label_resver.configure(text="Escreve um nome!", text_color="red")
            return
        gestor = GestorFile(nome_fich)
        conteudo = gestor.verificar_existencia()
        if conteudo == True and acaobool == True:
            self.trocar_frame(nextframe)
            titnxframe.configure(text=f"ADICIONAR A {nome_fich}")
        elif conteudo == True and acaobool == False:
            self.trocar_frame(nextframe)
            titnxframe.configure(text=f"REMOVER DE {nome_fich}")           
        else:
            label_resver.configure(text=f"A lista {nome_fich}.txt nao existe!", text_color="white")

    def executar_leitura(self, label_res, entry):
        nome_fich = entry.get().strip()
        if not nome_fich:
            label_res.configure(text="Escreve um nome!", text_color="red")
            return

        label_res.configure(text="A carregar...") 
        gestor = GestorFile(nome_fich)
        conteudo = gestor.ler_conteudo()
        label_res.configure(text=conteudo, text_color="white")