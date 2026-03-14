"""from random import randint
from time import sleep
print('Vamos brincar de advinhar de novo!')
print('Vou pensar em um número entre 0 e 10')
print('PENSANDO...')
sleep(1)

computador = randint(0, 10)
numero = -1
print('Sua vez!')
contador = 0
while numero != computador:
    try:
        numero = int(input('Em qual número eu pensei? '))

        if numero < 0 or numero > 10:
            print('Digite números entre 0 e 10')
        elif numero != computador:
            print('Errou, tente novamente...')

        contador += 1
    except ValueError:
        print('Digite penas números inteiros!')
print(f'Parabéns, você acertou com {contador} tentativas.')"""

from random import randint
from time import sleep

print("Vamos brincar de advinhar de novo!")
print("Vou pensar em um número entre 0 e 10")
print("PENSANDO...")
sleep(1)

computador = randint(0, 10)
acertou = False
contador = 0

try:

    while not acertou:
        pergunta = int(input("Digite seu palpite: "))

        if pergunta == computador:
            acertou = True

        if pergunta < computador:
            print("Errou, Mais!")
        elif pergunta > computador:
            print("Errou, Menos!")
        else:
            print("Na mosca!")

        contador += 1

    print(f"Parabéns, você acertou com {contador} tentativas.")

except ValueError:
    print("Digite somente números inteiros!")
