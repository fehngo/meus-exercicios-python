# Importa as funções
from time import sleep
from random import randint


# Cria as funções
def sorteia(lista):
    print("Sorteando 5 valores da lista...")
    sleep(1)
    for i in range(5):
        n = randint(0, 10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.7)
    print(f"Pronto, estes foram os números sorteados")


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}.")


# Cria lista
numeros = list()
sorteia(numeros)
somaPar(numeros)
