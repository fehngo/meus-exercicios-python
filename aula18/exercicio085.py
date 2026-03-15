"""## Criar a lista
numeros = [[], []]

## Receber 7 numeros do usuário e adicionar dentro da lista separados em par ou impar
for c in range(1, 8):
    while True:
        numero = input(f"Digite o {c}º número: ")
        if numero.isdigit():
            numero = int(numero)
            break
    if numero % 2 == 0:
        numeros[0].append(c)
    else:
        numeros[1].append(c)

## imprimir numeros pares em ordem crescente
print(f"A lista com os números pares é: {sorted(numeros[0])}")

## imprimir numeros impares em ordem crescente
print(f"A lista com os números impares é {sorted(numeros[1])}")
"""

## Criar a lista
numeros = [[], []]

## Receber 7 numeros do usuário e adicionar dentro da lista separados em par ou impar
for c in range(1, 8):
    while True:
        try:
            numero = int(input(f"Digite o {c}º número: "))
            break
        except ValueError:
            print("Digite apenas números inteiros ")
    if numero % 2 == 0:
        numeros[0].append(c)
    else:
        numeros[1].append(c)

## imprimir numeros pares em ordem crescente
print(f"A lista com os números pares é: {sorted(numeros[0])}")

## imprimir numeros impares em ordem crescente
print(f"A lista com os números impares é {sorted(numeros[1])}")
