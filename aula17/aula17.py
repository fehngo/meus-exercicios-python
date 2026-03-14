"""num = (2, 5, 9, 1)
num[2] = 3
print(num)

num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 10
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
# num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print(f"Não achei o valor {5}")
print(num)
print(f"Essa lista tem {len(num)} elementos.")"""

"""valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

print(valores)

for chave, valor in enumerate(valores):
    print(f"Na posição {chave} encontrei o valor {valor}!")
print(f"Cheguei ao final da lista")"""

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
