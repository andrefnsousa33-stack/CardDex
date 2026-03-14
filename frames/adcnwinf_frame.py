import customtkinter
from .base_frame import BaseFrame

class AdcnwinfFrame(BaseFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        filetoedit = getattr(controller, "msn_file", "Desconhecido")
        super().__init__(master, controller, f"Adicionar cartas a {filetoedit}")

        # --- Elementos Visuais ---
        self.entry_nname = customtkinter.CTkEntry(self.conteudo, placeholder_text="Nome...")
        self.entry_nname.pack(pady=20)
        self.entry_nid = customtkinter.CTkEntry(self.conteudo, placeholder_text="ID...")
        self.entry_nid.pack(pady=20)
        customtkinter.CTkButton(self.conteudo, text="Adicionar", command=lambda:self.controller.adicionar_card(self.controller.msn_file, self.entry_nname, self.entry_nid, self.label_resadcnwinf)).pack(pady=5)
        self.label_resadcnwinf = customtkinter.CTkLabel(self.conteudo, text="")
        self.label_resadcnwinf.pack(pady=20)
