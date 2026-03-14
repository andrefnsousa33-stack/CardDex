import customtkinter
from .base_frame import BaseFrame

class RemovctFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "REMOVER CARTAS")

        # --- Elementos Visuais ---

        self.entry_lstrem = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome da lista...")
        self.entry_lstrem.pack(pady=10)
        customtkinter.CTkButton(self.conteudo, text="Selecionar lista", command=lambda:self.controller.verif_file_trocar_frame(self.label_resr, self.entry_lstrem, "removctinf", False)).pack(pady=5)
        self.label_resr = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_resr.pack(pady=20)