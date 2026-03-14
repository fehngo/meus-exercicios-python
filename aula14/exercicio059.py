print("Hoje iremos operar dois numeros!")

try:

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resposta = ""

    while resposta != "5":
        resposta = input(
            """ Escolha uma opção: \n
        [1] Somar 
        [2] Multiplicar 
        [3] Maior 
        [4] Novos numeros 
        [5] Sair do programa \n
        Oque você deseja fazer?: """
        )

        if resposta == "1":
            print(f"A soma de {n1} + {n2} = {n1 + n2:.2f}.")
        elif resposta == "2":
            print(f"A multiplicação de {n1} * {n2} = {n1 * n2}.")
        elif resposta == "3":
            if n1 > n2:
                print(f"O maior número é {n1}.")
            else:
                print(f"O maior número é {n2}.")
        elif resposta == "4":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        elif resposta == "5":
            exit

    print("Fim do programa")
except ValueError:
    print("Digite apenas números!")
