matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                numero = int(
                    input(f"Digite um número para posição [{linha}, {coluna}]: ")
                )
                break
            except ValueError:
                print("Insira apenas números!")
        matriz[linha].append(numero)

for linha in matriz:
    for numero in linha:
        print(f"[{numero:^5}]", end="")
    print("")

soma_pares = 0
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            soma_pares += numero

maior2 = max(matriz[1])

soma3 = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma3}")
print(f"O maior valor da segunda linha é {maior2}")
