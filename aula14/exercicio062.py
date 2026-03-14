## Primeira Tentativa ## Funcional
"""print("Neste exercício iremos apresentar uma PA a partir do primeiro termo e da razão")

ptermo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))
termos = 10
contador = 0
termo_atual = ptermo

while contador < termos:
    if contador < termos - 1:
        print(f"{termo_atual} -> ", end="")
    else:
        print(termo_atual)

    termo_atual += razao
    contador += 1

controle = ""
while controle not in ["S", "N"]:
    controle = input("Você deseja continuar? [S/N]: ").strip().upper()
    if controle == "S":

        contador = 1
        termos = 11
        while contador != 0:
            quantidade = int(input("Você deseja inserir mais quantos termos? "))
            if quantidade == 0:
                break
            else:
                termo_atual = ptermo
                termos += quantidade

                while contador < termos:
                    if contador < termos - 1:
                        print(f"{termo_atual} -> ", end="")
                    else:
                        print(termo_atual)

                    termo_atual += razao
                    contador += 1
                contador = 1
    else:
        print("Fim!")
    print("Fim!")"""

## Correção Chat ##
"""print("Neste exercício iremos apresentar uma PA a partir do primeiro termo e da razão")

ptermo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

total_termos = 10

while True:

    termo_atual = ptermo
    contador = 0

    while contador < total_termos:
        if contador < total_termos - 1:
            print(f"{termo_atual} -> ", end="")
        else:
            print(termo_atual)

        termo_atual += razao
        contador += 1

    quantidade = int(input("Você deseja inserir mais quantos termos? (0 para sair) "))

    if quantidade == 0:
        break

    total_termos += quantidade

print("Fim da progressão.")"""


## Eu Fiz ##
"""print("Neste exercício iremos calcular a PA de 10 termos!")

try:

    ptermo = int(input("Digite o primeiro termo da progressão: "))
    razao = int(input("Digite a razão da progressão: "))
    total_de_termos = int(input("Digite quantos termos terá a progressão: "))

    while True:

        termo_atual = ptermo
        contador = 0

        while contador < total_de_termos:
            if contador < total_de_termos - 1:
                print(f"{termo_atual} -> ", end="")
            if contador == total_de_termos - 1:
                print(f"{termo_atual}")
            termo_atual += razao
            contador += 1

        controle = int(input("Deseja incluir mais quantos termos ? [0 = sair]: "))
        if controle == 0:
            break
        else:
            total_de_termos += controle
    print("Fim da progressão aritmética!")
except ValueError:
    print("Digite apenas números inteiros!")"""

print("Neste exercício iremos calcular a PA!")

try:
    ptermo = int(input("Digite o primeiro termo da progressão: "))
    razao = int(input("Digite a razão da progressão: "))
    total_de_termos = int(input("Digite quantos termos terá a progressão: "))

    termo_atual = ptermo
    contador = 0

    while True:

        while contador < total_de_termos:
            if contador < total_de_termos - 1:
                print(f"{termo_atual} -> ", end="")
            else:
                print(f"{termo_atual}")

            termo_atual += razao
            contador += 1

        controle = int(input("Deseja incluir mais quantos termos? [0 = sair]: "))

        if controle == 0:
            break

        total_de_termos += controle

    print("Fim da progressão aritmética!")

except ValueError:
    print("Digite apenas números inteiros!")
