print("O programa atual tem por finalidade apresentar o fatorial do número escolhido!")

numero_original = int(input("Digite um número! "))
if numero_original < 0:
    print("Não existe fatorial de número negativo!")
else:
    numero = numero_original
    resultado = 1

    while numero > 1:
        resultado = resultado * numero
        numero -= 1
    print(f"O resultado da fatoração de {numero_original} é {resultado}")
