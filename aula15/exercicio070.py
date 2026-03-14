total = produtos1000 = 0
nome_barato = None
preco_barato = float("inf")

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    total += preco

    if preco > 1000:
        produtos1000 += 1

    if preco < preco_barato:
        preco_barato = preco
        nome_barato = nome

    continuar = ""
    while continuar not in ["S", "N"]:
        continuar = input("Deseja Continuar? [S/N] ").strip().upper()

    if continuar == "N":
        break

print(f"O valor total gasto nessa compra foi R$ {total:.2f}")
print(f"Temos {produtos1000} produtos custando mais de R$ 1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R$ {preco_barato:.2f}")
