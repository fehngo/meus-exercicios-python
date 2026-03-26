def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except (ValueError, TypeError):
            print("Digite apenas valores inteiros!")


def linha(quant=60):
    return "-" * quant


def cabecalho(msg):
    tamanho = 60
    print(linha(tamanho))
    print(msg.center(tamanho))
    print(linha(tamanho))
    return tamanho


def opções(*opções):
    for i, v in enumerate(opções):
        print(f"{i+1} - {v}")
    print(linha())
    while True:
        escolha = leia_int("Digite o número da opção: ")
        return escolha
