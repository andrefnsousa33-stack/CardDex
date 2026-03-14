cartas = []

while True:
    # .strip() Limpa espaços e .lower() coloca tudo em minusculas
    carta = input(f"Dá-me o nome da tua {len(cartas) + 1}ª carta (ou 'sair'): ").strip().lower()
    if carta == "sair":
        break
    else:
        cartas.append(carta)

# = len() Guarda o numero de linhas em "cartas" numa variavel
numcartas = len(cartas)
if numcartas > 0:
    # .sort() Organiza alfabéticamente a lista
    cartas.sort()
    # {cartas[0]} Devolve o primeiro nome da lista "cartas" e .capitalize devolve o nome com a primeira letra maiuscula
    print(f"A primeiro da lista alfabeticamente é: {cartas[0].capitalize()}\n")
    print(f"Inseriste {numcartas}")
else:
    print("Não inseriste nenhuma carta.")

