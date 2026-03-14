print("Neste exercício irmos criar uma lista de valores...")

lista = []

while True:
    try:

        valor = int(input("Digite um número para ser adicionado: "))

    except ValueError:
        print("Digite apenas números inteiros!")
        continue

    if valor in lista:
        print("Este número ja se encontra na lista!!")

    else:
        lista.append(valor)

    while True:
        decisao = input("Deseja continuar ? [S/N]: ").strip().upper()

        if decisao in ["S", "N"]:
            break
        else:
            continue

    if decisao == "N":
        break
    else:
        continue


print(
    f"Você digitou os valores {sorted(lista)}.\n"
    "Eles estão ordenados em ordem crescente!"
)
