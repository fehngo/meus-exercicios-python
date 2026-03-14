print('Nesse exercício iremos calcular o seu IMC')
try:
    peso = float(input('Qual o seu peso em quilogramas? '))
    altura = float(input('Qual a sua altura metros? '))

    if altura <= 0 or peso <= 0:
        print('Você digitou valores incorretos')

    else:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            categoria = 'Abaixo do peso'
        elif imc < 25:
            categoria = 'Peso ideal'
        elif imc <= 30:
            categoria = 'Sobrepeso'
        elif imc <= 40:
            categoria = 'Obesidade'
        else:
            categoria = 'Obesidade mórbida'

        print(f'Seu IMC é {imc:.1f} e a sua categoria é {categoria}')

except ValueError:
    print('Digite seu peso corretamente!')