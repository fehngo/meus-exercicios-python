print("Neste exercicio calcularemos o valor a ser pago pelo aluguel do carro!")
dias = int(input("Quantos dias você ficou com o carro?: "))
quilometros = float(input("Qauntos quilometros você rodou? "))
valor1 = dias * 60
valor = valor1 + (quilometros * 0.15)
print(
    "Ja que você ficou com o carro por {} dias e rodou {} quilometros, deverá pagar o valor de R$ {:.2f} pelo aluguel do carro!".format(
        dias, quilometros, valor
    )
)
