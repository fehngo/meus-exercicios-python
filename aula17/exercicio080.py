print("Neste exercício vamos criar uma lista e ordená-la ao mesmo tempo")

lista = []

for _ in range(5):  # controla as 5 entradas válidas
    controle = False

    while True:  # valida a entrada
        try:
            numero = int(input("Digite um número para inserir na lista: "))
            break  # só sai quando for válido
        except ValueError:
            print("Digite apenas números inteiros!")

    for i, v in enumerate(lista):
        if v > numero:
            lista.insert(i, numero)
            print(f"Adicionado na posição {i} da lista.")
            controle = True
            break

    if not controle:
        lista.append(numero)
        print("Adicionado ao final da lista.")

print(f"Os valores digitados em ordem foram {lista}")
