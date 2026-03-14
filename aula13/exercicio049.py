print('Hoje criaremos a tabuada do número desejado!')

try:

    numero = int(input('Digite um número para calcularmos a tabuada: '))
    parar = int(input('Você gostaria da tabuada até qual número? '))
    if numero == 0:
        print('Digite um valor maior que zero, pois sabemos que tod numero multiplicado por 0 é 0')
    elif parar <= 0:
        print('Digite um valor maior que 0 para pararmos')
    else:
        for c in range(0, parar + 1):
            #resultado = numero * c
            print(f'{numero} x {c} = {numero * c}')

except ValueError:
    print('Digite apenas números inteiros!')