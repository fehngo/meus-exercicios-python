from datetime import datetime

print("Agora verificaremos se a pessoa ja atingiu a maioridade (21 Anos).")

try:

    quantidade = int(input("Quantas pessoas iremos verificar? "))
    maior = 0
    menor = 0
    if quantidade <= 0:
        print("Digite um número maior que zero!")
    else:
        for i in range(0, quantidade):
            ano = int(input("Digite o ano de nascimento: "))
            if ano > datetime.now().year - 21:
                menor += 1
            else:
                maior += 1
    print(
        f"Dessas pessoas que verificamos {maior} ja atingiram a maioridade e {menor} ainda não atingiram !"
    )

except ValueError:
    print("Digite um valor válido!")
