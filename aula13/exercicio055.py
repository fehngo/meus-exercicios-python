print('Analisaremos qual peso é maior e qual é menor!')

try:

    pessoas = int(input('Quantas pessoas analisaremos? '))
    pesos = []
    if pessoas <= 0:
        print('Insira um número de pessoas maior que zero!')
    else:
        for c in range(pessoas):
            peso = float(input(f'Digite o peso da pessoa {c + 1}: ').strip())
            if peso <= 0:
                print('Digite pesos maiores que zero!')
                exit()
            pesos.append(peso)

        if pesos:  # verifica se a lista não está vazia
            print(f'O maior peso desta lista é {max(pesos):.1f}, e o menor é {min(pesos):.1f}.')

except ValueError:
    print('Insira valores válidos!')