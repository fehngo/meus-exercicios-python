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


def aumentar(v, p, formato=False):
    vp = (v * p) / 100
    final = vp + v
    return final if formato is False else moeda(final)
    """if sit == True:
        return f"R$ {final:.2f}"
    else:
        return final"""


def diminuir(v, p, formato=False):
    vp = (v * p) / 100
    final = v - vp
    return final if formato is False else moeda(final)
    """if sit == True:
        return f"R$ {final:.2f}"
    else:
        return final"""


def dobro(n, formato=False):
    final = n * 2
    return final if formato is False else moeda(final)
    """if sit == True:
        return f"R$ {final:.2f}"
    else:
        return final"""


def metade(n, formato=False):
    final = n / 2
    return final if formato is False else moeda(final)
    """if sit == True:
        return f"R$ {final:.2f}"
    else:
        return final"""


def moeda(v=0, moeda="R$"):
    return f"{moeda}{v:>.2f}".replace(".", ",")


def resumo(preco=0, aumento=10, redução=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço Analisado: \t{moeda(preco)}")
    print(f"Dobro do Preço: \t{dobro(preco, True)}")
    print(f"Metade do Preço: \t{metade(preco, True)}")
    print(f"{aumento}% de Aumento: \t{aumentar(preco, aumento, True)}")
    print(f"{redução}% de Redução: \t{diminuir(preco, redução, True)}")
