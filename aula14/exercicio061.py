print("Neste exercício iremos apresentar uma PA a partir do primeiro termo e da razão")

ptermo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))
contador = 0
termo_atual = ptermo

while contador < 10:
    if contador < 9:
        print(f"{termo_atual} -> ", end="")
    else:
        print(termo_atual)

    termo_atual += razao
    contador += 1
