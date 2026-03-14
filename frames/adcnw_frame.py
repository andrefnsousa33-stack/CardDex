import customtkinter
from .base_frame import BaseFrame

class AdcnwFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "ADICIONAR LISTA")

        # --- Elementos Visuais ---

        self.entry_listanova = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome da lista...")
        self.entry_listanova.pack(pady=10)
        customtkinter.CTkButton(self.conteudo, text="Criar lista", command=lambda:self.controller.criar_file(self.entry_listanova, "adcnwinf", self.label_resadcnw)).pack(pady=5)
        self.label_resadcnw = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_resadcnw.pack(pady=20)
