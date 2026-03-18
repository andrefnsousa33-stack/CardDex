import customtkinter
from .base_frame import BaseFrame

class RemovlistFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "REMOVER LISTA")

        self.entry_listaremov = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome da lista...")
        self.entry_listaremov.pack(pady=10)
        customtkinter.CTkButton(self.conteudo, text="Remover", command=lambda:self.controller.remov_lista(self.entry_listaremov, self.label_resrem)).pack(pady=5)
        self.label_resrem = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_resrem.pack(pady=20)
