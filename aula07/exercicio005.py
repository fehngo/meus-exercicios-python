print(
    "O desafio de hoje é criar o algoritmo que dira o antecessor e o sucessor do numero escolhido por você."
)
n1 = int(input("Digite o seu numero: "))
a = n1 - 1
s = n1 + 1
print(
    "O numero escolhido por você foi {:.5f}.\nO seu antecessor é {:=^35}.\nE o sucessor é {:+<35}.".format(
        n1, a, s
    )
)
