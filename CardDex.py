import customtkinter
import CardDexTools

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Gestor de Cartas")

titulo = customtkinter.CTkLabel(app, text="MENU", font=("Arial", 18))
titulo.pack(pady=5)

menu = customtkinter.CTkFrame(app)
menu.pack(pady=10, padx=10)

frame_criar = customtkinter.CTkFrame(app, fg_color="transparent")
label_c = customtkinter.CTkLabel(frame_criar, text="MENU DE CRIAÇÃO", font=("Arial", 16, "bold"))
label_c.pack(pady=10)
entry_nome = customtkinter.CTkEntry(frame_criar, placeholder_text="Nome da lista...")
entry_nome.pack(pady=10)
botao = customtkinter.CTkButton(frame_criar, text="Criar Lista", command=lambda:CardDexTools.executar_criacao(entry_nome, label_resultado))
botao.pack(pady=10)
label_resultado = customtkinter.CTkLabel(frame_criar, text="")
label_resultado.pack(pady=10)


frame_ver = customtkinter.CTkFrame(app, fg_color="transparent")
label_v = customtkinter.CTkLabel(frame_ver, text="LISTA DE AMIGOS", font=("Arial", 16, "bold"))
label_v.pack(pady=10)
bibliover = customtkinter.CTkEntry(frame_ver, placeholder_text="Nome do ficheiro...")
bibliover.pack(pady=10)
botaover = customtkinter.CTkButton(frame_ver, text="Ver ficheiro", command=lambda:CardDexTools.ver_ficheiro(bibliover, labeltexto))
botaover.pack(pady=10)
labeltexto = customtkinter.CTkLabel(frame_ver, text="")
labeltexto.pack(pady=10)

btn_c = customtkinter.CTkButton(menu, text="Criar", fg_color="#2e4bcc", hover_color="#29badf", command=lambda:CardDexTools.mostrar_criar(frame_ver, frame_criar))
btn_c.pack(side="left", pady=10, padx=5)
btn_v = customtkinter.CTkButton(menu, text="Ver", fg_color="#2e4bcc", hover_color="#29badf", command=lambda:CardDexTools.mostrar_ver(frame_criar, frame_ver))
btn_v.pack(side="right", pady=10, padx=5)

app.mainloop()