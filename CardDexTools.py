def remover_carta(ficheiro_nome, nome_a_remover):
    linhas_vivas = []
    encontrado = False

    with open(f"{ficheiro_nome}.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if nome_a_remover not in linha:
                linhas_vivas.append(linha)
            else:
                encontrado = True
        
     # Reescrever o ficheiro apenas com as linhas que restaram
    with open(f"{ficheiro_nome}.txt", "w", encoding="utf-8") as f:
        f.writelines(linhas_vivas)
            
    if encontrado:
        print(f"A carta {nome_a_remover.capitalize()} foi removido.")
    else:
        print("Carta não encontrada.")
