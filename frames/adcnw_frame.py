import customtkinter

class AdcnwFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---

        customtkinter.CTkLabel(self, text="ADICIONAR LISTA", font=("Arial", 18)).pack(pady=10)
        self.entry_listanova = customtkinter.CTkEntry(self, placeholder_text="Nome da lista...")
        self.entry_listanova.pack(pady=10)
        customtkinter.CTkButton(self, text="Criar lista", command=lambda:self.controller.criar_file(self.entry_listanova, "adcnwinf", self.label_resadcnw)).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_resadcnw = customtkinter.CTkLabel(self, text="")
        self.label_resadcnw.pack(pady=20)
