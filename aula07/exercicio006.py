print("O desafio agora vai ser exibir o Dobro, Triplo e Raiz Quadrada.")
numero = int(input("Vamos começar com o seu numero: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)
print(
    "O numero escolhido por você foi {:.2f}.\nO seu dobro é {:=^25}.\nO triplo é {:k>30}.\nE a raiz dele é {:.5f}.".format(
        numero, dobro, triplo, raiz
    )
)
