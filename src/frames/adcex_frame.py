import customtkinter
from .base_frame import BaseFrame

class AdcexFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "ADICIONAR A LISTA")
        self.controller = controller

        # --- Elementos Visuais ---

        self.entry_filetoadd = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome da lista...")
        self.entry_filetoadd.pack(pady=10)
        customtkinter.CTkButton(self.conteudo, text="Carregar", command=lambda:self.controller.verif_file_trocar_frame(self.label_adcex, self.entry_filetoadd, "adcexinf", True)).pack(pady=5)
        self.label_adcex = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_adcex.pack(pady=20)
