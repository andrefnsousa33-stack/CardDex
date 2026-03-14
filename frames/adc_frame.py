import customtkinter

class AdcFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---

        customtkinter.CTkLabel(self, text="ADICIONAR A LISTA", font=("Arial", 18)).pack(pady=10)
        customtkinter.CTkButton(self, text="Nova", command=lambda:self.controller.trocar_frame("adcnw")).pack(pady=5)
        customtkinter.CTkButton(self, text="Existente", command=lambda:self.controller.trocar_frame("adcex")).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)