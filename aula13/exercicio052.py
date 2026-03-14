print('Descobrindo números primos.')

try:
    numero = int(input('Digite um número inteiro: '))
    primo = True

    if numero <= 1:
        primo = False

    for c in range(2, numero):
        if numero % c == 0:
            primo = False
            break

    if primo:
        print(f"{numero} é primo!")
    else:
        print(f"{numero} não é primo!")

except ValueError:
    print('Digite um número inteiro')