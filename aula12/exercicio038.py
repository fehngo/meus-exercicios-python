print('Vamos analisar qual número é maior e qual é menor!')
try:
    numero = float(input('Digite o primeiro numero: '))
    numero2 = float(input('Digite o segundo numero: '))

    if numero > numero2:
        print('O primeiro valor é maior')
    elif numero2 > numero:
        print('O Segundo valor é maior')
    else:
        print('Não existe valor maior, os dois são iguais')

except ValueError:
    print('Digite apenas números válidos!')