from datetime import datetime

print("Bem vindo ao programa de alistamento militar!")

try:

    nascimento = int(input("Em que ano você nasceu?: "))
    idade = datetime.today().year - nascimento
    alistamento = nascimento + 18

    if idade < 0:
        print("Ano inválido!")
    elif idade < 18:
        falta = 18 - idade
        # print('Não chegou seu ano de alistamento militar ainda, faltam exatamente {} anos para você se alistar!'.format(falta))
        print(
            f"Não chegou seu ano de alistamento militar ainda, faltam exatamento {falta} anos para você se alistar!"
        )
        print(f"Seu ano de alistamente será em {alistamento}")
    elif idade > 18:
        atraso = idade - 18
        # print('Seu ano de alistamento militar ja passou, você está {} anos atrasado!'.format(falta))
        print(f"Seu ano de alistamento militar já passou, você está {atraso} anos atrasado!")
        print(f"Seu ano de alistamento foi em {alistamento}")
    else:
        print("Você está na idade exata de se alistar para o serviço militar!")

except ValueError:
    print("Digite um ano válido!")
