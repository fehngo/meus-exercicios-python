# Criar funções de ler números e calcular área
def calc_area(x, y):
    area = x * y
    return area


def ler_float(msg):
    while True:
        try:
            temp = float(input(msg))
            return temp
        except ValueError:
            print("Digite apenas números!")


# Criar entrada de largura e altura
print("Vamos calcular a área de um terreno!")
largura = ler_float("Digite a largura do terreno: ")
comprimento = ler_float("Digite o comprimento do terreno: ")

# Calcular e imprimir área
area = calc_area(largura, comprimento)
print(
    f"Um terreno que tem {largura:.1f} metros de largura e {comprimento:.1f} metros de comprimento terá a area de {area:.1f} metros quadrados!"
)
