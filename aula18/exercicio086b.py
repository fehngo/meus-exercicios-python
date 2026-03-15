matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):

        while True:

            try:
                numero = int(input(f"Digite um número para [{linha}, {coluna}]: "))
                break
            except ValueError:
                print("Digite apenas números!")

        matriz[linha].append(numero)

for linha in matriz:
    for numero in linha:
        print(f"[{numero:^5}]", end="")
    print("")
