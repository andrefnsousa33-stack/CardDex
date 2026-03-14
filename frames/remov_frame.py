import customtkinter

class RemovFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---

        customtkinter.CTkLabel(self, text="REMOVER", font=("Arial", 18)).pack(pady=10)
        customtkinter.CTkButton(self, text="Lista", command=lambda:self.controller.trocar_frame("removlist")).pack(pady=5)
        customtkinter.CTkButton(self, text="Cartas", command=lambda:self.controller.trocar_frame("removct")).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)