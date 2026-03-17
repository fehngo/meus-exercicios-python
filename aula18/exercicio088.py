## Este código tem o objetivo de sortear números para jogos da mega sena de forma automática

## Importar o Sample de random e
from random import sample
from time import sleep

## Criar a lista matriz onde vão ser salvos os jogos de 6 numeros
matriz = []

## Receber do usuário quantos jogos serão
while True:
    try:
        quantidade = int(input("Quantos jogos você deseja gerar?: "))
        break
    except ValueError:
        print("Digite apenas números!")

## Criar os jogos e salvar dentro da lista
for c in range(quantidade):
    numeros = sample(range(1, 61), 6)
    matriz.append(numeros)

## Exibir os jogos
for index, jogo in enumerate(matriz):
    print(f"Jogo {index + 1}: {sorted(jogo)}")
    sleep(0.5)
