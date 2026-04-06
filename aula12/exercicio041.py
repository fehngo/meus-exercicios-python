from datetime import datetime

print("Vamos analisar sua idade e descobrir qual a sua categoria!")

try:
    ano = int(input("Digite o seu ano de nascimento: "))
    anoatual = datetime.now().year

    if ano > anoatual:
        print("Segundo os meus cálculos você nem nasceu ainda!")
    elif ano < 0:
        print("Digite um valor positivo!")
    else:
        idade = anoatual - ano

        if idade <= 9:
            categoria = "Mirim"
        elif idade <= 14:
            categoria = "Infantil"
        elif idade <= 19:
            categoria = "Junior"
        elif idade <= 20:
            categoria = "Sênior"
        else:
            categoria = "Master"

        print(f"Você tem {idade} anos e sua categoria é {categoria}")

except ValueError:
    print("Digite um ano válido!")
