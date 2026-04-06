## Criar 3 listas uma para cada linha da matriz, cada uma dessas listas terá 3 lista dentro
linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]

## ler 3 números para cada lista e armazenar cada número dentro de cada lista dentro da lista principal
for a in range(0, 3):

    while True:
        try:
            numero = int(input(f"Digite um valor para [0, {a}]: "))
            break
        except ValueError:
            print("Digite apenas números!")
    linha0[a].append(numero)

for b in range(3):

    while True:
        try:
            numero = int(input(f"Digite um valor para [1, {b}]: "))
            break
        except ValueError:
            print("Digite apenas números!")
    linha1[b].append(numero)

for c in range(3):

    while True:
        try:
            numero = int(input(f"Digite um valor para [1, {c}]: "))
            break
        except ValueError:
            print("Digite apenas números!")
    linha2[c].append(numero)

    ## imprimir cada uma das 3 listas principais formatadas com [:^5]
for a in range(3):
    print(f"[{linha0[a][0]:^6}]", end="")
print("")

for b in range(3):
    print(f"[{linha1[b][0]:^6}]", end="")
print("")

for c in range(3):
    print(f"[{linha2[c][0]:^6}]", end="")
