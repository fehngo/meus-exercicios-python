## Convertendo numeros entre bases ##
numero = int(input("Escreva um numero inteiro para ser convertido: "))
n = numero
base = (
    str(input("Para qual base você deseja converter, Binario, Octal ou Hexadecimal? "))
    .strip()
    .title()
)
if base == "Binario":
    if numero == 0:
        print("Seu número binário é {}".format(numero))
    elif numero < 0:
        print("Seu número é inválido!")
    else:
        binario = ""
        while n > 0:
            resto = n % 2
            binario = str(resto) + binario
            n = n // 2
        print("Seu número binário é {}".format(binario))
elif base == "Octal":
    if numero == 0:
        print("Seu número Octal é {}".format(numero))
    elif numero < 0:
        print("Seu número é inválido!")
    else:
        octal = ""
        while n > 0:
            resto = n % 8
            octal = str(resto) + octal
            n = n // 8
        print("Seu número Octal é {}".format(octal))
elif base == "Hexadecimal":
    if numero == 0:
        print("Seu número Hexadecimal é {}".format(numero))
    elif numero < 0:
        print("Seu número é inválido!")
    else:
        hexadecimal = ""
        digito = "0123456789ABCDEF"
        while n > 0:
            resto = n % 16
            hexadecimal = digito[resto] + hexadecimal
            n = n // 16
        print("Seu número Hexadecimal é {}".format(hexadecimal))
else:
    print("Você escolheu uma opção invalida!")
print("Tenha um excelente dia!")
