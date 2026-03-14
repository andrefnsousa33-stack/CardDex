import customtkinter

class RemovctFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---

        customtkinter.CTkLabel(self, text="REMOVER CARTAS", font=("Arial", 18)).pack(pady=10)
        self.entry_lstrem = customtkinter.CTkEntry(self, placeholder_text="Nome da lista...")
        self.entry_lstrem.pack(pady=10)
        customtkinter.CTkButton(self, text="Selecionar lista",
                                 command=lambda:self.controller.verif_file_trocar_frame(self.label_resr, self.entry_lstrem, "removctinf", False)
                                 ).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_resr = customtkinter.CTkLabel(self, text="")
        self.label_resr.pack(pady=20)