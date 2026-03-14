distancia = float(input('digite a distância da viagem: '))
print('Você esta prestes a começar uma viagem de {} quilometros!'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
    print('Sua viagem custará R$ {:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Sua viagem custará R$ {:.2f}'.format(valor))