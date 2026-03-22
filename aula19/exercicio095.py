def separalinha(t):
    print(t * 32)


def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite um valor inteiro!")


dados = dict()
jogadores = list()

# Nome do jogador
while True:
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

    # Adiciona dados na lista e apaga dados
    jogadores.append(dados.copy())
    dados.clear()

    # Repete laço
    while True:
        decisão = input("Deseja continuar? [S/N]: ").upper().strip()
        if decisão in "SN":
            break
        else:
            print('Digite apenas "S" ou "N"!')

    if decisão == "N":
        break

# Imprime tabela
separalinha("-=")
print(f'{"Nº":^10}|{"Nome":^16}|{"Gols":^26}|{"Total":^10}')
separalinha("-=")
for index, jogador in enumerate(jogadores):
    gols_str = ", ".join(map(str, jogador["Gols"]))
    print(
        f'{index + 1:^10}| {jogador["Nome"]:<15}| {gols_str:<25}|{jogador["Total"]:^10}'
    )
# Detalha jogador
while True:
    while True:
        escolha = input("Deseja detalhar algum jogador? [S/N]: ").upper().strip()
        if escolha in "SN":
            break
        else:
            print('Digite apenas "S" ou "N"!')

    if escolha == "S":
        num = ler_int("Digite o número do jogador que deseja detalhar: ")
        if num > len(jogadores):
            print(f"ERRO! Não existe jogador com o número {num}.")
            continue
        for index, valor in enumerate(jogadores):
            if index == num - 1:
                print(f'-- Levantamento do jogador {valor["Nome"]}:')
                for k, v in enumerate(valor["Gols"]):
                    print(f"    No jogo {k + 1} fez {v} gols.")

    else:
        break

print("<< Volte Sempre! >>")
