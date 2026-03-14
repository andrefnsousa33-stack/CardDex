import customtkinter

class VerFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---
        customtkinter.CTkLabel(self, text="VER CARTAS", font=("Arial", 22, "bold")).pack(pady=20)
        self.entry_ficheiro = customtkinter.CTkEntry(self, placeholder_text="Nome da lista...")
        self.entry_ficheiro.pack(pady=10)
        customtkinter.CTkButton(self, text="Carregar", command=lambda: self.controller.executar_leitura(self.label_ver, self.entry_ficheiro)).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda: self.controller.mostrar_menu()).pack(pady=5)
        self.label_ver = customtkinter.CTkLabel(self, text="")
        self.label_ver.pack(pady=20)