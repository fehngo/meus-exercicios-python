'''valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
print('O menor valor digitado foi {}'.format(min(valor1, valor2, valor3)))
print('O maior valor digitado foi {}'.format(max(valor1, valor2, valor3)))'''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
if valor1 < valor2 and valor1 < valor3:
    menor = valor1
    print('O menor valor digitado foi {}'.format(menor))
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
    print('O menor valor digitado foi {}'.format(menor))
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
    print('O menor valor digitado foi {}'.format(menor))
if valor1 > valor2 and valor1 > valor3:
    maior = valor1
    print('O maior valor digitado foi {}'.format(maior))
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
    print('O maior valor digitado foi {}'.format(maior))
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
    print('O maior valor digitado foi {}'.format(maior))
