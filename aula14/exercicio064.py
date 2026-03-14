print("Hoje iremos somar os seus números!")

numero = 0
soma = 0
contador = 0

while numero != 999:
    try:

        numero = int(input("Digite um número para somar, ou 999 para sair: "))

        if numero != 999:
            soma += numero
            contador += 1

    except ValueError:
        print("Digite apenas números inteiros!")

print(f"Você digitou {contador} números e a soma deles é {soma}.")
