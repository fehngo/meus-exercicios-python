print("Este exercício tem finalidade de ler varios números e separar em lista de pares e impares!")

numeros = list()
pares = list()
impares = list()

while True:
    try:
        n = int(input("Digite um número: "))
    except ValueError:
        print("Digite apenas números inteiros!")
        continue

    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    while True:
        decisao = input("Deseja continuar [S/N]?: ").upper().strip()
        if decisao in "SN":
            break

    if decisao == "N":
        break

print(f"A sua lista é {numeros}")
print(f"A lsita de números pares é {pares}")
print(f"A lista de números impares é {impares}")
