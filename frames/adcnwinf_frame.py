import customtkinter

class AdcnwinfFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---
        filetoedit = getattr(self.controller, "msn_file", "")
        self.label_adcnwtit = customtkinter.CTkLabel(self, text=f"Adicionar Cartas a {filetoedit}")
        self.label_adcnwtit.pack(pady=20)
        self.entry_nname = customtkinter.CTkEntry(self, placeholder_text="Nome...")
        self.entry_nname.pack(pady=20)
        self.entry_nid = customtkinter.CTkEntry(self, placeholder_text="ID...")
        self.entry_nid.pack(pady=20)
        customtkinter.CTkButton(self, text="Adicionar", command=lambda:self.controller.adicionar_card(self.controller.msn_file, self.entry_nname, self.entry_nid, self.label_resadcnwinf)).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_resadcnwinf = customtkinter.CTkLabel(self, text="")
        self.label_resadcnwinf.pack(pady=20)
