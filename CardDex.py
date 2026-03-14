import customtkinter
import CardDexTools
import CardDexTools2
from CardDexTools2 import GestorFicheiros

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Janelas Amarelas")


#frame menu
menu_frame = customtkinter.CTkFrame(app)
menu_frame.pack(pady=10, padx=10)
titulomenu = customtkinter.CTkLabel(menu_frame, text="Menu", font=("Arial", 18))
titulomenu.pack(pady=5)
btnver = customtkinter.CTkButton(menu_frame, text="Ver", fg_color="#2e4bcc", hover_color="#29badf", command=lambda:CardDexTools.mostrar_ver(menu_frame, frame_ver))
btnver.pack(side="left", pady=10, padx=5)
btnadc = customtkinter.CTkButton(menu_frame, text="Adicionar", fg_color="#2e4bcc", hover_color="#29badf", command=lambda:CardDexTools.mostrar_ver(menu_frame, frame_adic))
btnadc.pack(side="top", pady=10, padx=5)
btnrem = customtkinter.CTkButton(menu_frame, text="Remover", fg_color="#2e4bcc", hover_color="#29badf", command=lambda:CardDexTools.mostrar_ver(menu_frame, frame_remov))
btnrem.pack(side="right", pady=10, padx=5)

#frame ver
frame_ver = customtkinter.CTkFrame(app, fg_color="transparent")
label_ver = customtkinter.CTkLabel(frame_ver, text="Lista de cartas", font=("Arial", 16, "bold"))
label_ver.pack(pady=10)
ver_nome = customtkinter.CTkEntry(frame_ver, placeholder_text="Nome da Lista...")
ver_nome.pack(pady=10)
botaover = customtkinter.CTkButton(frame_ver, text="Ver lista", command=lambda:CardDexTools2.acao_ver_lista(ver_nome, label_resultadover))
botaover.pack(pady=10)
label_resultadover = customtkinter.CTkLabel(frame_ver, text="")
label_resultadover.pack(pady=10)

#frame adicionar
frame_adic = customtkinter.CTkFrame(app,fg_color="transparent")
label_adc = customtkinter.CTkLabel(frame_adic, text="Adicionar cartas", font=("Arial", 16, "bold"))
label_adc.pack(pady=10)
btnadcex = customtkinter.CTkButton(frame_adic, text="Lista Existente", command=lambda:CardDexTools.mostrar_ver(frame_adic, frame_adicex))
btnadcex.pack(side="left", pady=10)
btnadcnw = customtkinter.CTkButton(frame_adic, text="Lista Nova", command=lambda:CardDexTools.mostrar_ver(frame_adic, frame_adicnov))
btnadcnw.pack(side="right", pady=10)

#frame adicionar a existente
frame_adicex = customtkinter.CTkFrame(app, fg_color="transparent")
label_adcex = customtkinter.CTkLabel(frame_adicex, text="Adicionar cartas", font=("Arial", 16, "bold"))
label_adcex.pack(pady=10)
ver_nomee = customtkinter.CTkEntry(frame_adicex, placeholder_text="Nome da Lista...")
ver_nomee.pack(pady=10)
btnadclist = customtkinter.CTkButton(frame_adicex, text="Ver lista", command=lambda:CardDexTools.verif_file(ver_nomee, label_res, frame_adicex, frame_adicexname, label_adcexname))
btnadclist.pack(pady=10)
label_res = customtkinter.CTkLabel(frame_adicex, text="")
label_res.pack(pady=10)

#frame adicioran nomes e telemoveis a existente
frame_adicexname = customtkinter.CTkFrame(app, fg_color="transparent")
label_adcexname = customtkinter.CTkLabel(frame_adicexname, text=f"Adicionar cartas a ...", font=("Arial", 16, "bold"))
label_adcexname.pack(pady=10)
newnome = customtkinter.CTkEntry(frame_adicexname, placeholder_text="Nome")
newnome.pack(side="left", pady=10)
newtef = customtkinter.CTkEntry(frame_adicexname, placeholder_text="Tipo")
newtef.pack(side="right", pady=10)
btnadcnomeex = customtkinter.CTkButton(frame_adicexname, text="Adicionar", command=lambda:CardDexTools2.acao_adicionar_existente(ver_nomee, newnome, newtef, label_resultadadcex))
btnadcnomeex.pack(pady=10)
label_resultadadcex = customtkinter.CTkLabel(frame_adicexname, text="")
label_resultadadcex.pack(pady=10)

