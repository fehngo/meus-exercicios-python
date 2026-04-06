from time import sleep

print("Nesse exercicio iremos fazer uma contagem regressvia para o ano novo!!")

try:

    tempo = int(input("Quantos segundos deseja que a contagem tenha? "))
    if tempo <= 0:
        print("Insira um valor maior que zero!")
    else:
        for c in range(tempo, 0, -1):
            print(c)
            sleep(1)
        print("Feliz ano novo!! \U0001f386")

except ValueError:
    print("Algo não saiu como o esperado!")
