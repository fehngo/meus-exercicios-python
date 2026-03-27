def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
            print("Digite um valor inteiro!")
        else:
            return numero


def linha(quantidade=60):
    return "-" * quantidade


def cabecalho(texto="Menu Iterativo"):
    print(linha())
    print(texto.center(60))
    print(linha())


def menu(*funcoes):
    cabecalho()
    for i, v in enumerate(funcoes):
        print(f"{i+1} - {v}")
    print(linha())
    while True:
        escolha = leia_int("Digite o número da opção desejada: ")
        if 1 <= escolha <= len(funcoes):
            return escolha
        else:
            print("Opção inválida! Tente novamente.")
