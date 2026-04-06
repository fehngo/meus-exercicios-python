"""from random import choice

print('-' * 20)
print('Vamos Jogar Pedra, Papel, Tesoura.')
print('-' * 20)

try:

    opcoes = ['Pedra', 'Papel', 'Tesoura']
    usuario = input('Escolha sua jogada! \nPedra, Papel ou Tesoura: ').strip() .title()
    computador = choice(opcoes)

    if usuario not in opcoes:
        print('Você escolheu uma opção inválida!')
    else:
        if computador == 'Pedra' and usuario == 'Papel':
            print(f'Você venceu, escolhi {computador} e {usuario} ganha de {computador}.')
        elif computador == 'Pedra' and usuario == 'Tesoura':
            print(f'Eu venci, escolhi {computador} e {computador} ganha de {usuario}.')
        elif computador == 'Pedra' and usuario == 'Pedra':
            print(f'Empatamos, nós dois escolhemos {computador}.')
        elif computador == 'Papel' and usuario == 'Tesoura':
            print(f'Você venceu, escolhi {computador} e {usuario} ganha de {computador}.')
        elif computador == 'Papel' and usuario == 'Pedra':
            print(f'Eu venci, escolhi {computador} e {computador} ganha de {usuario}.')
        elif computador == 'Papel' and usuario == 'Papel':
            print(f'Empatamos, nós dois escolhemos {computador}.')
        elif computador == 'Tesoura' and usuario == 'Pedra':
            print(f'Você venceu, escolhi {computador} e {usuario} ganha de {computador}.')
        elif computador == 'Tesoura' and usuario == 'Papel':
            print(f'Eu venci, escolhi {computador} e {computador} ganha de {usuario}.')
        elif computador == 'Tesoura' and usuario == 'Tesoura':
            print(f'Empatamos, nós dois escolhemos {computador}.')

except ValueError:
    print('Valores Invalidos!')"""

from random import choice
from time import sleep

print("=" * 20)
print("Vamos jogar Pedra, Papel ou Tesoura")
print("=" * 20)

try:

    opcoes = ["Pedra", "Papel", "Tesoura"]
    usuario = input("Escolha sua jogada! \nPedra, Papel ou Tesoura: ").strip().title()
    computador = choice(opcoes)

    if usuario not in opcoes:
        print("Você escolheu uma opção inválida!")
    else:
        print("JO")
        sleep(0.7)
        print("KEN")
        sleep(0.7)
        print("PO!")
        sleep(0.7)
        print(f"Eu escolhi {computador}")
        if computador == usuario:
            print("Empatamos")
        elif (
            (usuario == "Pedra" and computador == "Tesoura")
            or (usuario == "Papel" and computador == "Pedra")
            or (usuario == "Tesoura" and computador == "Papel")
        ):
            print("Você Venceu!")
        else:
            print("Eu Venci!")

except ValueError:
    print("Valores Invalidos!")
