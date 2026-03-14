print('Neste exercício iremos somar os valores pares dos números digitados')

try:

    quantidade = int(input('Quantos números você deseja inserir? '))
    numeros = []

    if quantidade <= 0:
        print('Insira uma quantidade maior que zero')
    else:
        for c in range(0, quantidade):
            num = int(input('Digite um valor para testarmos: '))
            if num % 2 == 0:
                numeros.append(num)
        print(f'A soma dos números pares é: {sum(numeros)}')

except ValueError:
    print('Digite apenas números inteiros')