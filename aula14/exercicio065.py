"""print("Hoje vamos operar seus números")

continuar = "S"
contador = 0
soma = 0
maior = 0
menor = 99999999

while continuar == "S":
    num = int(input("Digite um número: "))
    contador += 1
    soma += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    continuar = input("Deseja Continuar [S/N]: ").strip().upper()[0]
    while continuar not in ["S", "N"]:
        continuar = input("Deseja Continuar [S/N]: ").strip().upper()[0]

media = soma / contador

print(f"Você digitou {contador} números")
print(f"A média deles é {media}")
print(f"O maior valor foi {maior}")
print(f"O menor valor foi {menor}")"""

print("Hoje vamos operar seus números")

continuar = "S"
contador = 0
soma = 0
maior = menor = None

while continuar == "S":
    try:
        num = int(input("Digite um número: "))
    except ValueError:
        print("Digite apenas números inteiros!")
        continue

    contador += 1
    soma += num

    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = input("Deseja Continuar [S/N]: ").strip().upper()
    while continuar not in ["S", "N"]:
        continuar = input("Deseja Continuar [S/N]: ").strip().upper()

if contador > 0:
    media = soma / contador
    print(f"Você digitou {contador} números")
    print(f"A média deles é {media}")
    print(f"O maior valor foi {maior}")
    print(f"O menor valor foi {menor}")
else:
    print("Nenhum número foi digitado.")
