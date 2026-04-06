"""print('O exercício de hoje irá coverter um número real para número inteiro!')
numero = float(input('Digite um numero real!: '))
numero = int(numero)
print('O seu numero convertido para numero inteiro é {}'.format(numero))"""

from math import trunc

print("O exercício de hoje irá coverter um número real para número inteiro!")
numero = float(input("Digite um numero real!: "))
print("O seu numero convertido para numero inteiro é {}".format(trunc(numero)))
