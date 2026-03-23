from time import sleep


def contar(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = abs(passo)

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}.")
    sleep(2.5)

    # Contagem crescente
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
    # Contagem regressiva
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=" ", flush=True)
            sleep(0.5)

    print("FIM!")
    print("-=" * 15)


def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor inteiro!")


# Programa principal
contar(1, 10, 1)
contar(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
inicio = ler_int("Início: ")
fim = ler_int("Fim: ")
passo = ler_int("Passo: ")

contar(inicio, fim, passo)
