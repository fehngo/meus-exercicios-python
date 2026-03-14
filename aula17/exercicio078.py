lista = []
for c in range(0, 5):
    lista.append(int(input("Digite um valor para a posição {c}: ")))


maior = max(lista)
menor = min(lista)
indicemaior = []
indicemenor = []

for i, valor in enumerate(lista):
    if valor == maior:
        indicemaior.append(i)

for i, valor in enumerate(lista):
    if valor == menor:
        indicemenor.append(i)


print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for indice, valor in enumerate(indicemaior):
    if indice != len(indicemaior) - 1:
        print(f"{valor + 1}, ", end="")
    else:
        print(f"{valor + 1}", end="")

print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for indice, valor in enumerate(indicemenor):
    if indice != len(indicemenor) - 1:
        print(f"{valor + 1}, ", end="")
    else:
        print(f"{valor + 1}", end="")
