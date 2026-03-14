import unicodedata

print('Hoje iremos calcular o juros do pagamento')

try:

    valor = float(input('Qual o valor do produto? R$ '))
    forma_pagamento = input('Qual a forma de pagamento? \nDinheiro, Pix ou Cartão ') .strip().lower()
    formapagamento = unicodedata.normalize('NFD', forma_pagamento)
    formapagamento = formapagamento.encode('ascii', 'ignore').decode('utf-8')

    if valor <= 0:
        print('Digite um valor maior que zero!')
    elif formapagamento not in ['dinheiro', 'pix', 'cartao']:
        print('Digite uma forma de pagamento válida!')
    else:
        if formapagamento in ['dinheiro', 'pix']:
            valor2 = valor - (valor * 0.1)
            print(f'o Valor do produto ficará R$ {valor2:.2f}')
        elif formapagamento == 'cartao':
            cartao = int(input('Em quantas vezes você pretende fazer? '))
            if cartao == 1:
                valor2 = valor - (valor * 0.05)
            elif cartao == 2:
                valor2 = valor
            else:
                valor2 = valor + (valor * 0.2)

            valordaparcela = valor2 / cartao
            print(f'O valor do produto ficará {cartao}X de R$ {valordaparcela:.2f}')
            print(f'Total: R$ {valor2:.2f}')
        else:
            print('opção Inválida')

except ValueError:
    print('Valores Invalidos!')