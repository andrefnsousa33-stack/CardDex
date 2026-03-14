import customtkinter
from .base_frame import BaseFrame

class RemovFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, controller, "REMOVER")
        self.controller = controller

        # --- Elementos Visuais ---

        customtkinter.CTkButton(self.conteudo, text="Lista", command=lambda:self.controller.trocar_frame("removlist")).pack(pady=5)
        customtkinter.CTkButton(self.conteudo, text="Cartas", command=lambda:self.controller.trocar_frame("removct")).pack(pady=5)