n1 = int(input("Um valor: "))
n2 = int(input("Outro Valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
rd = n1 % n2
print(
    "O resultado da soma é {:+>20}. \n Da multiplicação é {}. \n Da divisão é {:.3f}. \n Da divisão inteira é {} e o resto {}. \n E a exponenciação é {}".format(
        s, m, d, di, rd, e
    )
)
