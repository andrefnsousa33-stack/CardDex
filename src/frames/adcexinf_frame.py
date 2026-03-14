import customtkinter
from .base_frame import BaseFrame

class AdcexinfFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        filetoedit = getattr(controller, "msn_file", "Desconhecido")
        super().__init__(master, controller, f"Adicionar cartas a {filetoedit}")

        # --- Elementos Visuais ---

        self.entry_name = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome...")
        self.entry_name.pack(pady=20)
        self.entry_id = customtkinter.CTkEntry(self.conteudo, placeholder_text="ID...")
        self.entry_id.pack(pady=20)
        customtkinter.CTkButton(self.conteudo, text="Adicionar", command=lambda:self.controller.adicionar_card(self.controller.msn_file, self.entry_name, self.entry_id, self.label_resadc)).pack(pady=5)
        self.label_resadc = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_resadc.pack(pady=20)