"""numeros = (
    "Zero",
    "Um",
    "Dois",
    "Três",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez",
    "Onze",
    "Doze",
    "Treze",
    "Quatorze",
    "Quinze",
    "Dezesseis",
    "Dezessete",
    "Dezoito",
    "Dezenove",
    "Vinte",
)

while True:
    decisao = ""
    while True:
        try:
            pedido = int(input("Digite um número inteiro de 0 a 20: "))
            if 0 <= pedido <= 20:
                break
            else:
                print("Número fora do intervalo, tente novamente!")
        except ValueError:
            print("Digite um número inteiro!")
    print(f"O número digitado foi o número: {numeros[pedido]}")

    while decisao not in ["S", "N"]:
        decisao = input("Você deseja continuar? [S/N] ").strip().upper()[0]
        print(decisao)
    if decisao == "N":
        break"""

numeros = (
    "Zero",
    "Um",
    "Dois",
    "Três",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez",
    "Onze",
    "Doze",
    "Treze",
    "Quatorze",
    "Quinze",
    "Dezesseis",
    "Dezessete",
    "Dezoito",
    "Dezenove",
    "Vinte",
)

while True:
    while True:
        try:
            pedido = int(input("Digite um número inteiro de 0 a 20: "))
            if 0 <= pedido <= 20:
                break
            print("Número fora do intervalo, tente novamente!")
        except ValueError:
            print("Digite um número inteiro!")

    print(f"O número digitado foi: {numeros[pedido]}")

    decisao = input("Você deseja continuar? [S/N] ").strip().upper()
    if decisao == "N":
        break
