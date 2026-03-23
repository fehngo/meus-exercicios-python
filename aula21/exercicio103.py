"""def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


# Entrada
n = input("Nome do jogador: ").strip()
g = input("Número de gols: ").strip()

# Tratamento
if n == "":
    n = "<desconhecido>"

if g.isdigit():
    g = int(g)
else:
    g = 0

# Execução
ficha(n, g)"""


# Cria a função
def ficha(n="<Desconhecido>", g=0):
    print(f"O jogador {n} fez {g} gol(s) no campeonato.")


# Ler entradas
nome = input("Digite o nome do jogador: ")
gols = input("Digite quantos gols o jogador fez: ")

# Tratamento
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "":
    ficha(g=gols)
else:
    ficha(nome, gols)
