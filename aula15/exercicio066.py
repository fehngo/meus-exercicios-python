contador = soma = 0

while True:

    try:
        numero = int(input("Digite um numero: [999 = Sair]"))

        if numero == 999:
            break

        contador += 1
        soma += numero

    except ValueError:
        print("Digite um número inteiro!")

print(f"Você digitou {contador} números e a soma deles é {soma}.")
