def separalinha():
    print("-=" * 45)


def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite um valor inteiro!")


dados = dict()

# Nome do jogador
dados["Nome"] = input("Digite o nome do jogador: ")

# Número de partidas
partidas = ler_int(f"Digite quantas partidas {dados['Nome']} jogou: ")

# Gols por partida
gols = list()

for i in range(partidas):
    gol = ler_int(f"    Quantos gols na {i + 1}º partida?: ")
    gols.append(gol)

dados["Gols"] = gols[:]
dados["Total"] = sum(gols)

# Impressão geral
separalinha()
print(dados)
separalinha()

# Campos
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}.")
separalinha()

# Detalhado
print(f"O jogador {dados['Nome']} jogou {partidas} partidas.")
for i, v in enumerate(gols):
    print(f"    => Na {i + 1}º partida fez {v} gols.")

print(f"Foi um total de {dados['Total']} gols.")
