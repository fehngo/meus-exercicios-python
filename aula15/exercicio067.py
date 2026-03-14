print("Este programa tem a finalidade de te mostrar a tabuada")

while True:
    try:

        numero = int(input("Você quer ver a tabuada de qual número? "))

        if numero < 0:
            break

        for i in range(0, 10):
            print(f"{numero} x {i} = {numero * i}")

    except ValueError:
        print("Digite apenas números inteiros!")

print("Fim da tabuada!")
