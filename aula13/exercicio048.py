### Meu Exercício ###
"""print('Neste exercício iremos somar os números ímpares divisíveis por 3 que aparecerem na sua lista')

try:

    inicio = int(input('Digite um número para iniciar: '))
    fim = int(input('Digite um número para finalizar: '))
    impares = []
    divisiveis = []
    for c in range(inicio,fim+1):
        if c % 2 != 0:
            impares.append(c)
    print('Os números ímpares nesta lista são:')
    print(impares)
    print('Dentre esses números apenas esses são divisíveis por 3:')
    for c in impares:
        if c % 3 == 0:
            divisiveis.append(c)
    print(divisiveis)
    print(f'A soma dos números ímpares divisíveis por 3 é: {sum(divisiveis)}')

except ValueError:
    print('Ocorreu um erro inesperado!')"""

### Correção ###

print("Nesse exercício iremos somar os números ímpares divisíveis por 3")

try:

    inicio = int(input("Digite um número para iniciar: "))
    fim = int(input("Digite um número para finalizar: "))
    divisiveis = []
    cont = 0
    if inicio > fim:
        print("Digite um inicio menor que o fim!")
    else:
        for c in range(inicio, fim + 1):
            if c % 2 != 0 and c % 3 == 0:
                divisiveis.append(c)
                cont += 1
        print("Os números ímpares divisíveis por 3 são:")
        print(divisiveis)
        print(f"A soma desses {cont} números é {sum(divisiveis)}")

except ValueError:
    print("Digite apenas números inteiros!")
