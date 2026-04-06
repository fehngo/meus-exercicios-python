from random import randint
from time import sleep

print("Vou pensar em um numero entre 0 e 5, tente adivinhar... ")
certo = randint(0, 5)
numero = int(input("Em que numero eu estou pensando? "))
print("PROCESSANDO...")
sleep(3)
if numero == certo:
    print("Você me venceu!")
else:
    print("Eu te venci. \nPensei no numero {}, tente novamente!".format(certo))