#frame adicionar numeros a lista nova
frame_adicnov = customtkinter.CTkFrame(app, fg_color="transparent")
label_adcnova = customtkinter.CTkLabel(frame_adicnov, text=f"Adicionar cartas", font=("Arial", 16, "bold"))
label_adcnova.pack(pady=10)
newadclis = customtkinter.CTkEntry(frame_adicnov, placeholder_text="Nome da Lista Nova...")
newadclis.pack(pady=10)
btnadcnova = customtkinter.CTkButton(frame_adicnov, text="Criar Lista", command=lambda:CardDexTools.criar_file(newadclis, frame_adicnov, frame_adcnometel, label_adcnometel))
btnadcnova.pack(pady=10)
label_resultadadcn = customtkinter.CTkLabel(frame_adicnov, text="")
label_resultadadcn.pack(pady=10)

#frame adicioran nomes e telemoveis a nova
frame_adcnometel = customtkinter.CTkFrame(app, fg_color="transparent")
label_adcnometel = customtkinter.CTkLabel(frame_adcnometel, text=f"Adicionar cartas a ...", font=("Arial", 16, "bold"))
label_adcnometel.pack(pady=10)
newnoome = customtkinter.CTkEntry(frame_adcnometel, placeholder_text="Nome")
newnoome.pack(side="left", pady=10)
newteef = customtkinter.CTkEntry(frame_adcnometel, placeholder_text="Tipo")
newteef.pack(side="right", pady=10)
btnadcnmtl = customtkinter.CTkButton(frame_adcnometel, text="Adicionar", command=lambda:CardDexTools.add_nomesetipo(newadclis, newnoome, newteef))
btnadcnmtl.pack(pady=10)
label_resultadadnt = customtkinter.CTkLabel(frame_adcnometel, text="")
label_resultadadnt.pack(pady=10)

#frame remover
frame_remov = customtkinter.CTkFrame(app, fg_color="transparent")
label_remov = customtkinter.CTkLabel(frame_remov, text="Remover", font=("Arial", 16, "bold"))
label_remov.pack(pady=10)
btnremct = customtkinter.CTkButton(frame_remov, text="Cartas", command=lambda:CardDexTools.mostrar_ver(frame_remov, frame_remov_con))
btnremct.pack(side="left", pady=10)
btnremlis = customtkinter.CTkButton(frame_remov, text="Lista", command=lambda:CardDexTools.mostrar_ver(frame_remov, frame_remov_list))
btnremlis.pack(side="right", pady=10)

#frame remover lista
frame_remov_list = customtkinter.CTkFrame(app, fg_color="transparent")
label_removlist = customtkinter.CTkLabel(frame_remov_list, text=f"Remover Lista", font=("Arial", 16, "bold"))
label_removlist.pack(pady=10)
newremovli = customtkinter.CTkEntry(frame_remov_list, placeholder_text="Nome da Lista a remover...")
newremovli.pack(pady=10)
btnreml = customtkinter.CTkButton(frame_remov_list, text="Remover Lista", command=lambda:CardDexTools2.acao_eliminar_lista(newremovli, label_resultrem))
btnreml.pack(pady=10)
label_resultrem = customtkinter.CTkLabel(frame_remov_list, text="")
label_resultrem.pack(pady=10)

#frame remover contactos
frame_remov_con = customtkinter.CTkFrame(app, fg_color="transparent")
label_removcon = customtkinter.CTkLabel(frame_remov_con, text=f"Remover cartas", font=("Arial", 16, "bold"))
label_removcon.pack(pady=10)
newremovcon = customtkinter.CTkEntry(frame_remov_con, placeholder_text="Nome da Lista a Remover Cartas...")
newremovcon.pack(pady=10)
btnremovcon = customtkinter.CTkButton(frame_remov_con, text="Selecionar Lista", command=lambda:CardDexTools.verif_file(newremovcon, label_resultremcon, frame_remov_con, frame_remov_con_li , label_removconli))
btnremovcon.pack(pady=10)
label_resultremcon = customtkinter.CTkLabel(frame_remov_con, text="")
label_resultremcon.pack(pady=10)

#frame remover contactos da lista
frame_remov_con_li = customtkinter.CTkFrame(app, fg_color="transparent")
label_removconli = customtkinter.CTkLabel(frame_remov_con_li, text="Remover cartas de...", font=("Arial", 16, "bold"))
label_removconli.pack(pady=10)
newremovconli = customtkinter.CTkEntry(frame_remov_con_li, placeholder_text="Nome da carta...")
newremovconli.pack(pady=10)
btnremovconli = customtkinter.CTkButton(frame_remov_con_li, text="Remover Carta", command=lambda:CardDexTools.remover_carta(newremovcon, newremovconli))
btnremovconli.pack(pady=10)
label_resultremconli = customtkinter.CTkLabel(frame_remov_con_li, text="")
label_resultremconli.pack(pady=10)


app.mainloop()