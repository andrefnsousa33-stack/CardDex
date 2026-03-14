import customtkinter

class AdcexFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        # O 'master' é onde este frame vai ser "colado" (o container da App)
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elementos Visuais ---


        customtkinter.CTkLabel(self, text="ADICIONAR A LISTA", font=("Arial", 18)).pack(pady=10)
        self.entry_filetoadd = customtkinter.CTkEntry(self, placeholder_text="Nome da lista...")
        self.entry_filetoadd.pack(pady=10)
        customtkinter.CTkButton(self, text="Carregar", 
                                command=lambda:self.controller.verif_file_trocar_frame(self.label_adcex, self.entry_filetoadd, "adcexinf", True)
                                ).pack(pady=5)
        customtkinter.CTkButton(self, text="Voltar", command=lambda:self.controller.mostrar_menu()).pack(pady=5)
        self.label_adcex = customtkinter.CTkLabel(self, text="")
        self.label_adcex.pack(pady=20)
