import customtkinter
from .base_frame import BaseFrame

class AdcFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "ADICIONAR A LISTA")
        self.controller = controller

        # --- Elementos Visuais ---
        self.btn_nova = customtkinter.CTkButton(self.conteudo, text="Nova Lista", command=lambda: self.controller.trocar_frame("adcnw"))
        self.btn_nova.pack(pady=10)

        self.btn_existente = customtkinter.CTkButton(self.conteudo, text="Lista Existente", command=lambda: self.controller.trocar_frame("adcex"))
        self.btn_existente.pack(pady=10)