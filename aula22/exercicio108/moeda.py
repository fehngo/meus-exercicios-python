def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Digite apenas números inteiros!")


def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print("Digite apenas números inteiros ou reais")


def aumentar(v, p):
    vp = (v * p) / 100
    return vp + v


def diminuir(v, p):
    vp = (v * p) / 100
    return v - vp


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(msg):
    return f"R$ {msg:.2f}"
