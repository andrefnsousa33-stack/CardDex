import customtkinter

class AdcexinfFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---
        filetoedit = getattr(self.controller, "msn_file", "")
        self.label_adctit = customtkinter.CTkLabel(self, text=f"Adicionar cartas a {filetoedit}")
        self.label_adctit.pack(pady=20)
        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Nome...")
        self.entry_name.pack(pady=20)
        self.entry_id = customtkinter.CTkEntry(self, placeholder_text="ID...")
        self.entry_id.pack(pady=20)
        customtkinter.CTkButton(self, text="Adicionar", command=lambda:self.controller.adicionar_card(self.controller.msn_file, self.entry_name, self.entry_id, self.label_resadc)).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_resadc = customtkinter.CTkLabel(self, text="")
        self.label_resadc.pack(pady=20)