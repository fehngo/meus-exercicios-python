# Cria a função fatorial
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um númeoro.
    :param n: O numero a ser calculado.
    :param show: (Opcional) Mostrar ou não o calculo.
    :return: O valor do fatorial de um número N.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f"{i}", end=" ")
            if i > 1:
                print(f"X", end=" ")
            else:
                print(f"=", end=" ")
        f *= i
    return f


# Programa Principal
print(fatorial(5))
help(fatorial)
