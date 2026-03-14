## Primeira Tentativa ##
"""print("Hoje iremos calcular uma sequência de fibonacci!")

try:

    ntermo = int(input("Digite quantos termos essa sequência de fibonacci terá: "))
    controle = 0
    n1 = 0
    n2 = 1
    nproximo = 1

    while controle < ntermo:

        if controle < ntermo - 1:
            print(f"{n1} -> ", end="")

        if controle == ntermo - 1:
            print(f"{n1}")

        n1 = n2
        n2 = nproximo
        nproximo = n1 + n2
        controle += 1

    print("Fim da sequência!")


except ValueError:
    print("Digite apenas números inteiros!")"""

print("Hoje iremos calcular uma sequência de fibonacci!")

try:

    ntermo = int(input("Digite quantos termos essa sequência de fibonacci terá: "))
    controle = 0
    n1, n2 = 0, 1

    while controle < ntermo:
        print(n1, end="")

        if controle < ntermo - 1:
            print(" => ", end="")
        n1, n2 = n2, n1 + n2
        controle += 1

    print("\nFim da sequência de fibonacci!")

except ValueError:
    print("Digite apenas vores inteiros!")
