from random import randint

print("=-" * 20)
print("Vamos jogar par ou ímpar!")
print("=-" * 20)

contador = 0

while True:

    computador = randint(0, 10)
    escolha = ""
    usuario = int(input("Escolha um número: "))

    while escolha not in ["P", "I"]:
        escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()
        print("=-" * 20)

    if escolha == "P" and (computador + usuario) % 2 == 0:
        print(
            f"Você jogou {usuario} e eu joguei {computador}. "
            f"Total de {usuario + computador}: PAR"
        )
        print("Você venceu!!\nVamos jogar de novo!")
        contador += 1
    elif escolha == "P" and (computador + usuario) % 2 != 0:
        print(
            f"Você jogou {usuario} e eu joguei {computador}. "
            f"Total de {usuario + computador}: ÍMPAR"
        )
        print("Você perdeu!")
        break
    elif escolha == "I" and (computador + usuario) % 2 != 0:
        print(
            f"Você jogou {usuario} e eu joguei {computador}. "
            f"Total de {usuario + computador}: ÍMPAR"
        )
        print("Você venceu!!\nVamos jogar de novo!")
        contador += 1
    elif escolha == "I" and (computador + usuario) % 2 == 0:
        print(
            f"Você jogou {usuario} e eu joguei {computador}. "
            f"Total de {usuario + computador}: PAR"
        )
        print("Você perdeu!")
        break

print(f"Fim de Jogo, voce venceu {contador} vezes!")
