velocidade = int(input("Qual a velocidade atual do carro? "))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print("Tenha um bom dia, dirija sempre com segurança!")
elif velocidade > 80 and velocidade <= 96:
    print(
        "Você esta acima da velocidade permitida em até 20% e receberá uma multa de R$ {:.2f} e 5 pontos na carteira!".format(
            multa
        )
    )
else:
    print(
        "Você esta acima da velicidade permitida em mais de 20% e tera sua habilitação cassada, e receberá uma multa de R$ {:.2f}".format(
            multa
        )
    )
