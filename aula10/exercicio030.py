from time import sleep
numero = int(input('Me diz um nuemro qualquer: '))
print('PROCESSANDO...')
sleep(2)
if numero % 2 == 0:
    print('{} é um nuemro par'.format(numero))
else:
    print('{} é um numero impar'.format(numero))