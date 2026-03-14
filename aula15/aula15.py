"""cont = 1
while cont <= 10:
    print(cont, "-> ", end="")
    cont += 1
print("Acabou")"""

"""cont = 1
while True:
    print(cont, "-> ", end="")
    cont += 1
print("Acabou")"""

"""num = 0
while num != 999:
    num = int(input("Digite um número: "))"""

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(s)
