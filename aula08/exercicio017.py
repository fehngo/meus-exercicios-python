'''print('Hoje iremos calcular a hipotenusa de um triangulo retangulo')
catetoad = float(input('Digite o valor do cateto adjacente: '))
catetoop = float(input('Agora digite o valor do cateto oposto: '))
hipotenusa = (catetoad ** 2 + catetoop ** 2) ** (1/2)
print('A hipotenusa deste triangulo retangulo é {:.3f}' .format(hipotenusa))'''

from math import hypot
print('Hoje iremos calcular a hipotenusa de um triangulo retangulo')
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hi = hypot(ca, co)
print('Sendo {} o cateto adjacente o {} o cateto oposto, a hipontenusa sera {:.3f}'.format(ca, co, hi))