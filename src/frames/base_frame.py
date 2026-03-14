import customtkinter

class BaseFrame(customtkinter.CTkFrame):
    def __init__(self, master, controller, titulo_texto):
        super().__init__(master, fg_color="transparent")
        self.controller = controller

        # --- Elemento Comum: Título ---
        self.titulo = customtkinter.CTkLabel(self, text=titulo_texto, font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)

        # --- O Contentor para o conteúdo específico ---
        # Criamos um frame interno onde cada ecrã vai desenhar as suas coisas
        self.conteudo = customtkinter.CTkFrame(self, fg_color="transparent")
        self.conteudo.pack(fill="both", expand=True)

        # --- Elemento Comum: Botão Voltar (Sempre no fim) ---
        self.btn_voltar = customtkinter.CTkButton(self, text="Voltar ao Menu", command=self.controller.mostrar_menu)
        self.btn_voltar.pack(pady=20, side="bottom")
