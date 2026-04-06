print("Esse progama foi desenvolvido para te ajudar a saber quantos dolares você pode comprar.")
carteira = float(input("Quantos reais você tem na carteira?: "))
usd = 3.27
dolar = int(carteira / usd)
centavos = float(carteira % usd)
print(
    "Atualmente você tem {:.2f} Reais na carteira.\nCom esse valor é possivel comprar {} Dolares e sobraria para você {:.2f} Reais.".format(
        carteira, dolar, centavos
    )
)
