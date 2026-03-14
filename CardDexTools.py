import customtkinter

def mostrar_criar(framever, framecriar):
    framever.pack_forget()
    framecriar.pack(pady=20, fill="both", expand=True)

def mostrar_ver(frame_criar, frame_ver):
    frame_criar.pack_forget()
    frame_ver.pack(pady=20, fill="both", expand=True)


def executar_criacao(filename, label_resultado):
    nome_do_ficheiro = filename.get()
    while True:
        if nome_do_ficheiro.strip() == "":
            label_resultado.configure(text="Erro: Escreve um nome!", text_color="red")
        else:
            with open(f"{nome_do_ficheiro}.txt", "w", encoding="utf-8") as fileuser:
                fileuser.write("Lista de Amigos:\n")
                print(f"A criar: {nome_do_ficheiro}.txt")
            label_resultado.configure(text=f"Ficheiro {nome_do_ficheiro}.txt criado!", text_color="green")
            break

def ver_ficheiro(filenam, labelresultado):
    file = filenam.get()
    while True:
        try:
            with open(f"{file}.txt", "r", encoding="utf-8") as filee:
                conteudo = filee.read()
                print("--- Conteúdo do Ficheiro ---")
                print(conteudo)
                labelresultado.configure(text=f"Conteudo do ficheiro:\n{conteudo}", text_color="green")
        except FileNotFoundError:
            print("O ficheiro ainda não existe.")
            print(f"A criar: {file}.txt")
            labelresultado.configure(text="Ficheiro não existe!", text_color="red")
        break