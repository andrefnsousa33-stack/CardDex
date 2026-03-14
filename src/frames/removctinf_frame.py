import customtkinter
from .base_frame import BaseFrame

class RemovctinfFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        filetoedit = getattr(controller, "msn_file", "Desconhecido")
        super().__init__(master, controller, f"Remover cartas de {filetoedit}")

        customtkinter.CTkLabel(self.conteudo, text="Insere um nome ou um ID", font=("Arial", 18)).pack(pady=10)
        self.rem_name = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome...")
        self.rem_name.pack(pady=20)
        self.rem_id = customtkinter.CTkEntry(self.conteudo, placeholder_text="ID...")
        self.rem_id.pack(pady=20)
        customtkinter.CTkButton(self.conteudo, text="Remover", command=lambda:self.controller.remov_card(self.controller.msn_file, self.rem_name, self.rem_id, self.label_resremfi)).pack(pady=5)
        self.label_resremfi = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_resremfi.pack(pady=20)
