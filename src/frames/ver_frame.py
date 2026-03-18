import customtkinter
from .base_frame import BaseFrame

class VerFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "VER CARTAS")

        # --- Elementos Visuais ---
        self.entry_ficheiro = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome da lista...")
        self.entry_ficheiro.pack(pady=10)
        customtkinter.CTkButton(self.conteudo, text="Carregar", command=lambda: self.controller.executar_leitura(self.label_ver, self.entry_ficheiro)).pack(pady=5)
        self.label_ver = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_ver.pack(pady=20)