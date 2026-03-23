def voto(ano):
    from datetime import date

    idade = date.today().year - ano

    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    elif 16 <= idade < 18 or idade > 70:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


def le_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas números inteiros!")


# Programa principal
ano = le_int("Digite o seu ano de nascimento: ")
print(voto(ano))
