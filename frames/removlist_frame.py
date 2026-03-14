import customtkinter

class RemovlistFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        customtkinter.CTkLabel(self, text="REMOVER LISTA", font=("Arial", 18)).pack(pady=10)
        self.entry_listaremov = customtkinter.CTkEntry(self, placeholder_text="Nome da lista...")
        self.entry_listaremov.pack(pady=10)
        customtkinter.CTkButton(self, text="Remover", command=lambda:self.controller.remov_lista(self.entry_listaremov, self.label_resrem)).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_resrem = customtkinter.CTkLabel(self, text="")
        self.label_resrem.pack(pady=20)
