## Importa randint
from random import randint

## Criar lista jogadores
jogadores = list()
ordenado = list()
contador = 6
vencedor = list()

## Criar entrada de quantos jogadores participarão
while True:
    try:
        quantidade = int(input("Quantas pessoas participaraão do jogo? (Mínimo 2 e Máximo 6): "))
        if 6 >= quantidade >= 2:
            break
        else:
            print("Digite um valor entre 2 e 6!")
    except ValueError:
        print("Digite valores entre 2 e 6!")

## Criar loop para pegar nome de cada jogador, sortear o número e armazenar junto com o nome na lista
participantes = {}
for i in range(quantidade):
    participantes["Nome"] = input(f"Digite o nome do {i + 1}º participante: ")
    participantes["Número"] = randint(1, 6)
    jogadores.append(participantes.copy())

## Ordenar a
for i in range(6):
    for v in jogadores:
        if v["Número"] == contador:
            ordenado.append(v)
    contador -= 1

if ordenado[0]["Número"] != ordenado[1]["Número"]:
    vencedor.append(ordenado[0])
else:
    for v in ordenado:
        if v["Número"] == ordenado[0]["Número"]:
            vencedor.append(v)


## Imprimir vencedor e a classificação
print("-*" * 30)
print("O vencedor foi: ", end="")
for v in vencedor:
    print(f"{v["Nome"]:^10} ", end="")
print("")
print("-*" * 30)
print(f"{'CLASSIFICAÇÃO':^60}")
print("-*" * 30)

print(f"{'Posição':^15}|{'Nome':^28}|{'Número':^15}")
print("-*" * 30)
for index, valor in enumerate(ordenado):
    print(f"{(index + 1):^15}|{valor["Nome"]:<28}|{valor["Número"]:^15}")
