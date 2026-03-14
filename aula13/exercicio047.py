##Meu Jeito##
'''print('Neste programa listaremos todos os númeors pares!')
try:

    inicio = int(input('Insira um numero para início: '))
    fim = int(input('Insira um numero para o fim: '))

    if inicio < 0 or fim <= 0 or inicio >= fim:
        print('Insira valores válidos!')
    else:
        print('Os números pares são!')
        if inicio % 2 == 0:
            for i in range(inicio, fim + 1, 2):
                print(i)
        else:
            novo_inicio = inicio - 1
            if novo_inicio == 0:
                novo_inicio += 2
            else:
                for i in range(novo_inicio, fim + 1, 2):
                    print(i)

except ValueError:
    print('Ocorreu um erro inesperado!')'''

### Correção ###
print('Vamos fazer uma lista apenas com números pares!')

try:

    inicio = int(input('Insira um número para inicio: '))
    fim = int(input('Insira um número para fim: '))

    if inicio >= fim:
        print('Insira valores válidos!')
    else:
        print('Os números pares nesse intervalo são: ')
        if inicio % 2 != 0:
            inicio += 1
        for i in range(inicio, fim + 1, 2):
            print(i)

except ValueError:
    print('Ocorreu um erro inesperado!')