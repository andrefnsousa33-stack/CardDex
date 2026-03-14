import customtkinter

class RemovctinfFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        filetoedit = getattr(self.controller, "msn_file", "")
        self.label_remtit = customtkinter.CTkLabel(self, text=f"Remover cartas de {filetoedit}")
        customtkinter.CTkLabel(self, text="Insere um nome ou um ID", font=("Arial", 18)).pack(pady=10)
        self.label_remtit.pack(pady=20)
        self.rem_name = customtkinter.CTkEntry(self, placeholder_text="Nome...")
        self.rem_name.pack(pady=20)
        self.rem_id = customtkinter.CTkEntry(self, placeholder_text="ID...")
        self.rem_id.pack(pady=20)
        customtkinter.CTkButton(self, text="Remover", command=lambda:self.controller.remov_card(self.controller.msn_file, self.rem_name, self.rem_id, self.label_resremfi)).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_resremfi = customtkinter.CTkLabel(self, text="")
        self.label_resremfi.pack(pady=20)
