import customtkinter

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        customtkinter.CTkLabel(self, text="CARDDEX MENU", font=("Arial", 22, "bold")).pack(pady=20)

        customtkinter.CTkButton(self, text="Ver Coleção", command=lambda: self.controller.trocar_frame("ver")).pack(pady=10)
        customtkinter.CTkButton(self, text="Adicionar Cartas", command=lambda: self.controller.trocar_frame("adc")).pack(pady=10)        
        customtkinter.CTkButton(self, text="Remover", command=lambda: self.controller.trocar_frame("remov")).pack(pady=10)
        

